"""
Negentropy Metrics for Recursive Emergence

This module implements metrics for measuring negentropy (order) in chemical systems
across different organizational layers, supporting the recursive emergence theory.
"""

import numpy as np
import networkx as nx
from collections import defaultdict
from typing import Dict, List, Any, Optional, Tuple

class NegentropyCalculator:
    """
    Calculate negentropy metrics to validate Recursive Emergence theory in chemical simulations.
    
    Negentropy refers to the "negative entropy" or order/organization in a system.
    This class provides methods to quantify how much structural order exists and
    how it transfers between different organizational layers.
    """
    
    def __init__(self):
        """Initialize the negentropy calculator"""
        self.layers = {}
        self.history = defaultdict(list)
        self.baseline_entropy = None
        self.current_layer = 'chemical'
        
        # Define layer sequence for the origins of life context
        self.layer_sequence = ['chemical', 'replicative', 'autocatalytic', 'compartmental']
        
    def set_baseline_entropy(self, entropy: float) -> None:
        """
        Set the baseline entropy for normalization.
        
        Args:
            entropy: Baseline entropy value from a random/disordered system
        """
        self.baseline_entropy = entropy

    def calculate_chemical_negentropy(self, network) -> float:
        """
        Calculate negentropy in a chemical network.
        
        This quantifies how far the chemical system has moved from randomness.
        It measures structured patterns in the molecular distribution and reaction network.
        
        Args:
            network: ChemicalNetwork instance from the simulation
            
        Returns:
            float: Chemical layer negentropy value (0-1 scale)
        """
        if not hasattr(network, 'molecules') or not network.molecules:
            return 0.0
            
        # 1. Molecular Distribution Negentropy
        
        # Get molecule types and counts
        molecule_counts = {}
        for molecule, count in network.molecules.items():
            # Skip zero-count molecules
            if count <= 0:
                continue
                
            # Group by complexity level to simplify distribution
            complexity_level = int(molecule.complexity)
            if complexity_level not in molecule_counts:
                molecule_counts[complexity_level] = 0
            molecule_counts[complexity_level] += count
                
        # Calculate Shannon entropy of molecular distribution
        total_molecules = sum(molecule_counts.values())
        if total_molecules == 0:
            return 0.0
            
        distribution = [count / total_molecules for count in molecule_counts.values()]
        shannon_entropy = -sum(p * np.log2(p) for p in distribution if p > 0)
        
        # Convert to negentropy - more ordered distributions have lower Shannon entropy
        # Normalize to 0-1 scale (1 means max order)
        # Use empirically determined max entropy for normalization
        max_entropy = 4.5  # Typical max entropy for complex chemical distributions
        molecular_negentropy = max(0.0, 1.0 - (shannon_entropy / max_entropy))
        
        # 2. Network Structure Negentropy
        
        # Create network graph 
        reaction_graph = nx.DiGraph()
        
        # Add molecules as nodes
        for molecule in network.molecules:
            if network.molecules[molecule] > 0:
                reaction_graph.add_node(molecule.name, 
                                       complexity=molecule.complexity,
                                       count=network.molecules[molecule])
        
        # Add reactions as edges
        for reaction in network.active_reactions:
            # Connect reactants to products
            for reactant in reaction.reactants:
                for product in reaction.products:
                    reaction_graph.add_edge(reactant.name, product.name)
        
        # Calculate network metrics related to order
        network_negentropy = 0.0
        if reaction_graph.number_of_nodes() > 1:
            # Measure of edge density 
            edge_density = len(reaction_graph.edges) / max(1, len(reaction_graph.nodes) * (len(reaction_graph.nodes) - 1))
            
            # Clustering coefficient - local structure/order
            try:
                clustering = nx.average_clustering(reaction_graph.to_undirected())
            except:
                clustering = 0
                
            # Connected components - structural organization
            components = nx.number_strongly_connected_components(reaction_graph)
            normalized_components = 1.0 / max(1, np.log2(1 + components))  # Fewer large components = more order
            
            # Combine network metrics
            network_negentropy = 0.5 * clustering + 0.3 * edge_density + 0.2 * normalized_components
            
        # 3. Molecular Complexity Contribution
        
        # Higher average complexity suggests more order
        avg_complexity = np.mean([mol.complexity for mol in network.molecules if network.molecules[mol] > 0])
        max_expected_complexity = 10.0  # Based on typical complexity values
        complexity_negentropy = min(1.0, avg_complexity / max_expected_complexity)
        
        # 4. Catalytic Contribution
        
        # Count catalysts
        catalyst_count = 0
        for mol in network.molecules:
            if network.molecules[mol] > 0 and hasattr(mol, 'is_catalyst') and mol.is_catalyst:
                catalyst_count += 1
                
        # Calculate catalyst ratio
        if total_molecules > 0:
            catalyst_ratio = catalyst_count / len(network.molecules)
            catalyst_negentropy = min(1.0, catalyst_ratio * 5.0)  # Scale for importance 
        else:
            catalyst_negentropy = 0.0
            
        # Combine all components with weights reflecting their importance in order creation
        overall_negentropy = (
            0.3 * molecular_negentropy + 
            0.3 * network_negentropy + 
            0.2 * complexity_negentropy + 
            0.2 * catalyst_negentropy
        )
        
        # Store result in history
        self.history['chemical_negentropy'].append(overall_negentropy)
        
        return overall_negentropy
        
    def calculate_replicative_negentropy(self, network) -> float:
        """
        Calculate negentropy from replicative processes.
        
        This measures how much the system has developed standardized replication patterns,
        which represent a higher form of order and memory persistence.
        
        Args:
            network: ChemicalNetwork instance
            
        Returns:
            float: Replicative layer negentropy value (0-1 scale)
        """
        # This requires replication tracking in the simulation
        # If not available, we use proxy metrics:
        
        # 1. Autocatalytic reactions - a precursor to replication
        autocatalytic_count = 0
        for reaction in network.active_reactions:
            if hasattr(reaction, 'is_autocatalytic') and reaction.is_autocatalytic:
                autocatalytic_count += 1
        
        # Normalize the autocatalytic count
        max_expected_autocatalytic = 20.0
        autocatalytic_negentropy = min(1.0, autocatalytic_count / max_expected_autocatalytic)
        
        # 2. Information-carrying molecules (e.g., RNA-like)
        info_molecule_count = 0
        for mol in network.molecules:
            # Skip zero-count molecules
            if network.molecules[mol] <= 0:
                continue
                
            # Look for RNA-like molecules (high complexity, can be templates)
            if mol.complexity > 5 and hasattr(mol, 'is_template') and mol.is_template:
                info_molecule_count += 1
        
        # Normalize the information molecule count
        max_expected_info_molecules = 10.0
        info_molecule_negentropy = min(1.0, info_molecule_count / max_expected_info_molecules)
        
        # 3. Template-based reactions (key for replication)
        template_reactions = 0
        for reaction in network.active_reactions:
            if hasattr(reaction, 'is_template_based') and reaction.is_template_based:
                template_reactions += 1
        
        # Normalize template reactions
        max_expected_template_reactions = 15.0
        template_negentropy = min(1.0, template_reactions / max_expected_template_reactions)
        
        # Combine with weights based on importance to replication
        replicative_negentropy = (
            0.3 * autocatalytic_negentropy + 
            0.4 * info_molecule_negentropy + 
            0.3 * template_negentropy
        )
        
        # Store in history
        self.history['replicative_negentropy'].append(replicative_negentropy)
        
        return replicative_negentropy
    
    def calculate_autocatalytic_negentropy(self, network) -> float:
        """
        Calculate negentropy from autocatalytic feedback networks.
        
        This measures how much the system has developed self-reinforcing catalytic
        cycles, which represent organized feedback loops.
        
        Args:
            network: ChemicalNetwork instance
            
        Returns:
            float: Autocatalytic layer negentropy value (0-1 scale)  
        """
        # 1. Count autocatalytic cycles
        cycle_count = getattr(network, 'autocatalytic_cycles', 0)
        if hasattr(network, 'get_final_analysis'):
            analysis = network.get_final_analysis()
            cycle_count = analysis.get('autocatalytic_cycles', cycle_count)
        
        # Normalize cycle count
        max_expected_cycles = 10.0
        cycle_negentropy = min(1.0, cycle_count / max_expected_cycles)
        
        # 2. Mutual catalysis networks (catalyst A helps create catalyst B and vice versa)
        mutual_catalysis = 0
        if hasattr(network, 'reaction_network'):
            G = network.reaction_network
            
            # Look for mutual catalytic relationships
            catalysts = [mol for mol in network.molecules 
                        if network.molecules[mol] > 0 and hasattr(mol, 'is_catalyst') and mol.is_catalyst]
                        
            for i, cat1 in enumerate(catalysts):
                for cat2 in catalysts[i+1:]:
                    # Check if cat1 helps produce cat2
                    cat1_helps_cat2 = False
                    cat2_helps_cat1 = False
                    
                    # Check each reaction
                    for reaction in network.active_reactions:
                        if cat1 in reaction.catalysts and cat2 in reaction.products:
                            cat1_helps_cat2 = True
                        if cat2 in reaction.catalysts and cat1 in reaction.products:
                            cat2_helps_cat1 = True
                    
                    # If mutual catalysis is present
                    if cat1_helps_cat2 and cat2_helps_cat1:
                        mutual_catalysis += 1
        
        # Normalize mutual catalysis
        max_expected_mutual = 5.0
        mutual_negentropy = min(1.0, mutual_catalysis / max_expected_mutual)
        
        # 3. Feedback coefficient from existing analysis
        feedback_coef = 0
        if hasattr(network, 'get_final_analysis'):
            analysis = network.get_final_analysis()
            feedback_coef = analysis.get('entropy_catalysis_feedback', 0)
        
        # Normalize feedback coefficient (typically 0-1 already)
        feedback_negentropy = min(1.0, feedback_coef)
        
        # Combine with weights
        autocatalytic_negentropy = (
            0.4 * cycle_negentropy + 
            0.3 * mutual_negentropy + 
            0.3 * feedback_negentropy
        )
        
        # Store in history
        self.history['autocatalytic_negentropy'].append(autocatalytic_negentropy)
        
        return autocatalytic_negentropy
    
    def calculate_compartmental_negentropy(self, network) -> float:
        """
        Calculate negentropy from compartmentalization.
        
        This measures how much the system has developed spatial organization
        through membrane-like structures.
        
        Args:
            network: ChemicalNetwork instance
            
        Returns:
            float: Compartmental layer negentropy value (0-1 scale)
        """
        # 1. Count compartments if available
        compartment_count = 0
        if hasattr(network, 'compartments'):
            compartment_count = len(network.compartments)
            
        # Use compartment probability if direct count isn't available
        compartment_prob = 0
        if hasattr(network, 'get_compartment_probability'):
            compartment_prob = network.get_compartment_probability()
        elif hasattr(network, 'get_final_analysis'):
            analysis = network.get_final_analysis()
            compartment_prob = analysis.get('compartment_probability', {}).get('p_compartment', 0)
        
        # Take the higher of actual or probabilistic
        normalized_compartments = max(
            min(1.0, compartment_count / 5.0),  # Max expected 5 compartments
            min(1.0, compartment_prob)  # Probability already 0-1
        )
        
        # 2. Amphiphilic molecules - needed for compartment formation
        amphiphilic_count = 0
        for mol in network.molecules:
            if network.molecules[mol] > 0 and hasattr(mol, 'is_amphiphilic') and mol.is_amphiphilic:
                amphiphilic_count += 1
                
        # Normalize amphiphilic count
        max_expected_amphiphilic = 10.0
        amphiphilic_negentropy = min(1.0, amphiphilic_count / max_expected_amphiphilic)
        
        # 3. Spatial organization metrics
        spatial_organization = 0
        
        # If molecules have positions, we can measure spatial clustering
        position_count = 0
        cluster_count = 0
        
        for mol in network.molecules:
            if network.molecules[mol] > 0 and hasattr(mol, 'position') and mol.position is not None:
                position_count += 1
                
                # Simplified cluster detection via position
                if hasattr(mol, 'is_in_cluster') and mol.is_in_cluster:
                    cluster_count += 1
                    
        if position_count > 0:
            spatial_organization = min(1.0, cluster_count / position_count)
        
        # Combine metrics with weights
        compartmental_negentropy = (
            0.5 * normalized_compartments + 
            0.3 * amphiphilic_negentropy + 
            0.2 * spatial_organization
        )
        
        # Store in history
        self.history['compartmental_negentropy'].append(compartmental_negentropy)
        
        return compartmental_negentropy
    
    def calculate_all_layer_negentropies(self, network) -> Dict[str, float]:
        """
        Calculate negentropy across all layers.
        
        Args:
            network: ChemicalNetwork instance
            
        Returns:
            dict: Negentropy values for each layer
        """
        negentropies = {
            'chemical': self.calculate_chemical_negentropy(network),
            'replicative': self.calculate_replicative_negentropy(network),
            'autocatalytic': self.calculate_autocatalytic_negentropy(network),
            'compartmental': self.calculate_compartmental_negentropy(network)
        }
        
        return negentropies
    
    def calculate_interlayer_negentropy_transfer(
            self, 
            network,
            source_layer: str, 
            target_layer: str
        ) -> float:
        """
        Calculate negentropy transfer between layers.
        
        This is a key metric for the recursive emergence theory, measuring how
        much order from one layer enables and amplifies order in the next layer.
        
        Args:
            network: ChemicalNetwork instance
            source_layer: Name of the source layer
            target_layer: Name of the target layer
            
        Returns:
            float: Negentropy transfer coefficient (0-1)
        """
        # Get layer negentropies
        negentropies = self.calculate_all_layer_negentropies(network)
        
        if source_layer not in negentropies or target_layer not in negentropies:
            return 0.0
            
        source_negentropy = negentropies[source_layer]
        target_negentropy = negentropies[target_layer]
        
        # If source has no negentropy, can't transfer anything
        if source_negentropy <= 0:
            return 0.0
            
        # Transfer is a function of both source and target negentropies
        # Higher target with high source indicates successful transfer
        transfer = (target_negentropy * source_negentropy) ** 0.5
        
        # Store in history with unique key for each layer pair
        history_key = f"transfer_{source_layer}_to_{target_layer}"
        self.history[history_key].append(transfer)
        
        return transfer
    
    def calculate_layer_complexity_compression(
            self, 
            network, 
            source_layer: str, 
            target_layer: str
        ) -> float:
        """
        Calculate complexity compression between layers.
        
        This measures how information gets compactly encoded in higher layers,
        indicating efficient pattern reuse.
        
        Args:
            network: ChemicalNetwork instance
            source_layer: Name of the source layer
            target_layer: Name of the target layer
            
        Returns:
            float: Complexity compression ratio (higher means more compression)
        """
        # First, we need proxies for complexity at each layer
        
        # Chemical complexity - sum of molecular complexity scores
        chemical_complexity = sum(mol.complexity * count 
                               for mol, count in network.molecules.items() if count > 0)
        
        # Replicative complexity - weighted by template complexity
        replicative_complexity = 0
        for mol in network.molecules:
            if network.molecules[mol] > 0 and hasattr(mol, 'is_template') and mol.is_template:
                replicative_complexity += mol.complexity * 2  # Templates are worth double
                
        # Autocatalytic complexity - based on cycle count and feedback
        autocatalytic_complexity = 0
        cycle_count = getattr(network, 'autocatalytic_cycles', 0)
        if hasattr(network, 'get_final_analysis'):
            analysis = network.get_final_analysis()
            cycle_count = analysis.get('autocatalytic_cycles', cycle_count)
        
        # Each cycle represents significant complexity
        autocatalytic_complexity = cycle_count * 5
        
        # Add mutual catalysis complexity
        for reaction in network.active_reactions:
            if hasattr(reaction, 'catalysts') and reaction.catalysts:
                for product in reaction.products:
                    if product in reaction.catalysts:
                        # Self-catalysis is important
                        autocatalytic_complexity += 2
        
        # Compartmental complexity - based on compartment structure
        compartmental_complexity = 0
        if hasattr(network, 'compartments'):
            for compartment in network.compartments:
                # Base complexity for the compartment itself
                compartment_complexity = 5
                
                # Add complexity for molecules inside
                if hasattr(compartment, 'molecules'):
                    inner_count = sum(compartment.molecules.values())
                    compartment_complexity += inner_count * 0.5
                    
                compartmental_complexity += compartment_complexity
        
        # Map layer names to complexity values
        layer_complexity = {
            'chemical': chemical_complexity,
            'replicative': replicative_complexity,
            'autocatalytic': autocatalytic_complexity,
            'compartmental': compartmental_complexity
        }
        
        # Calculate compression ratio
        if source_layer not in layer_complexity or target_layer not in layer_complexity:
            return 0.0
            
        source_complexity = max(1.0, layer_complexity[source_layer])
        target_complexity = max(1.0, layer_complexity[target_layer])
        
        # Compression ratio: how much emergent complexity in target per unit of source complexity
        compression_ratio = target_complexity / source_complexity
        
        # Store in history
        history_key = f"compression_{source_layer}_to_{target_layer}"
        self.history[history_key].append(compression_ratio)
        
        return compression_ratio
    
    def calculate_emergence_potential(self, network) -> Dict[str, float]:
        """
        Calculate emergence potential for each layer in the hierarchy.
        
        This implements the core equation from the Recursive Emergence theory:
        P(E) = R(E) · (H(St) - H(St+1))
        
        Args:
            network: ChemicalNetwork instance
            
        Returns:
            dict: Emergence potential for each layer 
        """
        # Get negentropies for each layer
        negentropies = self.calculate_all_layer_negentropies(network)
        
        # Calculate reusability (R) for each layer
        reusabilities = self._calculate_layer_reusabilities(network)
        
        # For each layer, calculate emergence potential
        potentials = {}
        for i, layer in enumerate(self.layer_sequence[:-1]):  # Skip last layer
            next_layer = self.layer_sequence[i+1]
            
            # Get entropy reduction between layers
            # (we use negentropy directly, which is already a measure of reduction)
            source_negentropy = negentropies[layer]
            target_negentropy = negentropies[next_layer]
            
            # Entropy reduction = additional negentropy in target
            entropy_reduction = max(0, target_negentropy - source_negentropy)
            
            # Apply the formula P(E) = R(E) · (H(St) - H(St+1))
            potentials[layer] = reusabilities[layer] * entropy_reduction
            
        # Add the last layer with potential based on its own negentropy
        last_layer = self.layer_sequence[-1]
        potentials[last_layer] = reusabilities[last_layer] * negentropies[last_layer]
        
        return potentials
    
    def _calculate_layer_reusabilities(self, network) -> Dict[str, float]:
        """
        Calculate reusability scores for each layer.
        
        R(E) = U(E) / C(E)
        
        Where:
        - U(E) is usefulness/utility
        - C(E) is maintenance cost
        
        Args:
            network: ChemicalNetwork instance
            
        Returns:
            dict: Reusability score for each layer
        """
        reusabilities = {}
        
        # 1. Chemical Layer Reusability
        # Usefulness = contribution to reactions
        chemical_utility = 0
        total_molecules = sum(count for mol, count in network.molecules.items() if count > 0)
        reaction_count = len(network.active_reactions)
        
        if total_molecules > 0:
            chemical_utility = reaction_count / total_molecules
            
        # Cost = energy expenditure
        chemical_cost = 1.0  # Base cost
        if hasattr(network, 'get_statistics'):
            stats = network.get_statistics()
            energy = stats.get('energy_currency', 0)
            if energy > 0:
                chemical_cost = 1.0 / energy  # Higher energy = lower cost
                
        # Calculate reusability
        reusabilities['chemical'] = chemical_utility / max(0.1, chemical_cost)
        
        # 2. Replicative Layer Reusability
        # Usefulness = contribution to replication
        template_count = 0
        for mol in network.molecules:
            if (network.molecules[mol] > 0 and 
                hasattr(mol, 'is_template') and mol.is_template):
                template_count += 1
                
        replicative_utility = template_count * 2.0  # Templates are highly useful
        
        # Cost = complexity of maintaining templates
        replicative_cost = 1.0
        if template_count > 0:
            avg_template_complexity = 0
            count = 0
            for mol in network.molecules:
                if (network.molecules[mol] > 0 and 
                    hasattr(mol, 'is_template') and mol.is_template):
                    avg_template_complexity += mol.complexity
                    count += 1
            
            if count > 0:
                avg_template_complexity /= count
                replicative_cost = avg_template_complexity
                
        # Calculate reusability
        reusabilities['replicative'] = replicative_utility / max(0.1, replicative_cost)
        
        # 3. Autocatalytic Layer Reusability
        # Usefulness = cycle efficiency
        cycle_count = getattr(network, 'autocatalytic_cycles', 0)
        catalyst_count = sum(1 for mol in network.molecules
                          if network.molecules[mol] > 0 
                          and hasattr(mol, 'is_catalyst') and mol.is_catalyst)
        
        autocatalytic_utility = cycle_count * 3.0 + catalyst_count
        
        # Cost = maintaining catalysts
        autocatalytic_cost = 1.0
        if catalyst_count > 0:
            autocatalytic_cost = catalyst_count  # More catalysts = higher cost
            
        # Calculate reusability
        reusabilities['autocatalytic'] = autocatalytic_utility / max(0.1, autocatalytic_cost)
        
        # 4. Compartmental Layer Reusability
        # Usefulness = compartment stability and protection
        compartment_count = 0
        if hasattr(network, 'compartments'):
            compartment_count = len(network.compartments)
            
        # Higher compartment count = higher utility, with diminishing returns
        compartmental_utility = min(10.0, compartment_count * 2.0)
        
        # Cost = maintaining compartments
        compartmental_cost = 1.0
        if compartment_count > 0:
            compartmental_cost = compartment_count  # Each compartment has a cost
            
        # Calculate reusability
        reusabilities['compartmental'] = compartmental_utility / max(0.1, compartmental_cost)
        
        return reusabilities
    
    def get_persistence_scores(self, network) -> Dict[str, float]:
        """
        Calculate persistence scores for each layer.
        
        Φ(E) = R(E)/Δt
        
        Args:
            network: ChemicalNetwork instance
            
        Returns:
            dict: Persistence score for each layer
        """
        # Get reusability scores
        reusabilities = self._calculate_layer_reusabilities(network)
        
        # Assume a standard time window (could be simulation step-dependent)
        time_window = 10.0
        
        # Calculate persistence scores
        persistence_scores = {
            layer: reusability / time_window
            for layer, reusability in reusabilities.items()
        }
        
        return persistence_scores
    
    def get_all_negentropy_metrics(self, network) -> Dict[str, Any]:
        """
        Get a comprehensive set of negentropy metrics for the current state.
        
        Args:
            network: ChemicalNetwork instance
            
        Returns:
            dict: All negentropy metrics
        """
        # Calculate all metrics
        negentropies = self.calculate_all_layer_negentropies(network)
        persistence_scores = self.get_persistence_scores(network)
        emergence_potentials = self.calculate_emergence_potential(network)
        
        # Calculate layer transitions
        transitions = {}
        for i, src_layer in enumerate(self.layer_sequence[:-1]):
            target_layer = self.layer_sequence[i+1]
            
            transitions[f"{src_layer}_to_{target_layer}"] = {
                'negentropy_transfer': self.calculate_interlayer_negentropy_transfer(
                    network, src_layer, target_layer),
                'complexity_compression': self.calculate_layer_complexity_compression(
                    network, src_layer, target_layer)
            }
            
        # Determine current dominant layer
        dominant_layer = max(
            emergence_potentials.items(),
            key=lambda x: x[1]
        )[0]
        
        # Combine all metrics
        return {
            'negentropy_by_layer': negentropies,
            'persistence_scores': persistence_scores,
            'emergence_potentials': emergence_potentials,
            'layer_transitions': transitions,
            'dominant_layer': dominant_layer
        }
        
    def generate_layer_trajectory(self) -> List[str]:
        """
        Generate a trajectory of layer dominance across the simulation history.
        
        Returns:
            list: Sequence of dominant layers throughout the simulation
        """
        # This requires history from multiple simulation steps
        if not any(self.history.values()):
            return []
            
        # Get layer indexes for easy comparison
        layer_indexes = {layer: i for i, layer in enumerate(self.layer_sequence)}
        
        # Determine dominant layer at each step
        trajectory = []
        num_steps = len(next(iter(self.history.values())))
        
        for step in range(num_steps):
            # Get negentropy values for each layer at this step
            step_values = {}
            for layer in self.layer_sequence:
                key = f"{layer}_negentropy"
                if key in self.history and step < len(self.history[key]):
                    step_values[layer] = self.history[key][step]
                else:
                    step_values[layer] = 0
            
            # Find dominant layer (highest negentropy)
            dominant_layer = max(step_values.items(), key=lambda x: x[1])[0]
            trajectory.append(dominant_layer)
            
        return trajectory