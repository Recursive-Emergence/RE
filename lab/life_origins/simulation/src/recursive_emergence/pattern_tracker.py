"""
Pattern Tracking for Recursive Emergence

This module identifies and tracks emergent patterns in chemical simulations,
measuring their persistence, reusability, and relationships.
"""

import uuid
import networkx as nx
import numpy as np
from collections import defaultdict
from typing import Dict, List, Set, Any, Optional, Tuple

class Pattern:
    """
    Represents an emergent pattern in a chemical simulation.
    
    A pattern is a collection of components that persist and interact
    in a recognizable way over time.
    """
    
    def __init__(self, pattern_type: str, components: List[Any], layer: str):
        """
        Initialize a pattern.
        
        Args:
            pattern_type: Type of pattern (e.g., 'cycle', 'motif', 'compartment')
            components: List of components in the pattern
            layer: Organizational layer the pattern belongs to
        """
        self.id = str(uuid.uuid4())[:8]  # Short ID for the pattern
        self.pattern_type = pattern_type
        self.components = components
        self.layer = layer
        self.first_seen = None
        self.last_seen = None
        self.appearances = 0
        self.persistence = 0.0  # How long the pattern persists
        self.reusability = 0.0  # How often the pattern is reused in higher structures
        self.stability = 0.0    # How resistant to perturbations
        self.references = []    # Other patterns that reference this pattern
        
    def update_seen(self, timestep: int) -> None:
        """
        Update when the pattern was seen.
        
        Args:
            timestep: Current simulation timestep
        """
        if self.first_seen is None:
            self.first_seen = timestep
        
        self.last_seen = timestep
        self.appearances += 1
        
        # Update persistence based on time range and appearance frequency
        if self.first_seen < self.last_seen:
            time_range = self.last_seen - self.first_seen
            self.persistence = time_range * (self.appearances / (time_range + 1))
            
    def add_reference(self, pattern_id: str) -> None:
        """
        Add a reference to another pattern that uses this one.
        
        Args:
            pattern_id: ID of the referencing pattern
        """
        if pattern_id not in self.references:
            self.references.append(pattern_id)
            self.reusability = len(self.references)
            
    def update_metrics(self) -> None:
        """Update derived metrics for the pattern."""
        if self.appearances > 0:
            self.stability = min(1.0, self.persistence / self.appearances)
        
        self.reusability = len(self.references)
        
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert pattern to dictionary.
        
        Returns:
            dict: Dictionary representation of the pattern
        """
        return {
            'id': self.id,
            'type': self.pattern_type,
            'layer': self.layer,
            'first_seen': self.first_seen,
            'last_seen': self.last_seen,
            'appearances': self.appearances,
            'persistence': self.persistence,
            'reusability': self.reusability,
            'stability': self.stability,
            'component_count': len(self.components),
            'references': len(self.references)
        }
        
    def __str__(self) -> str:
        """String representation of the pattern."""
        return f"Pattern[{self.id}]: {self.pattern_type} ({self.layer}) - {len(self.components)} components"

class PatternTracker:
    """
    Tracks emergent patterns across a chemical simulation.
    """
    
    def __init__(self):
        """Initialize pattern tracker."""
        self.patterns = {}  # id -> Pattern
        self.active_patterns = set()  # IDs of patterns active in current timestep
        self.patterns_by_type = defaultdict(list)  # type -> [pattern_ids]
        self.patterns_by_layer = defaultdict(list)  # layer -> [pattern_ids]
        self.pattern_relationships = defaultdict(list)  # pattern_id -> [related_pattern_ids]
        self.history = defaultdict(list)  # metric -> [values over time]
        self.timestep = 0
        
    def update(self, network, timestep: int) -> None:
        """
        Update pattern tracking based on current network state.
        
        Args:
            network: ChemicalNetwork instance
            timestep: Current simulation timestep
        """
        self.timestep = timestep
        self.active_patterns = set()
        
        # 1. Detect chemical patterns (cycles, motifs, etc.)
        self._detect_chemical_patterns(network)
        
        # 2. Detect replicative patterns
        self._detect_replicative_patterns(network)
        
        # 3. Detect autocatalytic patterns
        self._detect_autocatalytic_patterns(network)
        
        # 4. Detect compartmental patterns
        self._detect_compartmental_patterns(network)
        
        # 5. Update pattern metrics
        for pattern_id in self.patterns:
            self.patterns[pattern_id].update_metrics()
            
        # 6. Update history
        self.history['total_patterns'].append(len(self.patterns))
        self.history['active_patterns'].append(len(self.active_patterns))
        self.history['patterns_by_layer'] = {
            layer: len(pids) for layer, pids in self.patterns_by_layer.items()
        }
        self.history['patterns_by_type'] = {
            ptype: len(pids) for ptype, pids in self.patterns_by_type.items()
        }
        
    def _detect_chemical_patterns(self, network) -> None:
        """
        Detect chemical patterns in the network.
        
        Args:
            network: ChemicalNetwork instance
        """
        # 1. Look for reaction cycles
        if hasattr(network, 'reaction_graph'):
            cycles = self._find_cycles(network.reaction_graph)
            for cycle in cycles:
                pattern_key = self._get_pattern_hash('cycle', cycle)
                
                if pattern_key not in self.patterns:
                    pattern = Pattern('reaction_cycle', cycle, 'chemical')
                    self.patterns[pattern.id] = pattern
                    self.patterns_by_type['reaction_cycle'].append(pattern.id)
                    self.patterns_by_layer['chemical'].append(pattern.id)
                else:
                    pattern = self.patterns[pattern_key]
                    
                pattern.update_seen(self.timestep)
                self.active_patterns.add(pattern.id)
                
        # 2. Check for catalytic motifs
        if hasattr(network, 'reactions'):
            catalytic_reactions = []
            for reaction in network.reactions:
                if hasattr(reaction, 'has_catalyst') and reaction.has_catalyst:
                    catalytic_reactions.append(reaction)
                    
            if catalytic_reactions:
                pattern_key = self._get_pattern_hash('catalytic_motif', catalytic_reactions)
                
                if pattern_key not in self.patterns:
                    pattern = Pattern('catalytic_motif', catalytic_reactions, 'chemical')
                    self.patterns[pattern.id] = pattern
                    self.patterns_by_type['catalytic_motif'].append(pattern.id)
                    self.patterns_by_layer['chemical'].append(pattern.id)
                else:
                    pattern = self.patterns[pattern_key]
                    
                pattern.update_seen(self.timestep)
                self.active_patterns.add(pattern.id)
                
        # 3. Find persistent molecular clusters
        if hasattr(network, 'get_molecular_clusters'):
            clusters = network.get_molecular_clusters()
            for cluster in clusters:
                if len(cluster) >= 3:  # Only track significant clusters
                    pattern_key = self._get_pattern_hash('molecular_cluster', cluster)
                    
                    if pattern_key not in self.patterns:
                        pattern = Pattern('molecular_cluster', cluster, 'chemical')
                        self.patterns[pattern.id] = pattern
                        self.patterns_by_type['molecular_cluster'].append(pattern.id)
                        self.patterns_by_layer['chemical'].append(pattern.id)
                    else:
                        pattern = self.patterns[pattern_key]
                        
                    pattern.update_seen(self.timestep)
                    self.active_patterns.add(pattern.id)
    
    def _detect_replicative_patterns(self, network) -> None:
        """
        Detect replicative patterns in the network.
        
        Args:
            network: ChemicalNetwork instance
        """
        # 1. Check for template-based replication
        template_molecules = []
        
        if hasattr(network, 'molecules'):
            for molecule in network.molecules:
                if hasattr(molecule, 'is_template') and molecule.is_template:
                    template_molecules.append(molecule)
                    
        if template_molecules:
            pattern_key = self._get_pattern_hash('template_replication', template_molecules)
            
            if pattern_key not in self.patterns:
                pattern = Pattern('template_replication', template_molecules, 'replicative')
                self.patterns[pattern.id] = pattern
                self.patterns_by_type['template_replication'].append(pattern.id)
                self.patterns_by_layer['replicative'].append(pattern.id)
            else:
                pattern = self.patterns[pattern_key]
                
            pattern.update_seen(self.timestep)
            self.active_patterns.add(pattern.id)
            
            # Connect to related chemical patterns
            for chem_id in self.patterns_by_layer.get('chemical', []):
                if self._check_pattern_relationship(pattern, self.patterns[chem_id]):
                    self.pattern_relationships[pattern.id].append(chem_id)
                    self.patterns[chem_id].add_reference(pattern.id)
                    
    def _detect_autocatalytic_patterns(self, network) -> None:
        """
        Detect autocatalytic patterns in the network.
        
        Args:
            network: ChemicalNetwork instance
        """
        # 1. Find autocatalytic sets or cycles
        autocatalytic_sets = []
        
        if hasattr(network, 'find_autocatalytic_sets'):
            autocatalytic_sets = network.find_autocatalytic_sets()
        elif hasattr(network, 'get_final_analysis'):
            analysis = network.get_final_analysis()
            if 'autocatalytic_sets' in analysis:
                autocatalytic_sets = analysis['autocatalytic_sets']
                
        for autocatalytic_set in autocatalytic_sets:
            if autocatalytic_set:  # Ensure the set is not empty
                pattern_key = self._get_pattern_hash('autocatalytic_set', autocatalytic_set)
                
                if pattern_key not in self.patterns:
                    pattern = Pattern('autocatalytic_set', autocatalytic_set, 'autocatalytic')
                    self.patterns[pattern.id] = pattern
                    self.patterns_by_type['autocatalytic_set'].append(pattern.id)
                    self.patterns_by_layer['autocatalytic'].append(pattern.id)
                else:
                    pattern = self.patterns[pattern_key]
                    
                pattern.update_seen(self.timestep)
                self.active_patterns.add(pattern.id)
                
                # Connect to related replicative patterns
                for repl_id in self.patterns_by_layer.get('replicative', []):
                    if self._check_pattern_relationship(pattern, self.patterns[repl_id]):
                        self.pattern_relationships[pattern.id].append(repl_id)
                        self.patterns[repl_id].add_reference(pattern.id)
    
    def _detect_compartmental_patterns(self, network) -> None:
        """
        Detect compartmental patterns in the network.
        
        Args:
            network: ChemicalNetwork instance
        """
        # 1. Check for membrane-bound compartments
        compartments = []
        
        if hasattr(network, 'compartments'):
            compartments = network.compartments
        elif hasattr(network, 'get_compartments'):
            compartments = network.get_compartments()
            
        for compartment in compartments:
            # Create a pattern for each compartment
            pattern_key = self._get_pattern_hash('compartment', compartment)
            
            if pattern_key not in self.patterns:
                pattern = Pattern('compartment', compartment, 'compartmental')
                self.patterns[pattern.id] = pattern
                self.patterns_by_type['compartment'].append(pattern.id)
                self.patterns_by_layer['compartmental'].append(pattern.id)
            else:
                pattern = self.patterns[pattern_key]
                
            pattern.update_seen(self.timestep)
            self.active_patterns.add(pattern.id)
            
            # Connect to related autocatalytic patterns
            for auto_id in self.patterns_by_layer.get('autocatalytic', []):
                if self._check_pattern_relationship(pattern, self.patterns[auto_id]):
                    self.pattern_relationships[pattern.id].append(auto_id)
                    self.patterns[auto_id].add_reference(pattern.id)
    
    def _find_cycles(self, graph) -> List[List[Any]]:
        """
        Find simple cycles in a graph.
        
        Args:
            graph: NetworkX graph or similar
            
        Returns:
            list: List of cycles (each cycle is a list of nodes)
        """
        try:
            import networkx as nx
            return list(nx.simple_cycles(graph))
        except (ImportError, AttributeError):
            # Fallback method if NetworkX is not available
            cycles = []
            
            # Try to detect cycles using basic methods
            if hasattr(graph, 'nodes') and hasattr(graph, 'edges'):
                # Simple DFS cycle detection
                visited = set()
                rec_stack = set()
                
                def dfs(node, parent, path):
                    visited.add(node)
                    rec_stack.add(node)
                    path.append(node)
                    
                    for neighbor in graph[node]:
                        if neighbor == parent:
                            continue
                            
                        if neighbor not in visited:
                            if dfs(neighbor, node, path):
                                return True
                        elif neighbor in rec_stack:
                            # Found a cycle
                            cycle_start = path.index(neighbor)
                            cycles.append(path[cycle_start:])
                            return True
                            
                    rec_stack.remove(node)
                    path.pop()
                    return False
                
                for node in graph.nodes():
                    if node not in visited:
                        dfs(node, None, [])
                        
            return cycles
    
    def _get_pattern_hash(self, pattern_type: str, components: List[Any]) -> str:
        """
        Generate a hash for a pattern.
        
        Args:
            pattern_type: Type of pattern
            components: Components of the pattern
            
        Returns:
            str: Pattern hash
        """
        # Create a simplified representation of components
        component_ids = []
        for component in components:
            if hasattr(component, 'id'):
                component_ids.append(component.id)
            elif hasattr(component, '__hash__'):
                component_ids.append(hash(component))
            else:
                component_ids.append(str(component))
                
        # Sort for consistency
        component_ids.sort()
        
        # Combine into a hash
        return f"{pattern_type}_{'.'.join(map(str, component_ids))}"
    
    def _check_pattern_relationship(self, pattern1: Pattern, pattern2: Pattern) -> bool:
        """
        Check if two patterns are related (shared components or interaction).
        
        Args:
            pattern1: First pattern
            pattern2: Second pattern
            
        Returns:
            bool: True if patterns are related
        """
        # Check for shared components
        components1 = set(self._get_component_ids(pattern1.components))
        components2 = set(self._get_component_ids(pattern2.components))
        
        # If there's significant overlap, they're related
        intersection = components1.intersection(components2)
        min_components = min(len(components1), len(components2))
        
        if min_components > 0 and len(intersection) / min_components >= 0.3:
            return True
            
        # Check for layer relationship (adjacent layers are more likely related)
        layer_sequence = ['chemical', 'replicative', 'autocatalytic', 'compartmental']
        
        if pattern1.layer in layer_sequence and pattern2.layer in layer_sequence:
            idx1 = layer_sequence.index(pattern1.layer)
            idx2 = layer_sequence.index(pattern2.layer)
            
            if abs(idx1 - idx2) == 1:
                # Adjacent layers with any overlap suggest relationship
                if intersection:
                    return True
        
        return False
    
    def _get_component_ids(self, components: List[Any]) -> List[str]:
        """
        Extract component IDs for comparison.
        
        Args:
            components: List of components
            
        Returns:
            list: Component IDs
        """
        component_ids = []
        for component in components:
            if hasattr(component, 'id'):
                component_ids.append(component.id)
            elif hasattr(component, '__hash__'):
                component_ids.append(str(hash(component)))
            else:
                component_ids.append(str(component))
                
        return component_ids
    
    def get_pattern_metrics(self) -> Dict[str, Any]:
        """
        Get metrics about patterns.
        
        Returns:
            dict: Pattern metrics
        """
        # Calculate average persistence and reusability
        persistence_values = [p.persistence for p in self.patterns.values()]
        reusability_values = [p.reusability for p in self.patterns.values()]
        
        avg_persistence = np.mean(persistence_values) if persistence_values else 0
        avg_reusability = np.mean(reusability_values) if reusability_values else 0
        
        # Count patterns by layer and type
        patterns_by_layer = {
            layer: len(pattern_ids) for layer, pattern_ids in self.patterns_by_layer.items()
        }
        
        patterns_by_type = {
            ptype: len(pattern_ids) for ptype, pattern_ids in self.patterns_by_type.items()
        }
        
        return {
            'total_patterns': len(self.patterns),
            'active_patterns': len(self.active_patterns),
            'avg_persistence': avg_persistence,
            'avg_reusability': avg_reusability,
            'patterns_by_layer': patterns_by_layer,
            'patterns_by_type': patterns_by_type
        }
    
    def find_high_reusability_patterns(self, threshold: float = 2.0) -> List[Pattern]:
        """
        Find patterns with high reusability.
        
        Args:
            threshold: Minimum reusability threshold
            
        Returns:
            list: High reusability patterns
        """
        return [p for p in self.patterns.values() if p.reusability >= threshold]
    
    def find_persistent_patterns(self, threshold: float = 10.0) -> List[Pattern]:
        """
        Find patterns with high persistence.
        
        Args:
            threshold: Minimum persistence threshold
            
        Returns:
            list: Persistent patterns
        """
        return [p for p in self.patterns.values() if p.persistence >= threshold]
    
    def get_active_patterns(self) -> List[Pattern]:
        """
        Get currently active patterns.
        
        Returns:
            list: Active patterns
        """
        return [self.patterns[pid] for pid in self.active_patterns if pid in self.patterns]
    
    def generate_pattern_network(self) -> nx.DiGraph:
        """
        Generate a network representation of pattern relationships.
        
        Returns:
            nx.DiGraph: NetworkX directed graph of patterns
        """
        G = nx.DiGraph()
        
        # Add pattern nodes
        for pattern_id, pattern in self.patterns.items():
            G.add_node(pattern_id, 
                      type=pattern.pattern_type, 
                      layer=pattern.layer,
                      persistence=pattern.persistence,
                      reusability=pattern.reusability)
        
        # Add relationship edges
        for pattern_id, related_ids in self.pattern_relationships.items():
            for related_id in related_ids:
                if pattern_id in self.patterns and related_id in self.patterns:
                    source_layer = self.patterns[pattern_id].layer
                    target_layer = self.patterns[related_id].layer
                    G.add_edge(pattern_id, related_id, 
                              source_layer=source_layer,
                              target_layer=target_layer)
        
        return G
    
    def get_layer_transition_patterns(self) -> Dict[str, List[Pattern]]:
        """
        Get patterns that bridge between layers.
        
        Returns:
            dict: Layer transition -> list of bridging patterns
        """
        layer_sequence = ['chemical', 'replicative', 'autocatalytic', 'compartmental']
        transitions = {}
        
        for i in range(len(layer_sequence) - 1):
            source = layer_sequence[i]
            target = layer_sequence[i + 1]
            transition_key = f"{source}_to_{target}"
            
            # Find patterns that reference patterns from the lower layer
            bridges = []
            for pattern_id in self.patterns_by_layer.get(target, []):
                pattern = self.patterns[pattern_id]
                
                for related_id in self.pattern_relationships.get(pattern_id, []):
                    if related_id in self.patterns:
                        related = self.patterns[related_id]
                        if related.layer == source:
                            bridges.append(pattern)
                            break
            
            transitions[transition_key] = bridges
            
        return transitions