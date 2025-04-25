#!/usr/bin/env python3
"""
Enhanced Recursive Emergence Simulation with advanced threshold detection.

This simulation models chemical evolution with a focus on detecting and analyzing
emergence thresholds that would normally require millions of years in nature.
"""

import os
import sys
import json
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from datetime import datetime
from collections import defaultdict

# Import our custom modules
from realistic_chemistry import RealisticChemistry
from src.emergence_threshold_detector import EmergenceThresholdDetector

class RecursiveEmergenceSimulation:
    def __init__(self, config=None):
        """
        Initialize the recursive emergence simulation with improved threshold detection.
        
        Args:
            config (dict): Configuration parameters for the simulation
        """
        self.config = config or {}
        
        # Default configuration
        self.time_steps = self.config.get('time_steps', 500)
        self.constraint_level = self.config.get('constraint_level', 2)
        self.molecule_types = self.config.get('molecule_types', ['simple', 'polymer', 'catalyst'])
        self.energy_sources = self.config.get('energy_sources', ['thermal', 'chemical'])
        self.compartment_enabled = self.config.get('compartment_enabled', True)
        self.run_id = datetime.now().strftime("%Y_%m_%d_%H%M%S")
        
        # Initialize chemistry model
        self.chemistry = RealisticChemistry(
            constraint_level=self.constraint_level,
            energy_sources=self.energy_sources
        )
        
        # Initialize emergence threshold detector with time compression factor
        # 1 simulation step = ~10,000 years of natural chemistry
        time_compression_factor = self.config.get('time_compression_factor', 1e10)
        self.threshold_detector = EmergenceThresholdDetector(time_compression_factor=time_compression_factor)
        
        # Setup data collection
        self.metrics = {
            'entropy_reduction': [],
            'catalytic_activity': [],
            'molecular_complexity': [],
            'molecular_diversity': [],
            'energy_level': [],
            'compartment_count': [],
            'compartment_stability': [],
            'information_content': [],
            'feedback_coefficient': [],
            'emergence_threshold_crossings': []
        }
        
        self.results_dir = f"emergence_simulation_{self.run_id}"
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)
            
    def run_simulation(self):
        """Run the full simulation with enhanced threshold detection."""
        print(f"Starting recursive emergence simulation with constraint level {self.constraint_level}")
        print(f"Time steps: {self.time_steps}, Compartmentalization: {self.compartment_enabled}")
        
        # Initialize the system
        self.chemistry.initialize_system()
        
        # Run simulation steps
        for step in range(self.time_steps):
            self.time_step = step
            if step % 20 == 0:
                print(f"Processing step {step}/{self.time_steps}...")
                
            # Execute chemistry step
            self.chemistry.step()
            
            # Calculate system metrics
            metrics = self.calculate_metrics()
            
            # Store metrics for this step
            for key, value in metrics.items():
                if key in self.metrics:
                    self.metrics[key].append(value)
                    
            # Use the emergence threshold detector
            self.threshold_detector.calculate_metrics(self)
            
            # Check for detected thresholds in this step
            latest_thresholds = [t for t in self.threshold_detector.detected_thresholds 
                                if t['time_step'] == step]
                                
            if latest_thresholds:
                threshold = latest_thresholds[0]  # Take the first if multiple
                self.metrics['emergence_threshold_crossings'].append({
                    'step': step,
                    'type': threshold['type'],
                    'score': threshold['score']
                })
                
                print(f"[Step {step}] Emergence threshold detected!")
                print(f"  Type: {threshold['type']}")
                print(f"  Score: {threshold['score']:.3f}")
                print(f"  Est. real-time equivalent: {threshold['estimated_real_time']}")
                
        print(f"Simulation completed. Detected {len(self.threshold_detector.detected_thresholds)} emergence thresholds.")
        self.save_results()
        self.visualize_results()
        
    def calculate_metrics(self):
        """Calculate key system metrics for the current state."""
        metrics = {}
        
        # Get basic chemistry metrics
        chemistry_metrics = self.chemistry.calculate_metrics()
        metrics.update(chemistry_metrics)
        
        # Calculate information content
        if hasattr(self.chemistry, 'molecules'):
            # Simple estimation based on molecular diversity and complexity
            unique_molecules = len([m for m, count in self.chemistry.molecules.items() 
                                  if count > 0])
            avg_complexity = np.mean([m.complexity for m, count in self.chemistry.molecules.items()
                                    if count > 0]) if unique_molecules > 0 else 0
            metrics['information_content'] = unique_molecules * avg_complexity
        else:
            metrics['information_content'] = 0
            
        # Compartment metrics
        if self.compartment_enabled and hasattr(self.chemistry, 'compartments'):
            metrics['compartment_count'] = len(self.chemistry.compartments)
            metrics['compartment_stability'] = np.mean([c.stability for c in self.chemistry.compartments]) \
                                             if self.chemistry.compartments else 0
        else:
            metrics['compartment_count'] = 0
            metrics['compartment_stability'] = 0
            
        # Calculate entropy-catalysis feedback coefficient
        if len(self.metrics['entropy_reduction']) > 10:
            # Use correlation between entropy reduction and catalytic activity as proxy
            recent_entropy = self.metrics['entropy_reduction'][-10:]
            recent_catalysis = self.metrics['catalytic_activity'][-10:]
            
            try:
                feedback_coef = np.corrcoef(recent_entropy, recent_catalysis)[0, 1]
                metrics['feedback_coefficient'] = feedback_coef
            except:
                metrics['feedback_coefficient'] = 0
        else:
            metrics['feedback_coefficient'] = 0
            
        return metrics
        
    def save_results(self):
        """Save simulation results and detector analysis."""
        # Save metrics as JSON
        metrics_file = os.path.join(self.results_dir, "metrics.json")
        with open(metrics_file, 'w') as f:
            json.dump(self.metrics, f, indent=2)
            
        # Save threshold detector summary
        threshold_file = os.path.join(self.results_dir, "thresholds.json")
        with open(threshold_file, 'w') as f:
            json.dump({
                'detected_thresholds': self.threshold_detector.detected_thresholds,
                'boundary_formation_events': self.threshold_detector.boundary_formation_events,
                'autopoietic_transitions': self.threshold_detector.autopoietic_transitions,
                'summary': self.threshold_detector.get_summary()
            }, f, indent=2)
            
        # Save threshold detector plot
        plot_file = os.path.join(self.results_dir, "threshold_analysis.png")
        self.threshold_detector.plot_threshold_analysis(output_file=plot_file, show=False)
        
        print(f"Results saved to {self.results_dir}/")
        
    def visualize_results(self):
        """Create visualizations of the simulation results."""
        # Create basic metrics plot
        plt.figure(figsize=(14, 10))
        
        plt.subplot(2, 2, 1)
        plt.plot(self.metrics['entropy_reduction'], label='Entropy Reduction')
        plt.plot(self.metrics['catalytic_activity'], label='Catalytic Activity')
        plt.title('Core Metrics Evolution')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        plt.subplot(2, 2, 2)
        plt.plot(self.metrics['molecular_complexity'], label='Molecular Complexity')
        plt.plot(self.metrics['molecular_diversity'], label='Molecular Diversity')
        plt.title('Molecular System Evolution')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        plt.subplot(2, 2, 3)
        plt.plot(self.metrics['energy_level'], label='System Energy')
        if self.compartment_enabled:
            plt.plot(self.metrics['compartment_stability'], label='Compartment Stability')
        plt.title('Energy and Stability')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        plt.subplot(2, 2, 4)
        plt.plot(self.metrics['information_content'], label='Information Content')
        plt.plot(self.metrics['feedback_coefficient'], label='Feedback Coefficient')
        
        # Mark threshold crossings
        for threshold in self.metrics['emergence_threshold_crossings']:
            plt.axvline(x=threshold['step'], color='r', linestyle='--', alpha=0.6)
            plt.text(threshold['step'], max(self.metrics['information_content']), 
                   f"{threshold['type']}", rotation=90, verticalalignment='top')
                   
        plt.title('Information and Feedback Evolution')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.results_dir, "evolution_metrics.png"))
        
        # Create reaction network visualization if available
        if hasattr(self.chemistry, 'reaction_network'):
            plt.figure(figsize=(10, 8))
            G = self.chemistry.reaction_network
            
            try:
                pos = nx.spring_layout(G)
                
                # Draw molecules as nodes
                molecule_nodes = [n for n in G.nodes() if hasattr(n, 'is_molecule') and n.is_molecule]
                nx.draw_networkx_nodes(G, pos, nodelist=molecule_nodes, 
                                     node_color='skyblue', node_size=300, alpha=0.8)
                                     
                # Draw reactions as nodes
                reaction_nodes = [n for n in G.nodes() if not hasattr(n, 'is_molecule') or not n.is_molecule]
                nx.draw_networkx_nodes(G, pos, nodelist=reaction_nodes, 
                                     node_color='salmon', node_size=200, alpha=0.8)
                                     
                # Draw edges
                nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
                
                # Draw labels
                labels = {}
                for node in G.nodes():
                    if hasattr(node, 'name'):
                        labels[node] = node.name
                    elif hasattr(node, 'formula'):
                        labels[node] = node.formula
                    else:
                        labels[node] = str(node)
                        
                nx.draw_networkx_labels(G, pos, labels=labels, font_size=8)
                
                plt.title('Chemical Reaction Network')
                plt.axis('off')
                plt.savefig(os.path.join(self.results_dir, "reaction_network.png"))
                
            except Exception as e:
                print(f"Could not generate network visualization: {str(e)}")
                
        plt.close('all')

