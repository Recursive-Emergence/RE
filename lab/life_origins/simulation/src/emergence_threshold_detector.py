#!/usr/bin/env python3
"""
Advanced Emergence Threshold Detector.

This module implements specialized algorithms for detecting transitions between 
organizational layers in chemical systems, with a focus on information-theoretic
metrics that can identify true emergence thresholds.
"""

import numpy as np
from scipy import stats
import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt
import warnings

class EmergenceThresholdDetector:
    """
    Specialized detector for emergence thresholds using information-theoretic principles.
    Designed to accelerate detection of transitions that would take millions of years in nature.
    """
    
    def __init__(self, time_compression_factor=1e6):
        """
        Initialize the emergence threshold detector.
        
        Args:
            time_compression_factor (float): Factor representing how much simulation time
                                           is compressed compared to real-world time
        """
        self.time_compression_factor = time_compression_factor
        self.information_history = []
        self.transfer_entropy_history = []
        self.causal_density_history = []
        self.integrative_information_history = []
        self.boundary_formation_events = []
        self.autopoietic_transitions = []
        self.detected_thresholds = []
        
    def calculate_metrics(self, simulation):
        """
        Calculate information-theoretic metrics for the current simulation state.
        
        Args:
            simulation: Current simulation state
        """
        # 1. Calculate effective information
        effective_info = self._calculate_effective_information(simulation)
        self.information_history.append(effective_info)
        
        # 2. Calculate transfer entropy between system components
        transfer_entropy = self._calculate_transfer_entropy(simulation)
        self.transfer_entropy_history.append(transfer_entropy)
        
        # 3. Calculate causal density (measure of causal interactions)
        causal_density = self._calculate_causal_density(simulation)
        self.causal_density_history.append(causal_density)
        
        # 4. Calculate integrated information (measure of system integration)
        integrated_info = self._calculate_integrated_information(simulation)
        self.integrative_information_history.append(integrated_info)
        
        # Check for threshold crossings
        self._detect_threshold_crossings(simulation)
        
    def _calculate_effective_information(self, simulation):
        """
        Calculate the effective information in the system.
        This measures how much the system constrains its possible future states.
        
        Args:
            simulation: Current simulation state
            
        Returns:
            float: Effective information estimate
        """
        # Count unique molecules present in the simulation
        unique_molecules = set(m for m, count in simulation.molecules.items() 
                             if count > 0)
        
        if not unique_molecules:
            return 0.0
            
        # Base entropy calculation on molecular diversity and complexity
        # Consider both molecule types and their relative abundance
        molecule_counts = {m: count for m, count in simulation.molecules.items() if count > 0}
        total_molecules = sum(molecule_counts.values())
        
        # Calculate average entropy of the molecular distribution
        probabilities = [count/total_molecules for count in molecule_counts.values()]
        distribution_entropy = -sum(p * np.log2(p) if p > 0 else 0 for p in probabilities)
        
        # Calculate entropy reduction through constraints (complexity)
        avg_complexity = sum(m.complexity * count for m, count in molecule_counts.items()) / total_molecules
        max_possible_complexity = 10.0  # Theoretical maximum
        complexity_ratio = avg_complexity / max_possible_complexity
        
        # Effective information increases as the system becomes more structured
        effective_information = (len(unique_molecules) * complexity_ratio) / (1 + distribution_entropy)
        return effective_information
        
    def _calculate_transfer_entropy(self, simulation):
        """
        Estimate transfer entropy in the chemical network.
        This measures directed information flow between components.
        
        Args:
            simulation: Current simulation state
            
        Returns:
            float: Transfer entropy estimate
        """
        if not hasattr(simulation, 'reaction_network') or not simulation.reaction_network:
            return 0.0
            
        G = simulation.reaction_network
        if len(G.nodes()) < 2:
            return 0.0
            
        try:
            # Instead of actually computing transfer entropy (which would require time series data),
            # we'll estimate it from network properties that correlate with information flow
            
            # 1. Count directed paths between nodes
            path_count = 0
            nodes = list(G.nodes())[:min(20, len(G.nodes()))]  # Sample at most 20 nodes for efficiency
            
            for i in range(len(nodes)):
                for j in range(len(nodes)):
                    if i != j:
                        try:
                            if nx.has_path(G, nodes[i], nodes[j]):
                                path_count += 1
                        except:
                            pass
                            
            max_possible_paths = len(nodes) * (len(nodes) - 1)
            path_ratio = path_count / max_possible_paths if max_possible_paths > 0 else 0
            
            # 2. Network asymmetry (directedness)
            # More asymmetric flows = higher transfer entropy
            edge_asymmetry = 0
            for u, v in G.edges():
                if not G.has_edge(v, u):  # One-way edge
                    edge_asymmetry += 1
                    
            asymmetry_ratio = edge_asymmetry / len(G.edges()) if G.edges() else 0
            
            # 3. Average out-degree variability (indicator of specialization)
            out_degrees = [G.out_degree(n) for n in G.nodes()]
            if out_degrees:
                degree_std = np.std(out_degrees) / max(1, np.mean(out_degrees))
            else:
                degree_std = 0
                
            # Combine factors - higher values indicate more directed information flow
            transfer_entropy = (0.4 * path_ratio) + (0.4 * asymmetry_ratio) + (0.2 * degree_std)
            return min(1.0, transfer_entropy)
            
        except Exception as e:
            print(f"Error calculating transfer entropy: {e}")
            return 0.0
            
    def _calculate_causal_density(self, simulation):
        """
        Estimate causal density in the chemical network.
        This measures how richly causal the system is, normalized by system size.
        
        Args:
            simulation: Current simulation state
            
        Returns:
            float: Causal density estimate
        """
        if not hasattr(simulation, 'reaction_network') or not simulation.reaction_network:
            return 0.0
            
        G = simulation.reaction_network
        if len(G.nodes()) < 3:
            return 0.0
            
        try:
            # 1. Calculate network transitivity (clustering)
            # High clustering indicates localized causal interactions
            try:
                transitivity = nx.transitivity(G.to_undirected())
            except:
                transitivity = 0.0
                
            # 2. Estimate causal pathway diversity
            # Sample some nodes and count distinct path patterns
            sample_size = min(10, len(G.nodes()))
            nodes = list(G.nodes())[:sample_size]
            
            path_patterns = set()
            for i in range(len(nodes)):
                for j in range(len(nodes)):
                    if i != j:
                        try:
                            paths = list(nx.all_simple_paths(G, nodes[i], nodes[j], cutoff=3))
                            for path in paths:
                                path_patterns.add(tuple(path))
                        except:
                            pass
                            
            max_possible_patterns = sample_size * (sample_size - 1) * 3  # Rough estimate
            pattern_diversity = len(path_patterns) / max(1, max_possible_patterns)
            
            # 3. Feedback loop presence
            # Count strongly connected components (feedback cycles)
            try:
                sccs = list(nx.strongly_connected_components(G))
                cycle_ratio = sum(len(c) for c in sccs if len(c) > 1) / len(G.nodes())
            except:
                cycle_ratio = 0.0
                
            # Combine into causal density estimate
            # Normalize by system size to get true density
            causal_density = (0.3 * transitivity + 0.4 * pattern_diversity + 0.3 * cycle_ratio)
            return causal_density
            
        except Exception as e:
            print(f"Error calculating causal density: {e}")
            return 0.0
            
    def _calculate_integrated_information(self, simulation):
        """
        Estimate integrated information (Φ) in the system.
        This measures how much information is generated by the system as a whole,
        beyond the information generated by its parts independently.
        
        Args:
            simulation: Current simulation state
            
        Returns:
            float: Integrated information estimate
        """
        if not hasattr(simulation, 'reaction_network') or not simulation.reaction_network:
            return 0.0
            
        # A proper Φ calculation requires temporal data and partitioning the system
        # Here we'll use graph-theoretic proxies that correlate with integration
        G = simulation.reaction_network
            
        try:
            # 1. Estimate integration from network modularity
            try:
                # Convert to undirected for community detection
                G_undirected = G.to_undirected()
                communities = nx.community.greedy_modularity_communities(G_undirected)
                
                # Calculate cross-community edges (integration between modules)
                cross_edges = 0
                total_edges = len(G.edges())
                
                # Create a map from node to community
                node_to_community = {}
                for i, comm in enumerate(communities):
                    for node in comm:
                        node_to_community[node] = i
                        
                # Count cross-community edges
                for u, v in G.edges():
                    if u in node_to_community and v in node_to_community:
                        if node_to_community[u] != node_to_community[v]:
                            cross_edges += 1
                            
                integration_score = cross_edges / max(1, total_edges)
                
            except Exception as e:
                # Fall back to simpler metric if community detection fails
                integration_score = len(G.edges()) / (len(G.nodes()) * (len(G.nodes()) - 1))
                
            # 2. Check for existence of central hub nodes (integrators)
            try:
                centrality = nx.betweenness_centrality(G)
                max_centrality = max(centrality.values()) if centrality else 0
            except:
                max_centrality = 0
                
            # 3. Check for compartmentalization (physical integration boundary)
            compartment_factor = 0
            if hasattr(simulation, 'compartments') and simulation.compartments:
                # Use compartment count and stability as integration indicator
                avg_stability = np.mean([c.stability for c in simulation.compartments])
                compartment_factor = min(1.0, len(simulation.compartments) * avg_stability / 5)
                
            # Calculate final Φ estimate
            phi = (0.4 * integration_score + 0.3 * max_centrality + 0.3 * compartment_factor)
            return min(1.0, phi)
            
        except Exception as e:
            print(f"Error calculating integrated information: {e}")
            return 0.0
            
    def _detect_threshold_crossings(self, simulation):
        """
        Detect emergence threshold crossings using the calculated metrics.
        
        Args:
            simulation: Current simulation state
        """
        # Need enough history to detect transitions
        if (len(self.information_history) < 10 or
            len(self.transfer_entropy_history) < 10):
            return
            
        # Get current values
        current_info = self.information_history[-1]
        current_transfer = self.transfer_entropy_history[-1]
        current_causal = self.causal_density_history[-1]
        current_phi = self.integrative_information_history[-1]
        
        # Get baseline values (from 5-10 steps ago)
        history_window = 5
        baseline_start = max(0, len(self.information_history) - 10)
        baseline_end = max(0, len(self.information_history) - 5)
        
        baseline_info = np.mean(self.information_history[baseline_start:baseline_end]) if baseline_end > baseline_start else 0
        baseline_transfer = np.mean(self.transfer_entropy_history[baseline_start:baseline_end]) if baseline_end > baseline_start else 0
        baseline_causal = np.mean(self.causal_density_history[baseline_start:baseline_end]) if baseline_end > baseline_start else 0
        baseline_phi = np.mean(self.integrative_information_history[baseline_start:baseline_end]) if baseline_end > baseline_start else 0
        
        # Define thresholds for significant increases
        info_threshold = max(0.1, baseline_info * 1.5)
        transfer_threshold = max(0.2, baseline_transfer * 1.8)
        causal_threshold = max(0.15, baseline_causal * 1.7)
        phi_threshold = max(0.25, baseline_phi * 2.0)  # Higher threshold for Φ
        
        # Check for various types of threshold crossings
        
        # 1. Boundary formation - physical separation between system and environment
        if (current_phi > phi_threshold and 
            hasattr(simulation, 'compartments') and 
            len(simulation.compartments) > 0):
                
            # Only record if this is a new event (not too close to previous ones)
            if (not self.boundary_formation_events or 
                simulation.time_step - self.boundary_formation_events[-1]['time_step'] > 20):
                
                self.boundary_formation_events.append({
                    'time_step': simulation.time_step,
                    'phi': current_phi,
                    'compartment_count': len(simulation.compartments),
                })
                
                print(f"[EmergenceThresholdDetector] Detected boundary formation at step {simulation.time_step}")
                print(f"  - Φ value: {current_phi:.3f}, Compartments: {len(simulation.compartments)}")
                
        # 2. Autopoietic transition - self-maintenance and self-production capability
        if (current_info > info_threshold and
            current_transfer > transfer_threshold and
            current_causal > causal_threshold):
                
            # Calculate additional autopoiesis indicators
            
            # Check for cyclic reactions (self-production)
            has_cycles = False
            if hasattr(simulation, 'reaction_network'):
                try:
                    cycles = list(nx.simple_cycles(simulation.reaction_network))
                    has_cycles = len(cycles) > 0
                except:
                    pass
                    
            # Check for catalytic closure (all reactions catalyzed)
            catalytic_closure = False
            if hasattr(simulation, 'reactions'):
                catalyzed_ratio = sum(1 for r in simulation.reactions if r.is_catalyzed) / max(1, len(simulation.reactions))
                catalytic_closure = catalyzed_ratio > 0.7  # 70% or more reactions are catalyzed
                
            # Check for energy autonomy
            energy_autonomy = False
            if hasattr(simulation, 'energy') and hasattr(simulation, 'energy_carriers'):
                energy_autonomy = simulation.energy > 50 and len(simulation.energy_carriers) >= 3
                
            # Only register if we have positive indicators
            if (has_cycles or catalytic_closure or energy_autonomy):
                if (not self.autopoietic_transitions or 
                    simulation.time_step - self.autopoietic_transitions[-1]['time_step'] > 30):
                    
                    self.autopoietic_transitions.append({
                        'time_step': simulation.time_step,
                        'info': current_info,
                        'transfer': current_transfer,
                        'causal': current_causal,
                        'has_cycles': has_cycles,
                        'catalytic_closure': catalytic_closure,
                        'energy_autonomy': energy_autonomy
                    })
                    
                    print(f"[EmergenceThresholdDetector] Detected autopoietic transition at step {simulation.time_step}")
                    print(f"  - Info: {current_info:.3f}, Transfer: {current_transfer:.3f}, Causal: {current_causal:.3f}")
                    print(f"  - Cycles: {has_cycles}, Catalytic closure: {catalytic_closure}, Energy autonomy: {energy_autonomy}")
                    
        # 3. General emergence threshold 
        # Look for coordinated increases across multiple metrics
        metrics_increasing = (
            current_info > baseline_info * 1.3 and
            current_transfer > baseline_transfer * 1.3 and
            current_phi > baseline_phi * 1.3
        )
        
        if metrics_increasing:
            # Calculate the integrated threshold score
            threshold_score = (
                (current_info / max(0.001, baseline_info) - 1) +
                (current_transfer / max(0.001, baseline_transfer) - 1) + 
                (current_phi / max(0.001, baseline_phi) - 1)
            ) / 3.0
            
            # Only record significant thresholds
            if threshold_score > 0.5:
                if (not self.detected_thresholds or 
                    simulation.time_step - self.detected_thresholds[-1]['time_step'] > 15):
                    
                    # Classify the threshold type
                    if current_phi > 0.6:
                        threshold_type = "Major organizational transition"
                    elif current_phi > 0.3:
                        threshold_type = "Proto-organizational emergence"
                    else:
                        threshold_type = "Chemical complexity threshold"
                        
                    # Estimate real-world timescale equivalent (very approximate)
                    estimated_years = simulation.time_step * self.time_compression_factor / (365 * 24 * 3600)
                    time_description = self._format_time_estimate(estimated_years)
                    
                    self.detected_thresholds.append({
                        'time_step': simulation.time_step,
                        'score': threshold_score,
                        'type': threshold_type,
                        'info': current_info,
                        'transfer': current_transfer,
                        'causal': current_causal,
                        'phi': current_phi,
                        'estimated_real_time': time_description
                    })
                    
                    print(f"[EmergenceThresholdDetector] Detected {threshold_type} at step {simulation.time_step}")
                    print(f"  - Threshold score: {threshold_score:.3f}")
                    print(f"  - Estimated real-world equivalent: {time_description}")
                    print(f"  - Φ: {current_phi:.3f}, Info: {current_info:.3f}, Transfer: {current_transfer:.3f}")
                    
    def _format_time_estimate(self, years):
        """Format the time estimate in a human-readable way."""
        if years < 1:
            return f"{years*365:.1f} days"
        elif years < 1000:
            return f"{years:.1f} years"
        elif years < 1000000:
            return f"{years/1000:.1f} thousand years"
        else:
            return f"{years/1000000:.1f} million years"
                    
    def plot_threshold_analysis(self, output_file=None, show=True):
        """
        Generate a comprehensive visualization of emergence thresholds.
        
        Args:
            output_file (str): Path to save the plot
            show (bool): Whether to display the plot
        """
        if not self.information_history:
            print("No data available for plotting")
            return
            
        # Create figure with multiple subplots
        fig, axes = plt.subplots(3, 1, figsize=(14, 18), gridspec_kw={'height_ratios': [2, 1, 2]})
        
        # Plot 1: Information metrics evolution
        steps = range(len(self.information_history))
        
        axes[0].plot(steps, self.information_history, 'b-', label='Effective Information')
        axes[0].plot(steps, self.transfer_entropy_history, 'g-', label='Transfer Entropy')
        axes[0].plot(steps, self.causal_density_history, 'r-', label='Causal Density')
        axes[0].plot(steps, self.integrative_information_history, 'purple', label='Φ (Integrated Information)')
        
        # Mark thresholds on the plot
        for threshold in self.detected_thresholds:
            step = threshold['time_step']
            score = threshold['score']
            t_type = threshold['type']
            
            # Add vertical line
            axes[0].axvline(x=step, color='gray', linestyle='--', alpha=0.7)
            
            # Add annotation
            y_pos = max(self.information_history[step], 
                       self.transfer_entropy_history[step],
                       self.integrative_information_history[step]) + 0.1
                       
            # Alternate annotation positions to avoid overlap
            if len(self.detected_thresholds) > 1:
                y_offset = 0.1 * (1 if self.detected_thresholds.index(threshold) % 2 == 0 else -0.5)
                y_pos += y_offset
                
            axes[0].annotate(
                f"{t_type}\nScore: {score:.2f}",
                xy=(step, y_pos),
                xytext=(10, 0),
                textcoords="offset points",
                ha='center',
                va='bottom',
                fontsize=9,
                bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=0.7),
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0")
            )
            
        axes[0].set_title('Information-Theoretic Metrics Over Time')
        axes[0].set_xlabel('Simulation Steps')
        axes[0].set_ylabel('Metric Value')
        axes[0].legend(loc='best')
        axes[0].grid(True, alpha=0.3)
        
        # Plot 2: Special events timeline
        axes[1].set_title('Emergence Events Timeline')
        axes[1].set_xlabel('Simulation Steps')
        axes[1].set_yticks([0.25, 0.75])
        axes[1].set_yticklabels(['Boundary\nFormation', 'Autopoietic\nTransition'])
        axes[1].set_ylim(0, 1)
        
        # Add boundary formation events
        for event in self.boundary_formation_events:
            step = event['time_step']
            axes[1].scatter([step], [0.25], c='blue', s=80, marker='o')
            
            # Add annotation for significant events
            if event['compartment_count'] > 1 or event['phi'] > 0.5:
                axes[1].annotate(
                    f"Compartments: {event['compartment_count']}\nΦ: {event['phi']:.2f}",
                    xy=(step, 0.25),
                    xytext=(0, -20),
                    textcoords="offset points",
                    ha='center',
                    fontsize=8,
                    bbox=dict(boxstyle="round,pad=0.2", fc="white", alpha=0.7)
                )
                
        # Add autopoietic transition events
        for event in self.autopoietic_transitions:
            step = event['time_step']
            axes[1].scatter([step], [0.75], c='red', s=80, marker='o')
            
            # Create feature string based on what's present
            features = []
            if event['has_cycles']: features.append("Cycles")
            if event['catalytic_closure']: features.append("Cat. Closure")
            if event['energy_autonomy']: features.append("Energy Auton.")
            feature_str = ", ".join(features)
            
            # Add annotation
            axes[1].annotate(
                feature_str,
                xy=(step, 0.75),
                xytext=(0, 15),
                textcoords="offset points",
                ha='center',
                fontsize=8,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", alpha=0.7)
            )
            
        # Add connecting lines between related events
        for bt_event in self.boundary_formation_events:
            bt_step = bt_event['time_step']
            
            # Find closest autopoietic transition
            close_ap_events = [ap for ap in self.autopoietic_transitions
                             if abs(ap['time_step'] - bt_step) < 15]
            
            for ap_event in close_ap_events:
                ap_step = ap_event['time_step']
                axes[1].plot([bt_step, ap_step], [0.25, 0.75], 'k--', alpha=0.3)
                
        axes[1].grid(True, alpha=0.3)
        
        # Plot 3: Real-time equivalent timeline and comparison
        if self.detected_thresholds:
            # Extract time points and labels
            time_steps = [th['time_step'] for th in self.detected_thresholds]
            time_labels = [th['estimated_real_time'] for th in self.detected_thresholds]
            threshold_types = [th['type'] for th in self.detected_thresholds]
            threshold_scores = [th['score'] for th in self.detected_thresholds]
            
            # Create the timeline visualization
            for i, (step, label, t_type, score) in enumerate(zip(time_steps, time_labels, threshold_types, threshold_scores)):
                # Position alternating events above/below the central line
                y_pos = 0.5 + (0.3 if i % 2 == 0 else -0.3)
                
                # Draw the marker
                marker_size = 100 + score * 80  # Size based on score
                axes[2].scatter([step], [y_pos], s=marker_size, 
                              c=[plt.cm.viridis(score/2)], 
                              alpha=0.7, zorder=10)
                
                # Connect to the timeline
                axes[2].plot([step, step], [y_pos, 0.5], 'k-', alpha=0.3)
                
                # Add the label
                axes[2].annotate(
                    f"{t_type}\n{label}",
                    xy=(step, y_pos),
                    xytext=(0, 10 if i % 2 == 0 else -25),
                    textcoords="offset points",
                    ha='center',
                    va='center',
                    fontsize=9,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=0.8)
                )
                
            # Draw the timeline itself
            axes[2].axhline(y=0.5, color='black', alpha=0.5, lw=2)
            
            # Add real-world events for comparison (approximate timeline)
            real_events = [
                {"time": 4000, "event": "Prebiotic Earth Formation", "y_offset": -0.2},
                {"time": 3800, "event": "Earliest Evidence of Life", "y_offset": 0.2},
                {"time": 3500, "event": "First Stromatolites", "y_offset": -0.2},
                {"time": 2700, "event": "Oxygen Photosynthesis", "y_offset": 0.2},
                {"time": 2000, "event": "Eukaryotic Cells", "y_offset": -0.2},
                {"time": 600, "event": "First Animals", "y_offset": 0.2},
                {"time": 400, "event": "Land Plants", "y_offset": -0.2}
            ]
            
            # Get the rough scale of our timeline in millions of years
            if self.time_compression_factor > 0:
                max_steps = max(time_steps) if time_steps else 100
                scale_factor = max_steps * self.time_compression_factor / (365 * 24 * 3600 * 1000000)
                
                # Only add events that fit our scale
                for event in real_events:
                    scaled_step = event["time"] / scale_factor if scale_factor > 0 else 0
                    if 0 <= scaled_step <= max(time_steps) * 1.2:
                        y_pos = 0.5 + event["y_offset"]
                        
                        # Draw the marker
                        axes[2].scatter([scaled_step], [y_pos], s=60, 
                                      c='gray', alpha=0.5, marker='s')
                                      
                        # Connect to timeline
                        axes[2].plot([scaled_step, scaled_step], [y_pos, 0.5], 
                                   'k--', alpha=0.2)
                                   
                        # Add label
                        axes[2].annotate(
                            f"{event['event']}\n({event['time']} Mya)",
                            xy=(scaled_step, y_pos),
                            xytext=(0, 10 if event["y_offset"] > 0 else -10),
                            textcoords="offset points",
                            ha='center',
                            va='center',
                            fontsize=8,
                            color='gray',
                            bbox=dict(boxstyle="round,pad=0.2", fc="white", alpha=0.6)
                        )
            
            axes[2].set_title('Emergence Timeline with Real-Time Equivalents')
            axes[2].set_xlabel('Simulation Steps')
            axes[2].set_yticks([])  # Hide Y axis ticks
            axes[2].grid(True, alpha=0.2)
        else:
            axes[2].text(0.5, 0.5, "No threshold events detected yet", 
                       ha='center', va='center', fontsize=12)
        
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            print(f"Threshold analysis plot saved to {output_file}")
            
        if show:
            plt.show()
        else:
            plt.close(fig)
            
    def get_summary(self):
        """
        Get a summary of detected emergence thresholds.
        
        Returns:
            dict: Summary of emergence thresholds and events
        """
        summary = {
            'detected_thresholds': len(self.detected_thresholds),
            'boundary_formation_events': len(self.boundary_formation_events),
            'autopoietic_transitions': len(self.autopoietic_transitions),
            'classification': {}
        }
        
        # Count threshold types
        for threshold in self.detected_thresholds:
            t_type = threshold['type']
            if t_type not in summary['classification']:
                summary['classification'][t_type] = 1
            else:
                summary['classification'][t_type] += 1
                
        # Add most significant threshold if available
        if self.detected_thresholds:
            most_significant = max(self.detected_thresholds, key=lambda x: x['score'])
            summary['most_significant_threshold'] = {
                'time_step': most_significant['time_step'],
                'type': most_significant['type'],
                'score': most_significant['score'],
                'estimated_real_time': most_significant['estimated_real_time']
            }
            
        # Add latest info metrics
        if self.information_history:
            summary['latest_metrics'] = {
                'information': self.information_history[-1],
                'transfer_entropy': self.transfer_entropy_history[-1],
                'causal_density': self.causal_density_history[-1],
                'integrated_information': self.integrative_information_history[-1]
            }
            
        return summary