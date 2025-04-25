#!/usr/bin/env python3
"""
Emergence Detector for Life Origins Simulation.

This module implements advanced algorithms for detecting emergence thresholds
in chemical systems, with a focus on identifying transitions between
organizational layers.
"""

import numpy as np
import networkx as nx
from scipy import stats
import matplotlib.pyplot as plt
from collections import defaultdict
import warnings

# Add the missing function needed for the simulation
def analyze_complexity_emergence(network):
    """
    Analyze a chemical network to detect emergence thresholds and complex behavior.
    This is a simplified wrapper around the EmergenceDetector class functionality.
    
    Args:
        network: The ChemicalNetwork instance to analyze
        
    Returns:
        dict: Analysis results including complexity scores and emergence metrics
    """
    # Get network's own analysis if available
    if hasattr(network, 'get_final_analysis'):
        network_analysis = network.get_final_analysis()
    else:
        network_analysis = {
            'complexity_score': 0,
            'entropy_catalysis_feedback': 0,
            'autocatalytic_cycles': 0
        }
    
    # Create a detector and analyze transfer entropy
    detector = EmergenceDetector()
    transfer_entropy = detector.calculate_transfer_entropy(network)
    
    # Calculate information metrics
    info_content = detector._calculate_information_content(network)
    resilience = detector._estimate_resilience(network)
    
    # Combine results
    results = {
        'complexity_score': network_analysis.get('complexity_score', 0),
        'entropy_catalysis_feedback': network_analysis.get('entropy_catalysis_feedback', 0),
        'autocatalytic_cycles': network_analysis.get('autocatalytic_cycles', 0),
        'transfer_entropy': transfer_entropy,
        'information_content': info_content,
        'resilience': resilience,
    }
    
    # Check for specific emergence thresholds
    if results['entropy_catalysis_feedback'] > 0.1:
        results['emergence_thresholds'] = ['entropy_catalysis_feedback']
        if results['autocatalytic_cycles'] > 0:
            results['emergence_thresholds'].append('autocatalytic')
        if results['resilience'] > 0.5:
            results['emergence_thresholds'].append('resilience')
    else:
        results['emergence_thresholds'] = []
    
    return results