def run_constraint_comparison(constraint_levels=None, time_steps=300):
    """
    Run simulations with different constraint levels and compare emergence thresholds.
    
    Args:
        constraint_levels (list): List of constraint levels to test
        time_steps (int): Number of time steps for each simulation
    """
    if constraint_levels is None:
        constraint_levels = [1, 2, 3, 4, 5]
        
    results_dir = f"constraint_comparison_{datetime.now().strftime('%Y_%m_%d_%H%M%S')}"
    os.makedirs(results_dir, exist_ok=True)
    
    comparison_results = {}
    
    for level in constraint_levels:
        print(f"\n=== Running simulation with constraint level {level} ===")
        
        config = {
            'constraint_level': level,
            'time_steps': time_steps,
            'compartment_enabled': True
        }
        
        sim = RecursiveEmergenceSimulation(config=config)
        sim.run_simulation()
        
        # Collect key results
        comparison_results[level] = {
            'feedback_coefficient': np.mean(sim.metrics['feedback_coefficient'][-20:]),
            'final_complexity': sim.metrics['molecular_complexity'][-1] if sim.metrics['molecular_complexity'] else 0,
            'final_diversity': sim.metrics['molecular_diversity'][-1] if sim.metrics['molecular_diversity'] else 0,
            'threshold_count': len(sim.threshold_detector.detected_thresholds),
            'threshold_types': [t['type'] for t in sim.threshold_detector.detected_thresholds],
            'simulation_path': sim.results_dir
        }
        
    # Create comparison visualization
    plt.figure(figsize=(15, 10))
    
    # Plot feedback coefficient
    plt.subplot(2, 2, 1)
    levels = list(comparison_results.keys())
    feedback = [comparison_results[l]['feedback_coefficient'] for l in levels]
    plt.bar(levels, feedback, color='blue', alpha=0.7)
    plt.title('Feedback Coefficient vs Constraint Level')
    plt.xlabel('Constraint Level')
    plt.ylabel('Avg. Feedback Coefficient')
    plt.grid(True, alpha=0.3)
    
    # Plot complexity and diversity
    plt.subplot(2, 2, 2)
    complexity = [comparison_results[l]['final_complexity'] for l in levels]
    diversity = [comparison_results[l]['final_diversity'] for l in levels]
    
    x = np.arange(len(levels))
    width = 0.35
    
    plt.bar(x - width/2, complexity, width, label='Final Complexity', color='green', alpha=0.7)
    plt.bar(x + width/2, diversity, width, label='Final Diversity', color='purple', alpha=0.7)
    plt.title('System Complexity vs Constraint Level')
    plt.xlabel('Constraint Level')
    plt.xticks(x, levels)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Plot threshold counts
    plt.subplot(2, 2, 3)
    thresholds = [comparison_results[l]['threshold_count'] for l in levels]
    plt.bar(levels, thresholds, color='red', alpha=0.7)
    plt.title('Emergence Thresholds vs Constraint Level')
    plt.xlabel('Constraint Level')
    plt.ylabel('Number of Thresholds')
    plt.grid(True, alpha=0.3)
    
    # Plot threshold types distribution
    plt.subplot(2, 2, 4)
    threshold_types = {}
    for level in levels:
        for t_type in comparison_results[level]['threshold_types']:
            if t_type not in threshold_types:
                threshold_types[t_type] = [0] * len(levels)
            idx = levels.index(level)
            threshold_types[t_type][idx] += 1
    
    bottom = np.zeros(len(levels))
    for t_type, counts in threshold_types.items():
        plt.bar(levels, counts, bottom=bottom, label=t_type, alpha=0.7)
        bottom = bottom + np.array(counts)
    
    plt.title('Threshold Types by Constraint Level')
    plt.xlabel('Constraint Level')
    plt.ylabel('Count')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, "constraint_comparison.png"))
    
    # Save comparison results
    with open(os.path.join(results_dir, "comparison_results.json"), 'w') as f:
        # Convert NumPy values to native Python types for JSON serialization
        json_safe_results = {}
        for level, data in comparison_results.items():
            json_safe_results[str(level)] = {
                k: v if not isinstance(v, np.number) else v.item()
                for k, v in data.items()
            }
        json.dump(json_safe_results, f, indent=2)
    
    print(f"Constraint comparison completed. Results saved to {results_dir}/")
    return results_dir

def main():
    """Main entry point for the simulation."""
    if len(sys.argv) > 1:
        if sys.argv[1] == "--compare":
            # Run constraint comparison
            constraint_levels = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else None
            time_steps = int(sys.argv[3]) if len(sys.argv) > 3 else 300
            run_constraint_comparison(constraint_levels, time_steps)
        elif sys.argv[1] == "--single":
            # Run single simulation
            constraint = int(sys.argv[2]) if len(sys.argv) > 2 else 2
            time_steps = int(sys.argv[3]) if len(sys.argv) > 3 else 500
            
            config = {
                'constraint_level': constraint,
                'time_steps': time_steps
            }
            
            sim = RecursiveEmergenceSimulation(config=config)
            sim.run_simulation()
    else:
        # Default behavior - run single simulation
        sim = RecursiveEmergenceSimulation()
        sim.run_simulation()

if __name__ == "__main__":
    main()