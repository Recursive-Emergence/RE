"""
Concept Hierarchy Module

This module enhances the concept hierarchy capabilities of the RECC system,
specifically targeting the concept hierarchy depth metric for MVP 1.6.
"""

import uuid
import time
from datetime import datetime
from collections import defaultdict

from event_bus import global_event_bus, EventTypes

class ConceptHierarchy:
    """
    Manages hierarchical relationships between concepts with
    explicit focus on developing multi-level abstractions.
    """
    
    def __init__(self, event_bus=None):
        """Initialize the concept hierarchy system"""
        self.event_bus = event_bus or global_event_bus
        
        # Core data structure: concepts and their hierarchical relationships
        self.concepts = {}  # Concept storage
        self.hierarchical_relationships = []  # Parent-child relationships
        
        # Track abstraction levels explicitly
        self.abstraction_levels = defaultdict(list)  # Maps level -> [concept_ids]
        self.max_observed_depth = 1  # Track the maximum hierarchy depth we've seen
        
        # Promotion criteria thresholds
        self.promotion_thresholds = {
            'usage_count': 5,       # How often a concept must be used before promotion
            'generality': 0.7,      # How general a concept must be (0-1)
            'connection_density': 3, # Minimum connections to other concepts
            'abstraction_score': 0.6 # Minimum abstraction score to be promoted
        }
        
    def add_concept(self, concept_id, concept_data, level=0):
        """
        Add a concept to the hierarchy at a specific abstraction level
        
        Args:
            concept_id: Unique ID for the concept
            concept_data: Concept information dictionary
            level: Initial abstraction level (0=concrete, higher=more abstract)
            
        Returns:
            The concept ID
        """
        if concept_id in self.concepts:
            # Update existing concept
            self.concepts[concept_id].update(concept_data)
            return concept_id
            
        # Create new concept with explicit abstraction tracking
        concept = {
            'id': concept_id,
            'name': concept_data.get('name', ''),
            'properties': concept_data.get('properties', {}),
            'abstraction_level': level,
            'created': datetime.now().isoformat(),
            'usage_count': 0,
            'generality_score': 0.0,
            'children': [],
            'parents': []
        }
        
        self.concepts[concept_id] = concept
        self.abstraction_levels[level].append(concept_id)
        
        # Emit concept creation event
        self.event_bus.publish(EventTypes.CONCEPT_CREATED, {
            'concept_id': concept_id,
            'concept_name': concept.get('name', ''),
            'abstraction_level': level,
            'timestamp': datetime.now().isoformat()
        })
        
        return concept_id
    
    def create_hierarchical_relationship(self, parent_id, child_id, relationship_type='is_a'):
        """
        Create a hierarchical relationship between two concepts
        
        Args:
            parent_id: ID of the parent (more abstract) concept
            child_id: ID of the child (more concrete) concept
            relationship_type: Type of hierarchical relationship
            
        Returns:
            ID of the created relationship
        """
        if parent_id not in self.concepts or child_id not in self.concepts:
            return None
            
        # Get the concepts
        parent = self.concepts[parent_id]
        child = self.concepts[child_id]
        
        # Create relationship ID
        rel_id = str(uuid.uuid4())
        
        # Create relationship
        relationship = {
            'id': rel_id,
            'parent': parent_id,
            'child': child_id,
            'type': relationship_type,
            'created': datetime.now().isoformat()
        }
        
        # Update the concepts
        if child_id not in parent['children']:
            parent['children'].append(child_id)
        
        if parent_id not in child['parents']:
            child['parents'].append(parent_id)
        
        # Add to relationships list
        self.hierarchical_relationships.append(relationship)
        
        # Check if this creates a deeper hierarchy
        self._update_hierarchy_depth()
        
        # Emit hierarchy change event
        self.event_bus.publish(EventTypes.CONCEPT_HIERARCHY_MODIFIED, {
            'relationship_id': rel_id,
            'parent_id': parent_id,
            'child_id': child_id,
            'type': relationship_type,
            'timestamp': datetime.now().isoformat()
        })
        
        return rel_id
    
    def promote_concept(self, concept_id):
        """
        Promote a concept to a higher abstraction level
        
        Args:
            concept_id: ID of the concept to promote
            
        Returns:
            New abstraction level or None if promotion failed
        """
        if concept_id not in self.concepts:
            return None
            
        concept = self.concepts[concept_id]
        current_level = concept['abstraction_level']
        new_level = current_level + 1
        
        # Remove from current level
        if concept_id in self.abstraction_levels[current_level]:
            self.abstraction_levels[current_level].remove(concept_id)
        
        # Add to new level
        self.abstraction_levels[new_level].append(concept_id)
        
        # Update the concept
        concept['abstraction_level'] = new_level
        
        # Update max depth if needed
        self._update_hierarchy_depth()
        
        # Emit promotion event
        self.event_bus.publish(EventTypes.CONCEPT_PROMOTED, {
            'concept_id': concept_id,
            'old_level': current_level,
            'new_level': new_level,
            'timestamp': datetime.now().isoformat()
        })
        
        return new_level
    
    def find_promotion_candidates(self):
        """
        Find concepts that are candidates for promotion to higher abstraction levels
        
        Returns:
            List of concept IDs that meet promotion criteria
        """
        candidates = []
        
        for concept_id, concept in self.concepts.items():
            # Skip concepts that are already at high abstraction levels
            if concept['abstraction_level'] >= 3:
                continue
                
            # Check promotion criteria
            if (concept['usage_count'] >= self.promotion_thresholds['usage_count'] and
                concept['generality_score'] >= self.promotion_thresholds['generality'] and
                len(concept['children']) >= self.promotion_thresholds['connection_density']):
                
                candidates.append(concept_id)
                
        return candidates
    
    def auto_promote_concepts(self):
        """
        Automatically promote concepts that meet the criteria
        
        Returns:
            Number of concepts promoted
        """
        candidates = self.find_promotion_candidates()
        promoted_count = 0
        
        for concept_id in candidates:
            self.promote_concept(concept_id)
            promoted_count += 1
            
        return promoted_count
    
    def suggest_new_abstractions(self, concepts):
        """
        Suggest new abstract concepts based on patterns in existing concepts
        
        Args:
            concepts: Dictionary of concepts to analyze for patterns
            
        Returns:
            List of suggested abstract concepts
        """
        # Group concepts by common properties
        property_groups = defaultdict(list)
        
        # Analyze concepts for common properties
        for concept_id, concept in concepts.items():
            if 'properties' not in concept:
                continue
                
            for prop_name, prop_value in concept['properties'].items():
                # Use string representation as a key
                key = f"{prop_name}:{prop_value}"
                property_groups[key].append(concept_id)
        
        # Find groups with multiple members (candidates for abstraction)
        suggestions = []
        
        for prop_key, member_ids in property_groups.items():
            if len(member_ids) >= 3:  # Require at least 3 concepts to suggest an abstraction
                prop_name, prop_value = prop_key.split(':', 1)
                
                # Create suggestion
                suggestion = {
                    'name': f"Abstract_{prop_name.capitalize()}",
                    'property': prop_name,
                    'value': prop_value,
                    'member_concepts': member_ids,
                    'score': len(member_ids) * 0.1  # Simple scoring function
                }
                
                suggestions.append(suggestion)
        
        # Sort by score (descending)
        suggestions.sort(key=lambda x: x['score'], reverse=True)
        
        return suggestions
    
    def create_abstraction_from_suggestion(self, suggestion):
        """
        Create a new abstract concept from a suggestion
        
        Args:
            suggestion: Suggestion dict from suggest_new_abstractions
            
        Returns:
            ID of the created abstract concept
        """
        # Create the abstract concept
        abstract_concept_data = {
            'name': suggestion['name'],
            'properties': {
                'is_abstraction': True,
                suggestion['property']: suggestion['value']
            }
        }
        
        # Determine appropriate abstraction level (one higher than members)
        member_levels = [
            self.concepts[member_id]['abstraction_level']
            for member_id in suggestion['member_concepts']
            if member_id in self.concepts
        ]
        
        target_level = 1 + max(member_levels) if member_levels else 1
        
        # Create the new abstract concept
        abstract_id = str(uuid.uuid4())
        self.add_concept(abstract_id, abstract_concept_data, level=target_level)
        
        # Create hierarchical relationships with members
        for member_id in suggestion['member_concepts']:
            if member_id in self.concepts:
                self.create_hierarchical_relationship(abstract_id, member_id)
        
        # Update max depth
        self._update_hierarchy_depth()
        
        return abstract_id
    
    def get_concept_hierarchy_data(self):
        """
        Get concept hierarchy data for visualization
        
        Returns:
            Dictionary with hierarchy data
        """
        # Organize concepts by level
        levels = {}
        for level, concept_ids in self.abstraction_levels.items():
            levels[level] = [
                {
                    'id': concept_id,
                    'name': self.concepts[concept_id]['name'],
                    'children': self.concepts[concept_id]['children'],
                    'parents': self.concepts[concept_id]['parents']
                }
                for concept_id in concept_ids
                if concept_id in self.concepts
            ]
        
        # Get relationships data
        relationships = []
        for rel in self.hierarchical_relationships:
            # Only include relationships where both concepts still exist
            if rel['parent'] in self.concepts and rel['child'] in self.concepts:
                relationships.append({
                    'id': rel['id'],
                    'parent': rel['parent'],
                    'child': rel['child'],
                    'type': rel['type']
                })
        
        return {
            'levels': levels,
            'relationships': relationships,
            'max_depth': self.max_observed_depth,
            'total_concepts': len(self.concepts),
            'level_distribution': {
                str(level): len(concepts)
                for level, concepts in self.abstraction_levels.items()
            }
        }
    
    def analyze_concept_abstraction(self, concept_data, reference_concepts=None):
        """
        Analyze how abstract a concept is based on its properties
        
        Args:
            concept_data: The concept to analyze
            reference_concepts: Optional dictionary of concepts to use as reference
            
        Returns:
            Abstraction score (0-1) and suggested abstraction level
        """
        # Default score if we can't calculate
        default_score = 0.3
        
        # If no reference concepts, use our existing concepts
        if reference_concepts is None:
            reference_concepts = self.concepts
            
        # If we don't have enough concepts for comparison
        if len(reference_concepts) < 5:
            return default_score, 0
            
        # Extract features for abstraction scoring
        properties_count = len(concept_data.get('properties', {}))
        is_explicitly_abstract = concept_data.get('properties', {}).get('is_abstraction', False)
        word_length = len(concept_data.get('name', ''))
        
        # Calculate base abstraction score
        abstraction_score = 0.0
        
        # Fewer properties often means more abstract
        property_factor = max(0.0, 1.0 - (properties_count / 10))
        abstraction_score += property_factor * 0.4
        
        # Explicitly abstract concepts get a boost
        if is_explicitly_abstract:
            abstraction_score += 0.3
            
        # Short names are often more abstract
        if word_length <= 5:
            abstraction_score += 0.2
        elif word_length <= 10:
            abstraction_score += 0.1
            
        # Suggested level based on score
        if abstraction_score >= 0.8:
            suggested_level = 3  # Very abstract
        elif abstraction_score >= 0.6:
            suggested_level = 2  # Moderately abstract
        elif abstraction_score >= 0.4:
            suggested_level = 1  # Somewhat abstract
        else:
            suggested_level = 0  # Concrete
            
        return abstraction_score, suggested_level
    
    def enhance_hierarchy(self):
        """
        Actively enhance the concept hierarchy by identifying patterns
        and creating new abstractions
        
        Returns:
            Number of new abstractions created
        """
        # Skip if we don't have enough concepts to work with
        if len(self.concepts) < 5:
            return 0
            
        # First, find promotion candidates and promote them
        promotion_count = self.auto_promote_concepts()
        
        # Then look for patterns that could become new abstractions
        suggestions = self.suggest_new_abstractions(self.concepts)
        
        # Create new abstractions from top suggestions
        abstraction_count = 0
        for suggestion in suggestions[:3]:  # Only use top 3 suggestions
            if suggestion['score'] > 0.3:  # Only use reasonably good suggestions
                self.create_abstraction_from_suggestion(suggestion)
                abstraction_count += 1
                
        # Return the total number of hierarchy improvements
        return promotion_count + abstraction_count
    
    def _update_hierarchy_depth(self):
        """
        Update the maximum observed hierarchy depth
        
        Returns:
            Current maximum hierarchy depth
        """
        if not self.abstraction_levels:
            self.max_observed_depth = 0
            return 0
            
        max_level = max(self.abstraction_levels.keys())
        
        # Only update if we found a deeper level
        if max_level > self.max_observed_depth:
            self.max_observed_depth = max_level
            
            # Emit event for a new max depth
            self.event_bus.publish(EventTypes.HIERARCHY_DEPTH_INCREASED, {
                'old_depth': self.max_observed_depth - 1,
                'new_depth': self.max_observed_depth,
                'timestamp': datetime.now().isoformat()
            })
            
        return self.max_observed_depth