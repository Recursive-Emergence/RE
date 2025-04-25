#!/usr/bin/env python3
"""
Entropy-Catalysis Feedback Loop Simulation

This module implements a simulation to test the key hypothesis from Appendix L:
A bidirectional feedback loop exists between entropy reduction and autocatalysis
in chemical systems, creating a self-reinforcing pathway toward higher-order organization.

The simulation tracks how initial entropy reduction enables catalysis, and how
catalytic structures then accelerate further entropy reduction.
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import networkx as nx
import random
import math

class MoleculeGraph:
    """Represents a molecule as a graph structure for binary polymer model."""
    def __init__(self, sequence=None, length=None):
        """Create a molecule with either a specific sequence or random of given length."""
        if sequence is not None:
            self.sequence = sequence
        elif length is not None:
            self.sequence = ''.join(random.choice('01') for _ in range(length))
        else:
            self.sequence = ''
        
    def __str__(self):
        return self.sequence
    
    def __len__(self):
        return len(self.sequence)
    
    def __hash__(self):
        return hash(self.sequence)
    
    def __eq__(self, other):
        if isinstance(other, MoleculeGraph):
            return self.sequence == other.sequence
        return False
    
    def can_catalyze(self, reaction):
        """Check if this molecule can catalyze a specific reaction.
        
        In the binary polymer model, a molecule can catalyze a reaction if
        it contains a specific pattern that matches characteristics of 
        the reactants or products.
        """
        # Simple implementation - a molecule catalyzes if it shares a subsequence
        # with either reactant or product
        min_match = 3  # Minimum subsequence match for catalysis
        
        for reactant in reaction.reactants:
            if len(self) >= min_match and len(reactant) >= min_match:
                if (self.sequence in reactant.sequence or 
                    reactant.sequence in self.sequence):
                    return True
                    
        for product in reaction.products:
            if len(self) >= min_match and len(product) >= min_match:
                if (self.sequence in product.sequence or 
                    product.sequence in self.sequence):
                    return True
        
        return False
    
    @property
    def complexity(self):
        """Return a measure of molecular complexity."""
        if not self.sequence:
            return 0
        
        # Simple complexity measure based on sequence length and pattern variety
        # More sophisticated measures could examine structure, bond types, etc.
        return len(self.sequence) * len(set(self.sequence))


class Reaction:
    """Represents a chemical reaction with reactants, products, and catalysis."""
    def __init__(self, reactants, products):
        self.reactants = reactants
        self.products = products
        self.catalysts = set()
        self.reaction_rate = 0.01  # Base reaction rate without catalysis
    
    def __str__(self):
        return " + ".join(str(r) for r in self.reactants) + " → " + " + ".join(str(p) for p in self.products)
    
    def add_catalyst(self, molecule):
        """Add a catalyst for this reaction."""
        self.catalysts.add(molecule)
    
    @property
    def is_catalyzed(self):
        """Check if the reaction has catalysts."""
        return len(self.catalysts) > 0
    
    @property
    def effective_rate(self):
        """Calculate the effective reaction rate with catalysis."""
        # Each catalyst increases the reaction rate by a factor
        catalyst_factor = 10.0
        
        if not self.catalysts:
            return self.reaction_rate
        
        # The more catalysts, the higher the rate, with diminishing returns
        return self.reaction_rate * (1 + catalyst_factor * math.log(1 + len(self.catalysts)))
    
    @property
    def entropy_reduction(self):
        """
        Calculate the entropy reduction achieved by this reaction.
        
        In this model, entropy reduction is related to:
        1. The increase in molecular complexity from reactants to products
        2. The specificity of the reaction (catalyzed reactions are more specific)
        """
        # Calculate complexity before and after
        reactant_complexity = sum(r.complexity for r in self.reactants)
        product_complexity = sum(p.complexity for p in self.products)
        
        # Base entropy change (negative if complexity increases)
        base_entropy_change = reactant_complexity - product_complexity
        
        # Catalyzed reactions achieve more ordered outcomes
        catalyst_factor = 1.5 if self.is_catalyzed else 1.0
        
        # Return entropy reduction (so negate if complexity increases)
        return -base_entropy_change * catalyst_factor


class ChemicalNetwork:
    """Represents a network of molecules and reactions."""
    def __init__(self, food_set=None):
        self.molecules = set()
        self.reactions = []
        self.reaction_network = nx.DiGraph()
        self.time_series_data = {
            'entropy_reduction': [],
            'catalytic_activity': [],
            'molecular_complexity': [],
            'memory_persistence': []
        }
        
        # Initialize with food molecules if provided
        if food_set:
            for molecule in food_set:
                self.molecules.add(molecule)
    
    def add_molecule(self, molecule):
        """Add a molecule to the chemical network."""
        self.molecules.add(molecule)
    
    def add_reaction(self, reaction):
        """Add a reaction to the chemical network."""
        self.reactions.append(reaction)
        
        # Update reaction network graph
        for reactant in reaction.reactants:
            for product in reaction.products:
                self.reaction_network.add_edge(reactant, product, reaction=reaction)
    
    def identify_catalysts(self):
        """Identify molecules that can catalyze reactions."""
        for molecule in self.molecules:
            for reaction in self.reactions:
                if molecule.can_catalyze(reaction):
                    reaction.add_catalyst(molecule)
    
    def update(self):
        """Perform one update step of the chemical network."""
        # Track new molecules created in this step
        new_molecules = set()
        
        # Execute reactions based on their rates
        for reaction in self.reactions:
            # Probability of reaction occurring is based on effective rate
            if random.random() < reaction.effective_rate:
                # Check if all reactants are available
                if all(reactant in self.molecules for reactant in reaction.reactants):
                    # Execute reaction - add products
                    for product in reaction.products:
                        new_molecules.add(product)
        
        # Add new molecules to the network
        self.molecules.update(new_molecules)
        
        # Identify new potential catalysts
        self.identify_catalysts()
        
        # Record metrics
        self._update_metrics()
        
        return len(new_molecules)  # Return number of new molecules created
    
    def _update_metrics(self):
        """Update time series metrics for analysis."""
        # Calculate total entropy reduction from all reactions
        total_entropy_reduction = sum(reaction.entropy_reduction for reaction in self.reactions 
                                    if any(reactant in self.molecules for reactant in reaction.reactants))
        
        # Calculate catalytic activity (proportion of reactions that are catalyzed)
        catalyzed_reactions = sum(1 for reaction in self.reactions if reaction.is_catalyzed)
        catalytic_activity = catalyzed_reactions / max(len(self.reactions), 1)
        
        # Calculate average molecular complexity
        avg_complexity = sum(mol.complexity for mol in self.molecules) / max(len(self.molecules), 1)
        
        # Calculate memory persistence (how long catalytic molecules persist)
        # For now, use a placeholder based on catalytic molecule count
        catalytic_molecules = set()
        for reaction in self.reactions:
            catalytic_molecules.update(reaction.catalysts)
        memory_persistence = len(catalytic_molecules) / max(len(self.molecules), 1)
        
        # Store metrics
        self.time_series_data['entropy_reduction'].append(total_entropy_reduction)
        self.time_series_data['catalytic_activity'].append(catalytic_activity)
        self.time_series_data['molecular_complexity'].append(avg_complexity)
        self.time_series_data['memory_persistence'].append(memory_persistence)
    
    def calculate_feedback_coefficient(self):
        """
        Calculate the entropy-catalysis feedback coefficient.
        
        This measures how strongly entropy reduction and catalytic activity are coupled.
        A value close to 1 indicates strong positive feedback between the two.
        """
        # Need at least a few data points for correlation
        if len(self.time_series_data['entropy_reduction']) < 3:
            return 0
            
        # Calculate correlation between entropy reduction and subsequent catalytic activity
        er = np.array(self.time_series_data['entropy_reduction'][:-1])  # All but last
        ca = np.array(self.time_series_data['catalytic_activity'][1:])  # All but first
        
        if len(er) == 0 or np.std(er) == 0 or np.std(ca) == 0:
            return 0
            
        correlation = np.corrcoef(er, ca)[0, 1]
        return correlation if not np.isnan(correlation) else 0
    
    def has_entered_runaway_phase(self):
        """
        Detect if the system has entered a runaway complexity phase.
        
        Returns True if we detect a significant acceleration in both
        entropy reduction and catalytic activity.
        """
        # Need enough history to detect a trend
        if len(self.time_series_data['entropy_reduction']) < 10:
            return False
            
        # Look at trends in the last portion of the simulation
        window = 10
        er_trend = self.time_series_data['entropy_reduction'][-window:]
        ca_trend = self.time_series_data['catalytic_activity'][-window:]
        
        # Check if both metrics are increasing consistently
        er_increases = sum(1 for i in range(1, len(er_trend)) if er_trend[i] > er_trend[i-1])
        ca_increases = sum(1 for i in range(1, len(ca_trend)) if ca_trend[i] > ca_trend[i-1])
        
        # If both metrics are increasing in at least 70% of time steps, consider it runaway
        threshold = 0.7
        return er_increases >= threshold * (window-1) and ca_increases >= threshold * (window-1)
    
    def visualize_metrics(self, output_file=None):
        """Visualize the time series metrics."""
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        
        # Plot entropy reduction
        axes[0, 0].plot(self.time_series_data['entropy_reduction'])
        axes[0, 0].set_title('Entropy Reduction Over Time')
        axes[0, 0].set_xlabel('Time Step')
        axes[0, 0].set_ylabel('Entropy Reduction')
        
        # Plot catalytic activity
        axes[0, 1].plot(self.time_series_data['catalytic_activity'])
        axes[0, 1].set_title('Catalytic Activity Over Time')
        axes[0, 1].set_xlabel('Time Step')
        axes[0, 1].set_ylabel('Proportion of Catalyzed Reactions')
        
        # Plot molecular complexity
        axes[1, 0].plot(self.time_series_data['molecular_complexity'])
        axes[1, 0].set_title('Average Molecular Complexity')
        axes[1, 0].set_xlabel('Time Step')
        axes[1, 0].set_ylabel('Complexity')
        
        # Plot memory persistence
        axes[1, 1].plot(self.time_series_data['memory_persistence'])
        axes[1, 1].set_title('Catalytic Memory Persistence')
        axes[1, 1].set_xlabel('Time Step')
        axes[1, 1].set_ylabel('Persistence Ratio')
        
        plt.tight_layout()
        
        # Save if output file specified, otherwise show
        if output_file:
            plt.savefig(output_file)
        else:
            plt.show()
    
    def visualize_reaction_network(self, output_file=None):
        """Visualize the reaction network as a graph."""
        plt.figure(figsize=(12, 10))
        
        # Create a more visually meaningful network
        G = nx.DiGraph()
        
        # Add nodes for molecules
        for molecule in self.molecules:
            # Determine if molecule is catalytic
            is_catalytic = any(molecule in reaction.catalysts for reaction in self.reactions)
            G.add_node(str(molecule), 
                      size=10 + molecule.complexity * 2,
                      color='red' if is_catalytic else 'blue')
        
        # Add edges for reactions
        for reaction in self.reactions:
            for reactant in reaction.reactants:
                for product in reaction.products:
                    if reactant in self.molecules and product in self.molecules:
                        G.add_edge(str(reactant), str(product), 
                                  weight=reaction.effective_rate * 5,
                                  color='green' if reaction.is_catalyzed else 'gray')
        
        # Extract node attributes for visualization
        node_sizes = [G.nodes[node]['size'] for node in G.nodes]
        node_colors = [G.nodes[node]['color'] for node in G.nodes]
        
        # Extract edge attributes for visualization
        edge_weights = [G.edges[edge]['weight'] for edge in G.edges]
        edge_colors = [G.edges[edge]['color'] for edge in G.edges]
        
        # Position nodes using force-directed layout
        pos = nx.spring_layout(G)
        
        # Draw the graph
        nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.8)
        nx.draw_networkx_edges(G, pos, width=edge_weights, edge_color=edge_colors, alpha=0.5)
        nx.draw_networkx_labels(G, pos, font_size=8, font_color='black')
        
        plt.title('Reaction Network')
        plt.axis('off')
        
        # Save if output file specified, otherwise show
        if output_file:
            plt.savefig(output_file)
        else:
            plt.show()


def generate_initial_food_set(count=5, max_length=3):
    """Generate an initial set of simple 'food' molecules."""
    return [MoleculeGraph(length=random.randint(1, max_length)) for _ in range(count)]


def generate_potential_reactions(molecules, max_reactions=100):
    """Generate potential reactions from available molecules."""
    reactions = []
    
    # For simplicity, consider ligation (joining) reactions
    molecule_list = list(molecules)
    
    # Select a subset of possible reactions to keep simulation manageable
    reaction_count = min(max_reactions, len(molecule_list) * (len(molecule_list) - 1) // 2)
    
    for _ in range(reaction_count):
        # Randomly select reactants
        if len(molecule_list) >= 2:
            reactant1, reactant2 = random.sample(molecule_list, 2)
            
            # Create product (simple concatenation for binary polymer model)
            product = MoleculeGraph(reactant1.sequence + reactant2.sequence)
            
            # Create the reaction
            reactions.append(Reaction([reactant1, reactant2], [product]))
    
    return reactions


def run_simulation(steps=100, initial_food_molecules=5, max_reactions_per_step=10):
    """Run the full simulation and analyze results."""
    # Create initial food set
    food_set = generate_initial_food_set(initial_food_molecules)
    
    # Create chemical network
    network = ChemicalNetwork(food_set)
    
    # Initial reactions
    initial_reactions = generate_potential_reactions(network.molecules, max_reactions_per_step)
    for reaction in initial_reactions:
        network.add_reaction(reaction)
    
    # Initial catalyst identification
    network.identify_catalysts()
    
    # For tracking phase transition
    runaway_detected_step = None
    
    # Run simulation steps
    for step in range(steps):
        # Update the network
        new_molecules = network.update()
        
        # Add new potential reactions periodically
        if step % 5 == 0 or new_molecules > 0:
            new_reactions = generate_potential_reactions(network.molecules, max_reactions_per_step)
            for reaction in new_reactions:
                network.add_reaction(reaction)
        
        # Check for runaway phase
        if runaway_detected_step is None and network.has_entered_runaway_phase():
            runaway_detected_step = step
            print(f"Runaway complexity phase detected at step {step}!")
    
    # Calculate the feedback coefficient
    feedback_coef = network.calculate_feedback_coefficient()
    print(f"Entropy-Catalysis Feedback Coefficient: {feedback_coef:.4f}")
    
    # Report phase transition if detected
    if runaway_detected_step is not None:
        print(f"System entered self-reinforcing phase at step {runaway_detected_step}/{steps}")
    else:
        print("No clear self-reinforcing phase detected in this run")
    
    # Final metrics
    final_catalytic = network.time_series_data['catalytic_activity'][-1]
    final_complexity = network.time_series_data['molecular_complexity'][-1]
    print(f"Final catalytic activity: {final_catalytic:.4f}")
    print(f"Final average molecular complexity: {final_complexity:.4f}")
    
    # Visualize results
    network.visualize_metrics("entropy_catalysis_metrics.png")
    network.visualize_reaction_network("reaction_network.png")
    
    return network


# Run simulations with different levels of initial constraint to test our hypothesis
def test_entropy_constraint_hypothesis():
    """
    Test how different initial entropy constraints affect the emergence of catalysis
    and subsequent runaway complexity.
    """
    # Create results storage
    results = {
        'initial_constraint': [],
        'feedback_coef': [],
        'runaway_detected': [],
        'final_complexity': [],
        'final_catalytic': []
    }
    
    # Test different constraint levels
    for constraint_level in range(1, 6):
        print(f"\nRunning simulation with constraint level {constraint_level}...")
        
        # Higher constraint = smaller, more ordered initial food set
        food_molecules = 10 - constraint_level  # Fewer initial molecules = higher constraint
        max_length = constraint_level  # Longer initial molecules = higher initial order
        
        # Food set with appropriate constraint
        food_set = [MoleculeGraph(length=max_length) for _ in range(food_molecules)]
        
        # Create network
        network = ChemicalNetwork(food_set)
        
        # Add limited initial reactions based on constraint
        initial_reactions = generate_potential_reactions(network.molecules, 5 * constraint_level)
        for reaction in initial_reactions:
            network.add_reaction(reaction)
        
        # Run simulation
        steps = 100
        runaway_detected = None
        
        for step in range(steps):
            network.update()
            
            # Add new reactions periodically
            if step % 5 == 0:
                new_reactions = generate_potential_reactions(network.molecules, 10)
                for reaction in new_reactions:
                    network.add_reaction(reaction)
            
            # Check for runaway phase
            if runaway_detected is None and network.has_entered_runaway_phase():
                runaway_detected = step
        
        # Record results
        feedback_coef = network.calculate_feedback_coefficient()
        final_catalytic = network.time_series_data['catalytic_activity'][-1]
        final_complexity = network.time_series_data['molecular_complexity'][-1]
        
        results['initial_constraint'].append(constraint_level)
        results['feedback_coef'].append(feedback_coef)
        results['runaway_detected'].append(runaway_detected)
        results['final_complexity'].append(final_complexity)
        results['final_catalytic'].append(final_catalytic)
        
        print(f"Constraint {constraint_level}: Feedback={feedback_coef:.4f}, " +
              f"Runaway={runaway_detected}, Complexity={final_complexity:.4f}")
    
    # Visualize comparison
    plt.figure(figsize=(12, 10))
    
    # Plot feedback coefficient vs constraint
    plt.subplot(2, 2, 1)
    plt.plot(results['initial_constraint'], results['feedback_coef'], 'o-')
    plt.title('Feedback Coefficient vs Initial Constraint')
    plt.xlabel('Initial Constraint Level')
    plt.ylabel('Entropy-Catalysis Feedback')
    
    # Plot runaway detection vs constraint
    plt.subplot(2, 2, 2)
    runaway_steps = [x if x is not None else float('nan') for x in results['runaway_detected']]
    plt.plot(results['initial_constraint'], runaway_steps, 'o-')
    plt.title('Runaway Detection Step vs Initial Constraint')
    plt.xlabel('Initial Constraint Level')
    plt.ylabel('Step at Runaway Detection')
    
    # Plot final complexity vs constraint
    plt.subplot(2, 2, 3)
    plt.plot(results['initial_constraint'], results['final_complexity'], 'o-')
    plt.title('Final Molecular Complexity vs Initial Constraint')
    plt.xlabel('Initial Constraint Level')
    plt.ylabel('Final Average Molecular Complexity')
    
    # Plot final catalytic activity vs constraint
    plt.subplot(2, 2, 4)
    plt.plot(results['initial_constraint'], results['final_catalytic'], 'o-')
    plt.title('Final Catalytic Activity vs Initial Constraint')
    plt.xlabel('Initial Constraint Level')
    plt.ylabel('Final Catalytic Activity')
    
    plt.tight_layout()
    plt.savefig("constraint_hypothesis_results.png")
    plt.show()
    
    return results


if __name__ == "__main__":
    # Run a standard simulation
    print("Running standard simulation...")
    network = run_simulation(steps=100)
    
    # Test the entropy constraint hypothesis
    print("\nTesting entropy constraint hypothesis...")
    results = test_entropy_constraint_hypothesis()
    
    print("\nSimulation complete! Results saved as PNG files.")