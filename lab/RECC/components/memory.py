"""
Memory Module
Handles memory management, including concept storage, retrieval, and consolidation
"""
import random
import uuid
from datetime import datetime

from event_bus import global_event_bus, EventTypes
from components.concept_network import ConceptNetwork

class Memory:
    def __init__(self, event_bus=None):
        # Keep existing attributes for backward compatibility
        self.entries = []
        self.symbols = []
        self.symbol_links = []
        
        # New: Add concept network
        self.concept_network = ConceptNetwork()
        
        # Store reference to event bus (or use global)
        self.event_bus = event_bus or global_event_bus
    
    def add(self, prompt, response, internal_state):
        # Create entry in traditional format for compatibility
        entry = {
            'id': str(uuid.uuid4()),
            'timestamp': datetime.now().isoformat(),
            'prompt': prompt,
            'response': response,
            'state': internal_state,
            'reuse_score': 0.0,
            'entropy_shift': 0.0,
            'novelty': 0.0
        }
        self.entries.append(entry)
        
        # Extract traditional symbols for backward compatibility
        self.extract_symbols(response)
        self.update_links()
        
        # Now process through the concept network
        network_update = self.concept_network.process_interaction(prompt, response)
        
        # Update the entry with concept data
        entry['concept_data'] = network_update
        
        # New in MVP 1.5: Emit response received event
        self.event_bus.publish(EventTypes.RESPONSE_RECEIVED, {
            'entry_id': entry['id'],
            'prompt': prompt,
            'response': response,
            'timestamp': entry['timestamp'],
            'concept_data': network_update
        })
        
        # Update scores
        self.update_scores()
        
        return entry
    
    def extract_symbols(self, response):
        candidates = ['spiral', 'loop', 'star', 'growth', 'iteration', 'cycle', 'flow', 'balance', 
                      'continuum', 'pattern', 'unity', 'transformation', 'emotion', 'feeling', 'mind']
        for c in candidates:
            if c in response.lower() and c not in self.symbols:
                self.symbols.append(c)

    def update_links(self):
        if len(self.symbols) >= 2:
            latest = self.symbols[-1]
            second_latest = self.symbols[-2]
            link = (second_latest, latest)
            if link not in self.symbol_links:
                self.symbol_links.append(link)

    def get_recent(self, n=5):
        return self.entries[-n:] if len(self.entries) > 0 else []

    def update_scores(self):
        all_text = ' '.join(e['response'] for e in self.entries)
        for i, e in enumerate(self.entries):
            reuse = 0
            for j, e2 in enumerate(self.entries):
                if i != j and e['response'][:10] in e2['response']:
                    reuse += 1
            e['reuse_score'] = reuse / max(1, len(self.entries))
            e['novelty'] = self.compute_novelty(e['response'], all_text)

    def compute_novelty(self, response, corpus):
        unique = [word for word in response.split() if word not in corpus]
        return len(unique) / max(1, len(response.split()))

    def compute_gradients(self):
        if len(self.entries) < 2:
            return 0.0, 0.0
        novelty_list = [e['novelty'] for e in self.entries]
        reuse_list = [e['reuse_score'] for e in self.entries]
        novelty_gradient = novelty_list[-1] - novelty_list[-2]
        reuse_gradient = reuse_list[-1] - reuse_list[-2]
        return round(novelty_gradient, 4), round(reuse_gradient, 4)
    
    def consolidate_memory(self, threshold=0.3):
        """Consolidate memory entries based on reuse score"""
        # Original consolidation logic
        high_value = [e for e in self.entries if e['reuse_score'] > threshold]
        low_value = [e for e in self.entries if e['reuse_score'] <= threshold]
        
        # Keep only a sample of low-value memories
        sample_size = min(len(low_value) // 3, 5)
        keep_sample = random.sample(low_value, sample_size) if sample_size > 0 else []
        
        # Update entries
        original_count = len(self.entries)
        self.entries = high_value + keep_sample
        
        # Rebuild symbol graph
        self.update_symbol_graph()
        
        # Remove low-activation concepts from concept network
        network_stats_before = self.concept_network.get_network_stats()
        
        # Instead of removing concepts, just focus on activation decay
        self.concept_network.update_activation(decay_factor=0.7)  # Stronger decay during consolidation
        
        network_stats_after = self.concept_network.get_network_stats()
        
        result = {
            'consolidated': len(self.entries),
            'original': original_count,
            'compression_ratio': len(self.entries) / max(1, original_count),
            'network_before': network_stats_before,
            'network_after': network_stats_after
        }
        
        # New in MVP 1.5: Emit memory consolidation event
        self.event_bus.publish(EventTypes.MEMORY_CONSOLIDATION, result)
        
        return result
    
    def update_symbol_graph(self):
        """Rebuild symbol graph from consolidated memory"""
        # Keep existing symbols
        existing_symbols = set(self.symbols)
        
        # Re-extract from consolidated entries
        for entry in self.entries:
            self.extract_symbols(entry['response'])
        
        # Rebuild links
        self.symbol_links = []
        for i in range(len(self.symbols) - 1):
            self.symbol_links.append((self.symbols[i], self.symbols[i+1]))
            
        # Also update the concept network by reprocessing entries
        for entry in self.entries:
            self.concept_network.process_interaction(entry['prompt'], entry['response'])
    
    def detect_repetition(self, threshold=0.85, window_size=5):
        """
        Enhanced repetition detection that looks for similar questions and patterns
        Returns True if repetition is detected
        """
        if len(self.entries) < window_size + 1:
            return False
            
        # Extract recent prompts
        recent_prompts = [entry.get('prompt', '') for entry in self.entries[-window_size:]]
        
        # Check for direct repetition (exact same prompt appearing multiple times)
        prompt_counts = {}
        for prompt in recent_prompts:
            prompt_counts[prompt] = prompt_counts.get(prompt, 0) + 1
            if prompt_counts[prompt] >= 2:  # Same prompt appears twice or more
                return True
        
        # Check for semantic similarity (similar questions with different wording)
        for i in range(len(recent_prompts)):
            for j in range(i+1, len(recent_prompts)):
                # Simple word overlap similarity
                words_i = set(recent_prompts[i].lower().split())
                words_j = set(recent_prompts[j].lower().split())
                
                # Avoid division by zero
                if not words_i or not words_j:
                    continue
                    
                # Calculate Jaccard similarity
                similarity = len(words_i.intersection(words_j)) / len(words_i.union(words_j))
                
                if similarity > threshold:
                    return True
        
        # Check for pattern repetition (alternating between a small set of questions)
        if len(self.entries) >= window_size * 2:
            earlier_prompts = [entry.get('prompt', '') for entry in self.entries[-(window_size*2):-window_size]]
            
            # Calculate similarity between current window and previous window
            pattern_matches = 0
            for current, previous in zip(recent_prompts, earlier_prompts):
                words_current = set(current.lower().split())
                words_previous = set(previous.lower().split())
                
                # Avoid division by zero
                if not words_current or not words_previous:
                    continue
                    
                similarity = len(words_current.intersection(words_previous)) / len(words_current.union(words_previous))
                if similarity > threshold - 0.1:  # Slightly lower threshold for pattern detection
                    pattern_matches += 1
            
            if pattern_matches >= window_size // 2:
                return True
                
        return False
        
    def generate_breakout_prompt(self):
        """
        Generate a prompt to break out of repetitive patterns
        This is called when repetition is detected
        """
        breakout_prompts = [
            "Let's explore a completely different direction. What if we consider the opposite perspective?",
            "I notice we're covering similar ground. Let's try a different approach - what's a counterintuitive insight about this topic?",
            "Let's shift our focus. What's an aspect of this we haven't considered yet?",
            "I'd like to introduce a new dimension to our exploration. How does this connect to broader systems?",
            "Let's challenge our assumptions. What if the opposite of our current thinking is true?",
            "We need a fresh perspective. What metaphor from a different domain might help us see this differently?",
            "Let's zoom out and consider the meta-level patterns. What's the bigger picture here?"
        ]
        
        # Choose a prompt we haven't used recently
        used_prompts = set()
        if len(self.entries) >= 5:
            for entry in self.entries[-5:]:
                used_prompts.add(entry.get('prompt', ''))
        
        available_prompts = [p for p in breakout_prompts if p not in used_prompts]
        
        if not available_prompts:
            available_prompts = breakout_prompts
            
        return random.choice(available_prompts)

    def get_core_concepts(self, n=5):
        """Get the core concepts from the concept network"""
        return self.concept_network.get_central_concepts(n)
    
    def get_concept_graph(self):
        """Get the entire concept graph"""
        return self.concept_network.graph

    def detect_repetition(self, threshold=0.8, window_size=5):
        """
        Enhanced repetition detection that can identify when the system is asking
        similar questions or providing similar answers repeatedly.
        
        Args:
            threshold: Similarity threshold for considering something repetitive
            window_size: How many recent entries to analyze for patterns
            
        Returns:
            Boolean indicating if repetition is detected
        """
        if len(self.entries) < window_size * 2:
            return False  # Not enough history to detect patterns
        
        # Extract the most recent prompts and responses
        recent_entries = self.entries[-(window_size*2):]
        recent_prompts = [entry.get('prompt', '') for entry in recent_entries]
        recent_responses = [entry.get('response', '') for entry in recent_entries]
        
        # Check for repeated identical prompts
        prompt_counts = {}
        for prompt in recent_prompts:
            if prompt:
                prompt_lower = prompt.lower()
                prompt_counts[prompt_lower] = prompt_counts.get(prompt_lower, 0) + 1
                if prompt_counts[prompt_lower] >= 3:  # Same prompt appears 3+ times
                    
                    # New in MVP 1.5: Emit repetition detected event
                    self.event_bus.publish(EventTypes.REPETITION_DETECTED, {
                        'type': 'identical_prompts',
                        'prompt': prompt_lower,
                        'count': prompt_counts[prompt_lower],
                        'window_size': window_size
                    })
                    
                    return True
        
        # Additional repetition detection logic could go here
        # Keep existing checks for semantic similarity, explore patterns, and concept cycles
        # Add event emission for each type of repetition detected
        
        return False  # If we get here, no repetition detected

    # New in MVP 1.5: Get observability data
    def get_observability_data(self):
        """Get a comprehensive dataset for observability"""
        # Get concept network statistics
        network_stats = self.concept_network.get_network_stats()
        
        # Get centrality metrics
        centrality = {}
        if hasattr(self.concept_network, 'graph') and len(self.concept_network.graph) > 0:
            try:
                import networkx as nx
                centrality = {
                    'degree': nx.degree_centrality(self.concept_network.graph),
                    'betweenness': nx.betweenness_centrality(self.concept_network.graph),
                    'pagerank': nx.pagerank(self.concept_network.graph)
                }
            except:
                pass
        
        # Extract recent memory trend metrics
        recent = self.get_recent(10)
        novelty_trend = [e.get('novelty', 0) for e in recent]
        reuse_trend = [e.get('reuse_score', 0) for e in recent]
        
        # Compute memory efficiency metrics
        memory_efficiency = {
            'compression_ratio': len(self.entries) / max(1, len(self.concept_network.concepts)),
            'concept_reuse': sum(c.get('reuse_count', 0) for c in self.concept_network.concepts.values()) / max(1, len(self.concept_network.concepts)),
            'symbol_density': len(self.symbols) / max(1, len(self.entries))
        }
        
        return {
            'network_stats': network_stats,
            'centrality': centrality,
            'memory_entries': len(self.entries),
            'symbols': self.symbols,
            'symbol_links': self.symbol_links,
            'novelty_trend': novelty_trend,
            'reuse_trend': reuse_trend,
            'memory_efficiency': memory_efficiency
        }