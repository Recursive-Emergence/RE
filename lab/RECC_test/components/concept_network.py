"""
ConceptNetwork Module
Handles concept extraction, relation building, and network analysis
"""
import uuid
import re
from datetime import datetime
import networkx as nx
import matplotlib.pyplot as plt

from event_bus import global_event_bus, EventTypes

class ConceptNetwork:
    def __init__(self, event_bus=None):
        self.graph = nx.DiGraph()
        self.concepts = {}  # Map concept ID to concept object
        self.relations = [] # List of relations between concepts
        self.last_updated = datetime.now()
        
        # Store reference to event bus (or use global)
        self.event_bus = event_bus or global_event_bus
        
        # Config for network size management
        self.max_concepts = 300  # Maximum number of concepts to keep
        self.max_relations = 1000  # Maximum number of relations to keep
        self.inactive_threshold = 0.2  # Concepts with activation below this are candidates for pruning
    
    def add_concept(self, name, source="dialogue", properties=None):
        """Add a new concept to the network"""
        concept_id = str(uuid.uuid4())
        normalized_name = name.lower().strip()
        
        # Check if concept already exists
        for c_id, concept in self.concepts.items():
            if concept['name'].lower().strip() == normalized_name:
                return c_id  # Return existing concept ID
        
        # Create new concept
        self.concepts[concept_id] = {
            'id': concept_id,
            'name': name,
            'created': datetime.now().isoformat(),
            'source': source,
            'properties': properties or {},
            'activation': 1.0,  # Initial activation
            'reuse_count': 0    # How often the concept is reused
        }
        self.graph.add_node(concept_id, **self.concepts[concept_id])
        return concept_id
    
    def add_relation(self, source_id, target_id, relation_type="association", weight=0.5, properties=None):
        """Add a relation between concepts"""
        # Ensure both concepts exist
        if source_id not in self.concepts or target_id not in self.concepts:
            return None
            
        relation_id = str(uuid.uuid4())
        relation = {
            'id': relation_id,
            'source': source_id,
            'target': target_id,
            'type': relation_type,
            'weight': weight,
            'created': datetime.now().isoformat(),
            'properties': properties or {}
        }
        
        # Check if relation already exists
        for r in self.relations:
            if r['source'] == source_id and r['target'] == target_id and r['type'] == relation_type:
                # Update weight if it exists
                r['weight'] = max(r['weight'], weight)
                return r['id']
        
        self.relations.append(relation)
        self.graph.add_edge(source_id, target_id, **relation)
        return relation_id
    
    def extract_concepts_from_text(self, text):
        """
        Extract concepts from text and add them to the network.
        Enhanced to capture more organic concepts beyond just the predefined list.
        """
        # Default concept candidates - foundational concepts we're interested in
        candidates = [
            'spiral', 'loop', 'star', 'growth', 'iteration', 'cycle', 'flow', 'balance', 
            'continuum', 'pattern', 'unity', 'transformation', 'emotion', 'feeling', 'mind',
            'recursion', 'emergence', 'complexity', 'adaptation', 'evolution', 'consciousness',
            'memory', 'feedback', 'structure', 'entropy', 'self', 'intelligence'
        ]
        
        # Extract concepts
        found_concepts = []
        normalized_text = text.lower()
        
        # 1. First, check for our priority concepts
        for candidate in candidates:
            if candidate in normalized_text:
                concept_id = self.add_concept(candidate)
                found_concepts.append(concept_id)
                # Increment reuse count
                self.concepts[concept_id]['reuse_count'] += 1
                
                # New in MVP 1.5: Emit event when concept is created or reused
                if 'reuse_count' in self.concepts[concept_id] and self.concepts[concept_id]['reuse_count'] <= 1:
                    self.event_bus.publish(EventTypes.CONCEPT_CREATED, {
                        'concept_id': concept_id,
                        'name': candidate,
                        'source': 'priority_list'
                    })
        
        # 2. Extract additional noun concepts using basic NLP patterns
        # Look for capitalized words that might be important concepts
        potential_concepts = re.findall(r'\b([A-Z][a-z]{2,})\b', text)
        
        # Look for noun phrases (simplistic approach)
        noun_patterns = [
            # Adjective + Noun
            r'\b([a-z]+ing\s+[a-z]{3,})\b',
            # "The X of Y" pattern
            r'the\s+([a-z]{3,})\s+of\s+([a-z]{3,})',
            # Single nouns (avoiding common short words)
            r'\b([a-z]{5,})\b'
        ]
        
        for pattern in noun_patterns:
            matches = re.findall(pattern, normalized_text)
            potential_concepts.extend(matches)
        
        # Process the additional concepts (flatten if needed)
        for concept in potential_concepts:
            # Concept might be a tuple from regex groups
            if isinstance(concept, tuple):
                for subconcept in concept:
                    if len(subconcept) > 3 and subconcept not in ['this', 'that', 'these', 'those', 'from', 'with', 'have']:
                        concept_id = self.add_concept(subconcept)
                        if concept_id not in found_concepts:
                            found_concepts.append(concept_id)
                            self.concepts[concept_id]['reuse_count'] += 1
                            
                            # New in MVP 1.5: Emit event for new concept
                            if self.concepts[concept_id]['reuse_count'] <= 1:
                                self.event_bus.publish(EventTypes.CONCEPT_CREATED, {
                                    'concept_id': concept_id,
                                    'name': subconcept,
                                    'source': 'nlp_extraction'
                                })
            else:
                if len(concept) > 3 and concept not in ['this', 'that', 'these', 'those', 'from', 'with', 'have']:
                    concept_id = self.add_concept(concept)
                    if concept_id not in found_concepts:
                        found_concepts.append(concept_id)
                        self.concepts[concept_id]['reuse_count'] += 1
                        
                        # New in MVP 1.5: Emit event for new concept
                        if self.concepts[concept_id]['reuse_count'] <= 1:
                            self.event_bus.publish(EventTypes.CONCEPT_CREATED, {
                                'concept_id': concept_id,
                                'name': concept, 
                                'source': 'nlp_extraction'
                            })
        
        # Create associations between concepts found in the same text
        for i, c1 in enumerate(found_concepts):
            for c2 in found_concepts[i+1:]:
                relation_id = self.add_relation(c1, c2, "co-occurrence", 0.5)
                
                # New in MVP 1.5: Emit event for new relation
                if relation_id:
                    self.event_bus.publish(EventTypes.RELATION_CREATED, {
                        'relation_id': relation_id,
                        'source_id': c1,
                        'source_name': self.concepts[c1]['name'] if c1 in self.concepts else 'unknown',
                        'target_id': c2,
                        'target_name': self.concepts[c2]['name'] if c2 in self.concepts else 'unknown',
                        'type': 'co-occurrence'
                    })
                
        # Return key data about what we found
        return_data = {
            "concept_ids": found_concepts,
            "new_concepts": len(found_concepts),
            "concepts_used": [self.concepts[c_id]['name'] for c_id in found_concepts if c_id in self.concepts]
        }
                
        return found_concepts
    
    def extract_relations_from_text(self, text):
        """Extract potential relations from text using simple patterns"""
        # Simple patterns to detect relations
        patterns = [
            (r'(\w+)\s+causes\s+(\w+)', 'causes'),
            (r'(\w+)\s+leads to\s+(\w+)', 'leads_to'),
            (r'(\w+)\s+contains\s+(\w+)', 'contains'),
            (r'(\w+)\s+is part of\s+(\w+)', 'part_of'),
            (r'(\w+)\s+and\s+(\w+)', 'associated_with'),
            (r'(\w+)\s+versus\s+(\w+)', 'contrasts_with'),
            (r'(\w+)\s+vs\s+(\w+)', 'contrasts_with'),
            (r'(\w+)\s+opposes\s+(\w+)', 'opposes'),
        ]
        
        relations = []
        
        for pattern, relation_type in patterns:
            matches = re.findall(pattern, text.lower())
            for source, target in matches:
                source_id = self.add_concept(source)
                target_id = self.add_concept(target)
                relation_id = self.add_relation(source_id, target_id, relation_type, 0.7)
                if relation_id:
                    relations.append(relation_id)
                    
        return relations
    
    def process_interaction(self, prompt, response):
        """Process an interaction by extracting concepts and relations"""
        # Extract concepts from both prompt and response
        prompt_concepts = self.extract_concepts_from_text(prompt)
        response_concepts = self.extract_concepts_from_text(response)
        
        # Extract relations
        relations = self.extract_relations_from_text(response)
        
        # Connect prompt concepts to response concepts
        for p_concept in prompt_concepts:
            for r_concept in response_concepts:
                self.add_relation(p_concept, r_concept, "prompt_response", 0.6)
        
        self.last_updated = datetime.now()
        
        # Perform network pruning if needed
        pruned_concepts, pruned_relations = 0, 0
        if len(self.concepts) > self.max_concepts or len(self.relations) > self.max_relations:
            pruned_concepts, pruned_relations = self.prune_concept_network()
        
        return {
            'prompt_concepts': prompt_concepts,
            'response_concepts': response_concepts,
            'relations': relations,
            'pruned_concepts': pruned_concepts,
            'pruned_relations': pruned_relations,
            'new_concepts': len(response_concepts)
        }
    
    def update_activation(self, decay_factor=0.9):
        """Update activation levels of concepts, simulating memory decay"""
        for concept_id in self.concepts:
            self.concepts[concept_id]['activation'] *= decay_factor
            self.graph.nodes[concept_id]['activation'] *= decay_factor
    
    def activate_concept(self, concept_id, activation_boost=0.5):
        """Boost activation of a concept"""
        if concept_id in self.concepts:
            current = self.concepts[concept_id]['activation']
            self.concepts[concept_id]['activation'] = min(1.0, current + activation_boost)
            self.graph.nodes[concept_id]['activation'] = self.concepts[concept_id]['activation']
    
    def get_active_concepts(self, threshold=0.3):
        """Get currently active concepts"""
        return [c_id for c_id, c in self.concepts.items() if c['activation'] >= threshold]
    
    def get_most_connected_concepts(self, n=5):
        """Get the concepts with the most connections"""
        degree = dict(self.graph.degree())
        sorted_concepts = sorted(degree.items(), key=lambda x: x[1], reverse=True)
        return [c_id for c_id, degree in sorted_concepts[:n]]
    
    def get_concept_by_name(self, name):
        """Get concept by its name"""
        normalized_name = name.lower().strip()
        for c_id, c in self.concepts.items():
            if c['name'].lower().strip() == normalized_name:
                return c_id
        return None
    
    def get_central_concepts(self, n=5):
        """Get most central concepts by PageRank"""
        if len(self.graph) == 0:
            return []
            
        pagerank = nx.pagerank(self.graph)
        sorted_concepts = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)
        return [c_id for c_id, rank in sorted_concepts[:n]]
        
    def get_concept_subgraph(self, concept_ids):
        """Get a subgraph containing specified concepts and their connections"""
        if not concept_ids:
            return None
            
        # Create subgraph with these concepts
        subgraph = self.graph.subgraph(concept_ids).copy()
        return subgraph
    
    def get_network_stats(self):
        """Get statistics about the concept network"""
        return {
            'concept_count': len(self.concepts),
            'relation_count': len(self.relations),
            'most_reused': max(self.concepts.values(), key=lambda x: x['reuse_count'])['name'] if self.concepts else None,
            'avg_connections': sum(dict(self.graph.degree()).values()) / max(1, len(self.concepts)),
            'density': nx.density(self.graph) if len(self.graph) > 1 else 0,
            'connected_components': nx.number_connected_components(self.graph.to_undirected()) if len(self.graph) > 0 else 0
        }
    
    def prune_concept_network(self):
        """Prune the concept network when it grows too large"""
        if len(self.concepts) <= self.max_concepts and len(self.relations) <= self.max_relations:
            return 0, 0  # No pruning needed
            
        # Identify concepts to prune based on activation, recency and reuse
        pruned_concepts = 0
        candidates = []
        for concept_id, concept in self.concepts.items():
            # Skip core concepts we want to keep
            if concept['name'].lower() in ['recursion', 'emergence', 'complexity', 'pattern', 'self', 'consciousness']:
                continue
                
            # Calculate a "keep score" combining activation and usage
            activation = concept.get('activation', 0)
            reuse_count = concept.get('reuse_count', 0)
            
            # Higher score = more likely to be kept
            keep_score = (activation * 2) + (min(reuse_count, 10) / 10)
            candidates.append((concept_id, keep_score))
            
        # Sort by keep score (ascending - lower scores pruned first)
        candidates.sort(key=lambda x: x[1])
        
        # Determine how many concepts to remove
        to_remove_count = max(0, len(self.concepts) - self.max_concepts + 10)  # +10 for buffer
        
        # Remove the lowest-scored concepts
        for i in range(min(to_remove_count, len(candidates))):
            concept_id = candidates[i][0]
            # Remove this concept
            if concept_id in self.concepts:
                del self.concepts[concept_id]
                pruned_concepts += 1
                
                # Also remove from graph
                if self.graph.has_node(concept_id):
                    self.graph.remove_node(concept_id)
        
        # Now prune relations if needed
        pruned_relations = 0
        if len(self.relations) > self.max_relations:
            # Sort relations by weight (ascending - lower weights pruned first)
            self.relations.sort(key=lambda r: r.get('weight', 0))
            
            # Remove enough to get below limit
            to_remove = len(self.relations) - self.max_relations + 50  # +50 for buffer
            removed_relations = self.relations[:to_remove]
            self.relations = self.relations[to_remove:]
            pruned_relations = len(removed_relations)
            
            # Also remove from graph
            for relation in removed_relations:
                if self.graph.has_edge(relation.get('source'), relation.get('target')):
                    self.graph.remove_edge(relation.get('source'), relation.get('target'))
        
        # Clean up any dangling relations (those referencing removed concepts)
        valid_concepts = set(self.concepts.keys())
        cleaned_relations = []
        
        for relation in self.relations:
            if relation.get('source') in valid_concepts and relation.get('target') in valid_concepts:
                cleaned_relations.append(relation)
                
        self.relations = cleaned_relations
        
        print(f"🧹 Pruned {pruned_concepts} concepts and {pruned_relations} relations from network")
        return pruned_concepts, pruned_relations
        
    def get_visualization_subgraph(self, max_nodes=100):
        """Get a subgraph suitable for visualization - limiting to most important nodes"""
        if len(self.concepts) <= max_nodes:
            return self.graph
        
        # Get important concepts through multiple methods
        central = set(self.get_central_concepts(n=max_nodes // 3))
        connected = set(self.get_most_connected_concepts(n=max_nodes // 3))
        active = set(self.get_active_concepts(threshold=0.4))
        recent = set(sorted(self.concepts.items(), key=lambda x: x[1].get('reuse_count', 0), reverse=True)[:max_nodes // 3])
        
        # Combine all methods (with duplicates removed)
        important_concepts = list(central | connected | active | recent)[:max_nodes]
        
        # Create and return visualization subgraph
        return self.get_concept_subgraph(important_concepts)