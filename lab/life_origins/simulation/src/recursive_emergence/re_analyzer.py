"""
Recursive Emergence Analyzer

This module integrates all the recursive emergence metrics and provides a unified
interface for analyzing chemical networks from the perspective of the RE theory.
"""

import os
import json
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Any, Optional

from .negentropy_metrics import NegentropyCalculator
from .pattern_tracker import PatternTracker
from .layer_transition_detector import LayerTransitionDetector

class RecursiveEmergenceAnalyzer:
    """
    Main analyzer for applying Recursive Emergence theory to chemical simulations.
    
    This class integrates all components of the RE framework and provides
    a unified interface for analyzing emergence in chemical networks.
    """
    
    def __init__(self, output_dir: Optional[str] = None):
        """
        Initialize the analyzer.
        
        Args:
            output_dir: Directory to save analysis results
        """
        self.negentropy = NegentropyCalculator()
        self.pattern_tracker = PatternTracker()
        self.layer_detector = LayerTransitionDetector()
        self.timestep = 0
        self.history = {}
        self.output_dir = output_dir
        
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def analyze_step(self, network, timestep: int) -> Dict[str, Any]:
        """
        Analyze the current simulation step.
        
        Args:
            network: ChemicalNetwork instance
            timestep: Current simulation timestep
            
        Returns:
            dict: Analysis results for this step
        """
        self.timestep = timestep
        
        # 1. Calculate negentropy metrics
        negentropy_metrics = self.negentropy.calculate_all_layer_negentropies(network)
        emergence_potential = self.negentropy.calculate_emergence_potential(network)
        persistence_scores = self.negentropy.get_persistence_scores(network)
        
        # 2. Update pattern tracking
        self.pattern_tracker.update(network, timestep)
        pattern_metrics = self.pattern_tracker.get_pattern_metrics()
        
        # 3. Combine metrics for layer transition detection
        combined_metrics = {
            **negentropy_metrics,
            'persistence_scores': persistence_scores,
            'emergence_potential': emergence_potential,
            'pattern_counts': {
                layer: len(pids) for layer, pids 
                in self.pattern_tracker.patterns_by_layer.items()
            }
        }
        
        # Flatten the nested metrics for layer transition detection
        flat_metrics = {}
        for key, value in negentropy_metrics.items():
            flat_metrics[f"{key}_negentropy"] = value
            
        for layer, score in persistence_scores.items():
            flat_metrics[f"{layer}_persistence"] = score
            
        # Add pattern counts by type
        for ptype, pids in self.pattern_tracker.patterns_by_type.items():
            flat_metrics[f"{ptype}_count"] = len(pids)
            
        # Get active pattern counts
        active_patterns = self.pattern_tracker.get_active_patterns()
        active_by_layer = {}
        for pattern in active_patterns:
            if pattern.layer not in active_by_layer:
                active_by_layer[pattern.layer] = 0
            active_by_layer[pattern.layer] += 1
            
        for layer, count in active_by_layer.items():
            flat_metrics[f"active_{layer}_patterns"] = count
        
        # Count specific entity types from the network
        if hasattr(network, 'molecules'):
            # Count template molecules
            template_count = sum(1 for mol in network.molecules 
                              if network.molecules[mol] > 0 and 
                              hasattr(mol, 'is_template') and mol.is_template)
            flat_metrics['template_molecules'] = template_count
            
            # Count amphiphilic molecules
            amphiphilic_count = sum(1 for mol in network.molecules
                                  if network.molecules[mol] > 0 and
                                  hasattr(mol, 'is_amphiphilic') and mol.is_amphiphilic)
            flat_metrics['amphiphilic_molecules'] = amphiphilic_count
        
        # Count specific reaction types
        if hasattr(network, 'active_reactions'):
            # Count replication events
            replication_count = sum(1 for r in network.active_reactions
                                  if hasattr(r, 'is_template_based') and r.is_template_based)
            flat_metrics['replication_events'] = replication_count
            
            # Get other reaction types
            for reaction in network.active_reactions:
                if hasattr(reaction, 'reaction_type'):
                    reaction_type = reaction.reaction_type
                    if f"{reaction_type}_reactions" not in flat_metrics:
                        flat_metrics[f"{reaction_type}_reactions"] = 0
                    flat_metrics[f"{reaction_type}_reactions"] += 1
        
        # Count compartments
        if hasattr(network, 'compartments'):
            flat_metrics['compartment_count'] = len(network.compartments)
        
        # Get feedback coefficient if available
        if hasattr(network, 'calculate_feedback_coefficient'):
            feedback = network.calculate_feedback_coefficient()
            flat_metrics['feedback_coefficient'] = feedback
        elif hasattr(network, 'get_final_analysis'):
            analysis = network.get_final_analysis()
            flat_metrics['feedback_coefficient'] = analysis.get('entropy_catalysis_feedback', 0)
            flat_metrics['autocatalytic_cycles'] = analysis.get('autocatalytic_cycles', 0)
        
        # 4. Update layer transition detector
        self.layer_detector.update(network, timestep, flat_metrics)
        layer_metrics = self.layer_detector.get_transition_metrics()
        
        # 5. Generate the complete analysis for this step
        analysis = {
            'timestep': timestep,
            'negentropy_by_layer': negentropy_metrics,
            'emergence_potential': emergence_potential,
            'persistence_scores': persistence_scores,
            'current_layer': self.layer_detector.get_current_layer(),
            'pattern_metrics': pattern_metrics,
            'layer_metrics': layer_metrics,
            'high_reusability_patterns': len(self.pattern_tracker.find_high_reusability_patterns()),
            'persistent_patterns': len(self.pattern_tracker.find_persistent_patterns())
        }
        
        # Store results in history
        self.history[timestep] = analysis
        
        return analysis
    
    def get_comprehensive_analysis(self) -> Dict[str, Any]:
        """
        Get a comprehensive analysis of the entire simulation run.
        
        Returns:
            dict: Comprehensive analysis results
        """
        if not self.history:
            return {'error': 'No data collected yet'}
            
        # Get final layer info
        transition_summary = self.layer_detector.get_transition_summary()
        
        # Get pattern network
        pattern_network = self.pattern_tracker.generate_pattern_network()
        pattern_network_stats = {
            'node_count': pattern_network.number_of_nodes(),
            'edge_count': pattern_network.number_of_edges(),
            'avg_degree': np.mean([d for _, d in pattern_network.degree()]) if pattern_network.number_of_nodes() > 0 else 0
        }
        
        # Get layer trajectory
        layer_trajectory = self.negentropy.generate_layer_trajectory()
        
        # Calculate layer transition efficiency
        transition_efficiency = {}
        for i in range(len(self.layer_detector.layer_sequence) - 1):
            source = self.layer_detector.layer_sequence[i]
            target = self.layer_detector.layer_sequence[i + 1]
            key = f"{source}_to_{target}"
            
            # Check if this transition happened
            if target in transition_summary.get('transition_times', {}):
                time_to_transition = transition_summary['transition_times'][key]
                # Efficiency is inversely proportional to time
                transition_efficiency[key] = 100.0 / (1.0 + time_to_transition)
            else:
                transition_efficiency[key] = 0.0
        
        # Identify the most significant patterns
        top_patterns = []
        for pattern in sorted(self.pattern_tracker.patterns.values(), 
                             key=lambda p: p.persistence * p.reusability, 
                             reverse=True)[:5]:
            top_patterns.append({
                'id': pattern.id,
                'type': pattern.pattern_type,
                'layer': pattern.layer,
                'persistence': pattern.persistence,
                'reusability': pattern.reusability,
                'component_count': len(pattern.components)
            })
        
        # Compile the comprehensive analysis
        analysis = {
            'simulation_duration': self.timestep,
            'highest_layer_reached': transition_summary['highest_layer_reached'],
            'transitions': transition_summary['transitions'],
            'transition_efficiency': transition_efficiency,
            'pattern_network_stats': pattern_network_stats,
            'top_patterns': top_patterns,
            'final_negentropy': {k: v[-1] if v else 0 for k, v in self.negentropy.history.items() 
                               if k.endswith('negentropy') and v},
            'overall_reusability': np.mean([p.reusability for p in self.pattern_tracker.patterns.values()])
                                if self.pattern_tracker.patterns else 0,
            'recursive_strength': self._calculate_recursive_strength()
        }
        
        return analysis
    
    def _calculate_recursive_strength(self) -> float:
        """
        Calculate the overall recursive strength of the system.
        
        This is a measure of how strongly each layer enables the next one,
        reflecting the core principle of recursive emergence.
        
        Returns:
            float: Recursive strength score (0-1)
        """
        if not self.history:
            return 0.0
        
        # Get the last recorded negentropy values
        latest = max(self.history.keys())
        latest_data = self.history[latest]
        layer_negentropies = latest_data.get('negentropy_by_layer', {})
        
        # If we don't have at least two layers with data, recursion is minimal
        if len([v for v in layer_negentropies.values() if v > 0.1]) < 2:
            return 0.0
        
        # Calculate how much each layer builds on the previous
        recursive_score = 0.0
        layer_sequence = self.layer_detector.layer_sequence
        
        # Sum of all direct layer transitions
        for i in range(len(layer_sequence) - 1):
            source = layer_sequence[i]
            target = layer_sequence[i + 1]
            
            # Get negentropy values
            source_neg = layer_negentropies.get(source, 0)
            target_neg = layer_negentropies.get(target, 0)
            
            # Skip if source has no significant negentropy
            if source_neg < 0.05:
                continue
                
            # If target has more negentropy than source, that's recursive building
            if target_neg > 0.1:
                # The more the target exceeds the source, the stronger the recursion
                diff = target_neg - source_neg
                if diff > 0:
                    # Weight by source's negentropy - stronger sources enable stronger targets
                    recursive_score += diff * source_neg
        
        # Normalize to 0-1 range
        # We expect at most 3 layer transitions, each with an average diff of 0.3
        normalization_factor = 0.3 * 3
        normalized_score = min(1.0, recursive_score / normalization_factor)
        
        return normalized_score
    
    def generate_report(self, output_file: Optional[str] = None) -> Dict[str, Any]:
        """
        Generate a comprehensive report of the analysis.
        
        Args:
            output_file: File to save the report
            
        Returns:
            dict: Report data
        """
        # Get comprehensive analysis
        analysis = self.get_comprehensive_analysis()
        
        # Generate plots
        if self.output_dir:
            plot_dir = os.path.join(self.output_dir, 'plots')
            if not os.path.exists(plot_dir):
                os.makedirs(plot_dir)
                
            # Plot layer transitions
            transition_plot = os.path.join(plot_dir, 'layer_transitions.png')
            self.layer_detector.plot_layer_transitions(transition_plot, show=False)
            analysis['plots'] = {'layer_transitions': transition_plot}
            
            # Plot negentropy over time
            self._plot_negentropy_over_time(os.path.join(plot_dir, 'negentropy_over_time.png'))
            analysis['plots']['negentropy'] = os.path.join(plot_dir, 'negentropy_over_time.png')
            
            # Plot patterns metrics
            self._plot_pattern_metrics(os.path.join(plot_dir, 'pattern_metrics.png'))
            analysis['plots']['patterns'] = os.path.join(plot_dir, 'pattern_metrics.png')
            
            # Plot emergence potential
            self._plot_emergence_potential(os.path.join(plot_dir, 'emergence_potential.png'))
            analysis['plots']['emergence'] = os.path.join(plot_dir, 'emergence_potential.png')
        
        # Save report if output file is specified
        if output_file:
            with open(output_file, 'w') as f:
                json.dump(analysis, f, indent=2)
                
            # Generate text report
            report_file = output_file.replace('.json', '.md')
            self._generate_text_report(report_file, analysis)
                
        return analysis
    
    def _plot_negentropy_over_time(self, output_file: str) -> None:
        """
        Plot negentropy metrics over time.
        
        Args:
            output_file: File to save the plot
        """
        # Extract negentropy history
        metrics = ['chemical_negentropy', 'replicative_negentropy', 
                 'autocatalytic_negentropy', 'compartmental_negentropy']
                 
        data = {}
        timesteps = sorted(self.history.keys())
        
        for metric in metrics:
            data[metric] = []
            
            for t in timesteps:
                value = self.history[t].get('negentropy_by_layer', {}).get(
                    metric.replace('_negentropy', ''), 0)
                data[metric].append(value)
        
        # Create plot
        plt.figure(figsize=(10, 6))
        
        for metric in metrics:
            plt.plot(timesteps, data[metric], 
                    label=metric.replace('_', ' ').title())
        
        plt.title('Negentropy by Layer Over Time')
        plt.xlabel('Simulation Time Step')
        plt.ylabel('Negentropy Value')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(output_file, dpi=300)
        plt.close()
    
    def _plot_pattern_metrics(self, output_file: str) -> None:
        """
        Plot pattern metrics over time.
        
        Args:
            output_file: File to save the plot
        """
        # Extract pattern metrics
        metrics = ['total_patterns', 'active_patterns', 'persistent_patterns']
        data = {m: [] for m in metrics}
        
        # Layer-specific pattern counts
        layer_counts = {layer: [] for layer in self.layer_detector.layer_sequence}
        
        timesteps = sorted(self.history.keys())
        
        for t in timesteps:
            data['total_patterns'].append(
                self.history[t].get('pattern_metrics', {}).get('total_patterns', 0))
            data['active_patterns'].append(
                self.history[t].get('pattern_metrics', {}).get('active_patterns', 0))
            data['persistent_patterns'].append(
                self.history[t].get('persistent_patterns', 0))
                
            # Get layer counts
            layer_data = self.history[t].get('pattern_metrics', {}).get('patterns_by_layer', {})
            for layer in layer_counts:
                layer_counts[layer].append(layer_data.get(layer, 0))
        
        # Create plot (2 subplots)
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True)
        
        # Plot 1: Overall pattern metrics
        for metric in metrics:
            ax1.plot(timesteps, data[metric], 
                   label=metric.replace('_', ' ').title())
        
        ax1.set_title('Pattern Metrics Over Time')
        ax1.set_ylabel('Count')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Layer-specific pattern counts
        for layer, counts in layer_counts.items():
            ax2.plot(timesteps, counts, 
                   label=f"{layer.capitalize()} Patterns")
        
        ax2.set_title('Pattern Count by Layer Over Time')
        ax2.set_xlabel('Simulation Time Step')
        ax2.set_ylabel('Count')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(output_file, dpi=300)
        plt.close()
    
    def _plot_emergence_potential(self, output_file: str) -> None:
        """
        Plot emergence potential over time.
        
        Args:
            output_file: File to save the plot
        """
        # Extract emergence potential data
        layers = self.layer_detector.layer_sequence
        data = {layer: [] for layer in layers}
        
        timesteps = sorted(self.history.keys())
        
        for t in timesteps:
            potentials = self.history[t].get('emergence_potential', {})
            for layer in layers:
                data[layer].append(potentials.get(layer, 0))
        
        # Create plot
        plt.figure(figsize=(10, 6))
        
        for layer in layers:
            plt.plot(timesteps, data[layer], 
                    label=f"{layer.capitalize()} Potential")
        
        plt.title('Emergence Potential by Layer Over Time')
        plt.xlabel('Simulation Time Step')
        plt.ylabel('Emergence Potential Value')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(output_file, dpi=300)
        plt.close()
    
    def _generate_text_report(self, output_file: str, analysis: Dict[str, Any]) -> None:
        """
        Generate a text report of the analysis.
        
        Args:
            output_file: File to save the report
            analysis: Analysis data
        """
        with open(output_file, 'w') as f:
            f.write("# Recursive Emergence Analysis Report\n\n")
            
            f.write("## Simulation Overview\n\n")
            f.write(f"- **Duration:** {analysis['simulation_duration']} time steps\n")
            f.write(f"- **Highest Layer Reached:** {analysis['highest_layer_reached'].capitalize()}\n")
            f.write(f"- **Recursive Strength:** {analysis['recursive_strength']:.2f}\n")
            f.write(f"- **Number of Layer Transitions:** {len(analysis['transitions'])}\n\n")
            
            f.write("## Layer Transitions\n\n")
            if analysis['transitions']:
                f.write("| From Layer | To Layer | Time Step | Time to Transition |\n")
                f.write("|------------|----------|-----------|-------------------|\n")
                
                for i, event in enumerate(analysis['transitions']):
                    from_layer = event['from_layer']
                    to_layer = event['to_layer']
                    time_step = event['timestep']
                    
                    # Calculate time to transition
                    if i == 0:
                        time_to = time_step
                    else:
                        time_to = time_step - analysis['transitions'][i-1]['timestep']
                        
                    f.write(f"| {from_layer.capitalize()} | {to_layer.capitalize()} | {time_step} | {time_to} |\n")
            else:
                f.write("No layer transitions detected.\n")
            
            f.write("\n## Final Negentropy Values\n\n")
            f.write("| Layer | Negentropy Value |\n")
            f.write("|-------|------------------|\n")
            
            for layer, value in analysis['final_negentropy'].items():
                layer_name = layer.replace('_negentropy', '').capitalize()
                f.write(f"| {layer_name} | {value:.4f} |\n")
            
            f.write("\n## Top Persistent Patterns\n\n")
            if analysis['top_patterns']:
                f.write("| Pattern Type | Layer | Persistence | Reusability |\n")
                f.write("|-------------|-------|-------------|-------------|\n")
                
                for pattern in analysis['top_patterns']:
                    f.write(f"| {pattern['type'].replace('_', ' ').title()} | "
                          f"{pattern['layer'].capitalize()} | "
                          f"{pattern['persistence']:.1f} | "
                          f"{pattern['reusability']:.2f} |\n")
            else:
                f.write("No significant patterns detected.\n")
                
            f.write("\n## Pattern Network Statistics\n\n")
            f.write(f"- **Pattern Nodes:** {analysis['pattern_network_stats']['node_count']}\n")
            f.write(f"- **Connections:** {analysis['pattern_network_stats']['edge_count']}\n")
            f.write(f"- **Average Connections Per Pattern:** {analysis['pattern_network_stats']['avg_degree']:.2f}\n\n")
            
            f.write("## Analysis Summary\n\n")
            
            recursive_strength = analysis['recursive_strength']
            if recursive_strength > 0.7:
                assessment = "strong evidence of recursive emergence"
            elif recursive_strength > 0.4:
                assessment = "moderate evidence of recursive emergence"
            elif recursive_strength > 0.2:
                assessment = "weak evidence of recursive emergence"
            else:
                assessment = "insufficient evidence of recursive emergence"
                
            f.write(f"This simulation shows **{assessment}**. ")
            
            highest_layer = analysis['highest_layer_reached']
            if highest_layer == 'compartmental':
                f.write("The system reached the highest layer (compartmental), demonstrating a complete "
                        "recursive emergence sequence.\n")
            elif highest_layer == 'autocatalytic':
                f.write("The system reached the autocatalytic layer but did not develop compartmentalization. "
                        "This represents partial recursive emergence.\n")
            elif highest_layer == 'replicative':
                f.write("The system developed replicative structures but did not achieve full autocatalytic "
                        "feedback cycles. Early-stage recursive emergence is evident.\n")
            else:  # chemical
                f.write("The system remained at the chemical layer without developing significant "
                        "higher-order structures. No significant recursive emergence was detected.\n")
                
            # Add plot references if available
            if 'plots' in analysis:
                f.write("\n## Visualization\n\n")
                for plot_name, plot_path in analysis['plots'].items():
                    relative_path = os.path.relpath(plot_path, os.path.dirname(output_file))
                    f.write(f"- [{plot_name.replace('_', ' ').title()}]({relative_path})\n")