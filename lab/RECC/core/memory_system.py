import time
import uuid
import math
import random
from collections import defaultdict, deque

class MemorySystem:
    """
    Enhanced memory system that manages all experiences, concepts,
    and their interconnections using hierarchical structures.
    
    The memory system is central to the mind's ability to:
    1. Store and retrieve experiences
    2. Form and evolve concepts over time
    3. Connect related memories into meaningful structures
    4. Support recursive self-reference through memory reuse
    """
    
    def __init__(self):
        # External experiences (from environment)
        self.experiences = []
        
        # Internal experiences (from reflection and self-reference)
        self.internal_experiences = []
        
        # Hierarchical memory structures
        self.hierarchies = {
            'time': {},      # Time-based organization
            'concept': {},   # Concept-based organization
            'emotion': {},   # Emotion-based organization
            'salience': {}   # Importance-based organization
        }
        
        # Concept graph for semantic relationships
        self.concept_graph = {
            'nodes': {},  # Concepts as nodes
            'edges': []   # Relationships as edges
        }
        
        # Add metrics dictionary for tracking reuse, etc.
        self.metrics = {
            'total_experiences': 0,
            'internal_experiences': 0,
            'external_experiences': 0,
            'total_concept_accesses': 0,
            'unique_concepts_accessed': set(),
            'recent_access_window': deque(maxlen=100) # Track recent concept accesses
        }

        # Consolidation metrics
        self.last_consolidation = time.time()
        self.consolidation_count = 0
        self.concept_evolution_metrics = {
            'concepts_formed': 0,
            'concepts_evolved': 0,
            'hierarchies_created': 0
        }
    
    # Rename record_experience to process_and_store and adjust signature
    def process_and_store(self, input_data, output_data, emotional_state, 
                         entropy_at_experience, is_internal=False, tags=None):
        """
        Process and store a new experience in memory, including output.
        Renamed from record_experience.
        
        Args:
            input_data: Content of the experience input/stimulus
            output_data: Content of the behavior output/result
            emotional_state: Emotional state during the experience
            entropy_at_experience: System entropy when experience occurred
            is_internal: Whether this is an internal experience
            tags: List of concept tags associated with this experience
            
        Returns:
            str: The ID of the recorded experience
        """
        # Create a unique ID for the experience
        exp_id = str(uuid.uuid4())
        
        # Create tags if none provided
        if tags is None:
            # Basic tag extraction (placeholder)
            tags = self._extract_tags(input_data, output_data)
            
        # Extract timestamp
        timestamp = time.time()
        
        # Create the experience object, including output_data
        experience = {
            'id': exp_id,
            'input': input_data,
            'output': output_data, # Added output_data
            'timestamp': timestamp,
            'emotional_state': emotional_state,
            'is_internal': is_internal,
            'tags': tags,
            'entropy_at_experience': entropy_at_experience,
            'access_count': 0,
            'reuse_count': 0,
            'last_access': timestamp,
            'salience': 1.0,  # Initial importance
        }
        
        # Store in the appropriate list
        if is_internal:
            self.internal_experiences.append(experience)
            self.metrics['internal_experiences'] += 1
        else:
            self.experiences.append(experience)
            self.metrics['external_experiences'] += 1
        self.metrics['total_experiences'] += 1
            
        # Add to time-based hierarchy
        self._add_to_time_hierarchy(experience)
        
        # Add to concept-based hierarchy for each tag
        for tag in tags:
            self._add_to_concept_hierarchy(experience, tag)
            
            # Ensure concept exists in graph and update access metrics
            self._ensure_concept_in_graph(tag)
            self._track_concept_access(tag) # Track access for reuse calculation
        
        # Return the ID
        return exp_id 

    def _extract_tags(self, input_data, output_data):
        """Placeholder for basic tag extraction from experience data."""
        tags = set()
        # Simple keyword extraction (example)
        words = (str(input_data) + " " + str(output_data)).lower().split()
        common_words = {'the', 'a', 'is', 'in', 'it', 'of', 'to', 'and'}
        for word in words:
            if len(word) > 3 and word not in common_words:
                tags.add(word.strip('.,!?;:'))
        return list(tags)[:5] # Limit number of tags

    def record_self_reference(self, reference_data):
        """
        Record a self-reference event as an internal experience
        
        Args:
            reference_data: Data describing the self-reference
            
        Returns:
            dict: The recorded experience
        """
        # Extract key information from reference
        ref_type = reference_data.get('type', 'unknown')
        insight = reference_data.get('insight', 'Self-reference event')
        source = reference_data.get('source_type', 'unknown')
        target = reference_data.get('target_type', 'unknown')
        depth = reference_data.get('depth', 1)
        
        # Create tags based on reference information
        tags = ['self_reference', ref_type, f'depth_{depth}', source, target]
        
        # Create descriptive input for the experience
        input_data = f"Self-Reference: {insight} (Depth: {depth})"
        
        # Record as internal experience
        return self.process_and_store(
            input_data=input_data,
            output_data="", # No output data for self-reference
            emotional_state={}, # Or capture emotion state during reflection?
            is_internal=True,
            tags=tags,
            entropy_at_experience=reference_data.get('entropy_impact', 0.0)
        )
    
    def _add_to_time_hierarchy(self, experience):
        """Add experience to time-based hierarchy"""
        # Calculate time buckets for hierarchical organization
        timestamp = experience.get('timestamp', time.time())
        day = int(timestamp / 86400)  # days since epoch
        hour = int((timestamp % 86400) / 3600)  # hour within day
        
        # Ensure day exists in hierarchy
        if day not in self.hierarchies['time']:
            self.hierarchies['time'][day] = {}
            
        # Ensure hour exists in day
        if hour not in self.hierarchies['time'][day]:
            self.hierarchies['time'][day][hour] = []
            
        # Add to appropriate bucket
        self.hierarchies['time'][day][hour].append(experience['id'])
    
    def _add_to_concept_hierarchy(self, experience, concept):
        """Add experience to concept-based hierarchy"""
        # Ensure concept exists in hierarchy
        if concept not in self.hierarchies['concept']:
            self.hierarchies['concept'][concept] = {
                'primary': [],    # Directly tagged with this concept
                'secondary': [],  # Related to this concept
                'abstract': []    # Higher-level abstractions of this concept
            }
            
        # Add to primary bucket for this concept
        self.hierarchies['concept'][concept]['primary'].append(experience['id'])
    
    def _ensure_concept_in_graph(self, concept):
        """Ensure concept exists in concept graph"""
        if concept not in self.concept_graph['nodes']:
            # Create new concept node
            self.concept_graph['nodes'][concept] = {
                'first_seen': time.time(),
                'usage_count': 1,
                'salience': 0.5,  # Initial importance
                'abstraction_level': 0.0,  # Concrete by default
                'related_concepts': [],
                'properties': {}
            }
            
            # Update metrics
            self.concept_evolution_metrics['concepts_formed'] += 1
        else:
            # Update existing concept
            self.concept_graph['nodes'][concept]['usage_count'] += 1
    
    def _track_concept_access(self, concept):
        """Tracks concept access for reuse calculation."""
        self.metrics['total_concept_accesses'] += 1
        self.metrics['unique_concepts_accessed'].add(concept)
        self.metrics['recent_access_window'].append(concept)

    def create_concept_relationship(self, concept1, concept2, relationship_type, strength=0.5):
        """
        Create a relationship between two concepts
        
        Args:
            concept1: First concept
            concept2: Second concept
            relationship_type: Type of relationship
            strength: Strength of relationship (0-1)
            
        Returns:
            dict: The created relationship
        """
        # Ensure both concepts exist
        self._ensure_concept_in_graph(concept1)
        self._ensure_concept_in_graph(concept2)
        
        # Create relationship
        relationship = {
            'source': concept1,
            'target': concept2,
            'type': relationship_type,
            'strength': strength,
            'created': time.time()
        }
        
        # Add to graph
        self.concept_graph['edges'].append(relationship)
        
        # Update related concepts lists
        if concept2 not in self.concept_graph['nodes'][concept1]['related_concepts']:
            self.concept_graph['nodes'][concept1]['related_concepts'].append(concept2)
            
        if concept1 not in self.concept_graph['nodes'][concept2]['related_concepts']:
            self.concept_graph['nodes'][concept2]['related_concepts'].append(concept1)
        
        return relationship
    
    def retrieve_by_concept(self, concept, limit=10, include_secondary=True):
        """
        Retrieve experiences related to a concept
        
        Args:
            concept: Concept to retrieve by
            limit: Maximum number of experiences to retrieve
            include_secondary: Whether to include secondary relations
            
        Returns:
            list: Relevant experiences
        """
        exp_ids = []
        results = []
        
        # Check if concept exists
        if concept not in self.hierarchies['concept']:
            return []
            
        # Get primary experiences
        primary_ids = self.hierarchies['concept'][concept]['primary']
        exp_ids.extend(primary_ids)
        
        # Add secondary if requested
        if include_secondary and len(exp_ids) < limit:
            secondary_ids = self.hierarchies['concept'][concept]['secondary']
            exp_ids.extend(secondary_ids)
        
        # Get unique IDs up to limit
        exp_ids = list(set(exp_ids))[:limit]
        
        # Retrieve full experiences
        for exp_id in exp_ids:
            experience = self._get_experience_by_id(exp_id)
            if experience:
                # Update access metrics
                experience['access_count'] += 1
                experience['last_access'] = time.time()
                
                # Track concept access for reuse
                for tag in experience.get('tags', []):
                    if tag == concept:
                         self._track_concept_access(tag)
                         # Increment reuse count on the experience itself if retrieved by concept?
                         experience['reuse_count'] = experience.get('reuse_count', 0) + 1
                
                results.append(experience)
        
        return results
    
    def _get_experience_by_id(self, exp_id):
        """Retrieve an experience by ID"""
        # Search in external experiences
        for exp in self.experiences:
            if exp['id'] == exp_id:
                return exp
                
        # Search in internal experiences
        for exp in self.internal_experiences:
            if exp['id'] == exp_id:
                return exp
                
        return None
        
    def get_recent_experiences(self, count=10):
        """
        Get most recent external experiences
        
        Args:
            count: Number of experiences to retrieve
            
        Returns:
            list: Recent experiences
        """
        # Sort by timestamp
        sorted_exps = sorted(
            self.experiences, 
            key=lambda x: x.get('timestamp', 0), 
            reverse=True
        )
        
        # Return requested count
        return sorted_exps[:count]
    
    def get_internal_experiences(self, count=10):
        """
        Get most recent internal experiences
        
        Args:
            count: Number of experiences to retrieve
            
        Returns:
            list: Recent internal experiences
        """
        # Sort by timestamp
        sorted_exps = sorted(
            self.internal_experiences, 
            key=lambda x: x.get('timestamp', 0), 
            reverse=True
        )
        
        # Return requested count
        return sorted_exps[:count]
    
    def search_by_tags(self, tags, require_all=False, limit=10):
        """
        Search for experiences with specific tags
        
        Args:
            tags: List of tags to search for
            require_all: Whether all tags must be present
            limit: Maximum number of results
            
        Returns:
            list: Matching experiences
        """
        results = []
        
        # Combine all experiences
        all_exps = self.experiences + self.internal_experiences
        
        # Filter by tags
        for exp in all_exps:
            exp_tags = exp.get('tags', [])
            
            if require_all:
                # All tags must match
                if all(tag in exp_tags for tag in tags):
                    results.append(exp)
            else:
                # Any tag can match
                if any(tag in exp_tags for tag in tags):
                    results.append(exp)
                    
            # Stop if we have enough results
            if len(results) >= limit:
                break
                
        return results
    
    def consolidate_memories(self):
        """
        Periodically consolidate memories to:
        1. Form new concepts
        2. Create relationships between concepts
        3. Update memory hierarchies
        4. Adjust saliency
        
        Returns:
            dict: Results of consolidation
        """
        now = time.time()
        
        # Calculate time since last consolidation
        time_since_last = now - self.last_consolidation
        self.last_consolidation = now
        
        # Prepare results
        results = {
            'timestamp': now,
            'new_concepts': [],
            'new_relationships': [],
            'hierarchies_updated': [],
            'time_since_last': time_since_last
        }
        
        # 1. Update concept usage from recent experiences
        self._update_concept_usage()
        
        # 2. Find related concepts based on co-occurrence
        new_relationships = self._find_related_concepts()
        results['new_relationships'] = new_relationships
        
        # 3. Identify potential new abstract concepts
        new_concepts = self._identify_new_concepts()
        results['new_concepts'] = new_concepts
        
        # 4. Update memory hierarchy organization
        updated_hierarchies = self._update_hierarchies()
        results['hierarchies_updated'] = updated_hierarchies
        
        # 5. Update experience salience
        self._update_experience_salience()
        
        # Update consolidation count
        self.consolidation_count += 1
        
        return results
    
    def _update_concept_usage(self):
        """Update concept usage statistics from recent experiences"""
        # Get recent experiences
        recent_exps = self.get_recent_experiences(20) + self.get_internal_experiences(10)
        
        # Count concept occurrences
        concept_counts = defaultdict(int)
        for exp in recent_exps:
            for tag in exp.get('tags', []):
                concept_counts[tag] += 1
                
        # Update concept graph with new counts
        for concept, count in concept_counts.items():
            if concept in self.concept_graph['nodes']:
                # Update existing concept
                node = self.concept_graph['nodes'][concept]
                node['usage_count'] += count
                
                # Increase salience based on recent usage
                node['salience'] = min(1.0, node['salience'] + 0.05 * count)
                
                # Record concept evolution
                self.concept_evolution_metrics['concepts_evolved'] += 1
            else:
                # This is handled by ensure_concept_in_graph but check just in case
                self._ensure_concept_in_graph(concept)
    
    def _find_related_concepts(self):
        """Find relationships between concepts based on co-occurrence"""
        new_relationships = []
        
        # Get all experiences
        all_exps = self.experiences + self.internal_experiences
        
        # Track concept co-occurrences
        co_occurrences = defaultdict(int)
        
        # Count co-occurrences in experiences
        for exp in all_exps:
            tags = exp.get('tags', [])
            
            # Skip if less than 2 tags
            if len(tags) < 2:
                continue
                
            # Count each unique pair
            for i, tag1 in enumerate(tags):
                for tag2 in tags[i+1:]:
                    # Create sorted key for consistency
                    key = tuple(sorted([tag1, tag2]))
                    co_occurrences[key] += 1
        
        # Create relationships for concepts with significant co-occurrence
        for (concept1, concept2), count in co_occurrences.items():
            # Skip if relationship already exists
            if self._relationship_exists(concept1, concept2):
                continue
                
            # Only create relationship if sufficient co-occurrence
            if count >= 2:
                # Calculate relationship strength
                strength = min(0.9, 0.3 + (count * 0.1))
                
                # Create relationship
                relationship = self.create_concept_relationship(
                    concept1, concept2, 'co-occurrence', strength
                )
                
                new_relationships.append({
                    'source': concept1,
                    'target': concept2,
                    'type': 'co-occurrence',
                    'strength': strength,
                    'count': count
                })
        
        return new_relationships
    
    def _relationship_exists(self, concept1, concept2):
        """Check if a relationship already exists between concepts"""
        for edge in self.concept_graph['edges']:
            # Check both directions
            if ((edge['source'] == concept1 and edge['target'] == concept2) or
                (edge['source'] == concept2 and edge['target'] == concept1)):
                return True
                
        return False
    
    def _identify_new_concepts(self):
        """Identify potential new abstract concepts"""
        new_concepts = []
        
        # Find clusters of related concepts
        clusters = self._find_concept_clusters()
        
        # Generate abstract concepts from significant clusters
        for i, cluster in enumerate(clusters):
            # Skip small clusters
            if (len(cluster) < 3):
                continue
                
            # Create abstract concept name
            abstract_name = f"abstract_concept_{i}_{int(time.time())}"
            
            # Create the concept
            self._ensure_concept_in_graph(abstract_name)
            
            # Set as abstract
            self.concept_graph['nodes'][abstract_name]['abstraction_level'] = 0.7
            
            # Create relationships to member concepts
            for concept in cluster:
                self.create_concept_relationship(
                    abstract_name, concept, 'abstraction', 0.6
                )
            
            new_concepts.append({
                'name': abstract_name,
                'members': cluster,
                'abstraction_level': 0.7
            })
            
            # Update metrics
            self.concept_evolution_metrics['concepts_formed'] += 1
        
        return new_concepts
    
    def _find_concept_clusters(self):
        """Find clusters of related concepts in the graph"""
        # Simple clustering based on relationship density
        clusters = []
        visited = set()
        
        # Examine each concept as a potential cluster seed
        for concept in self.concept_graph['nodes']:
            # Skip if already in a cluster
            if concept in visited:
                continue
                
            # Get related concepts
            related = self._get_related_concepts(concept, min_strength=0.4)
            
            # Form cluster if enough related concepts
            if len(related) >= 2:
                cluster = [concept] + related
                clusters.append(cluster)
                
                # Mark all as visited
                for c in cluster:
                    visited.add(c)
        
        return clusters
    
    def _get_related_concepts(self, concept, min_strength=0.0):
        """Get concepts related to a given concept"""
        related = []
        
        for edge in self.concept_graph['edges']:
            # Check outgoing relationships
            if edge['source'] == concept and edge['strength'] >= min_strength:
                related.append(edge['target'])
                
            # Check incoming relationships
            elif edge['target'] == concept and edge['strength'] >= min_strength:
                related.append(edge['source'])
                
        return related
    
    def _update_hierarchies(self):
        """Update hierarchical organization of memories"""
        updated = []
        
        # Update concept hierarchies
        for concept, hierarchy in self.hierarchies['concept'].items():
            # Skip if not enough primary examples
            if len(hierarchy['primary']) < 3:
                continue
                
            # Find secondary relationships
            node = self.concept_graph['nodes'].get(concept)
            if node:
                related = node.get('related_concepts', [])
                
                # Add experiences from related concepts as secondary
                for related_concept in related:
                    if related_concept in self.hierarchies['concept']:
                        related_exps = self.hierarchies['concept'][related_concept]['primary']
                        
                        # Add only new secondary relationships
                        for exp_id in related_exps:
                            if exp_id not in hierarchy['secondary'] and exp_id not in hierarchy['primary']:
                                hierarchy['secondary'].append(exp_id)
                                
                # Record update
                updated.append({
                    'hierarchy': 'concept',
                    'concept': concept,
                    'secondary_count': len(hierarchy['secondary'])
                })
                
                # Update metrics
                self.concept_evolution_metrics['hierarchies_created'] += 1
        
        return updated
    
    def _update_experience_salience(self):
        """Update salience of experiences based on various factors"""
        now = time.time()
        
        # Update all experiences
        for exp_list in [self.experiences, self.internal_experiences]:
            for exp in exp_list:
                # Start with base salience
                base_salience = exp.get('salience', 0.5)
                
                # Factors affecting salience
                
                # 1. Recency decay
                age_seconds = now - exp.get('timestamp', now)
                age_days = age_seconds / 86400
                recency_factor = math.exp(-0.05 * age_days)  # Exponential decay
                
                # 2. Access frequency boost
                access_count = exp.get('access_count', 0)
                access_factor = min(2.0, 1.0 + (0.1 * access_count))
                
                # 3. Reuse importance boost
                reuse_count = exp.get('reuse_count', 0)
                reuse_factor = min(3.0, 1.0 + (0.3 * reuse_count))
                
                # 4. Tag importance
                tag_importance = 1.0
                for tag in exp.get('tags', []):
                    if tag in self.concept_graph['nodes']:
                        tag_importance = max(tag_importance, 
                                           self.concept_graph['nodes'][tag].get('salience', 0.5))
                
                # Calculate new salience
                new_salience = base_salience * recency_factor * access_factor * reuse_factor * tag_importance
                
                # Apply bounds
                exp['salience'] = max(0.1, min(1.0, new_salience))
    
    def get_concept_statistics(self):
        """
        Get statistics about concepts
        
        Returns:
            dict: Concept statistics
        """
        if not self.concept_graph['nodes']:
            return {
                'count': 0,
                'avg_usage': 0,
                'avg_salience': 0,
                'relationship_count': 0
            }
            
        # Calculate statistics
        concepts = list(self.concept_graph['nodes'].values())
        count = len(concepts)
        avg_usage = sum(c.get('usage_count', 0) for c in concepts) / count
        avg_salience = sum(c.get('salience', 0) for c in concepts) / count
        relationship_count = len(self.concept_graph['edges'])
        
        return {
            'count': count,
            'avg_usage': avg_usage,
            'avg_salience': avg_salience,
            'relationship_count': relationship_count,
            'evolution_metrics': self.concept_evolution_metrics
        }
    
    def get_most_salient_experiences(self, count=5):
        """
        Get most important experiences based on salience
        
        Args:
            count: Number of experiences to retrieve
            
        Returns:
            list: Important experiences
        """
        # Combine and sort by salience
        all_exps = self.experiences + self.internal_experiences
        sorted_exps = sorted(
            all_exps, 
            key=lambda x: x.get('salience', 0), 
            reverse=True
        )
        
        return sorted_exps[:count]
    
    def get_memory_usage(self):
        """
        Get memory usage statistics
        
        Returns:
            dict: Memory usage statistics
        """
        return {
            'experience_count': len(self.experiences),
            'internal_experience_count': len(self.internal_experiences),
            'concept_count': len(self.concept_graph['nodes']),
            'relationship_count': len(self.concept_graph['edges']),
            'hierarchy_count': sum(len(h) for h in self.hierarchies.values())
        }

    def calculate_memory_reuse_ratio(self):
        """Calculates the ratio of reused concepts/experiences recently."""
        # Uses the recent_access_window deque
        recent_accesses = list(self.metrics['recent_access_window'])
        total_accesses = len(recent_accesses)
        
        if total_accesses == 0:
            return 0.0 # No accesses yet
            
        unique_accesses = len(set(recent_accesses))
        
        if total_accesses == unique_accesses:
             return 0.0 # All unique, no reuse in recent window

        # Ratio of non-unique accesses to total accesses in the window
        reuse_count = total_accesses - unique_accesses
        reuse_ratio = reuse_count / total_accesses
        
        # Decay unique concept set periodically to focus on recent activity
        if self.metrics['total_concept_accesses'] % 100 == 0: 
             self.metrics['unique_concepts_accessed'] = set(recent_accesses)
             
        return reuse_ratio

    def calculate_graph_sparsity(self):
        """Calculates the sparsity of the concept graph."""
        # Sparsity = 1 - density
        # Density = 2 * num_edges / (num_nodes * (num_nodes - 1))
        num_nodes = len(self.concept_graph['nodes'])
        num_edges = len(self.concept_graph['edges'])

        if num_nodes < 2:
            return 1.0 # Max sparsity if less than 2 nodes

        max_possible_edges = num_nodes * (num_nodes - 1)
        if max_possible_edges == 0:
             return 1.0 # Avoid division by zero

        density = (2.0 * num_edges) / max_possible_edges
        sparsity = 1.0 - density
        return max(0.0, min(1.0, sparsity)) # Clamp between 0 and 1

    def calculate_complexity(self):
        """
        Calculate the complexity of the memory structures
        as a metric of cognitive development.
        """
        # Placeholder - combine various metrics
        concept_count = len(self.concept_graph['nodes'])
        edge_count = len(self.concept_graph['edges'])
        experience_count = self.metrics['total_experiences']
        
        # Simple complexity measure (needs refinement)
        complexity = (math.log1p(concept_count) * 0.4 + 
                      math.log1p(edge_count) * 0.3 + 
                      math.log1p(experience_count) * 0.3)
        return complexity

    def calculate_concept_network_density(self):
        """
        Calculates the density of the concept graph.
        Density = 1 - Sparsity
        """
        return 1.0 - self.calculate_graph_sparsity()

    def store_reflection_insight(self, insight):
        """
        Store a new insight generated through reflection
        as a special type of internal experience.
        """
        # Example insight structure: {'text': '...', 'concepts': [...], 'source_exp_ids': [...]} 
        input_data = f"Reflection Insight: {insight.get('text', 'No details')}"
        tags = ['reflection', 'insight'] + insight.get('concepts', [])
        # Link to source experiences if available (needs more structure)
        
        self.process_and_store(
            input_data=input_data,
            output_data="", # No output data for reflection insight
            emotional_state={}, # Or capture emotion state during reflection?
            is_internal=True,
            tags=tags,
            entropy_at_experience=insight.get('entropy_at_insight', 0.0)
        )