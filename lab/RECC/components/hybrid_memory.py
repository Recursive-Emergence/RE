"""
Hybrid Memory Module
Implements the hybrid memory architecture for MVP 1.6 with emergent properties
and meta-memory capabilities for recursive self-reference.
"""

import time
import copy
import uuid
import random
from datetime import datetime

from event_bus import global_event_bus, EventTypes
from components.memory import Memory
from components.concept_network import ConceptNetwork

class WorkingMemory:
    """
    Implementation of limited-capacity working memory with attention control
    and decay dynamics
    """
    def __init__(self, initial_capacity=7):
        self.capacity = initial_capacity
        self.contents = []  # FIFO queue of items currently in working memory
        self.attention_weights = {}  # Attention weights for different content
        self.access_history = []  # History of memory access operations
        
    def process(self, input_data, context=None):
        """Process input through working memory, applying attention filters"""
        # Generate unique ID for this working memory operation
        operation_id = str(uuid.uuid4())
        
        # Apply attention filtering
        attention_score = self._calculate_attention_score(input_data, context)
        focused_content = self._apply_attention_filter(input_data, attention_score)
        
        # Add to working memory (respecting capacity limits)
        if len(self.contents) >= self.capacity:
            # Remove oldest item (FIFO)
            self.contents.pop(0)
            
        # Add new content
        memory_item = {
            'id': str(uuid.uuid4()),
            'timestamp': time.time(),
            'content': focused_content,
            'original_input': copy.deepcopy(input_data),
            'attention_score': attention_score,
            'context': context
        }
        self.contents.append(memory_item)
        
        # Record this operation
        self.access_history.append({
            'operation': 'process',
            'id': operation_id,
            'timestamp': time.time(),
            'attention_score': attention_score,
            'content_id': memory_item['id']
        })
        
        return {
            'operation_id': operation_id,
            'attention_score': attention_score,
            'focused_content': focused_content
        }
        
    def retrieve(self, query, context=None):
        """Retrieve items from working memory based on query"""
        # Generate unique ID for this retrieval operation
        operation_id = str(uuid.uuid4())
        
        matches = []
        relevance_scores = {}
        
        for item in self.contents:
            # Calculate relevance between query and this item
            relevance = self._calculate_relevance(query, item['content'], context)
            
            if relevance > 0.2:  # Minimum relevance threshold
                matches.append(item)
                relevance_scores[item['id']] = relevance
        
        # Sort matches by relevance
        sorted_matches = sorted(matches, 
                               key=lambda x: relevance_scores.get(x['id'], 0),
                               reverse=True)
        
        # Record this operation
        self.access_history.append({
            'operation': 'retrieve',
            'id': operation_id,
            'timestamp': time.time(),
            'query': query,
            'match_count': len(matches)
        })
        
        return {
            'operation_id': operation_id,
            'matches': sorted_matches,
            'relevance_scores': relevance_scores
        }
    
    def adapt_capacity(self, new_capacity):
        """Dynamically adapt working memory capacity"""
        old_capacity = self.capacity
        self.capacity = max(1, int(new_capacity))
        
        # If capacity decreased, remove oldest items
        while len(self.contents) > self.capacity:
            self.contents.pop(0)
            
        return {
            'old_capacity': old_capacity,
            'new_capacity': self.capacity
        }
        
    def _calculate_attention_score(self, input_data, context=None):
        """Calculate attention score for incoming data"""
        # Simple implementation; in practice would use more sophisticated
        # relevance algorithms
        base_score = 0.5
        
        # Adjust based on known attention weights if we have context
        if context and context in self.attention_weights:
            base_score = self.attention_weights[context]
            
        # Add some randomness to model variability in attention
        noise = (time.time() % 10) / 100  # Small random factor
        
        return min(1.0, max(0.1, base_score + noise))
    
    def _apply_attention_filter(self, input_data, attention_score):
        """Apply attention filtering to input data"""
        # This is a simplified implementation
        # In practice, would use more sophisticated filtering
        
        # If input is a dictionary, focus on the most important keys
        if isinstance(input_data, dict):
            if attention_score > 0.7:  # High attention = keep most information
                return copy.deepcopy(input_data)
            else:  # Lower attention = keep only essential information
                focused = {}
                # Prioritize certain keys based on their importance
                priority_keys = ['prompt', 'response', 'patterns', 'core']
                for key in priority_keys:
                    if key in input_data:
                        focused[key] = input_data[key]
                return focused
                
        # For other types, return as is (simplified implementation)
        return input_data
        
    def _calculate_relevance(self, query, content, context=None):
        """Calculate relevance between query and content item"""
        # Simple implementation; in practice would use semantic similarity
        
        # Handle dictionary content
        if isinstance(content, dict) and isinstance(query, dict):
            # Calculate overlap of keys
            common_keys = set(content.keys()).intersection(set(query.keys()))
            return len(common_keys) / max(1, len(set(content.keys()).union(set(query.keys()))))
            
        # Handle string content (simple word overlap for demo)
        elif isinstance(content, str) and isinstance(query, str):
            content_words = set(content.lower().split())
            query_words = set(query.lower().split())
            
            if not content_words or not query_words:
                return 0.0
                
            return len(content_words.intersection(query_words)) / len(content_words.union(query_words))
            
        # Default case
        return 0.2  # Base relevance

