"""
SelfModel component: maintains an explicit self-model and generates introspection tokens for self-reinforcement.
Also includes specialized learning acceleration from LLM mentor interactions.
"""
import time

class SelfModel:
    def __init__(self, memory_graph, introspection_size=3):
        self.memory_graph = memory_graph
        self.introspection_size = introspection_size
        # For tracking mentor interactions and extracting patterns
        self.mentor_interactions = []
        self.pattern_extraction_threshold = 3  # How many similar interactions before forming a pattern
        self.last_reflection_time = time.time()
        self.reflection_interval = 60 * 5  # 5 minutes between deep reflections

    def simulate(self, input_tokens):
        """
        Generate introspection tokens reflecting the agent's internal state.
        For each input token, find related patterns in memory_graph and
        collect their content as introspection tokens.
        """
        introspection = []
        # for each token, find node IDs and neighbors
        for token in input_tokens:
            node_ids = self.memory_graph.find_nodes_by_keyword(token)
            for nid in node_ids:
                # get neighbors of this node
                neighbors = self.memory_graph.get_neighbors(nid)
                for neighbor_id in neighbors:
                    node = self.memory_graph.get_node(neighbor_id)
                    if node and node.content not in introspection:
                        introspection.extend(node.content.split())
                        if len(introspection) >= self.introspection_size:
                            return introspection[:self.introspection_size]
        # fallback self-reflection token
        return ['self', 'reflect']
    
    def record_mentor_interaction(self, input_tokens, mentor_response):
        """
        Record an interaction with the LLM mentor for later pattern extraction.
        This builds a dataset of mentor interactions for compressed learning.
        """
        self.mentor_interactions.append({
            'input': input_tokens,
            'response': mentor_response,
            'timestamp': time.time()
        })
        
        # Check if it's time for deep reflection (pattern extraction)
        current_time = time.time()
        if current_time - self.last_reflection_time > self.reflection_interval:
            self.extract_mentor_patterns()
            self.last_reflection_time = current_time
            
        return True
        
    def extract_mentor_patterns(self):
        """
        Analyze recorded mentor interactions to extract high-value patterns.
        These become compressed knowledge structures that the ACI can reuse.
        """
        if len(self.mentor_interactions) < self.pattern_extraction_threshold:
            return []
            
        # Group similar interactions
        patterns = []
        
        # A simple clustering approach - group by keyword overlap
        for i, interaction in enumerate(self.mentor_interactions):
            # Skip already processed interactions
            if 'processed' in interaction and interaction['processed']:
                continue
                
            # Find similar interactions based on input keyword overlap
            cluster = [interaction]
            interaction['processed'] = True
            
            for j in range(i+1, len(self.mentor_interactions)):
                other = self.mentor_interactions[j]
                if 'processed' in other and other['processed']:
                    continue
                    
                # Simple similarity: common keywords
                common_words = set(interaction['input']) & set(other['input'])
                if len(common_words) >= 2:  # At least 2 common keywords
                    cluster.append(other)
                    other['processed'] = True
            
            # If we found a cluster of similar interactions
            if len(cluster) >= self.pattern_extraction_threshold:
                # Extract common pattern from responses
                response_texts = [' '.join(inter['response'].split()) for inter in cluster if 'response' in inter]
                
                # Extract a simple pattern (this could be more sophisticated)
                if response_texts:
                    # Create a compressed pattern node from these similar interactions
                    pattern_content = f"pattern:{','.join(common_words)}"
                    pattern_id = self.memory_graph.add_node(pattern_content)
                    
                    # Add connections to original input keywords
                    for word in common_words:
                        word_nodes = self.memory_graph.find_nodes_by_keyword(word)
                        if word_nodes:
                            self.memory_graph.add_edge(pattern_id, word_nodes[0], 'pattern_of', 2.0)
                    
                    # Add this high-persistence pattern
                    patterns.append({
                        'id': pattern_id,
                        'content': pattern_content,
                        'source_interactions': len(cluster)
                    })
                    
                    # Boost the persistence of this pattern node (compressed knowledge)
                    self.memory_graph.update_persistence(pattern_id, 2.0)
        
        # Reset processed flags for next time
        for interaction in self.mentor_interactions:
            if 'processed' in interaction:
                del interaction['processed']
                
        return patterns
        
    def generate_reflection_prompt(self):
        """
        Generate a self-reflection prompt based on accumulated knowledge.
        Used during quiet periods to stimulate mentor-guided learning.
        """
        # Find highest persistence nodes (our most stable knowledge)
        nodes_by_persistence = sorted(
            [(nid, node.persistence_score) for nid, node in self.memory_graph.nodes.items()],
            key=lambda x: x[1],
            reverse=True
        )[:5]  # Top 5 highest-persistence nodes
        
        if not nodes_by_persistence:
            return "What am I learning about my environment?"
            
        # Get the content of these high-persistence nodes
        high_p_contents = [self.memory_graph.get_node(nid).content for nid, _ in nodes_by_persistence]
        
        # Form a reflection question based on these
        reflection_prompt = f"How do {high_p_contents[0]} and {high_p_contents[1]} relate to each other?"
        
        return reflection_prompt
