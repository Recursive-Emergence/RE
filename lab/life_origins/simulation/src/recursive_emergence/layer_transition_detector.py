"""
Layer Transition Detection for Recursive Emergence

This module handles the detection of transitions between organizational layers
in recursive emergence systems, with a focus on identifying threshold-crossing events.
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from typing import Dict, List, Any, Optional, Tuple

class LayerTransitionDetector:
    """
    Detects transitions between organizational layers in chemical simulations.
    
    This class focuses on identifying when a system crosses critical thresholds
    that represent transitions to a new emergent layer.
    """
    
    def __init__(self):
        """Initialize the layer transition detector"""
        self.history = defaultdict(list)
        self.transitions = {}
        self.layer_sequence = ['chemical', 'replicative', 'autocatalytic', 'compartmental']
        self.current_layer = 'chemical'
        self.timestep = 0
        
        # Threshold values for transitions between layers
        self.thresholds = {
            'chemical_to_replicative': {
                'template_molecules': 1,       # At least one template molecule
                'replication_events': 2,       # Multiple replication events
                'chemical_negentropy': 0.3     # Sufficient chemical order
            },
            'replicative_to_autocatalytic': {
                'autocatalytic_cycles': 1,     # At least one autocatalytic cycle
                'feedback_coefficient': 0.2,   # Significant feedback
                'replicative_negentropy': 0.25 # Sufficient replicative order
            },
            'autocatalytic_to_compartmental': {
                'compartment_count': 1,        # At least one compartment
                'amphiphilic_molecules': 3,    # Several amphiphilic molecules
                'autocatalytic_negentropy': 0.3 # Sufficient autocatalytic order
            }
        }
        
        # History of layer transitions
        self.transition_events = []
        
    def update(self, network, timestep: int, metrics: Dict[str, Any]) -> None:
        """
        Update the detector with current simulation state.
        
        Args:
            network: ChemicalNetwork instance
            timestep: Current simulation timestep
            metrics: Current negentropy metrics and other layer-specific data
        """
        self.timestep = timestep
        
        # Store metrics history
        for key, value in metrics.items():
            if isinstance(value, (int, float, bool)):
                self.history[key].append(value)
        
        # Check for layer transitions
        self._detect_layer_transitions(network, metrics)
        
    def _detect_layer_transitions(self, network, metrics: Dict[str, Any]) -> None:
        """
        Check if any layer transitions have occurred.
        
        Args:
            network: ChemicalNetwork instance
            metrics: Current metrics
        """
        # Get current index in layer sequence
        current_idx = self.layer_sequence.index(self.current_layer)
        
        # Check if we can transition to the next layer
        if current_idx < len(self.layer_sequence) - 1:
            next_layer = self.layer_sequence[current_idx + 1]
            transition_key = f"{self.current_layer}_to_{next_layer}"
            
            if self._check_transition_thresholds(transition_key, network, metrics):
                # Transition detected
                self.current_layer = next_layer
                
                # Record the transition
                transition_event = {
                    'timestep': self.timestep,
                    'from_layer': self.layer_sequence[current_idx],
                    'to_layer': next_layer,
                    'metrics_snapshot': {k: metrics.get(k, 0) for k in self.thresholds[transition_key].keys()}
                }
                
                self.transition_events.append(transition_event)
                self.transitions[next_layer] = self.timestep
                
                print(f"[Layer Transition] {transition_key.replace('_', ' ')} at step {self.timestep}")
    
    def _check_transition_thresholds(
            self, 
            transition_key: str,
            network,
            metrics: Dict[str, Any]
        ) -> bool:
        """
        Check if thresholds for a layer transition have been met.
        
        Args:
            transition_key: Transition identifier (e.g., "chemical_to_replicative")
            network: ChemicalNetwork instance
            metrics: Current metrics
            
        Returns:
            bool: True if transition thresholds are met
        """
        if transition_key not in self.thresholds:
            return False
            
        thresholds = self.thresholds[transition_key]
        all_met = True
        
        for metric_name, threshold_value in thresholds.items():
            # Check if metric exists in provided metrics
            current_value = metrics.get(metric_name, 0)
            
            # If not in metrics, try to get from network or its analysis
            if current_value == 0 and hasattr(network, 'get_final_analysis'):
                analysis = network.get_final_analysis()
                current_value = analysis.get(metric_name, 0)
            
            # Compare with threshold
            if current_value < threshold_value:
                all_met = False
                break
        
        return all_met
    
    def set_thresholds(self, transition_thresholds: Dict[str, Dict[str, float]]) -> None:
        """
        Set custom thresholds for layer transitions.
        
        Args:
            transition_thresholds: Dictionary of thresholds by transition
        """
        # Update thresholds with provided values
        for transition, thresholds in transition_thresholds.items():
            if transition in self.thresholds:
                self.thresholds[transition].update(thresholds)
            else:
                self.thresholds[transition] = thresholds
    
    def get_current_layer(self) -> str:
        """
        Get the current organizational layer.
        
        Returns:
            str: Current layer name
        """
        return self.current_layer
    
    def get_transition_metrics(self) -> Dict[str, Any]:
        """
        Get metrics about layer transitions.
        
        Returns:
            dict: Transition metrics
        """
        metrics = {
            'current_layer': self.current_layer,
            'layer_index': self.layer_sequence.index(self.current_layer),
            'transitions_occurred': len(self.transition_events),
            'time_in_current_layer': self.timestep - self.transitions.get(
                self.current_layer, 0),
            'all_transitions': {
                layer: time for layer, time in self.transitions.items()
            }
        }
        
        # Calculate average time spent in each layer
        if len(self.transition_events) > 0:
            layer_durations = []
            prev_time = 0
            
            for event in self.transition_events:
                duration = event['timestep'] - prev_time
                layer_durations.append(duration)
                prev_time = event['timestep']
                
            metrics['avg_layer_duration'] = np.mean(layer_durations) if layer_durations else 0
            
        return metrics
    
    def plot_layer_transitions(self, output_file: str = None, show: bool = True) -> None:
        """
        Generate a plot of layer transitions over time.
        
        Args:
            output_file: Path to save the plot
            show: Whether to display the plot
        """
        if not self.transition_events and not self.history:
            print("Insufficient data for plotting layer transitions")
            return
            
        # Create figure
        fig, axes = plt.subplots(2, 1, figsize=(12, 10), sharex=True, gridspec_kw={'height_ratios': [1, 3]})
        
        # Time steps for x-axis
        max_time = self.timestep
        time_steps = list(range(max_time + 1))
        
        # Plot 1: Layer transitions
        ax_layers = axes[0]
        
        # Create layer presence array
        layer_data = np.zeros((len(self.layer_sequence), max_time + 1))
        
        # Fill based on transitions
        current_layer_idx = 0
        current_layer = self.layer_sequence[0]
        
        for t in time_steps:
            # Check if we have a transition at this time
            for event in self.transition_events:
                if event['timestep'] == t:
                    current_layer = event['to_layer']
                    current_layer_idx = self.layer_sequence.index(current_layer)
            
            # Mark this layer as active at this time
            layer_data[current_layer_idx, t] = 1
            
        # Plot each layer as a line
        for i, layer in enumerate(self.layer_sequence):
            ax_layers.plot(time_steps, layer_data[i], drawstyle='steps-post', 
                          label=layer.capitalize(), linewidth=2)
            
        # Mark transition points
        for event in self.transition_events:
            ax_layers.axvline(x=event['timestep'], color='red', linestyle='--', alpha=0.7)
            ax_layers.annotate(
                f"{event['from_layer'].capitalize()} → {event['to_layer'].capitalize()}",
                xy=(event['timestep'], 0.5),
                xytext=(5, 0),
                textcoords="offset points",
                ha='left',
                va='center',
                fontsize=9,
                bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=0.8)
            )
            
        ax_layers.set_yticks(range(len(self.layer_sequence)))
        ax_layers.set_yticklabels([layer.capitalize() for layer in self.layer_sequence])
        ax_layers.set_ylabel('Active Layer')
        ax_layers.set_ylim(-0.2, len(self.layer_sequence) - 0.8)
        ax_layers.set_title('Layer Transitions Over Time')
        ax_layers.grid(True, axis='x', alpha=0.3)
        ax_layers.legend(loc='upper right')
        
        # Plot 2: Metrics that drive transitions
        ax_metrics = axes[1]
        
        # Plot relevant metrics from history
        metrics_to_plot = [
            'chemical_negentropy',
            'replicative_negentropy', 
            'autocatalytic_negentropy',
            'compartmental_negentropy'
        ]
        
        for metric in metrics_to_plot:
            if metric in self.history and len(self.history[metric]) > 0:
                # Pad or truncate to match time_steps length
                values = self.history[metric]
                if len(values) < len(time_steps):
                    values = values + [values[-1]] * (len(time_steps) - len(values))
                elif len(values) > len(time_steps):
                    values = values[:len(time_steps)]
                    
                ax_metrics.plot(time_steps, values, label=metric.replace('_', ' ').title())
        
        # Add threshold lines for transitions
        for transition, thresholds in self.thresholds.items():
            for metric, value in thresholds.items():
                if metric.endswith('negentropy'):  # Only show negentropy thresholds
                    ax_metrics.axhline(y=value, color='gray', linestyle=':', alpha=0.7,
                                     label=f"{transition.replace('_', ' ')} threshold ({value})")
        
        ax_metrics.set_xlabel('Simulation Time Steps')
        ax_metrics.set_ylabel('Negentropy Value')
        ax_metrics.set_title('Layer-Specific Negentropy Over Time')
        ax_metrics.grid(True, alpha=0.3)
        ax_metrics.legend(loc='upper left')
        
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            print(f"Layer transition plot saved to {output_file}")
            
        if show:
            plt.show()
        else:
            plt.close(fig)
            
    def get_transition_summary(self) -> Dict[str, Any]:
        """
        Get a summary of all layer transitions.
        
        Returns:
            dict: Summary information
        """
        if not self.transition_events:
            return {
                'transitions': [],
                'highest_layer_reached': self.current_layer,
                'total_transitions': 0
            }
            
        # Calculate transition statistics
        transition_times = {}
        for i, event in enumerate(self.transition_events):
            from_layer = event['from_layer']
            to_layer = event['to_layer']
            transition_key = f"{from_layer}_to_{to_layer}"
            
            # Calculate time to this transition
            if i == 0:
                time_to_transition = event['timestep']
            else:
                time_to_transition = event['timestep'] - self.transition_events[i-1]['timestep']
                
            transition_times[transition_key] = time_to_transition
            
        return {
            'transitions': self.transition_events,
            'transition_times': transition_times,
            'highest_layer_reached': self.current_layer,
            'total_transitions': len(self.transition_events),
        }
        
    def predict_next_transition_time(self) -> Dict[str, Any]:
        """
        Predict when the next layer transition might occur.
        
        Returns:
            dict: Prediction information including estimated time to next transition
        """
        # This requires at least one transition to have occurred
        if not self.transition_events:
            return {"prediction": "insufficient data"}
            
        # Get current layer index
        current_idx = self.layer_sequence.index(self.current_layer)
        
        # Check if we're already at the highest layer
        if current_idx >= len(self.layer_sequence) - 1:
            return {"prediction": "highest layer reached"}
            
        # Calculate average transition time from previous transitions
        transition_times = []
        for i, event in enumerate(self.transition_events):
            if i == 0:
                transition_times.append(event['timestep'])
            else:
                transition_times.append(event['timestep'] - self.transition_events[i-1]['timestep'])
                
        avg_transition_time = np.mean(transition_times)
        
        # Get time since last transition
        time_in_current = self.timestep - self.transitions.get(self.current_layer, 0)
        
        # Calculate estimated time remaining
        remaining_time = max(0, avg_transition_time - time_in_current)
        
        # Identify next layer
        next_layer = self.layer_sequence[current_idx + 1]
        
        # Check thresholds for prediction confidence
        transition_key = f"{self.current_layer}_to_{next_layer}"
        confidence = 0.0
        
        if transition_key in self.thresholds:
            thresholds = self.thresholds[transition_key]
            metrics_met = 0
            
            for metric_name, threshold_value in thresholds.items():
                if metric_name in self.history and self.history[metric_name]:
                    current_value = self.history[metric_name][-1]
                    if current_value / threshold_value > 0.5:  # At least halfway to threshold
                        metrics_met += 1
                        
            if thresholds:
                confidence = metrics_met / len(thresholds)
            
        return {
            "next_layer": next_layer,
            "average_transition_time": avg_transition_time,
            "time_in_current_layer": time_in_current,
            "estimated_remaining_time": remaining_time,
            "prediction_confidence": confidence,
            "predicted_timestep": self.timestep + remaining_time
        }