class ReferenceMemory:
    """
    Persistent storage for concepts, episodic memory, and theories
    """
    def __init__(self, initial_capacity=100):
        self.capacity = initial_capacity
        self.concepts = {}  # Concept storage
        self.relations = []  # Relations between concepts
        self.episodes = []  # Episodic memory
        self.theories = []  # Developed theories
        self.access_history = []  # History of memory access
        self.concept_hierarchy = {}  # Explicit concept hierarchy
        self.abstraction_layers = {
            0: [],  # Concrete/sensory concepts
            1: [],  # Basic patterns/relations
            2: [],  # Abstract concepts
            3: []   # Meta-concepts (concepts about concepts)
        }
        
    def store_concept(self, concept):
        """Store a new concept or update existing concept"""
        concept_id = concept.get('id', str(uuid.uuid4()))
        
        # If concept exists, update it
        if concept_id in self.concepts:
            # Track original abstraction level before update
            original_level = self.concepts[concept_id].get('abstraction_level', 0)
            
            # Update the concept
            self.concepts[concept_id].update(concept)
            
            # If abstraction_level wasn't provided but now the concept has more attributes,
            # increase the abstraction level as the concept becomes richer
            if 'abstraction_level' not in concept and len(self.concepts[concept_id]) > 5:
                self.concepts[concept_id]['abstraction_level'] = min(3, original_level + 0.5)
                
            operation = 'update'
        else:
            # Add new concept
            concept['id'] = concept_id
            concept['created'] = time.time()
            concept['access_count'] = 0
            
            # Set initial abstraction level based on content
            if 'abstraction_level' not in concept:
                # More attributes means potentially more abstract
                abstraction_level = min(3, 0.5 + (len(concept) - 3) * 0.1)
                
                # Check for hierarchy references (concepts that refer to other concepts)
                if 'related_concepts' in concept or 'parent_concept' in concept:
                    abstraction_level += 0.5
                    
                # Check for meta-concepts (concepts about concepts)
                if 'meta' in concept or any('concept' in k for k in concept.keys()):
                    abstraction_level += 1.0
                
                concept['abstraction_level'] = abstraction_level
                
            self.concepts[concept_id] = concept
            operation = 'create'
            
        # Update concept hierarchy based on abstraction level
        self._update_concept_hierarchy(concept_id)
            
        # Record operation
        self.access_history.append({
            'operation': f'{operation}_concept',
            'timestamp': time.time(),
            'concept_id': concept_id
        })
            
        return concept_id
    
    def add_concept_relation(self, source_id, target_id, relation_type='association', weight=0.5):
        """Add a relation between two concepts"""
        if source_id not in self.concepts or target_id not in self.concepts:
            return None
            
        # Create unique ID for relation
        relation_id = str(uuid.uuid4())
        
        # Create relation object
        relation = {
            'id': relation_id,
            'source': source_id,
            'target': target_id,
            'type': relation_type,
            'weight': weight,
            'created': time.time()
        }
        
        # Add to relations list
        self.relations.append(relation)
        
        # If this is a hierarchical relation, update concept hierarchy
        if relation_type in ['is_a', 'part_of', 'specialization_of', 'type_of']:
            # In hierarchical relations, target is higher in abstraction than source
            self._update_hierarchical_relation(source_id, target_id)
        
        return relation_id
    
    def _update_concept_hierarchy(self, concept_id):
        """Update the concept hierarchy for a concept"""
        if concept_id not in self.concepts:
            return
            
        # Get abstraction level
        concept = self.concepts[concept_id]
        abstraction_level = int(concept.get('abstraction_level', 0))
        
        # Add to appropriate abstraction layer
        for layer in range(4):  # We have 4 layers (0-3)
            if concept_id in self.abstraction_layers[layer]:
                self.abstraction_layers[layer].remove(concept_id)
                
        # Add to correct layer
        layer = min(3, max(0, abstraction_level))
        if concept_id not in self.abstraction_layers[layer]:
            self.abstraction_layers[layer].append(concept_id)
            
        # Update hierarchy depth of the concept if needed
        self._recalculate_hierarchy_depth(concept_id)
        
    def _update_hierarchical_relation(self, lower_id, higher_id):
        """Update the concept hierarchy based on a hierarchical relation"""
        # Make sure both concepts exist
        if lower_id not in self.concepts or higher_id not in self.concepts:
            return
            
        lower_concept = self.concepts[lower_id]
        higher_concept = self.concepts[higher_id]
        
        # Update hierarchy records
        if 'parent_concepts' not in lower_concept:
            lower_concept['parent_concepts'] = []
            
        if higher_id not in lower_concept['parent_concepts']:
            lower_concept['parent_concepts'].append(higher_id)
            
        if 'child_concepts' not in higher_concept:
            higher_concept['child_concepts'] = []
            
        if lower_id not in higher_concept['child_concepts']:
            higher_concept['child_concepts'].append(lower_id)
            
        # Update concept hierarchy depth
        self._recalculate_hierarchy_depth(lower_id)
        self._recalculate_hierarchy_depth(higher_id)
        
        # Update concept hierarchy visualization data
        if higher_id not in self.concept_hierarchy:
            self.concept_hierarchy[higher_id] = []
            
        if lower_id not in self.concept_hierarchy[higher_id]:
            self.concept_hierarchy[higher_id].append(lower_id)
            
    def _recalculate_hierarchy_depth(self, concept_id):
        """Calculate the hierarchy depth of a concept"""
        if concept_id not in self.concepts:
            return 0
            
        concept = self.concepts[concept_id]
        
        # If no parents, depth is 1
        if 'parent_concepts' not in concept or not concept['parent_concepts']:
            concept['hierarchy_depth'] = 1
            return 1
            
        # Calculate maximum depth through all parents
        max_parent_depth = 0
        for parent_id in concept['parent_concepts']:
            # Avoid infinite recursion by checking if we're the parent of our parent
            if parent_id == concept_id:
                continue
                
            # Ensure parent has depth calculated
            if parent_id in self.concepts:
                if 'hierarchy_depth' not in self.concepts[parent_id]:
                    parent_depth = self._recalculate_hierarchy_depth(parent_id)
                else:
                    parent_depth = self.concepts[parent_id]['hierarchy_depth']
                    
                max_parent_depth = max(max_parent_depth, parent_depth)
            
        # Our depth is max parent depth + 1
        concept['hierarchy_depth'] = max_parent_depth + 1
        return concept['hierarchy_depth']
    
    def get_active_concepts(self, threshold=0.5):
        """Get concepts with activation above threshold"""
        active_concepts = []
        for concept_id, concept in self.concepts.items():
            if concept.get('activation', 0) >= threshold:
                active_concepts.append(concept_id)
        return active_concepts
        
    def get_central_concepts(self, n=10):
        """Get the n most central concepts based on connections"""
        # Count connections for each concept
        connection_counts = {}
        
        # Count connections from relations
        for relation in self.relations:
            source = relation.get('source', '')
            target = relation.get('target', '')
            
            if source:
                connection_counts[source] = connection_counts.get(source, 0) + 1
                
            if target:
                connection_counts[target] = connection_counts.get(target, 0) + 1
                
        # Sort by connection count
        sorted_concepts = sorted(
            connection_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        # Return top n concept IDs
        return [c[0] for c in sorted_concepts[:n]]
    
    def get_concepts_by_abstraction(self, level):
        """Get concepts at a specific abstraction level"""
        return [self.concepts[c_id] for c_id in self.abstraction_layers.get(level, []) 
                if c_id in self.concepts]
    
    def build_hierarchical_concepts(self):
        """Build hierarchical concept relationships based on abstraction levels"""
        # Create hierarchical relations between abstraction levels
        # This simulates the formation of natural hierarchies in knowledge
        
        # Try to connect layer 0 (concrete) to layer 1 (basic)
        for lower_id in self.abstraction_layers[0]:
            if lower_id not in self.concepts:
                continue
                
            # Find suitable parents in layer 1
            lower_name = self.concepts[lower_id].get('name', '').lower()
            
            for higher_id in self.abstraction_layers[1]:
                if higher_id not in self.concepts or higher_id == lower_id:
                    continue
                    
                higher_name = self.concepts[higher_id].get('name', '').lower()
                
                # Check for name overlap or other relation indicators
                if (lower_name and higher_name and 
                    (lower_name in higher_name or higher_name in lower_name or
                     any(word in lower_name for word in higher_name.split()))):
                    # Create hierarchical relation
                    self.add_concept_relation(lower_id, higher_id, 'is_a')
        
        # Connect layer 1 (basic) to layer 2 (abstract)
        for lower_id in self.abstraction_layers[1]:
            if lower_id not in self.concepts:
                continue
                
            # Find suitable parents in layer 2
            for higher_id in self.abstraction_layers[2]:
                if higher_id not in self.concepts or higher_id == lower_id:
                    continue
                    
                # Determine if there's a plausible connection
                # (In a real system, we'd use semantic similarity)
                if random.random() < 0.3:  # 30% chance to connect
                    self.add_concept_relation(lower_id, higher_id, 'part_of')
        
        # Connect layer 2 (abstract) to layer 3 (meta)
        for lower_id in self.abstraction_layers[2]:
            if lower_id not in self.concepts:
                continue
                
            # Connect to meta-concepts in layer 3
            for higher_id in self.abstraction_layers[3]:
                if higher_id not in self.concepts or higher_id == lower_id:
                    continue
                    
                # Meta-concepts encompass abstract concepts
                self.add_concept_relation(lower_id, higher_id, 'type_of')
                
        # Recalculate all hierarchy depths
        for concept_id in self.concepts:
            self._recalculate_hierarchy_depth(concept_id)
                
    def store_episode(self, episode):
        """Store a new episodic memory"""
        episode_id = episode.get('id', str(uuid.uuid4()))
        
        # Ensure episode has required fields
        episode['id'] = episode_id
        episode['created'] = time.time()
        
        # Add to episodes
        self.episodes.append(episode)
        
        # Record operation
        self.access_history.append({
            'operation': 'store_episode',
            'timestamp': time.time(),
            'episode_id': episode_id
        })
        
        return episode_id
    
    def store_theory(self, theory):
        """Store a new theory"""
        theory_id = theory.get('id', str(uuid.uuid4()))
        
        # Ensure theory has required fields
        theory['id'] = theory_id
        theory['created'] = time.time()
        theory['evaluation_score'] = theory.get('evaluation_score', 0.5)
        
        # Add to theories
        self.theories.append(theory)
        
        # Record operation
        self.access_history.append({
            'operation': 'store_theory',
            'timestamp': time.time(),
            'theory_id': theory_id
        })
        
        return theory_id
    
    def retrieve(self, query):
        """Retrieve content from reference memory based on query"""
        # Generate unique ID for this retrieval operation
        operation_id = str(uuid.uuid4())
        
        # Search in concepts
        matching_concepts = []
        for concept_id, concept in self.concepts.items():
            relevance = self._calculate_relevance(query, concept)
            if relevance > 0.2:  # Minimum relevance threshold
                concept_copy = copy.deepcopy(concept)
                concept_copy['relevance'] = relevance
                matching_concepts.append(concept_copy)
                
                # Update access count and increase activation
                self.concepts[concept_id]['access_count'] = self.concepts[concept_id].get('access_count', 0) + 1
                self.concepts[concept_id]['activation'] = min(1.0, self.concepts[concept_id].get('activation', 0.5) + 0.1)
        
        # Search in episodes
        matching_episodes = []
        for episode in self.episodes:
            relevance = self._calculate_relevance(query, episode)
            if relevance > 0.2:  # Minimum relevance threshold
                episode_copy = copy.deepcopy(episode)
                episode_copy['relevance'] = relevance
                matching_episodes.append(episode_copy)
        
        # Search in theories
        matching_theories = []
        for theory in self.theories:
            relevance = self._calculate_relevance(query, theory)
            if relevance > 0.2:  # Minimum relevance threshold
                theory_copy = copy.deepcopy(theory)
                theory_copy['relevance'] = relevance
                matching_theories.append(theory_copy)
        
        # Sort results by relevance
        matching_concepts.sort(key=lambda x: x.get('relevance', 0), reverse=True)
        matching_episodes.sort(key=lambda x: x.get('relevance', 0), reverse=True)
        matching_theories.sort(key=lambda x: x.get('relevance', 0), reverse=True)
        
        # Record operation
        self.access_history.append({
            'operation': 'retrieve',
            'id': operation_id,
            'timestamp': time.time(),
            'query': query,
            'concept_matches': len(matching_concepts),
            'episode_matches': len(matching_episodes),
            'theory_matches': len(matching_theories)
        })
        
        return {
            'operation_id': operation_id,
            'matching_concepts': matching_concepts[:5],  # Limit results
            'matching_episodes': matching_episodes[:3],
            'matching_theories': matching_theories[:2],
            'retrieval_strength': max([
                len(matching_concepts) / max(1, len(self.concepts)),
                len(matching_episodes) / max(1, len(self.episodes)),
                len(matching_theories) / max(1, len(self.theories))
            ])
        }
    
    def _calculate_relevance(self, query, content):
        """Calculate relevance between query and stored content"""
        # Simple implementation for demonstration
        relevance = 0.0
        
        if isinstance(query, dict) and isinstance(content, dict):
            # Check for key/value matches
            for k, v in query.items():
                if k in content and content[k] == v:
                    relevance += 0.3
                elif k in content:
                    relevance += 0.1
            
            # Normalize
            relevance = min(1.0, relevance)
            
        elif isinstance(query, str):
            # For string queries, check if query appears in any string values
            query_lower = query.lower()
            for k, v in content.items():
                if isinstance(v, str) and query_lower in v.lower():
                    relevance = max(relevance, 0.5)
                    break
        
        return relevance
    
    def get_concept_hierarchy_stats(self):
        """Calculate statistics about the concept hierarchy"""
        if not self.concepts:
            return {
                'total_concepts': 0,
                'avg_abstraction_level': 0,
                'max_abstraction_level': 0,
                'hierarchical_depth': 1
            }
        
        # Calculate abstraction levels
        abstraction_levels = [c.get('abstraction_level', 0) for c in self.concepts.values()]
        avg_level = sum(abstraction_levels) / len(abstraction_levels)
        max_level = max(abstraction_levels) if abstraction_levels else 0
        
        # Count concepts with direct hierarchical relationships
        hierarchical_concepts = 0
        max_hierarchy_depth = 1
        
        for c in self.concepts.values():
            if ('parent_concepts' in c and c['parent_concepts']) or ('child_concepts' in c and c['child_concepts']):
                hierarchical_concepts += 1
                
                # Get hierarchy depth
                if 'hierarchy_depth' in c:
                    max_hierarchy_depth = max(max_hierarchy_depth, c['hierarchy_depth'])
        
        # Count concepts at each abstraction layer
        layer_counts = [len(self.abstraction_layers.get(i, [])) for i in range(4)]
        
        # Calculate hierarchy depth based on multiple factors
        hierarchy_factors = [
            max_hierarchy_depth,                      # Explicit hierarchical relationships
            1 + int(max_level > 0) + int(max_level > 1.5) + int(max_level > 2.5),  # Based on abstraction levels
            1 + sum(1 for i in range(4) if layer_counts[i] > 0)  # Number of non-empty layers
        ]
        
        hierarchy_depth = max(hierarchy_factors)
        
        return {
            'total_concepts': len(self.concepts),
            'avg_abstraction_level': avg_level,
            'max_abstraction_level': max_level,
            'hierarchical_concepts': hierarchical_concepts,
            'hierarchical_depth': hierarchy_depth,
            'layer_counts': layer_counts
        }

class ProceduralMemory:
    """
    Storage for reflection patterns, mutation strategies, and compression methods
    """
    def __init__(self, initial_strategies=5):
        self.strategies = {}
        self.effectiveness_history = []
        self.access_history = []
        
        # Initialize with basic strategies
        self._initialize_strategies(initial_strategies)
        
    def _initialize_strategies(self, count):
        """Initialize procedural memory with basic strategies"""
        basic_strategies = [
            {
                'id': 'pattern_recognition',
                'type': 'reflection',
                'description': 'Identify recurring patterns in data',
                'effectiveness': 0.7
            },
            {
                'id': 'chunking',
                'type': 'compression',
                'description': 'Group related items into chunks',
                'effectiveness': 0.8
            },
            {
                'id': 'abstraction',
                'type': 'compression',
                'description': 'Extract general concepts from specific instances',
                'effectiveness': 0.6
            },
            {
                'id': 'exploration',
                'type': 'mutation',
                'description': 'Introduce random variations to explore new possibilities',
                'effectiveness': 0.5
            },
            {
                'id': 'analogy_formation',
                'type': 'reflection',
                'description': 'Draw connections between different domains',
                'effectiveness': 0.6
            }
        ]
        
        # Store strategies
        for i in range(min(count, len(basic_strategies))):
            strategy = basic_strategies[i]
            self.strategies[strategy['id']] = strategy
    
    def apply_strategies(self, content, context=None):
        """Apply appropriate strategies to content"""
        operation_id = str(uuid.uuid4())
        results = []
        
        # Select relevant strategies based on content and context
        relevant_strategies = self._select_strategies(content, context)
        
        # Apply each strategy
        for strategy_id in relevant_strategies:
            strategy = self.strategies[strategy_id]
            
            # Apply the strategy (implementation would be more complex in practice)
            result = self._apply_strategy(strategy, content)
            
            if result['applied']:
                results.append({
                    'strategy_id': strategy_id,
                    'strategy_type': strategy['type'],
                    'result': result['result']
                })
        
        # Record operation
        self.access_history.append({
            'operation': 'apply_strategies',
            'id': operation_id,
            'timestamp': time.time(),
            'strategy_count': len(relevant_strategies),
            'results_count': len(results)
        })
        
        return {
            'operation_id': operation_id,
            'results': results,
            'strategy_relevance': len(results) / max(1, len(relevant_strategies))
        }
    
    def update_strategy_effectiveness(self, strategy_id, success_score):
        """Update the effectiveness score for a strategy"""
        if strategy_id in self.strategies:
            old_score = self.strategies[strategy_id]['effectiveness']
            
            # Update with moving average
            alpha = 0.2  # Learning rate
            new_score = (1 - alpha) * old_score + alpha * success_score
            
            self.strategies[strategy_id]['effectiveness'] = new_score
            
            # Record update
            self.effectiveness_history.append({
                'timestamp': time.time(),
                'strategy_id': strategy_id,
                'old_score': old_score,
                'new_score': new_score,
                'success_score': success_score
            })
            
            return {
                'strategy_id': strategy_id,
                'old_score': old_score,
                'new_score': new_score
            }
        
        return None
    
    def learn_new_strategy(self, strategy):
        """Add a new strategy to procedural memory"""
        if 'id' not in strategy:
            strategy['id'] = str(uuid.uuid4())
            
        strategy['added'] = time.time()
        strategy['effectiveness'] = strategy.get('effectiveness', 0.5)  # Initial moderate effectiveness
        
        self.strategies[strategy['id']] = strategy
        
        # Record learning
        self.access_history.append({
            'operation': 'learn_strategy',
            'timestamp': time.time(),
            'strategy_id': strategy['id'],
            'strategy_type': strategy.get('type', 'unknown')
        })
        
        return strategy['id']
    
    def _select_strategies(self, content, context=None):
        """Select relevant strategies based on content and context"""
        relevant_ids = []
        
        # Strategy selection logic would be more sophisticated in practice
        # Here's a simplified version
        
        # For chunking-compatible content
        if isinstance(content, (list, dict)) and len(content) > 5:
            # Find chunking strategies
            for sid, strategy in self.strategies.items():
                if strategy['type'] == 'compression':
                    relevant_ids.append(sid)
        
        # For content needing pattern recognition
        if isinstance(content, dict) and content.get('patterns'):
            # Find reflection strategies
            for sid, strategy in self.strategies.items():
                if strategy['type'] == 'reflection':
                    relevant_ids.append(sid)
        
        # Always include at least one strategy
        if not relevant_ids and self.strategies:
            # Get highest effectiveness strategy
            best_strategy = max(self.strategies.values(), key=lambda x: x.get('effectiveness', 0))
            relevant_ids.append(best_strategy['id'])
            
        return relevant_ids
    
    def _apply_strategy(self, strategy, content):
        """Apply a specific strategy to content"""
        # This would be much more sophisticated in practice
        # Here's a simplified implementation
        
        strategy_type = strategy['type']
        result = None
        
        # Apply different types of strategies
        if strategy_type == 'compression':
            if isinstance(content, dict):
                # Simplified: extract only the most important fields
                result = {key: content[key] for key in content 
                         if key in ['id', 'patterns', 'core', 'essential']}
                return {'applied': True, 'result': result}
                
        elif strategy_type == 'reflection':
            if isinstance(content, dict):
                # Simplified: identify patterns or relationships
                result = {'meta_observation': f"Analysis of {len(content)} elements"}
                return {'applied': True, 'result': result}
                
        elif strategy_type == 'mutation':
            if isinstance(content, dict):
                # Simplified: create a variation
                result = copy.deepcopy(content)
                result['variation'] = True
                return {'applied': True, 'result': result}
        
        # Default case: strategy couldn't be applied
        return {'applied': False, 'result': None}

class MetaMemory:
    """
    Meta-memory system that monitors and adapts memory performance
    """
    def __init__(self, memory_system):
        self.memory_system = memory_system
        self.performance_metrics = {}
        self.strategy_effectiveness = {}
        self.observed_patterns = []
        
        # Recursive observation at different levels
        self.observation_levels = {
            1: [],  # Records of direct memory operations
            2: [],  # Patterns in memory operations
            3: []   # Patterns in how patterns of operations change
        }
    
    def observe_process(self, interactions, results):
        """Observe a memory process at multiple levels"""
        # Level 1 observation: Direct memory operations
        level1_observation = {
            'time': time.time(),
            'interactions': interactions,
            'results': {k: v for k, v in results.items() if k != 'emergent_properties'}
        }
        self.observation_levels[1].append(level1_observation)
        
        # Level 2 observation: Patterns in operations
        if len(self.observation_levels[1]) >= 5:  # Need sufficient L1 observations
            recent_l1 = self.observation_levels[1][-5:]
            pattern = self._extract_pattern(recent_l1)
            self.observation_levels[2].append({
                'time': time.time(),
                'pattern_type': pattern['type'],
                'strength': pattern['strength'],
                'description': pattern['description']
            })
            
        # Level 3 observation: Patterns in patterns
        if len(self.observation_levels[2]) >= 5:  # Need sufficient L2 observations
            recent_l2 = self.observation_levels[2][-5:]
            meta_pattern = self._extract_meta_pattern(recent_l2)
            self.observation_levels[3].append({
                'time': time.time(),
                'meta_pattern_type': meta_pattern['type'],
                'trend': meta_pattern['trend'],
                'implication': meta_pattern['implication']
            })
        
        # Update performance metrics
        self._update_performance_metrics(results)
    
    def recommend_adaptations(self):
        """Recommend adaptations to memory system based on recursive observations"""
        adaptations = []
        
        # Level 1 adaptations: Direct performance optimization
        if self.performance_metrics.get('working_memory_overflow', 0) > 0.2:
            adaptations.append({
                'level': 1,
                'component': 'working',
                'action': 'increase_chunking',
                'priority': 'high'
            })
            
        # Level 2 adaptations: Strategic changes
        if len(self.observation_levels[2]) > 0:
            recent_patterns = self.observation_levels[2][-3:]
            if all(p['pattern_type'] == 'retrieval_failure' for p in recent_patterns):
                adaptations.append({
                    'level': 2,
                    'component': 'reference',
                    'action': 'expand_search_context',
                    'priority': 'medium'
                })
                
        # Level 3 adaptations: Architectural changes
        if len(self.observation_levels[3]) > 0:
            recent_meta = self.observation_levels[3][-1]
            if recent_meta['meta_pattern_type'] == 'increasing_abstraction':
                adaptations.append({
                    'level': 3,
                    'component': 'system',
                    'action': 'add_hierarchical_layer',
                    'priority': 'low'
                })
                
        return adaptations
    
    def get_metric(self, metric_name):
        """Get a specific performance metric"""
        return self.performance_metrics.get(metric_name, 0)
        
    def _extract_pattern(self, observations):
        """Extract patterns from level 1 observations"""
        # This is simplified for the example
        # In practice, would implement actual pattern recognition
        
        # Count operation types
        operation_counts = {}
        retrieval_success_rate = 0
        total_retrievals = 0
        
        for obs in observations:
            for interaction in obs.get('interactions', []):
                operation = interaction[0] if isinstance(interaction, tuple) else 'unknown'
                operation_counts[operation] = operation_counts.get(operation, 0) + 1
                
                # Track retrieval success
                if operation == 'working' and interaction[2] > 0.5:
                    retrieval_success_rate += 1
                    total_retrievals += 1
                elif operation == 'working':
                    total_retrievals += 1
        
        # Determine dominant operation
        dominant_op = max(operation_counts.items(), key=lambda x: x[1])[0] if operation_counts else 'unknown'
        
        # Determine if there's a retrieval issue
        pattern_type = 'normal_operation'
        description = "Normal memory operations observed"
        strength = 0.5
        
        if total_retrievals > 0 and retrieval_success_rate / total_retrievals < 0.3:
            pattern_type = 'retrieval_failure'
            description = "Low retrieval success rate detected"
            strength = 0.8
            
        if dominant_op == 'working' and operation_counts.get('working', 0) > 3:
            pattern_type = 'working_memory_focus'
            description = "Heavy reliance on working memory"
            strength = 0.7
            
        return {
            'type': pattern_type,
            'strength': strength,
            'description': description
        }
        
    def _extract_meta_pattern(self, patterns):
        """Extract meta-patterns from level 2 observations"""
        # This is simplified for the example
        # In practice, would implement actual meta-pattern recognition
        
        # Count pattern types
        pattern_counts = {}
        for p in patterns:
            pattern_counts[p['pattern_type']] = pattern_counts.get(p['pattern_type'], 0) + 1
        
        # Look for trends in strengths
        strengths = [p['strength'] for p in patterns]
        increasing_strength = all(strengths[i] <= strengths[i+1] for i in range(len(strengths)-1))
        decreasing_strength = all(strengths[i] >= strengths[i+1] for i in range(len(strengths)-1))
        
        # Determine meta-pattern type
        meta_type = 'stable_patterns'
        trend = 'stable'
        implication = 'Current memory strategies are consistent'
        
        if increasing_strength:
            meta_type = 'increasing_pattern_strength'
            trend = 'increasing'
            implication = 'Memory patterns are becoming more pronounced'
            
        if len(pattern_counts) == 1:
            # Same pattern repeating
            pattern_type = list(pattern_counts.keys())[0]
            if pattern_type == 'retrieval_failure':
                meta_type = 'persistent_retrieval_failure'
                trend = 'persistent'
                implication = 'Systemic issue with memory retrieval'
            
        return {
            'type': meta_type,
            'trend': trend,
            'implication': implication
        }
        
    def _update_performance_metrics(self, results):
        """Update performance metrics based on process results"""
        # Extract metrics from results
        if isinstance(results, dict):
            # Calculate working memory utilization
            if 'working_result' in results:
                working_result = results['working_result']
                if hasattr(self.memory_system.components.get('working'), 'capacity'):
                    capacity = self.memory_system.components['working'].capacity
                    contents_count = len(self.memory_system.components['working'].contents)
                    self.performance_metrics['working_memory_utilization'] = contents_count / max(1, capacity)
                    self.performance_metrics['working_memory_overflow'] = max(0, (contents_count - capacity) / capacity)
            
            # Calculate retrieval effectiveness
            if 'reference_result' in results:
                reference_result = results['reference_result']
                if 'retrieval_strength' in reference_result:
                    # Update with moving average
                    current = self.performance_metrics.get('retrieval_effectiveness', 0.5)
                    new_value = reference_result['retrieval_strength']
                    self.performance_metrics['retrieval_effectiveness'] = 0.8 * current + 0.2 * new_value
            
            # Calculate abstract concept ratio if concept network available
            if hasattr(self.memory_system, 'hybrid_memory') and hasattr(self.memory_system.hybrid_memory, 'components'):
                if 'reference' in self.memory_system.hybrid_memory.components:
                    reference = self.memory_system.hybrid_memory.components['reference']
                    if hasattr(reference, 'concepts'):
                        abstract_count = sum(1 for c in reference.concepts.values() 
                                           if c.get('abstraction_level', 0) > 1)
                        total_concepts = len(reference.concepts)
                        self.performance_metrics['abstract_concept_ratio'] = abstract_count / max(1, total_concepts)

class HybridMemory:
    """
    Hybrid memory architecture integrating working, reference, and procedural memory
    with emergent properties and meta-memory capabilities
    """
    def __init__(self, event_bus=None, initial_capacity={
        'working': 7,         # Initial capacity, not fixed
        'reference': 100,     # Initial size, can grow
        'procedural': 5       # Initial strategies, will evolve
    }):
        # Initialize components with initial capacities
        self.components = {
            'working': WorkingMemory(initial_capacity['working']),
            'reference': ReferenceMemory(initial_capacity['reference']),
            'procedural': ProceduralMemory(initial_capacity['procedural'])
        }
        
        # Meta-memory system that monitors and adapts memory performance
        self.meta_memory = MetaMemory(self)
        
        # Store reference to event bus
        self.event_bus = event_bus or global_event_bus
        
        # Interaction history between components
        self.component_interactions = []
        
        # Emergent properties that develop over time
        self.emergent_properties = {
            'working_capacity': initial_capacity['working'],
            'concept_hierarchy_depth': 1,
            'strategy_sophistication': 1,
            'attention_selectivity': 0.5,
            'consolidation_efficiency': 0.5
        }
        
        # Seed initial meta-concepts to bootstrap the hierarchy
        self._seed_initial_concepts()
    
    def _seed_initial_concepts(self):
        """Seed initial abstract concepts to bootstrap the hierarchy"""
        # Create a set of initial meta-concepts that can be built upon
        meta_concepts = [
            {
                'name': 'Meta-cognition',
                'definition': 'Thinking about thinking; awareness and understanding of one\'s own thought processes',
                'abstraction_level': 3.0,
                'is_meta': True
            },
            {
                'name': 'Recursion',
                'definition': 'A process in which the output of one iteration becomes the input to the next',
                'abstraction_level': 2.5,
                'related_terms': ['self-reference', 'iteration', 'loop']
            },
            {
                'name': 'Self-Reference',
                'definition': 'A system\'s capability to refer to and model itself',
                'abstraction_level': 2.8,
                'is_meta': True
            },
            {
                'name': 'Pattern',
                'definition': 'A discernible regularity or structure in information',
                'abstraction_level': 1.5,
                'categories': ['spatial', 'temporal', 'causal']
            }
        ]
        
        # Store these abstract concepts
        for concept in meta_concepts:
            concept_id = self.components['reference'].store_concept(concept)
            # Add activation to ensure they're more prominent
            if concept_id in self.components['reference'].concepts:
                self.components['reference'].concepts[concept_id]['activation'] = 0.8
        
        # Add some basic level concepts
        basic_concepts = [
            {
                'name': 'Memory',
                'definition': 'System for storing and retrieving information',
                'abstraction_level': 1.0
            },
            {
                'name': 'Attention',
                'definition': 'The process of focusing cognitive resources on specific information',
                'abstraction_level': 1.0
            },
            {
                'name': 'Learning',
                'definition': 'The acquisition of knowledge or skills through experience or study',
                'abstraction_level': 1.2
            }
        ]
        
        for concept in basic_concepts:
            concept_id = self.components['reference'].store_concept(concept)
            if concept_id in self.components['reference'].concepts:
                self.components['reference'].concepts[concept_id]['activation'] = 0.6
        
        # Build the initial hierarchy relationships
        self.components['reference'].build_hierarchical_concepts()
        
        # Update concept hierarchy depth based on initial seed
        hierarchy_stats = self.components['reference'].get_concept_hierarchy_stats()
        self.emergent_properties['concept_hierarchy_depth'] = hierarchy_stats['hierarchical_depth']
    
    def update_emergent_properties(self):
        """Update emergent properties based on system performance and usage"""
        # Update working memory capacity based on utilization
        if self.meta_memory.get_metric('working_memory_utilization') > 0.9:
            self.emergent_properties['working_capacity'] *= 1.05
            self.components['working'].adapt_capacity(self.emergent_properties['working_capacity'])
            
        # Update concept hierarchy depth based on reference memory stats
        hierarchy_stats = self.components['reference'].get_concept_hierarchy_stats()
        current_depth = hierarchy_stats.get('hierarchical_depth', 1)
        
        # Improve concept hierarchy if possible
        if len(self.components['reference'].concepts) >= 5 and random.random() < 0.3:
            # Periodically rebuild hierarchical relationships to improve depth
            self.components['reference'].build_hierarchical_concepts()
            # Get updated stats after building
            hierarchy_stats = self.components['reference'].get_concept_hierarchy_stats()
            current_depth = hierarchy_stats.get('hierarchical_depth', 1)
        
        # Gradually increase concept hierarchy depth, but don't decrease it
        self.emergent_properties['concept_hierarchy_depth'] = max(
            self.emergent_properties['concept_hierarchy_depth'],
            current_depth
        )
            
        # Track learning progress for strategies
        if hasattr(self.components['procedural'], 'effectiveness_history'):
            recent_effectiveness = self.components['procedural'].effectiveness_history[-10:] if \
                                  self.components['procedural'].effectiveness_history else []
            
            if recent_effectiveness:
                # Calculate average improvement in strategy effectiveness
                avg_improvement = sum(e.get('new_score', 0) - e.get('old_score', 0) 
                                   for e in recent_effectiveness) / len(recent_effectiveness)
                
                # Update strategy sophistication based on improvement
                if avg_improvement > 0:
                    self.emergent_properties['strategy_sophistication'] += 0.05
                    
                    # Track this as meta-strategy evolution
                    self.emergent_properties['meta_strategy_evolution'] = avg_improvement
        
        # Publish event about emergent property changes
        self.event_bus.publish(EventTypes.EMERGENT_PROPERTIES_UPDATED, {
            'properties': self.emergent_properties,
            'timestamp': datetime.now().isoformat()
        })
    
    def process(self, input_data, context=None):
        """
        Process input through the memory system
        
        Args:
            input_data: Data to be processed
            context: Optional context information
            
        Returns:
            Dictionary containing processing results from each memory component
        """
        # Track interactions between components
        interactions = []
        
        # First, process through working memory (attention, filtering)
        working_result = self.components['working'].process(input_data, context)
        interactions.append(('input', 'working', working_result['attention_score']))
        
        # Check reference memory for related concepts
        reference_result = self.components['reference'].retrieve(working_result['focused_content'])
        interactions.append(('working', 'reference', reference_result['retrieval_strength']))
        
        # Apply procedural strategies
        procedural_result = self.components['procedural'].apply_strategies(
            working_result['focused_content'],
            reference_result['retrieved_content'] if 'retrieved_content' in reference_result else None
        )
        interactions.append(('reference', 'procedural', procedural_result['strategy_relevance']))
        
        # Extract and store concepts from input if it contains text
        if isinstance(input_data, dict) and ('prompt' in input_data or 'response' in input_data):
            self._extract_concepts_from_input(input_data)
        
        # Update interaction history
        self.component_interactions.extend(interactions)
        
        # Update emergent properties
        self.update_emergent_properties()
        
        # Let meta-memory monitor this process
        self.meta_memory.observe_process(interactions, {
            'working_result': working_result,
            'reference_result': reference_result,
            'procedural_result': procedural_result
        })
        
        # Create the combined result
        result = {
            'working_result': working_result,
            'reference_result': reference_result,
            'procedural_result': procedural_result,
            'emergent_properties': self.emergent_properties,
            'id': str(uuid.uuid4())  # Add unique ID for this processing result
        }
        
        # Publish memory processing event
        self.event_bus.publish(EventTypes.MEMORY_PROCESSED, {
            'input_type': type(input_data).__name__,
            'components_used': list(result.keys()),
            'timestamp': datetime.now().isoformat()
        })
        
        return result
    
    def _extract_concepts_from_input(self, input_data):
        """Extract concepts from input and store in reference memory"""
        # This is a simplified implementation
        # In a real system, this would use more sophisticated techniques
        concepts_to_store = []
        
        # Extract from prompt
        if 'prompt' in input_data and isinstance(input_data['prompt'], str):
            # Simple extraction: look for key phrases
            prompt = input_data['prompt'].lower()
            for phrase in ['pattern', 'concept', 'model', 'think', 'reflect', 'recursion']:
                if phrase in prompt:
                    concept = {
                        'name': phrase.capitalize(),
                        'source': 'prompt',
                        'context': prompt[:50] + "..." if len(prompt) > 50 else prompt
                    }
                    concepts_to_store.append(concept)
        
        # Extract from response (more detailed)
        if 'response' in input_data and isinstance(input_data['response'], str):
            response = input_data['response']
            
            # Look for more abstract concepts in responses
            if 'meta' in response.lower() or 'recursive' in response.lower():
                concept = {
                    'name': 'Meta-reflection',
                    'definition': 'Reflection on the process of reflection itself',
                    'abstraction_level': 2.5,
                    'source': 'response'
                }
                concepts_to_store.append(concept)
                
            # Look for pattern-related concepts
            if 'pattern' in response.lower():
                concept = {
                    'name': 'Pattern Recognition',
                    'related_to': 'cognition',
                    'abstraction_level': 1.5,
                    'source': 'response'
                }
                concepts_to_store.append(concept)
                
        # Store extracted concepts
        for concept in concepts_to_store:
            self.components['reference'].store_concept(concept)
    
    def retrieve(self, query, context=None):
        """
        Retrieve information from memory using a query
        
        This method provides a unified interface to search across
        all memory components.
        
        Args:
            query: Search query (can be dict, string, etc.)
            context: Optional context to focus the search
            
        Returns:
            Dictionary with combined retrieval results
        """
        # Track interactions for this retrieval
        interactions = []
        
        # First, focus the query through working memory
        working_result = self.components['working'].process({'query': query}, context)
        interactions.append(('query', 'working', working_result['attention_score']))
        
        # Retrieve from reference memory
        reference_result = self.components['reference'].retrieve(working_result['focused_content'])
        interactions.append(('working', 'reference', reference_result['retrieval_strength']))
        
        # Apply procedural strategies to refine results
        if reference_result['retrieval_strength'] < 0.3:
            # If direct retrieval was weak, apply strategies
            procedural_result = self.components['procedural'].apply_strategies(
                {'query': query, 'weak_results': reference_result},
                context
            )
            interactions.append(('reference', 'procedural', procedural_result['strategy_relevance']))
        else:
            procedural_result = {'results': []}
        
        # Update interaction history
        self.component_interactions.extend(interactions)
        
        # Let meta-memory monitor this process
        self.meta_memory.observe_process(interactions, {
            'working_result': working_result,
            'reference_result': reference_result,
            'procedural_result': procedural_result
        })
        
        # Create the combined result
        result = {
            'query': query,
            'context': context,
            'working_result': working_result,
            'reference_result': reference_result,
            'procedural_result': procedural_result,
            'combined_results': self._combine_retrieval_results(reference_result, procedural_result)
        }
        
        # Publish retrieval event
        self.event_bus.publish(EventTypes.MEMORY_RETRIEVED, {
            'query_type': type(query).__name__,
            'result_count': len(result['combined_results']),
            'timestamp': datetime.now().isoformat()
        })
        
        return result
    
    def store(self, content, content_type=None, context=None):
        """
        Store content in the appropriate memory component
        
        Args:
            content: Content to store
            content_type: Optional type hint ('concept', 'episode', 'theory')
            context: Optional context information
            
        Returns:
            Dictionary with storage result
        """
        # Determine appropriate storage location if not specified
        if not content_type:
            content_type = self._infer_content_type(content)
        
        # Process through working memory first
        working_result = self.components['working'].process({
            'content': content,
            'content_type': content_type,
            'context': context
        })
        
        storage_id = None
        
        # Store in reference memory based on content type
        if content_type == 'concept':
            storage_id = self.components['reference'].store_concept(working_result['focused_content']['content'])
        elif content_type == 'episode':
            storage_id = self.components['reference'].store_episode(working_result['focused_content']['content'])
        elif content_type == 'theory':
            storage_id = self.components['reference'].store_theory(working_result['focused_content']['content'])
        elif content_type == 'strategy':
            storage_id = self.components['procedural'].learn_new_strategy(working_result['focused_content']['content'])
        
        # Publish storage event
        self.event_bus.publish(EventTypes.MEMORY_STORED, {
            'content_type': content_type,
            'storage_id': storage_id,
            'timestamp': datetime.now().isoformat()
        })
        
        return {
            'content_type': content_type,
            'storage_id': storage_id,
            'success': storage_id is not None
        }
    
    def _infer_content_type(self, content):
        """Infer the type of content based on its structure"""
        if isinstance(content, dict):
            # Check for type indicators
            if 'type' in content:
                content_type = content['type']
                if content_type in ['concept', 'episode', 'theory', 'strategy']:
                    return content_type
            
            # Check for typical fields
            if 'pattern' in content or 'definition' in content:
                return 'concept'
            elif 'sequence' in content or 'timestamp' in content:
                return 'episode'
            elif 'hypothesis' in content or 'evidence' in content:
                return 'theory'
            elif 'procedure' in content or 'effectiveness' in content:
                return 'strategy'
        
        # Default
        return 'concept'
    
    def _combine_retrieval_results(self, reference_result, procedural_result):
        """Combine retrieval results from different components"""
        combined = []
        
        # Add concept results
        if 'matching_concepts' in reference_result:
            combined.extend(reference_result['matching_concepts'])
        
        # Add episode results
        if 'matching_episodes' in reference_result:
            combined.extend(reference_result['matching_episodes'])
        
        # Add theory results
        if 'matching_theories' in reference_result:
            combined.extend(reference_result['matching_theories'])
        
        # Add results from procedural strategies
        if 'results' in procedural_result:
            for result in procedural_result['results']:
                if 'result' in result and result['result']:
                    combined.append({
                        'source': 'procedural',
                        'strategy': result.get('strategy_id', 'unknown'),
                        'data': result['result']
                    })
        
        # Sort by relevance if available
        combined.sort(key=lambda x: x.get('relevance', 0), reverse=True)
        
        return combined
    
    def get_observability_data(self):
        """Get comprehensive data for visualization and monitoring"""
        # Collect data from each component
        working_data = {
            'capacity': self.components['working'].capacity,
            'item_count': len(self.components['working'].contents),
            'utilization': len(self.components['working'].contents) / max(1, self.components['working'].capacity)
        }
        
        reference_data = {
            'concept_count': len(self.components['reference'].concepts),
            'episode_count': len(self.components['reference'].episodes),
            'theory_count': len(self.components['reference'].theories),
        }
        
        procedural_data = {
            'strategy_count': len(self.components['procedural'].strategies),
            'strategies': list(self.components['procedural'].strategies.values())
        }
        
        meta_data = {
            'level1_observations': len(self.meta_memory.observation_levels[1]),
            'level2_observations': len(self.meta_memory.observation_levels[2]),
            'level3_observations': len(self.meta_memory.observation_levels[3]),
            'metrics': self.meta_memory.performance_metrics
        }
        
        return {
            'timestamp': datetime.now().isoformat(),
            'working_memory': working_data,
            'reference_memory': reference_data,
            'procedural_memory': procedural_data,
            'meta_memory': meta_data,
            'emergent_properties': self.emergent_properties,
            'interaction_count': len(self.component_interactions)
        }