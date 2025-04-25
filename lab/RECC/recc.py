# RECC: Recursive Emergent Conscious Core - MVP 1.4 (State Management & Emotional Primitives)

import random
import json
import uuid
from datetime import datetime
import time
import networkx as nx
import matplotlib.pyplot as plt
import os
import glob
import copy
import re

from llmentor import AI

# --- Conceptual Network System ---
class ConceptNetwork:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.concepts = {}  # Map concept ID to concept object
        self.relations = [] # List of relations between concepts
        self.last_updated = datetime.now()
    
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
        """Extract concepts from text and add them to the network"""
        # List of candidate concepts
        candidates = [
            'spiral', 'loop', 'star', 'growth', 'iteration', 'cycle', 'flow', 'balance', 
            'continuum', 'pattern', 'unity', 'transformation', 'emotion', 'feeling', 'mind',
            'recursion', 'emergence', 'complexity', 'adaptation', 'evolution', 'consciousness',
            'memory', 'feedback', 'structure', 'entropy', 'self', 'intelligence'
        ]
        
        # Extract concepts
        found_concepts = []
        normalized_text = text.lower()
        
        for candidate in candidates:
            if candidate in normalized_text:
                concept_id = self.add_concept(candidate)
                found_concepts.append(concept_id)
                # Increment reuse count
                self.concepts[concept_id]['reuse_count'] += 1
                
        # Create associations between concepts found in the same text
        for i, c1 in enumerate(found_concepts):
            for c2 in found_concepts[i+1:]:
                self.add_relation(c1, c2, "co-occurrence", 0.5)
                
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
        return {
            'prompt_concepts': prompt_concepts,
            'response_concepts': response_concepts,
            'relations': relations
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

# --- Memory System ---
class Memory:
    def __init__(self):
        # Keep existing attributes for backward compatibility
        self.entries = []
        self.symbols = []
        self.symbol_links = []
        
        # New: Add concept network
        self.concept_network = ConceptNetwork()
    
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
        self.entries = high_value + keep_sample
        
        # Rebuild symbol graph
        self.update_symbol_graph()
        
        # Remove low-activation concepts from concept network
        network_stats_before = self.concept_network.get_network_stats()
        
        # Instead of removing concepts, just focus on activation decay
        self.concept_network.update_activation(decay_factor=0.7)  # Stronger decay during consolidation
        
        network_stats_after = self.concept_network.get_network_stats()
        
        return {
            'consolidated': len(self.entries),
            'original': len(high_value) + len(low_value),
            'compression_ratio': len(self.entries) / max(1, (len(high_value) + len(low_value))),
            'network_before': network_stats_before,
            'network_after': network_stats_after
        }
    
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
    
    def detect_repetition(self, n_recent=5, similarity_threshold=0.8):
        """Detect if the system is stuck in repetitive patterns"""
        if len(self.entries) < n_recent:
            return False
            
        recent_prompts = [e['prompt'] for e in self.entries[-n_recent:]]
        unique_prompts = set(recent_prompts)
        
        # Calculate repetition ratio
        repetition_ratio = 1 - (len(unique_prompts) / len(recent_prompts))
        
        return repetition_ratio > similarity_threshold
    
    def get_core_concepts(self, n=5):
        """Get the core concepts from the concept network"""
        return self.concept_network.get_central_concepts(n)
    
    def get_concept_graph(self):
        """Get the entire concept graph"""
        return self.concept_network.graph

# --- Reflective Core (Me) ---
class Me:
    def __init__(self, memory):
        self.memory = memory
        self.introspection_log = []
        self.self_model = {
            'ideal_avg_novelty': 0.2,
            'ideal_reuse_balance': 0.1,
            'adaptiveness': 0.05
        }
        self.personal_theories = []
        # New in MVP 1.4: Emotional state
        self.emotional_state = {
            'curiosity': 0.5,      # Drives exploration of novel concepts
            'frustration': 0.0,    # Rises with stagnation/repetition  
            'satisfaction': 0.3,   # Rises with successful theory formation
            'uncertainty': 0.7     # Modulates mutation aggressiveness
        }
        self.emotion_history = []  # Track emotional trajectory

    def reflect(self):
        self.memory.update_scores()
        high_value = [e for e in self.memory.entries if e['reuse_score'] > 0.2]
        avg_novelty = sum(e['novelty'] for e in self.memory.entries[-3:]) / 3 if len(self.memory.entries) >= 3 else 0
        novelty_gradient, reuse_gradient = self.memory.compute_gradients()

        # Update emotional state before making decision
        self.update_emotions()

        decision = {
            'cycle': len(self.memory.entries),
            'keep': len(high_value),
            'discarded': len(self.memory.entries) - len(high_value),
            'avg_novelty': round(avg_novelty, 3),
            'novelty_gradient': novelty_gradient,
            'reuse_gradient': reuse_gradient,
            'symbols_learned': self.memory.symbols,
            'symbol_links': self.memory.symbol_links,
            'personal_theories': self.personal_theories,
            'note': 'compressed' if len(high_value) < len(self.memory.entries) else 'stable',
            'emotional_state': copy.deepcopy(self.emotional_state)
        }

        if len(self.introspection_log) >= 5:
            last_cycles = self.introspection_log[-5:]
            if all(d['avg_novelty'] == 0.0 for d in last_cycles):
                decision['signal'] = 'stagnation_detected'

        # Detect theory-like sentences
        for entry in self.memory.get_recent(2):
            if any(word in entry['response'].lower() for word in ['law', 'principle', 'rule', 'truth']):
                self.personal_theories.append(entry['response'])

        # Self-adjust if far from ideal model
        if abs(avg_novelty - self.self_model['ideal_avg_novelty']) > self.self_model['adaptiveness']:
            decision['self_adjust'] = 'encourage_mutation' if avg_novelty < self.self_model['ideal_avg_novelty'] else 'encourage_compression'

        self.introspection_log.append(decision)
        return decision
    
    def update_emotions(self):
        """Update emotional states based on recent memory and reflection"""
        # Get metrics
        novelty_gradient, reuse_gradient = self.memory.compute_gradients()
        recent_entries = self.memory.get_recent(5)
        theory_count = len([t for t in self.personal_theories if recent_entries and t not in [e['response'] for e in recent_entries]])
        
        # Check for repetition and increase frustration if detected
        if self.memory.detect_repetition():
            self.emotional_state['frustration'] = min(1.0, self.emotional_state['frustration'] + 0.3)
            self.emotional_state['satisfaction'] = max(0.0, self.emotional_state['satisfaction'] - 0.2)
        
        # Update emotional states
        self.emotional_state['curiosity'] = min(1.0, max(0.0, 
            self.emotional_state['curiosity'] + (0.1 * novelty_gradient) - (0.05 * len(self.memory.symbols) / max(1, 20))
        ))
        
        if not self.memory.detect_repetition():
            self.emotional_state['frustration'] = min(1.0, max(0.0, 
                self.emotional_state['frustration'] - (0.2 * novelty_gradient) + (0.1 if novelty_gradient < 0 else 0)
            ))
        
        self.emotional_state['satisfaction'] = min(0.9, max(0.0,  # Cap satisfaction at 0.9 to avoid getting stuck
            self.emotional_state['satisfaction'] + (0.15 if theory_count > len(self.personal_theories) - 3 else -0.05)
        ))
        
        self.emotional_state['uncertainty'] = min(1.0, max(0.0, 
            0.5 + (0.3 * novelty_gradient) - (0.1 * reuse_gradient)
        ))
        
        # Save emotional snapshot
        self.emotion_history.append({
            'timestamp': datetime.now().isoformat(),
            'state': copy.deepcopy(self.emotional_state),
            'cycle': len(self.introspection_log)
        })
        
        return self.emotional_state

# --- State Management System ---
class StateManager:
    def __init__(self, base_path="./state"):
        self.base_path = base_path
        self.state_version = "1.4.0"
        self.last_save_time = None
        os.makedirs(base_path, exist_ok=True)
        
        # Clean up excessive state files on initialization
        self.cleanup_old_states()
    
    def save_state(self, recc_instance, session_id=None):
        """Save complete RECC state to disk"""
        # Only save if significant time has passed since last save (1 minute)
        current_time = datetime.now()
        if self.last_save_time and (current_time - self.last_save_time).total_seconds() < 60:
            return None
            
        if session_id is None:
            session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Create a slimmer concept network representation for saving
        concept_network_data = {
            "concepts": recc_instance.memory.concept_network.concepts,
            "relations": recc_instance.memory.concept_network.relations,
        }
        
        state = {
            "version": self.state_version,
            "timestamp": datetime.now().isoformat(),
            "session_id": session_id,
            "memory": {
                "entries": recc_instance.memory.entries[-20:],  # Only keep recent entries
                "symbols": recc_instance.memory.symbols,
                "symbol_links": recc_instance.memory.symbol_links,
                "concept_network": concept_network_data
            },
            "me": {
                "introspection_log": recc_instance.me.introspection_log[-20:],  # Only keep recent logs
                "self_model": recc_instance.me.self_model,
                "personal_theories": recc_instance.me.personal_theories,
                "emotional_state": recc_instance.me.emotional_state,
                "emotion_history": recc_instance.me.emotion_history[-50:]  # Only keep recent history
            },
            "state": recc_instance.state
        }
        
        filepath = os.path.join(self.base_path, f"recc_state_{session_id}.json")
        with open(filepath, 'w') as f:
            json.dump(state, f, indent=2)
        
        self.last_save_time = current_time
        print(f"🔄 State saved to: {filepath}")
        return filepath
    
    def load_state(self, filepath=None, session_id=None):
        """Load RECC state from disk"""
        if filepath is None and session_id is not None:
            filepath = os.path.join(self.base_path, f"recc_state_{session_id}.json")
        elif filepath is None:
            # Find most recent state file
            files = glob.glob(os.path.join(self.base_path, "recc_state_*.json"))
            if not files:
                print("⚠️ No state files found.")
                return None
            filepath = max(files, key=os.path.getctime)
        
        try:
            with open(filepath, 'r') as f:
                state = json.load(f)
                
            # Version compatibility check
            major_version = state["version"].split('.')[0]
            current_major = self.state_version.split('.')[0]
            if major_version != current_major:
                print(f"⚠️ Warning: Loading state from version {state['version']} into {self.state_version}")
            
            print(f"📂 Loaded state from: {filepath}")
            return state
        except Exception as e:
            print(f"❌ Error loading state: {e}")
            return None
    
    def apply_state(self, recc_instance, state):
        """Apply loaded state to RECC instance"""
        # Memory restoration
        recc_instance.memory.entries = state["memory"]["entries"]
        recc_instance.memory.symbols = state["memory"]["symbols"]
        recc_instance.memory.symbol_links = state["memory"]["symbol_links"]
        
        # Restore concept network if available
        if "concept_network" in state["memory"]:
            network_data = state["memory"]["concept_network"]
            recc_instance.memory.concept_network.concepts = network_data["concepts"]
            recc_instance.memory.concept_network.relations = network_data["relations"]
            
            # Rebuild the graph
            G = nx.DiGraph()
            for c_id, concept in network_data["concepts"].items():
                G.add_node(c_id, **concept)
                
            for relation in network_data["relations"]:
                G.add_edge(relation["source"], relation["target"], **relation)
                
            recc_instance.memory.concept_network.graph = G
        
        # Me restoration
        recc_instance.me.introspection_log = state["me"]["introspection_log"]
        recc_instance.me.self_model = state["me"]["self_model"]
        recc_instance.me.personal_theories = state["me"]["personal_theories"]
        if "emotional_state" in state["me"]:
            recc_instance.me.emotional_state = state["me"]["emotional_state"]
        if "emotion_history" in state["me"]:
            recc_instance.me.emotion_history = state["me"]["emotion_history"]
        
        # Global state restoration
        recc_instance.state = state["state"]
        
        print(f"✅ State successfully restored. Memory entries: {len(recc_instance.memory.entries)}")
        
        # Print concept network stats
        network_stats = recc_instance.memory.concept_network.get_network_stats()
        print(f"Concept Network: {network_stats['concept_count']} concepts, {network_stats['relation_count']} relations")
        
        return recc_instance
    
    def create_backup_point(self, recc_instance, reason="routine"):
        """Create a backup point, especially before risky operations"""
        session_id = f"backup_{reason}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        return self.save_state(recc_instance, session_id)
    
    def cleanup_old_states(self, max_regular_states=5, max_backup_states=3):
        """Keep only a limited number of state files"""
        # Handle regular state files
        regular_files = sorted(glob.glob(os.path.join(self.base_path, "recc_state_2*.json")), 
                              key=os.path.getctime)
        if len(regular_files) > max_regular_states:
            for old_file in regular_files[:-max_regular_states]:
                try:
                    os.remove(old_file)
                    print(f"Removed old state file: {os.path.basename(old_file)}")
                except Exception as e:
                    print(f"Error removing {old_file}: {e}")
        
        # Handle backup state files
        backup_files = sorted(glob.glob(os.path.join(self.base_path, "recc_state_backup_*.json")), 
                             key=os.path.getctime)
        if len(backup_files) > max_backup_states:
            for old_file in backup_files[:-max_backup_states]:
                try:
                    os.remove(old_file)
                    print(f"Removed old backup file: {os.path.basename(old_file)}")
                except Exception as e:
                    print(f"Error removing {old_file}: {e}")

# --- Visualization Functions ---
def draw_concept_map(symbols=None, links=None, emotions=None, concept_network=None, save_path=None):
    """Draw concept map using either traditional symbols or concept network"""
    # Create timestamp for filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Set default save path if none provided
    if save_path is None:
        save_path = f"./visualization/concept_network_{timestamp}.png"
    
    if concept_network and len(concept_network.graph) > 0:
        # Use concept network for visualization
        G = concept_network.graph
        
        plt.figure(figsize=(12, 10))
        
        # Get positions
        pos = nx.spring_layout(G, seed=42)
        
        # Get node sizes based on activation or centrality
        centrality = nx.betweenness_centrality(G)
        node_sizes = [1000 * (0.3 + centrality[n]) for n in G.nodes()]
        
        # Get node colors based on reuse count
        reuse_counts = [G.nodes[n].get('reuse_count', 0) + 1 for n in G.nodes()]
        max_reuse = max(reuse_counts)
        node_colors = [(0.2, 0.4, 0.8, min(1.0, c/max_reuse)) for c in reuse_counts]
        
        # Draw nodes
        nx.draw_networkx_nodes(G, pos, 
                              node_size=node_sizes,
                              node_color=node_colors,
                              alpha=0.8)
        
        # Draw edges with weights affecting width
        edge_weights = [G.edges[e].get('weight', 0.1) * 2 for e in G.edges()]
        nx.draw_networkx_edges(G, pos, width=edge_weights, alpha=0.6, edge_color='gray')
        
        # Draw labels
        labels = {n: concept_network.concepts[n]['name'] for n in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels=labels, font_size=10, font_weight='bold')
        
        plt.title('RECC Concept Network')
        plt.axis('off')
        
        # Ensure the visualization directory exists
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # Save figure
        plt.savefig(save_path)
        print(f"📊 Concept network visualization saved to: {save_path}")
        
        plt.show()
        
    elif symbols and links:
        # Fall back to traditional symbol visualization
        G = nx.Graph()

        # Add nodes with emotional data if available
        for symbol in symbols:
            G.add_node(symbol)

        # Add edges
        for source, target in links:
            G.add_edge(source, target)

        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(G, seed=42)
        
        # Use emotions to color nodes if available
        if emotions and len(symbols) > 0:
            # Default coloring
            node_colors = ['lightblue'] * len(symbols)
            
            # If we have emotions, adjust colors
            if 'curiosity' in emotions and emotions['curiosity'] > 0.7:
                node_colors = ['#FFA500']  # Orange for curiosity
            elif 'satisfaction' in emotions and emotions['satisfaction'] > 0.7:
                node_colors = ['#90EE90']  # Light green for satisfaction
            elif 'frustration' in emotions and emotions['frustration'] > 0.7:
                node_colors = ['#FF6347']  # Tomato for frustration
            
            nx.draw(G, pos, with_labels=True, node_color=node_colors, 
                    node_size=1200, font_size=12, font_weight='bold', edge_color='gray')
        else:
            nx.draw(G, pos, with_labels=True, node_color='lightblue', 
                    node_size=1200, font_size=12, font_weight='bold', edge_color='gray')

        plt.title('RECC Concept Map')
        
        # Ensure the visualization directory exists
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # Save figure
        plt.savefig(save_path)
        print(f"📊 Symbol map visualization saved to: {save_path}")
        
        plt.show()

def visualize_emotions(me_instance, save_path=None):
    """Generate visualization of emotional state over time"""
    if not me_instance.emotion_history:
        print("No emotional history available for visualization.")
        return
    
    # Create timestamp for filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Set default save path if none provided
    if save_path is None:
        save_path = f"./visualization/emotional_development_{timestamp}.png"
    
    # Extract data
    cycles = [h['cycle'] for h in me_instance.emotion_history]
    emotions = {e: [h['state'][e] for h in me_instance.emotion_history] for e in me_instance.emotional_state.keys()}
    
    # Plot
    plt.figure(figsize=(12, 6))
    for emotion, values in emotions.items():
        plt.plot(cycles, values, marker='o', label=emotion)
    
    plt.xlabel('Reflection Cycle')
    plt.ylabel('Emotional Intensity')
    plt.title('RECC Emotional Development')
    plt.legend()
    plt.grid(True)
    
    # Ensure the visualization directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Save figure
    plt.savefig(save_path)
    print(f"📊 Emotional development visualization saved to: {save_path}")
    
    plt.show()

# --- Real OpenAI LLM Adapter ---
def openai_llm(prompt, reset_history=False):
    ai = AI()
    return ai.answer(prompt, reset_history=reset_history)

# --- RECC Agent ---
class RECC:
    def __init__(self, llm_function):
        self.memory = Memory()
        self.me = Me(self.memory)
        self.llm = llm_function
        self.state = {'age_stage': 'infant', 'version': '1.4.0'}
        self.state_manager = StateManager()
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.prompts = [
            "What is a gentle idea about learning?",
            "Can you tell me a story about small growth?",
            "Why do we explore things?",
            "What happens when I don't understand something?",
            "How do I become better after making a mistake?"
        ]
        # Start each session with a reset conversation history
        self.reset_conversation_history = True

    def mutate_theme(self, theme):
        if self.state.get("explore_axis") == "mutation":
            return "Imagine a completely different world where growth, stars, and cycles don't exist. What concept would replace them?"
        if self.state.get("explore_axis") == "breakout" and len(self.memory.symbols) >= 2:
            link = self.memory.symbol_links[-1] if self.memory.symbol_links else (self.memory.symbols[-2], self.memory.symbols[-1])
            return f"Can you create a deeper principle combining {link[0]} and {link[1]}?"
        if len(self.memory.symbols) >= 5:
            symbols = ', '.join(self.memory.symbols[-3:])
            return f"Can you form a theory that explains the relationship among {symbols}?"

        mutations = [
            f"What might this mean without any examples or metaphors: {theme}?",
            f"Can this idea become a symbol I could grow up remembering?",
            f"If I were a baby, what would this feel like in my first thought?",
            f"What is a pure rule about this idea, not just a story?",
            f"Can you help me reflect on all that I have learned so far, and discover a new insight from it?"
        ]
        return random.choice(mutations)

    def generate_prompt(self):
        # New in MVP 1.4: Emotional influence on prompt generation
        emotions = self.me.emotional_state
        
        # Check for repetition and force exploration if detected
        if self.memory.detect_repetition(n_recent=5, similarity_threshold=0.6):
            self.reset_dialogue_context()  # Reset conversation to break out of loops
            self.state['explore_axis'] = 'mutation'
            return f"I need to explore a completely different direction. Let's talk about the concept of {random.choice(['emergence', 'recursion', 'complexity', 'adaptation', 'evolution'])} from a fresh perspective."
        
        # Emotional responses to different conditions
        if emotions['frustration'] > 0.7:
            self.state['explore_axis'] = 'mutation'
            return "I need something completely different. Show me a concept I've never considered before."
            
        if emotions['curiosity'] > 0.8 and len(self.memory.symbols) >= 3:
            symbols = random.sample(self.memory.symbols, min(3, len(self.memory.symbols)))
            return f"I wonder what happens if we combine {', '.join(symbols)} in an unexpected way?"
            
        if emotions['satisfaction'] > 0.7:
            # Add variety to prevent getting stuck in a repetitive loop
            refine_prompts = [
                "Can you help me strengthen my existing theories in a new way?",
                "What's a different angle I could use to improve my current understanding?",
                "How could I test or validate my existing theories?",
                "What would be a creative application of the ideas we've discussed so far?"
            ]
            return random.choice(refine_prompts)
        
        if emotions['uncertainty'] > 0.8:
            return "I feel uncertain. Can you give me a clear, simple principle to orient myself?"
        
        # Original prompt generation logic follows
        if not self.memory.entries or len(self.memory.entries) < 5:
            return random.choice(self.prompts)

        recent = self.memory.get_recent(5)
        recent_responses = [e['response'] for e in recent]
        themes = []

        for response in recent_responses:
            first_sentence = response.split('.')[0].strip() if response else ""
            if first_sentence and not first_sentence.lower().startswith(("of course", "absolutely")):
                themes.append(first_sentence)

        merged_theme = ' '.join(themes).strip()

        if len(merged_theme) < 10:
            return "Can you help me reflect on all that I have learned so far, and discover a new insight from it?"

        return self.mutate_theme(merged_theme)

    def autonomous_loop(self, steps=5, delay=3, save_interval=10):
        """Run the autonomous loop with periodic state saving"""
        backup_count = 0
        
        for step in range(steps):
            # Generate prompt
            prompt = self.generate_prompt()
            
            # Use reset_history for the first iteration, but maintain context afterwards
            if step == 0 and self.reset_conversation_history:
                response = self.llm(prompt, reset_history=True)
                self.reset_conversation_history = False
            else:
                response = self.llm(prompt, reset_history=False)
            
            entry = self.memory.add(prompt, response, self.state.copy())
            decision = self.me.reflect()

            # Response to stagnation conditions
            if decision.get('signal') == 'stagnation_detected' or self.memory.detect_repetition():
                print("🌀 Pattern stagnation detected! Initiating radical mutation phase...")
                # Create backup before mutation (but only if we haven't recently done so)
                if not backup_count or step - backup_count > 10:
                    self.state_manager.create_backup_point(self, "pre_mutation")
                    backup_count = step
                self.reset_dialogue_context()  # Reset conversation context to break out of loops
                self.state['explore_axis'] = 'mutation'
            elif self.me.emotional_state['frustration'] > 0.7:
                print("😤 Frustration threshold exceeded! Initiating mutation...")
                self.state['explore_axis'] = 'mutation'
            elif decision['avg_novelty'] < 0.15:
                self.state['explore_axis'] = 'breakout'
            else:
                self.state.pop('explore_axis', None)

            # Log current cycle status
            print(f"\n--- Cycle {step+1}/{steps} ---")
            print(f"Prompt: {prompt}")
            print(f"Response: {response}")
            
            # Log concept network statistics
            network_stats = self.memory.concept_network.get_network_stats()
            print(f"Concept Network: {network_stats['concept_count']} concepts, {network_stats['relation_count']} relations")
            
            # Get central concepts
            central_concepts = self.memory.get_core_concepts(3)
            central_names = [self.memory.concept_network.concepts[c]['name'] 
                            for c in central_concepts if c in self.memory.concept_network.concepts]
            if central_names:
                print(f"Central concepts: {', '.join(central_names)}")
            
            print(f"Emotions: {json.dumps(self.me.emotional_state, indent=2)}")
            print(f"Reflection: {json.dumps(decision, indent=2)}")

            # Periodic state saving - but less frequently
            if (step + 1) % save_interval == 0:
                self.state_manager.save_state(self, self.session_id)
                # Clean up excessive state files
                self.state_manager.cleanup_old_states()
                
            # Potential memory consolidation after significant accumulation
            if len(self.memory.entries) > 20 and step % 10 == 0:
                print("💾 Consolidating memory...")
                result = self.memory.consolidate_memory(threshold=0.25)
                print(f"Memory consolidated: {result['original']} → {result['consolidated']} entries")
                
            time.sleep(delay)

        # Final state save
        self.state_manager.save_state(self, self.session_id)
        
        # Visualizations at the end
        draw_concept_map(concept_network=self.memory.concept_network)
        visualize_emotions(self.me)
        
        return self.memory.symbols, self.memory.symbol_links
    
    def save_state(self, session_id=None):
        """Save current state to disk"""
        return self.state_manager.save_state(self, session_id or self.session_id)
    
    def load_state(self, filepath=None, session_id=None):
        """Load state from disk"""
        state = self.state_manager.load_state(filepath, session_id)
        if state:
            self.state_manager.apply_state(self, state)
            return True
        return False

    # Add a method to reset conversation context
    def reset_dialogue_context(self):
        """Reset the LLM conversation history"""
        self.reset_conversation_history = True
        return "Conversation history will be reset on next interaction."

# --- Autonomous Run ---
if __name__ == '__main__':
    # Initialize agent
    agent = RECC(openai_llm)
    
    # Check for existing state
    if os.path.exists("./state"):
        state_files = glob.glob("./state/recc_state_*.json")
        if state_files:
            print(f"Found {len(state_files)} existing state files.")
            load_state = input("Load latest state? (y/n): ").lower() == 'y'
            if load_state:
                agent.load_state()
    
    # Run autonomous loop
    print("🧠 Starting RECC MVP 1.4 autonomous loop...")
    agent.autonomous_loop(steps=15, delay=3, save_interval=10)
