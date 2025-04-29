"""
Recursive Reflection Visualization Module

This module provides visualization tools for understanding the recursive
reflection capabilities of the RECC MVP 1.6 system.
"""

import os
import json
import sys
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Make sure the components directory is in the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.recc_integration import RECC_MVP16

class RecursiveViz:
    """
    Visualization tools for recursive reflection capabilities
    """
    
    def __init__(self, recc=None):
        """Initialize with optional RECC instance"""
        self.recc = recc or RECC_MVP16()
        self.output_dir = "viz_output"
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
    
    def visualize_recursive_depth(self, save=True, show=True):
        """
        Visualize the recursive depth of reflection levels
        
        Args:
            save: Whether to save the visualization to file
            show: Whether to show the visualization
            
        Returns:
            Path to saved file if save=True
        """
        # Get visualization data
        viz_data = self.recc.visualize_recursive_depth()
        
        # Setup figure
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Extract data
        depths = [level['depth'] for level in viz_data['levels']]
        history_entries = [level['history_entries'] for level in viz_data['levels']]
        states = [level['state'] == 'active' for level in viz_data['levels']]
        
        # Create bars for each level
        bar_colors = ['#69b3a2' if state else '#cccccc' for state in states]
        bars = ax.bar(depths, history_entries, color=bar_colors, alpha=0.8)
        
        # Highlight current effective depth
        effective_depth = viz_data['effective_depth']
        ax.axvline(x=effective_depth, color='red', linestyle='--', 
                  linewidth=2, label=f'Effective Depth: {effective_depth}')
        
        # Add labels and title
        ax.set_xlabel('Reflection Level')
        ax.set_ylabel('History Entries')
        ax.set_title('Recursive Reflection Depth')
        
        # Add annotations
        for i, v in enumerate(history_entries):
            ax.text(i, v + 0.5, str(v), ha='center')
            
        # Add legend for active/inactive states
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='#69b3a2', alpha=0.8, label='Active'),
            Patch(facecolor='#cccccc', alpha=0.8, label='Inactive'),
            plt.Line2D([0], [0], color='red', linestyle='--', label=f'Effective Depth: {effective_depth}')
        ]
        ax.legend(handles=legend_elements)
        
        # Add threshold line for cognitive threshold
        ax.axvline(x=3, color='blue', linestyle=':', 
                  linewidth=2, label='Cognitive Threshold')
        
        # Add text annotation for cognitive threshold
        ax.text(3.1, max(history_entries) * 0.8, 'Cognitive Threshold (n ≥ 3)', 
                rotation=90, verticalalignment='center')
        
        # Add cross-level modifications count
        modifications = viz_data['cross_level_modifications']
        plt.figtext(0.02, 0.02, f'Cross-Level Modifications: {modifications}', 
                   fontsize=10, ha='left')
        
        # Add timestamp
        plt.figtext(0.98, 0.02, f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', 
                   fontsize=8, ha='right')
        
        # Adjust layout
        plt.tight_layout()
        
        # Save if requested
        filepath = None
        if save:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filepath = os.path.join(self.output_dir, f'recursive_depth_{timestamp}.png')
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            print(f"Visualization saved to: {filepath}")
        
        # Show if requested
        if show:
            plt.show()
        else:
            plt.close()
            
        return filepath
    
    def visualize_memory_interactions(self, save=True, show=True):
        """
        Visualize memory component interactions
        
        Args:
            save: Whether to save the visualization to file
            show: Whether to show the visualization
            
        Returns:
            Path to saved file if save=True
        """
        # Get memory observability data
        memory_data = self.recc.hybrid_memory.get_observability_data()
        
        # Setup figure
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Visualize memory component sizes
        components = ['Working', 'Reference', 'Procedural', 'Meta']
        sizes = [
            memory_data['working_memory']['item_count'],
            memory_data['reference_memory']['concept_count'] + 
            memory_data['reference_memory']['episode_count'] + 
            memory_data['reference_memory']['theory_count'],
            memory_data['procedural_memory']['strategy_count'],
            memory_data['meta_memory']['level1_observations'] +
            memory_data['meta_memory']['level2_observations'] +
            memory_data['meta_memory']['level3_observations']
        ]
        
        # Create pie chart
        ax1.pie(sizes, labels=components, autopct='%1.1f%%', startangle=90,
               colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
        ax1.axis('equal')
        ax1.set_title('Memory Component Distribution')
        
        # Visualize meta-memory observation levels
        meta_levels = ['Level 1', 'Level 2', 'Level 3']
        meta_counts = [
            memory_data['meta_memory']['level1_observations'],
            memory_data['meta_memory']['level2_observations'],
            memory_data['meta_memory']['level3_observations']
        ]
        
        # Create bar chart for meta-memory levels
        bars = ax2.bar(meta_levels, meta_counts, color='#ffcc99')
        ax2.set_xlabel('Meta-Memory Level')
        ax2.set_ylabel('Observation Count')
        ax2.set_title('Meta-Memory Observation Levels')
        
        # Add annotations
        for i, v in enumerate(meta_counts):
            ax2.text(i, v + 0.5, str(v), ha='center')
        
        # Add emergent properties annotation
        props = memory_data['emergent_properties']
        props_text = '\n'.join([f"{k}: {v:.2f}" for k, v in props.items()])
        plt.figtext(0.5, 0.02, f"Emergent Properties:\n{props_text}", 
                   fontsize=9, ha='center', 
                   bbox=dict(boxstyle="round,pad=0.5", facecolor='lightyellow', alpha=0.5))
        
        # Add timestamp
        plt.figtext(0.98, 0.02, f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', 
                   fontsize=8, ha='right')
        
        # Adjust layout
        plt.tight_layout()
        
        # Save if requested
        filepath = None
        if save:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filepath = os.path.join(self.output_dir, f'memory_interactions_{timestamp}.png')
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            print(f"Visualization saved to: {filepath}")
        
        # Show if requested
        if show:
            plt.show()
        else:
            plt.close()
            
        return filepath
    
    def visualize_performance_metrics(self, metrics=None, save=True, show=True):
        """
        Visualize performance metrics against MVP 1.6 success criteria
        
        Args:
            metrics: Optional performance metrics dict (will get from recc if None)
            save: Whether to save the visualization to file
            show: Whether to show the visualization
            
        Returns:
            Path to saved file if save=True
        """
        # Get metrics if not provided
        if metrics is None:
            metrics = self.recc.get_performance_metrics()
        
        # Define metric info: name, value, target, formatter
        metrics_info = [
            ('Effective\nRecursive Depth', metrics['effective_recursive_depth'], 3.0, lambda x: f"{x:.1f}"),
            ('Self-Model\nStability', metrics['self_model_stability'], 0.8, lambda x: f"{x*100:.1f}%"),
            ('Modification Rate\n(per 100 cycles)', metrics['modification_rate_per_100_cycles'], 10, lambda x: f"{x:.1f}"),
            ('Concept\nHierarchy Depth', metrics['concept_hierarchy_depth'], 3, lambda x: f"{x:.1f}"),
            ('Meta-Strategy\nEvolution', metrics['meta_strategy_evolution'], 0.05, lambda x: f"{x:.3f}")
        ]
        
        # Setup figure
        fig, ax = plt.subplots(figsize=(12, 7))
        
        # Define bars
        metric_names = [info[0] for info in metrics_info]
        values = [info[1] for info in metrics_info]
        targets = [info[2] for info in metrics_info]
        
        # Define bar positions
        x = np.arange(len(metric_names))
        width = 0.35
        
        # Create bars
        value_bars = ax.bar(x - width/2, values, width, label='Current Value', color='#66b3ff')
        target_bars = ax.bar(x + width/2, targets, width, label='Target Value', color='#ff9999', alpha=0.6)
        
        # Add labels
        ax.set_ylabel('Value')
        ax.set_title('MVP 1.6 Performance Metrics')
        ax.set_xticks(x)
        ax.set_xticklabels(metric_names)
        ax.legend()
        
        # Add value annotations
        for i, info in enumerate(metrics_info):
            value, target, formatter = info[1], info[2], info[3]
            # Value annotation
            ax.text(i - width/2, value * 1.05, formatter(value), 
                   ha='center', va='bottom', fontsize=9)
            # Target annotation
            ax.text(i + width/2, target * 1.05, formatter(target), 
                   ha='center', va='bottom', fontsize=9, alpha=0.7)
            
            # Add pass/fail indicator
            passed = value >= target
            color = 'green' if passed else 'red'
            status = "PASS" if passed else "FAIL"
            ax.text(i, max(value, target) * 1.15, status, 
                   ha='center', va='bottom', fontsize=10, 
                   color=color, weight='bold')
        
        # Add cycle count and timestamp
        plt.figtext(0.02, 0.02, f"Cycle Count: {metrics['cycle_count']}", 
                   fontsize=9, ha='left')
        plt.figtext(0.98, 0.02, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 
                   fontsize=8, ha='right')
        
        # Adjust layout
        plt.tight_layout()
        
        # Save if requested
        filepath = None
        if save:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filepath = os.path.join(self.output_dir, f'performance_metrics_{timestamp}.png')
            plt.savefig(filepath, dpi=300, bbox_inches='tight')
            print(f"Visualization saved to: {filepath}")
        
        # Show if requested
        if show:
            plt.show()
        else:
            plt.close()
            
        return filepath

def generate_all_visualizations(recc=None, show=True):
    """
    Generate all visualizations for a RECC instance
    
    Args:
        recc: Optional RECC instance (creates new one if None)
        show: Whether to show visualizations
        
    Returns:
        Dictionary with paths to saved visualizations
    """
    viz = RecursiveViz(recc)
    
    paths = {}
    
    # Generate all visualizations
    paths['recursive_depth'] = viz.visualize_recursive_depth(save=True, show=show)
    paths['memory_interactions'] = viz.visualize_memory_interactions(save=True, show=show)
    paths['performance_metrics'] = viz.visualize_performance_metrics(save=True, show=show)
    
    return paths

if __name__ == "__main__":
    # If run directly, create a RECC instance, run autonomous cycles, and visualize
    recc = RECC_MVP16()
    print("Running 10 autonomous cycles...")
    recc.autonomous_cycle(steps=10)
    print("Generating visualizations...")
    paths = generate_all_visualizations(recc)
    print(f"Visualizations saved to: {os.path.abspath(paths['recursive_depth'])}")