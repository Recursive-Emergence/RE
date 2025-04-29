"""
State Management Module
Handles saving and loading RECC state to/from disk
"""
import os
import glob
import json
from datetime import datetime

class StateManager:
    def __init__(self, base_path="./state"):
        self.base_path = base_path
        self.state_version = "1.5.0"
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
        try:
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
                import networkx as nx
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
            
        except Exception as e:
            print(f"❌ Error applying state: {e}")
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
                    
    def list_available_states(self):
        """List all available saved states"""
        files = glob.glob(os.path.join(self.base_path, "recc_state_*.json"))
        states = []
        
        for file in sorted(files, key=os.path.getctime, reverse=True):
            try:
                with open(file, 'r') as f:
                    data = json.load(f)
                states.append({
                    'filepath': file,
                    'session_id': data.get('session_id', 'unknown'),
                    'timestamp': data.get('timestamp', ''),
                    'version': data.get('version', 'unknown'),
                    'memory_entries': len(data.get('memory', {}).get('entries', [])),
                    'file_size': os.path.getsize(file) // 1024  # Size in KB
                })
            except:
                # If can't parse, just add basic file info
                states.append({
                    'filepath': file,
                    'session_id': os.path.basename(file).replace('recc_state_', '').replace('.json', ''),
                    'timestamp': datetime.fromtimestamp(os.path.getctime(file)).isoformat(),
                    'version': 'unknown',
                    'file_size': os.path.getsize(file) // 1024  # Size in KB
                })
                
        return states