class EmergenceDetector:
    """
    Class for detecting and analyzing emergence thresholds in simulations.
    """
    
    def __init__(self, sensitivity=0.05, window_size=20):
        """
        Initialize the emergence detector.
        
        Args:
            sensitivity (float): Threshold sensitivity for detecting significant changes
            window_size (int): Window size for moving calculations and trend detection
        """
        self.sensitivity = sensitivity
        self.window_size = window_size
        self.metrics_history = {
            'entropy_reduction': [],
            'catalytic_activity': [],
            'molecular_complexity': [],
            'compartment_count': [],
            'information_content': [],
            'feedback_coefficient': [],
            'resilience_score': []
        }
        self.detected_events = []
        self.emergence_thresholds = {}
        self.current_layer = 0  # Track the current organizational layer
        
    def update(self, simulation, time_step):
        """
        Update metrics history with the current simulation state.
        
        Args:
            simulation: Current simulation state
            time_step (int): Current simulation time step
        """
        # Update standard metrics from simulation
        for metric in ['entropy_reduction', 'catalytic_activity', 
                      'molecular_complexity', 'compartment_count']:
            if hasattr(simulation, 'metrics') and metric in simulation.metrics:
                if simulation.metrics[metric]:  # Check if the metric has values
                    self.metrics_history[metric].append(simulation.metrics[metric][-1])
                else:
                    self.metrics_history[metric].append(0)
            else:
                self.metrics_history[metric].append(0)
                
        # Calculate advanced metrics
        if hasattr(simulation, 'calculate_feedback_coefficient'):
            feedback = simulation.calculate_feedback_coefficient()
            self.metrics_history['feedback_coefficient'].append(feedback)
        else:
            self.metrics_history['feedback_coefficient'].append(0)
            
        # Calculate information content based on molecular diversity and complexity
        info_content = self._calculate_information_content(simulation)
        self.metrics_history['information_content'].append(info_content)
        
        # Calculate system resilience if possible
        resilience = self._estimate_resilience(simulation)
        self.metrics_history['resilience_score'].append(resilience)
        
        # Detect emergence events
        if time_step >= self.window_size:
            self._detect_emergence_events(time_step)
            
    def _calculate_information_content(self, simulation):
        """
        Calculate the information content of the system.
        Uses molecule diversity, complexity and network structure.
        
        Args:
            simulation: Current simulation state
        
        Returns:
            float: Information content estimate
        """
        # Base information on molecule count and diversity
        molecule_diversity = len([m for m in simulation.molecules if simulation.molecules[m] > 0])
        avg_complexity = np.mean([m.complexity for m in simulation.molecules 
                                if simulation.molecules[m] > 0]) if molecule_diversity > 0 else 0
                                
        # Information from network structure
        network_info = 0
        if hasattr(simulation, 'reaction_network') and len(simulation.reaction_network) > 0:
            G = simulation.reaction_network
            # Calculate network metrics that correlate with information content
            if len(G) > 1:
                try:
                    # Average clustering coefficient - indicator of functional modules
                    clustering = nx.average_clustering(G.to_undirected())
                    # Number of strongly connected components - indicator of functional subsystems
                    components = len(list(nx.strongly_connected_components(G)))
                    network_info = 0.1 * (clustering * 10 + components)
                except:
                    # Fallback if network metrics calculation fails
                    network_info = 0.05 * len(G.edges)
                    
        # Information from compartmentalization
        compartment_info = 0
        if hasattr(simulation, 'compartments'):
            for compartment in simulation.compartments:
                # Calculate information in each compartment
                molecules_inside = sum(compartment.molecules.values()) if hasattr(compartment, 'molecules') else 0
                stability = getattr(compartment, 'stability', 0.5)
                compartment_info += molecules_inside * stability * 0.1
                
        # Combine all sources of information
        total_info = (molecule_diversity * avg_complexity * 0.5 + 
                     network_info + compartment_info)
                     
        return max(0, total_info)
        
    def _estimate_resilience(self, simulation):
        """
        Estimate the system's resilience to perturbation.
        
        Args:
            simulation: Current simulation state
            
        Returns:
            float: Resilience score between 0-1
        """
        # Start with baseline resilience
        baseline = 0.2
        
        # Factor 1: Network redundancy (multiple pathways)
        redundancy = 0
        if hasattr(simulation, 'reaction_network'):
            G = simulation.reaction_network
            if len(G) > 2:
                try:
                    # Average number of alternate paths between pairs of nodes
                    sample_size = min(10, len(G.nodes))
                    if sample_size >= 2:
                        nodes = list(G.nodes)[:sample_size]
                        path_counts = []
                        for i in range(len(nodes)):
                            for j in range(i+1, len(nodes)):
                                try:
                                    paths = list(nx.all_simple_paths(G, nodes[i], nodes[j], cutoff=3))
                                    path_counts.append(len(paths))
                                except:
                                    path_counts.append(0)
                        redundancy = min(0.3, np.mean(path_counts) * 0.1)
                except:
                    redundancy = 0
                    
        # Factor 2: Catalytic coverage
        catalytic_coverage = 0
        if self.metrics_history['catalytic_activity']:
            catalytic_coverage = min(0.3, self.metrics_history['catalytic_activity'][-1])
            
        # Factor 3: Compartmentalization
        compartment_factor = 0
        if hasattr(simulation, 'compartments') and simulation.compartments:
            # Average compartment stability
            stability = np.mean([getattr(c, 'stability', 0) for c in simulation.compartments])
            compartment_factor = min(0.2, stability)
        
        # Calculate overall resilience
        resilience = baseline + redundancy + catalytic_coverage + compartment_factor
        return min(1.0, resilience)
        
    def _detect_emergence_events(self, time_step):
        """
        Detect emergence events based on metrics history.
        
        Args:
            time_step (int): Current simulation time step
        """
        # Define the window for looking back
        start_idx = max(0, len(self.metrics_history['molecular_complexity']) - self.window_size)
        current_idx = len(self.metrics_history['molecular_complexity']) - 1
        
        if start_idx >= current_idx:
            return  # Not enough history
            
        detected_this_step = False
        
        # Check for significant changes in key metrics
        for metric in ['molecular_complexity', 'information_content', 'feedback_coefficient']:
            if len(self.metrics_history[metric]) <= self.window_size:
                continue
                
            # Get metric history
            metric_history = self.metrics_history[metric]
            
            # Calculate baseline mean and std
            baseline = metric_history[start_idx:start_idx + self.window_size//2]
            baseline_mean = np.mean(baseline) if baseline else 0
            baseline_std = np.std(baseline) if baseline else 0
            
            # Get current value
            current_value = metric_history[current_idx]
            
            # Check for significant change
            if baseline_std > 0:
                z_score = (current_value - baseline_mean) / baseline_std
                
                # Significant positive change indicates emergence
                if z_score > 2.5 and not detected_this_step:
                    # Check if this is a sustained change, not just a spike
                    recent_values = metric_history[current_idx-5:current_idx+1]
                    if all(v > baseline_mean + baseline_std for v in recent_values):
                        self._record_emergence_event(time_step, metric, 
                                                   current_value, baseline_mean, z_score)
                        detected_this_step = True
                        
        # Special check for compartment formation
        if ('compartment_count' in self.metrics_history and 
            len(self.metrics_history['compartment_count']) > self.window_size):
            
            compartment_history = self.metrics_history['compartment_count']
            if (compartment_history[current_idx] > 0 and 
                np.mean(compartment_history[start_idx:start_idx + self.window_size//2]) == 0):
                
                # First compartment formation is a clear emergence event
                self._record_emergence_event(time_step, 'compartment_formation', 
                                          compartment_history[current_idx], 0, float('inf'))
                                          
        # Check for feedback coefficient threshold crossing
        if ('feedback_coefficient' in self.metrics_history and 
            len(self.metrics_history['feedback_coefficient']) > self.window_size):
            
            feedback_history = self.metrics_history['feedback_coefficient']
            # Threshold for significant feedback coefficient
            if (feedback_history[current_idx] > 0.2 and 
                np.mean(feedback_history[start_idx:start_idx + self.window_size//2]) < 0.1):
                
                self._record_emergence_event(time_step, 'feedback_threshold', 
                                          feedback_history[current_idx], 
                                          np.mean(feedback_history[start_idx:start_idx + self.window_size//2]),
                                          feedback_history[current_idx] / 0.1)
                                          
        # Check for transfer entropy threshold (if available)
        # Transfer entropy measures causal information flow between components
        # Significant increase suggests new organization level
        if hasattr(self, 'transfer_entropy') and self.transfer_entropy is not None:
            if self.transfer_entropy > 0.5:  # Threshold for significant transfer
                self._record_emergence_event(time_step, 'transfer_entropy_threshold',
                                          self.transfer_entropy, 0.25, self.transfer_entropy / 0.25)
        
    def _record_emergence_event(self, time_step, metric, current_value, baseline, z_score):
        """
        Record a detected emergence event.
        
        Args:
            time_step (int): Current simulation time step
            metric (str): Metric that triggered the event
            current_value (float): Current value of the metric
            baseline (float): Baseline value for comparison
            z_score (float): Z-score of the change
        """
        event = {
            'time_step': time_step,
            'metric': metric,
            'value': current_value,
            'baseline': baseline,
            'z_score': z_score,
            'metrics_snapshot': {k: v[-1] if v else 0 for k, v in self.metrics_history.items()}
        }
        
        self.detected_events.append(event)
        
        # Check if this represents a new layer transition
        if len(self.detected_events) > 1:
            prev_event = self.detected_events[-2]
            # If significant time has passed and multiple metrics show emergence
            if (time_step - prev_event['time_step'] > self.window_size * 2 or
                metric not in [e['metric'] for e in self.detected_events[-3:-1]]):
                
                # This may represent a new layer
                self.current_layer += 1
                event['new_layer'] = self.current_layer
                self.emergence_thresholds[self.current_layer] = time_step
                
        print(f"[EmergenceDetector] Detected emergence event at step {time_step}: "
              f"{metric} increased from {baseline:.3f} to {current_value:.3f} "
              f"(z-score: {z_score:.2f})")
                
    def calculate_transfer_entropy(self, simulation):
        """
        Calculate transfer entropy in the system as a measure of causal information flow.
        Requires time series data from simulation components.
        
        Args:
            simulation: Current simulation state
            
        Returns:
            float: Transfer entropy estimate
        """
        # This is a complex calculation that would ideally use scipy's mutual information
        # For a simplified implementation, we'll use a proxy based on network structure
        if not hasattr(simulation, 'reaction_network'):
            self.transfer_entropy = 0
            return 0
            
        G = simulation.reaction_network
        if len(G) < 3:
            self.transfer_entropy = 0
            return 0
            
        try:
            # Calculate network properties related to information flow
            # 1. Edge density: more edges = more potential information paths
            edge_density = len(G.edges) / (len(G.nodes) * (len(G.nodes) - 1))
            
            # 2. Average path length: shorter paths = faster information flow
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                avg_path_length = nx.average_shortest_path_length(G) if nx.is_strongly_connected(G) else 10
            inv_path_length = 1.0 / max(1.0, avg_path_length)
            
            # 3. Information flow potential
            info_flow = edge_density * inv_path_length * 5.0  # Scale factor
            
            self.transfer_entropy = min(1.0, info_flow)
            return self.transfer_entropy
            
        except:
            self.transfer_entropy = 0
            return 0
            
    def get_emergence_summary(self):
        """
        Get a summary of detected emergence events and thresholds.
        
        Returns:
            dict: Summary of emergence events and layer transitions
        """
        # Count events by type
        event_types = {}
        for event in self.detected_events:
            metric = event['metric']
            if metric not in event_types:
                event_types[metric] = 1
            else:
                event_types[metric] += 1
                
        # Get layer transitions
        layer_transitions = {k: {'time_step': v, 'events': []} for k, v in self.emergence_thresholds.items()}
        
        for event in self.detected_events:
            if 'new_layer' in event:
                layer = event['new_layer']
                if layer in layer_transitions:
                    layer_transitions[layer]['events'].append(event)
                    
        # Calculate some summary statistics
        avg_interval = 0
        if len(self.detected_events) > 1:
            intervals = [self.detected_events[i+1]['time_step'] - self.detected_events[i]['time_step'] 
                       for i in range(len(self.detected_events)-1)]
            avg_interval = np.mean(intervals) if intervals else 0
            
        return {
            'total_events': len(self.detected_events),
            'event_types': event_types,
            'layer_transitions': layer_transitions,
            'current_layer': self.current_layer,
            'avg_interval_between_events': avg_interval
        }
        
    def plot_emergence_analysis(self, output_file=None, show=True):
        """
        Generate a comprehensive plot of emergence analysis.
        
        Args:
            output_file (str): Path to save the plot
            show (bool): Whether to display the plot
        """
        if not self.metrics_history['molecular_complexity']:
            print("Insufficient data for plotting")
            return
            
        # Create figure
        fig, axes = plt.subplots(3, 1, figsize=(12, 15), sharex=True)
        
        # Time steps
        time_steps = range(len(self.metrics_history['molecular_complexity']))
        
        # Plot 1: Core metrics
        axes[0].plot(time_steps, self.metrics_history['molecular_complexity'], 'b-', 
                   label='Molecular Complexity')
        axes[0].plot(time_steps, self.metrics_history['information_content'], 'g-',
                   label='Information Content')
        if all(v == 0 for v in self.metrics_history['compartment_count']):
            # Don't plot flat line of zeros
            pass
        else:
            axes[0].plot(time_steps, self.metrics_history['compartment_count'], 'r-',
                       label='Compartment Count')
                       
        axes[0].set_ylabel('Metric Value')
        axes[0].legend(loc='best')
        axes[0].set_title('Core Emergence Metrics')
        axes[0].grid(True, alpha=0.3)
        
        # Plot 2: Feedback and resilience
        axes[1].plot(time_steps, self.metrics_history['feedback_coefficient'], 'purple-',
                   label='Feedback Coefficient')
        axes[1].plot(time_steps, self.metrics_history['resilience_score'], 'orange-',
                   label='Resilience Score')
        axes[1].plot(time_steps, self.metrics_history['catalytic_activity'], 'c-',
                   label='Catalytic Activity')
        
        # Add horizontal threshold lines for interpretation
        axes[1].axhline(y=0.2, color='purple', linestyle='--', alpha=0.7, 
                      label='Feedback Threshold')
        axes[1].axhline(y=0.5, color='orange', linestyle='--', alpha=0.7,
                      label='Resilience Threshold')
        
        axes[1].set_ylabel('Score (0-1)')
        axes[1].legend(loc='best')
        axes[1].set_title('Feedback and Resilience Indicators')
        axes[1].grid(True, alpha=0.3)
        
        # Plot 3: Emergence events and layer transitions
        # This is blank initially but we'll mark events on it
        axes[2].set_xlabel('Simulation Time Steps')
        axes[2].set_ylabel('Event Significance')
        axes[2].set_ylim(0, 10)
        axes[2].set_title('Detected Emergence Events and Layer Transitions')
        
        # Mark events with vertical lines and annotations
        max_y = 10  # Max height for plotting
        event_y_positions = []
        
        for i, event in enumerate(self.detected_events):
            step = event['time_step']
            metric = event['metric']
            value = event['value']
            
            # Set position and color based on event type
            if metric == 'molecular_complexity':
                color = 'blue'
                y_pos = 3
                label = 'Complexity'
            elif metric == 'information_content':
                color = 'green'
                y_pos = 5
                label = 'Information'
            elif metric == 'compartment_formation':
                color = 'red'
                y_pos = 7
                label = 'Compartment'
            elif metric == 'feedback_threshold':
                color = 'purple'
                y_pos = 9
                label = 'Feedback'
            else:
                color = 'gray'
                y_pos = 1
                label = metric.split('_')[0]
                
            # Avoid overlapping labels
            while y_pos in event_y_positions:
                y_pos = max(1, (y_pos + 2) % max_y)
            event_y_positions.append(y_pos)
            
            # Draw the event
            axes[2].axvline(x=step, color=color, linestyle='-', alpha=0.5)
            axes[2].scatter([step], [y_pos], color=color, s=50, zorder=10)
            
            # Add label for significant events or layer transitions
            if 'new_layer' in event or event['z_score'] > 5:
                axes[2].annotate(
                    f"{label}: {value:.2f}" + (" [New Layer]" if 'new_layer' in event else ""),
                    xy=(step, y_pos),
                    xytext=(10, 0),
                    textcoords="offset points",
                    ha='left',
                    va='center',
                    fontsize=9,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=0.8),
                    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2")
                )
                
        # Mark layer transitions with background shading
        for layer, data in self.emergence_thresholds.items():
            step = data
            # Shade from this transition to next one or end
            next_steps = [s for s in self.emergence_thresholds.values() if s > step]
            end_step = min(next_steps) if next_steps else len(time_steps)
            
            # Add shaded region
            axes[2].axvspan(step, end_step, alpha=0.1, color=f'C{layer % 10}',
                          label=f"Layer {layer}" if layer > 0 else "Base Layer")
                          
            # Add layer label
            axes[2].text(
                step + (end_step - step)/2, 
                8,
                f"Layer {layer}",
                ha='center',
                va='bottom',
                fontsize=10,
                bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=0.7)
            )
            
        # Add grid
        axes[2].grid(True, alpha=0.3)
        
        # Adjust layout and save/show plot
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            print(f"Emergence analysis plot saved to {output_file}")
            
        if show:
            plt.show()
        else:
            plt.close(fig)
            
    def plot_threshold_sensitivity(self, simulation, output_file=None, show=True):
        """
        Plot how different threshold sensitivities affect emergence detection.
        
        Args:
            simulation: Current simulation state
            output_file (str): Path to save the plot
            show (bool): Whether to display the plot
        """
        # Create range of sensitivities to test
        sensitivities = [0.01, 0.025, 0.05, 0.075, 0.1, 0.15, 0.2]
        event_counts = []
        layer_counts = []
        
        # Test each sensitivity
        original_sensitivity = self.sensitivity
        original_events = self.detected_events.copy()
        original_thresholds = self.emergence_thresholds.copy()
        original_layer = self.current_layer
        
        try:
            for sens in sensitivities:
                # Reset detector
                self.sensitivity = sens
                self.detected_events = []
                self.emergence_thresholds = {}
                self.current_layer = 0
                
                # Re-detect with new sensitivity
                for t in range(len(self.metrics_history['molecular_complexity'])):
                    if t >= self.window_size:
                        self._detect_emergence_events(t)
                        
                # Count results
                event_counts.append(len(self.detected_events))
                layer_counts.append(self.current_layer)
                
            # Create figure
            fig, ax1 = plt.subplots(figsize=(10, 6))
            
            # Plot event counts
            color = 'tab:blue'
            ax1.set_xlabel('Sensitivity Threshold')
            ax1.set_ylabel('Number of Events', color=color)
            ax1.plot(sensitivities, event_counts, 'o-', color=color)
            ax1.tick_params(axis='y', labelcolor=color)
            
            # Create second y-axis
            ax2 = ax1.twinx()
            color = 'tab:red'
            ax2.set_ylabel('Number of Layers', color=color)
            ax2.plot(sensitivities, layer_counts, 'o-', color=color)
            ax2.tick_params(axis='y', labelcolor=color)
            
            # Add title and grid
            plt.title('Impact of Sensitivity Threshold on Emergence Detection')
            ax1.grid(True, alpha=0.3)
            
            # Highlight current sensitivity
            ax1.axvline(x=original_sensitivity, color='black', linestyle='--', alpha=0.5,
                      label=f'Current Sensitivity: {original_sensitivity}')
            ax1.legend(loc='upper right')
            
            # Save/show
            if output_file:
                plt.savefig(output_file, dpi=300, bbox_inches='tight')
                print(f"Sensitivity analysis plot saved to {output_file}")
                
            if show:
                plt.show()
            else:
                plt.close(fig)
                
        finally:
            # Restore original state
            self.sensitivity = original_sensitivity
            self.detected_events = original_events
            self.emergence_thresholds = original_thresholds
            self.current_layer = original_layer