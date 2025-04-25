#!/usr/bin/env python3
"""
Visualization module for Life Origins Simulation.

This module provides visualization capabilities for the simulation,
including molecule positions, compartments, chemical networks,
and various metrics to track the simulation progress.
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import numpy as np
import networkx as nx
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
from collections import defaultdict
import matplotlib.ticker as ticker
import random

# Add the missing function needed by realistic_chemistry.py
def visualize_stability_analysis(analysis_results, output_file=None, show=True):
    """
    Visualize the stability analysis results from a simulation.
    
    Args:
        analysis_results (dict): Results dictionary from analyze_complexity_emergence
        output_file (str): Optional path to save the visualization
        show (bool): Whether to display the plot
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Extract key metrics
    metrics = {
        'Complexity Score': analysis_results.get('complexity_score', 0),
        'Entropy-Catalysis Feedback': analysis_results.get('entropy_catalysis_feedback', 0),
        'Autocatalytic Cycles': analysis_results.get('autocatalytic_cycles', 0),
        'Transfer Entropy': analysis_results.get('transfer_entropy', 0),
        'Information Content': analysis_results.get('information_content', 0),
        'Resilience': analysis_results.get('resilience', 0),
    }
    
    # Create bar chart
    y_pos = np.arange(len(metrics))
    values = list(metrics.values())
    
    # Use different colors for different metric types
    colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan']
    
    # Create horizontal bar chart
    bars = ax.barh(y_pos, values, align='center', color=colors, alpha=0.7)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(list(metrics.keys()))
    ax.invert_yaxis()  # Labels read top-to-bottom
    ax.set_xlabel('Value')
    ax.set_title('Simulation Stability Analysis')
    
    # Add values as text labels
    for i, v in enumerate(values):
        ax.text(v + 0.1, i, f"{v:.3f}", va='center')
    
    # Add a threshold line for significant values
    ax.axvline(x=0.5, color='gray', linestyle='--', alpha=0.7, label='Significance Threshold')
    
    # Add annotations for significant emergent properties
    thresholds = analysis_results.get('emergence_thresholds', [])
    if thresholds:
        threshold_text = "Emergent properties detected:\n- " + "\n- ".join(thresholds)
        ax.text(0.02, 0.02, threshold_text, transform=ax.transAxes, 
              bbox=dict(facecolor='white', alpha=0.7))
    
    plt.tight_layout()
    
    if output_file:
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"Stability analysis visualization saved to {output_file}")
    
    if show:
        plt.show()
    else:
        plt.close(fig)
    
    return fig

class SimulationVisualization:
    """Handles visualization of the Life Origins Simulation."""
    
    def __init__(self, width=10, height=10, dpi=100):
        """
        Initialize the visualization.
        
        Args:
            width (int): Width of the figure in inches
            height (int): Height of the figure in inches
            dpi (int): Dots per inch for the figure
        """
        self.width = width
        self.height = height
        self.dpi = dpi
        
        # Create figure with subplots
        self.fig = plt.figure(figsize=(width, height), dpi=dpi)
        
        # Color maps
        self.molecule_colors = {}
        self.compartment_cmap = LinearSegmentedColormap.from_list('compartment_cmap', 
                                                               ['red', 'yellow', 'green'])
        
        # Animation
        self.animation = None
        self.time_text = None
        
        # Tracking
        self.compartment_tracking = []
        
    def setup_plot_layout(self, focus_compartments=False, detailed_visualization=False):
        """Set up the layout of subplots."""
        # Clear any existing plots
        self.fig.clear()
        
        # Determine layout based on focus
        if focus_compartments:
            # Layout optimized for compartment visualization
            gs = self.fig.add_gridspec(3, 4)
            
            # Main simulation view (larger)
            self.sim_axes = self.fig.add_subplot(gs[0:2, 0:3])
            self.sim_axes.set_title("Compartment Formation Simulation")
            
            # Compartment metrics panel (prominent)
            self.compartment_axes = self.fig.add_subplot(gs[0, 3])
            self.compartment_axes.set_title("Compartment Stats")
            
            # Molecule panel (smaller)
            self.molecule_axes = self.fig.add_subplot(gs[1, 3])
            self.molecule_axes.set_title("Amphiphilic Molecules")
            
            # Network view (below)
            self.network_axes = self.fig.add_subplot(gs[2, 0:2])
            self.network_axes.set_title("Reaction Network")
            self.network_axes.set_xticks([])
            self.network_axes.set_yticks([])
            
            # Metrics panel
            self.metrics_axes = self.fig.add_subplot(gs[2, 2:])
            self.metrics_axes.set_title("Key Metrics")
            
            # Environment and info panels are hidden in compartment focus mode
            self.env_axes = None
            self.info_axes = None
        else:
            # Standard layout (more balanced)
            gs = self.fig.add_gridspec(3, 4)
            
            # Main layout grid
            self.sim_axes = self.fig.add_subplot(gs[0:2, 0:2])
            self.sim_axes.set_title("Life Origins Simulation")
            self.sim_axes.set_xlabel("X")
            self.sim_axes.set_ylabel("Y")
            self.sim_axes.set_xlim(0, 1)
            self.sim_axes.set_ylim(0, 1)
            
            # Reaction network graph
            self.network_axes = self.fig.add_subplot(gs[0, 2:4])
            self.network_axes.set_title("Reaction Network")
            self.network_axes.set_xticks([])
            self.network_axes.set_yticks([])
            
            # Molecule counts bar chart
            self.molecule_axes = self.fig.add_subplot(gs[1, 2])
            self.molecule_axes.set_title("Molecule Counts")
            self.molecule_axes.set_ylabel("Count")
            
            # Compartment counts/stats
            self.compartment_axes = self.fig.add_subplot(gs[1, 3])
            self.compartment_axes.set_title("Compartment Stats")
            
            # Environmental conditions
            self.env_axes = self.fig.add_subplot(gs[2, 0])
            self.env_axes.set_title("Environment")
            self.env_axes.set_xticks([])
            self.env_axes.set_yticks([])
            
            # Entropy catalysis metrics over time
            self.metrics_axes = self.fig.add_subplot(gs[2, 1:3])
            self.metrics_axes.set_title("Entropy & Catalysis")
            self.metrics_axes.set_xlabel("Time Steps")
            self.metrics_axes.set_ylabel("Value")
            
            # Information panel (text)
            self.info_axes = self.fig.add_subplot(gs[2, 3])
            self.info_axes.set_title("Information")
            self.info_axes.set_xticks([])
            self.info_axes.set_yticks([])
        
        # Set up the simulation space
        self.sim_axes.set_xlim(0, 1)
        self.sim_axes.set_ylim(0, 1)
        
        # Text for time step display
        self.time_text = self.fig.text(0.5, 0.01, "Time Step: 0", ha='center')
        
        # Add detailed tracking elements if needed
        if detailed_visualization:
            self.compartment_tracking = []
            
        # Adjust layout
        self.fig.tight_layout(rect=[0, 0.03, 1, 0.97])
    
    def init_animation(self):
        """Initialize empty plots for animation."""
        # Clear all axes
        self.sim_axes.clear()
        if self.network_axes:
            self.network_axes.clear()
        self.molecule_axes.clear()
        self.compartment_axes.clear()
        if self.env_axes:
            self.env_axes.clear()
        self.metrics_axes.clear()
        if self.info_axes:
            self.info_axes.clear()
        
        # Reset axes
        self.sim_axes.set_title("Life Origins Simulation")
        self.sim_axes.set_xlim(0, 1)
        self.sim_axes.set_ylim(0, 1)
        
        if self.network_axes:
            self.network_axes.set_title("Reaction Network")
            self.network_axes.set_xticks([])
            self.network_axes.set_yticks([])
        
        self.molecule_axes.set_title("Molecule Counts")
        
        self.compartment_axes.set_title("Compartment Stats")
        
        if self.env_axes:
            self.env_axes.set_title("Environment")
            self.env_axes.set_xticks([])
            self.env_axes.set_yticks([])
        
        self.metrics_axes.set_title("Entropy & Catalysis")
        self.metrics_axes.set_xlabel("Time Steps")
        self.metrics_axes.set_ylabel("Value")
        
        if self.info_axes:
            self.info_axes.set_title("Information")
            self.info_axes.set_xticks([])
            self.info_axes.set_yticks([])
        
        # Return empty artists
        return []
        
    def update_animation(self, frame, simulation, environment, focus_compartments=False):
        """
        Update the animation frame with current simulation state.
        
        Args:
            frame (int): Current frame number
            simulation (object): The simulation object
            environment (object): The environment object
            focus_compartments (bool): Whether to focus on compartment visualization
        """
        time_step = frame
        
        # Update time step text
        self.time_text.set_text(f"Time Step: {time_step}")
        
        # Update simulation space plot
        self._update_simulation_space(simulation, focus_compartments)
        
        # Update reaction network if available
        if self.network_axes:
            self._update_reaction_network(simulation, focus_on_compartments=focus_compartments)
        
        # Update molecule counts - focused on amphiphilic if in compartment mode
        self._update_molecule_counts(simulation, focus_amphiphilic=focus_compartments)
        
        # Update compartment stats with extra detail if in compartment mode
        self._update_compartment_stats(simulation, detailed=focus_compartments)
        
        # Update environment visualization if available
        if self.env_axes:
            self._update_environment(environment)
        
        # Update metrics over time - focused on compartment metrics if in compartment mode
        self._update_metrics(simulation, focus_compartments=focus_compartments)
        
        # Update information panel if available
        if self.info_axes:
            self._update_information(simulation, environment)
            
        # Track compartment data for analysis
        self._track_compartment_data(simulation, time_step)
        
        return []
    
    def _track_compartment_data(self, simulation, time_step):
        """Track compartment data for later analysis."""
        # Get compartment data
        compartment_count = len(simulation.compartments) if hasattr(simulation, 'compartments') else 0
        
        # Count amphiphilic molecules
        amphiphilic_count = sum(1 for mol in simulation.molecules.keys() 
                              if hasattr(mol, 'is_amphiphilic') and mol.is_amphiphilic)
        
        # Track compartment positions and sizes if they exist
        compartment_positions = []
        if compartment_count > 0:
            for comp in simulation.compartments:
                compartment_positions.append({
                    'position': comp.position,
                    'radius': comp.radius,
                    'stability': getattr(comp, 'stability', 0.5),
                    'age': getattr(comp, 'age', 0)
                })
        
        # Save data
        self.compartment_tracking.append({
            'time_step': time_step,
            'compartment_count': compartment_count,
            'amphiphilic_count': amphiphilic_count,
            'compartment_positions': compartment_positions,
            'feedback_coefficient': simulation.calculate_feedback_coefficient() 
                                   if hasattr(simulation, 'calculate_feedback_coefficient') else 0
        })
    
    def _update_simulation_space(self, simulation, focus_compartments=False):
        """Update the main simulation space visualization."""
        self.sim_axes.clear()
        self.sim_axes.set_title("Life Origins Simulation" if not focus_compartments else "Compartment Formation")
        self.sim_axes.set_xlim(0, 1)
        self.sim_axes.set_ylim(0, 1)
        
        # Plot molecules with appropriate styling
        x_coords = []
        y_coords = []
        colors = []
        sizes = []
        molecule_types = []
        
        for molecule, count in simulation.molecules.items():
            if count > 0:
                # Get or assign color for this molecule type
                if molecule.name not in self.molecule_colors:
                    # Assign color based on molecular properties
                    if getattr(molecule, 'is_amphiphilic', False):
                        self.molecule_colors[molecule.name] = 'blue'
                    else:
                        # Color based on complexity
                        if molecule.complexity < 3:
                            self.molecule_colors[molecule.name] = 'lightgray'
                        elif molecule.complexity < 10:
                            self.molecule_colors[molecule.name] = 'lightgreen'
                        else:
                            self.molecule_colors[molecule.name] = 'darkgreen'
                
                # Use more vibrant colors for amphiphilic molecules in compartment focus mode
                if focus_compartments and getattr(molecule, 'is_amphiphilic', False):
                    self.molecule_colors[molecule.name] = 'deepskyblue'
                
                # Add molecule(s) to plot - represent counts as clustered dots
                base_x, base_y = molecule.position
                for i in range(min(count, 10)):  # Limit to 10 dots per molecule type
                    # Add slight jitter for multiple molecules of same type
                    if i > 0:
                        jitter = 0.01
                        x = base_x + random.uniform(-jitter, jitter)
                        y = base_y + random.uniform(-jitter, jitter)
                    else:
                        x, y = base_x, base_y
                    
                    x_coords.append(x)
                    y_coords.append(y)
                    colors.append(self.molecule_colors[molecule.name])
                    
                    # Size based on complexity, but make amphiphilic molecules more visible
                    size = max(20, min(100, molecule.complexity * 10))
                    if getattr(molecule, 'is_amphiphilic', False):
                        size *= 1.5  # Make amphiphilic molecules more noticeable
                    sizes.append(size)
                    molecule_types.append(molecule.name)
                
        # Plot the molecules
        if x_coords:
            scatter = self.sim_axes.scatter(x_coords, y_coords, c=colors, s=sizes, alpha=0.6)
            
            # Add legend if in compartment focus mode and not too many molecule types
            if focus_compartments:
                unique_molecules = set(molecule_types)
                if len(unique_molecules) < 10:
                    handles = []
                    labels = []
                    for molecule_name in unique_molecules:
                        handles.append(plt.Line2D([0], [0], marker='o', color='w', 
                                              markerfacecolor=self.molecule_colors[molecule_name], 
                                              markersize=8))
                        labels.append(molecule_name)
                    self.sim_axes.legend(handles, labels, loc='upper right', fontsize='x-small')
            
        # Plot compartments with enhanced visualization
        for compartment in simulation.compartments:
            # Draw compartment membrane with color based on stability
            stability = getattr(compartment, 'stability', 0.5)
            color = self.compartment_cmap(stability)
            
            if focus_compartments:
                # Draw a more detailed compartment
                # 1. Outer membrane
                outer_circle = plt.Circle(compartment.position, compartment.radius, 
                                        color=color, 
                                        fill=False, linewidth=2.5, alpha=0.9)
                self.sim_axes.add_patch(outer_circle)
                
                # 2. Inner fill with transparency
                inner_circle = plt.Circle(compartment.position, compartment.radius * 0.95, 
                                        color=color, alpha=0.1)
                self.sim_axes.add_patch(inner_circle)
                
                # 3. Add a label with the compartment's age or ID
                comp_id = getattr(compartment, 'id', '')
                age = getattr(compartment, 'age', 0)
                label = f"{comp_id}" if comp_id else f"Age: {age}"
                self.sim_axes.text(compartment.position[0], compartment.position[1], 
                                 label, ha='center', va='center', fontsize=8,
                                 color='black', fontweight='bold')
                
            else:
                # Standard compartment visualization
                circle = plt.Circle(compartment.position, compartment.radius, 
                                 color=color, 
                                 fill=False, linewidth=2, alpha=0.7)
                self.sim_axes.add_patch(circle)
            
            # Add a small dot at the center of the compartment
            self.sim_axes.scatter([compartment.position[0]], [compartment.position[1]], 
                               c='black', s=5, alpha=1.0)
    
    def _update_reaction_network(self, simulation, focus_on_compartments=False):
        """Update the reaction network visualization."""
        self.network_axes.clear()
        self.network_axes.set_title("Reaction Network")
        self.network_axes.set_xticks([])
        self.network_axes.set_yticks([])
        
        # Get only active molecules (that exist in the system)
        active_molecules = {m for m, c in simulation.molecules.items() if c > 0}
        
        if not active_molecules:
            self.network_axes.text(0.5, 0.5, "No active molecules", 
                                ha='center', va='center')
            return
            
        # Create a subgraph of the reaction network with only active molecules
        subgraph = nx.DiGraph()
        
        # Add nodes
        for molecule in active_molecules:
            complexity = molecule.complexity
            
            # Node size: base on complexity but highlight amphiphilic molecules
            if focus_on_compartments and getattr(molecule, 'is_amphiphilic', False):
                size = 300 + 50 * np.log1p(complexity)  # Much larger for amphiphilic in compartment mode
                color = 'blue'
            else:
                size = 100 + 50 * np.log1p(complexity)
                
                if getattr(molecule, 'is_amphiphilic', False):
                    color = 'blue'
                else:
                    # Color based on complexity
                    if complexity < 3:
                        color = 'lightgray'
                    elif complexity < 10:
                        color = 'lightgreen'
                    else:
                        color = 'darkgreen'
                
            subgraph.add_node(molecule.name, size=size, color=color, 
                             is_amphiphilic=getattr(molecule, 'is_amphiphilic', False),
                             complexity=complexity)
        
        # Add edges from reactions
        for reaction in simulation.reactions:
            # Only include reactions where all reactants and products exist
            if (all(r in active_molecules for r in reaction.reactants) and
                all(p in active_molecules for p in reaction.products)):
                
                for reactant in reaction.reactants:
                    for product in reaction.products:
                        if reactant.name in subgraph and product.name in subgraph:
                            width = 1.0
                            # Emphasize catalyzed reactions
                            if reaction.is_catalyzed:
                                width = 2.5
                            # Further emphasize reactions involving amphiphilic molecules
                            if (focus_on_compartments and 
                                (getattr(reactant, 'is_amphiphilic', False) or 
                                 getattr(product, 'is_amphiphilic', False))):
                                width *= 2
                            subgraph.add_edge(reactant.name, product.name, 
                                             weight=reaction.effective_rate*100,
                                             width=width,
                                             is_catalyzed=reaction.is_catalyzed)
        
        if not subgraph.nodes():
            self.network_axes.text(0.5, 0.5, "No active reactions", 
                                ha='center', va='center')
            return
        
        # Create positions using a spring layout
        try:
            # For compartment focus mode, try to place amphiphilic molecules centrally
            if focus_on_compartments:
                # First identify amphiphilic molecules
                amphiphilic_nodes = [n for n in subgraph.nodes() 
                                   if subgraph.nodes[n].get('is_amphiphilic', False)]
                
                # Create fixed positions for amphiphilic molecules in a central cluster
                fixed_positions = {}
                if amphiphilic_nodes:
                    for i, node in enumerate(amphiphilic_nodes):
                        angle = 2 * np.pi * i / len(amphiphilic_nodes)
                        fixed_positions[node] = (0.5 + 0.2 * np.cos(angle), 
                                               0.5 + 0.2 * np.sin(angle))
                    
                # Use spring layout with fixed positions for amphiphilic molecules
                pos = nx.spring_layout(subgraph, k=0.15, iterations=50, 
                                     seed=42, fixed=fixed_positions.keys(),
                                     pos=fixed_positions)
            else:
                # Standard spring layout for general view
                pos = nx.spring_layout(subgraph, k=0.15, iterations=20, seed=42)
            
            # Get node attributes
            node_sizes = [subgraph.nodes[node]['size'] for node in subgraph.nodes()]
            node_colors = [subgraph.nodes[node]['color'] for node in subgraph.nodes()]
            
            # Draw nodes
            nx.draw_networkx_nodes(subgraph, pos, 
                                 node_size=node_sizes,
                                 node_color=node_colors,
                                 alpha=0.8,
                                 ax=self.network_axes)
            
            # Get edge attributes
            edge_widths = [subgraph.edges[edge]['width'] for edge in subgraph.edges()]
            edge_colors = ['red' if subgraph.edges[edge]['is_catalyzed'] else 'gray' 
                         for edge in subgraph.edges()]
            
            # Draw edges
            nx.draw_networkx_edges(subgraph, pos,
                                width=edge_widths,
                                edge_color=edge_colors,
                                alpha=0.6,
                                arrows=True,
                                arrowstyle='-|>',
                                arrowsize=10,
                                ax=self.network_axes)
            
            # Draw labels for important nodes
            if focus_on_compartments:
                # In compartment mode, label amphiphilic molecules and high complexity
                labels = {node: node for node in subgraph.nodes() 
                        if (subgraph.nodes[node].get('is_amphiphilic', False) or
                            subgraph.nodes[node]['complexity'] > 5)}
            else:
                # In standard mode, label nodes with complexity > 2
                labels = {node: node for node in subgraph.nodes() 
                        if subgraph.nodes[node]['complexity'] > 2}
                
            nx.draw_networkx_labels(subgraph, pos, labels=labels, font_size=8, 
                                  ax=self.network_axes)
            
            # Add title with network stats
            amphiphilic_count = sum(1 for n in subgraph.nodes 
                                  if subgraph.nodes[n].get('is_amphiphilic', False))
            catalyzed_edges = sum(1 for e in subgraph.edges 
                                if subgraph.edges[e]['is_catalyzed'])
            
            if focus_on_compartments:
                title = f"Reaction Network: {amphiphilic_count} amphiphilic, {catalyzed_edges} catalyzed"
            else:
                title = f"Reaction Network: {len(subgraph.nodes)} molecules, {len(subgraph.edges)} reactions"
                
            self.network_axes.set_title(title, fontsize=10)
            
        except Exception as e:
            self.network_axes.text(0.5, 0.5, f"Network visualization error: {str(e)}", 
                                ha='center', va='center')
    
    def _update_molecule_counts(self, simulation, focus_amphiphilic=False):
        """Update the molecule counts bar chart."""
        self.molecule_axes.clear()
        
        if focus_amphiphilic:
            self.molecule_axes.set_title("Amphiphilic Molecules")
        else:
            self.molecule_axes.set_title("Molecule Counts")
        
        # Get molecules with non-zero counts
        molecules = [(m, c) for m, c in simulation.molecules.items() if c > 0]
        
        # Handle the case where we want to focus on amphiphilic molecules
        if focus_amphiphilic:
            # Filter to only show amphiphilic molecules
            amphiphilic_molecules = [
                (m, c) for m, c in molecules 
                if getattr(m, 'is_amphiphilic', False)
            ]
            
            if not amphiphilic_molecules:
                self.molecule_axes.text(0.5, 0.5, "No amphiphilic molecules present", 
                                     ha='center', va='center')
                return
                
            molecules = amphiphilic_molecules
        
        # Sort by complexity
        molecules.sort(key=lambda x: x[0].complexity)
        
        # If we have too many molecules, show only the top molecules by count
        limit = 5 if focus_amphiphilic else 10
        if len(molecules) > limit:
            molecules.sort(key=lambda x: x[1], reverse=True)
            molecules = molecules[:limit]
            
        if not molecules:
            self.molecule_axes.text(0.5, 0.5, "No molecules present", 
                                 ha='center', va='center')
            return
            
        # Extract names, counts, and properties
        names = [m[0].name for m in molecules]
        counts = [m[1] for m in molecules]
        colors = []
        
        for m, _ in molecules:
            if getattr(m, 'is_amphiphilic', False):
                # Use darker blue for amphiphilic in focused mode
                colors.append('deepskyblue' if focus_amphiphilic else 'blue')
            else:
                # Standard coloring based on complexity
                if m.complexity < 3:
                    colors.append('lightgray')
                elif m.complexity < 10:
                    colors.append('lightgreen')
                else:
                    colors.append('darkgreen')
        
        # Create bar chart
        bars = self.molecule_axes.bar(names, counts, color=colors)
        
        # Add complexity labels in amphiphilic focus mode
        if focus_amphiphilic:
            for i, (m, c) in enumerate(molecules):
                self.molecule_axes.text(
                    i, c + max(counts) * 0.05, 
                    f"C:{m.complexity:.1f}", 
                    ha='center', rotation=0, fontsize=8
                )
        
        # Rotate x labels if needed
        if len(names) > 5:
            self.molecule_axes.set_xticks(range(len(names)))
            self.molecule_axes.set_xticklabels(names, rotation=45, ha='right', fontsize=8)
        
        self.molecule_axes.set_ylabel("Count")
        
        # Add some margin at the top
        self.molecule_axes.set_ylim(0, max(counts) * 1.2)
    
    def _update_compartment_stats(self, simulation, detailed=False):
        """Update the compartment statistics visualization."""
        self.compartment_axes.clear()
        self.compartment_axes.set_title("Compartment Stats")
        
        if not simulation.compartments:
            self.compartment_axes.text(0.5, 0.5, "No compartments present", 
                                    ha='center', va='center')
            return
        
        # Calculate compartment statistics
        count = len(simulation.compartments)
        radii = [c.radius for c in simulation.compartments]
        avg_size = np.mean(radii)
        avg_stability = np.mean([getattr(c, 'stability', 0.5) for c in simulation.compartments])
        avg_age = np.mean([getattr(c, 'age', 0) for c in simulation.compartments])
        
        if detailed:
            # In detailed mode, show more comprehensive information
            # Create a table layout
            data = [
                ["Count", f"{count}"],
                ["Avg Size", f"{avg_size:.3f}"],
                ["Avg Stability", f"{avg_stability:.3f}"],
                ["Avg Age", f"{avg_age:.1f}"],
                ["Size Range", f"{min(radii):.3f} - {max(radii):.3f}"]
            ]
            
            # Add contents information if available
            if hasattr(simulation.compartments[0], 'contents'):
                total_molecules = sum(len(getattr(c, 'contents', [])) for c in simulation.compartments)
                avg_molecules = total_molecules / count
                data.append(["Total Molecules", f"{total_molecules}"])
                data.append(["Avg Molecules", f"{avg_molecules:.1f}"])
                
                # Count catalysts inside compartments if available
                catalysts = sum(sum(1 for m in getattr(c, 'contents', []) 
                                  if getattr(m, 'is_catalyst', False))
                             for c in simulation.compartments)
                if catalysts > 0:
                    data.append(["Catalysts", f"{catalysts}"])
            
            # Create table
            table = self.compartment_axes.table(
                cellText=data,
                loc='center',
                cellLoc='center',
                colWidths=[0.5, 0.5]
            )
            table.auto_set_font_size(False)
            table.set_fontsize(9)
            table.scale(1, 1.5)
            
            # Color code the table rows based on values
            for i in range(len(data)):
                table[(i, 0)].set_facecolor('lightgray')
                # Color code values based on their quality
                if i == 2:  # Stability row
                    if avg_stability > 0.7:
                        table[(i, 1)].set_facecolor('lightgreen')
                    elif avg_stability < 0.3:
                        table[(i, 1)].set_facecolor('lightcoral')
            
            # Remove axes
            self.compartment_axes.set_xticks([])
            self.compartment_axes.set_yticks([])
            
            # Add annotations
            if count > 1:
                self.compartment_axes.set_title(f"Compartment Analysis ({count} compartments)")
            else:
                self.compartment_axes.set_title("Compartment Analysis (1 compartment)")
                
        else:
            # Standard view with horizontal bars
            metrics = ['Count', 'Avg Size', 'Avg Stability', 'Avg Age']
            values = [count, avg_size, avg_stability, avg_age]
            
            # Normalize values to 0-1 for display
            norm_values = [
                count / max(10, count),  # Max expected count
                avg_size / 0.2,  # Max expected size
                avg_stability,  # Already 0-1
                avg_age / max(100, avg_age)  # Normalize age
            ]
            
            # Plot bars
            bars = self.compartment_axes.barh(metrics, norm_values, color='skyblue')
            
            # Add actual values as text
            for i, v in enumerate(values):
                if i == 0:  # Count is integer
                    self.compartment_axes.text(norm_values[i] + 0.05, i, f"{int(v)}", 
                                            va='center')
                else:
                    self.compartment_axes.text(norm_values[i] + 0.05, i, f"{v:.2f}", 
                                            va='center')
            
            # Set limits
            self.compartment_axes.set_xlim(0, 1.3)
            
            # Axes formatting
            self.compartment_axes.set_xticks([])
    
    def _update_environment(self, environment):
        """Update the environment visualization."""
        self.env_axes.clear()
        self.env_axes.set_title("Environment")
        self.env_axes.set_xticks([])
        self.env_axes.set_yticks([])
        
        env_data = environment.get_visualization_data()
        
        # Create a text summary of the environment
        env_text = (
            f"Type: {env_data['type']}\n"
            f"Temp: {env_data['temperature']:.1f}°C\n"
            f"pH: {env_data['ph']:.1f}\n"
            f"UV: {env_data['uv']:.2f}\n"
            f"{'WET' if env_data['is_wet'] else 'DRY'} ({env_data['wet_phase']:.2f})\n"
            f"Constraint: {env_data['constraint_level']}"
        )
        
        # Draw as text block
        self.env_axes.text(0.5, 0.5, env_text, 
                        ha='center', va='center', 
                        bbox=dict(boxstyle="round,pad=0.5", 
                                 fc="lightyellow", 
                                 ec="orange", 
                                 lw=1))
    
    def _update_metrics(self, simulation, focus_compartments=False):
        """Update the metrics plots showing entropy reduction and catalytic activity over time."""
        self.metrics_axes.clear()
        
        if focus_compartments:
            self.metrics_axes.set_title("Compartment Formation Metrics")
        else:
            self.metrics_axes.set_title("Entropy & Catalysis")
        
        # Get metrics data
        time_steps = range(len(simulation.metrics['entropy_reduction']))
        entropy_reduction = simulation.metrics['entropy_reduction']
        catalytic_activity = simulation.metrics['catalytic_activity']
        complexity = simulation.metrics['molecular_complexity']
        
        if not time_steps:
            self.metrics_axes.text(0.5, 0.5, "No metrics data yet", 
                                ha='center', va='center')
            return
        
        # Plot metrics with appropriate focus
        if focus_compartments:
            # When focusing on compartments, emphasize compartment stats
            # Plot compartment count if available
            if simulation.metrics['compartment_count']:
                comp_steps = range(len(simulation.metrics['compartment_count']))
                self.metrics_axes.plot(comp_steps, simulation.metrics['compartment_count'], 
                                     'b-', label='Compartment Count', linewidth=3)
                
                # Plot compartment stability if available
                if simulation.metrics['avg_stability'] and len(simulation.metrics['avg_stability']) > 0:
                    stab_steps = range(len(simulation.metrics['avg_stability']))
                    stability_values = [s if s is not None else 0 for s in simulation.metrics['avg_stability']]
                    if len(stab_steps) == len(stability_values) and len(stability_values) > 0:
                        # Scale stability to be visible on same axis
                        max_count = max(max(simulation.metrics['compartment_count']), 1)
                        scaled_stability = [s * max_count for s in stability_values]
                        self.metrics_axes.plot(stab_steps, scaled_stability, 
                                            'g-', label='Stability (scaled)', alpha=0.7)
            
            # Still plot catalyst activity for context
            self.metrics_axes.plot(time_steps, catalytic_activity, 'r-', 
                                label='Catalytic Activity', alpha=0.5)
                
            # Add amphiphilic molecule count to the graph
            amphiphilic_count = []
            for t in time_steps:
                count = sum(1 for mol, c in list(simulation.molecules.items()) 
                          if c > 0 and getattr(mol, 'is_amphiphilic', False))
                amphiphilic_count.append(count)
            
            if amphiphilic_count:
                # Get the maximum compartment count safely
                max_comp_count = 1
                if simulation.metrics['compartment_count'] and len(simulation.metrics['compartment_count']) > 0:
                    max_comp_count = max(1, max(simulation.metrics['compartment_count']))
                
                # Scale amphiphilic count to be visible
                scale_factor = max_comp_count / max(1, max(amphiphilic_count))
                scaled_amphiphilic = [c * scale_factor for c in amphiphilic_count]
                self.metrics_axes.plot(time_steps, scaled_amphiphilic, 
                                    'c--', label='Amphiphilic (scaled)', alpha=0.7)
        else:
            # Standard metrics view
            self.metrics_axes.plot(time_steps, entropy_reduction, 'g-', 
                                label='Entropy Reduction', alpha=0.7)
            self.metrics_axes.plot(time_steps, catalytic_activity, 'r-', 
                                label='Catalytic Activity', alpha=0.7)
            self.metrics_axes.plot(time_steps, complexity, 'b-', 
                                label='Avg. Complexity', alpha=0.7)
            
            # Also plot compartment count if available and non-zero
            if (simulation.metrics['compartment_count'] and 
                any(c > 0 for c in simulation.metrics['compartment_count'])):
                comp_steps = range(len(simulation.metrics['compartment_count']))
                self.metrics_axes.plot(comp_steps, simulation.metrics['compartment_count'], 
                                    'm-', label='Compartments', alpha=0.7)
        
        # Add feedback coefficient as text
        feedback_coef = simulation.calculate_feedback_coefficient()
        self.metrics_axes.text(0.02, 0.95, f"Feedback: {feedback_coef:.2f}", 
                            transform=self.metrics_axes.transAxes)
        
        # Axes formatting
        self.metrics_axes.set_xlabel("Time Steps")
        self.metrics_axes.set_ylabel("Value")
        self.metrics_axes.legend(loc='upper right', fontsize='x-small')
        
        # If we have a lot of time steps, only show a subset of x-ticks
        if len(time_steps) > 10:
            step = max(1, len(time_steps) // 10)
            self.metrics_axes.set_xticks(time_steps[::step])
        
        # Set y-limits based on what we're plotting
        if focus_compartments:
            max_value = 0
            for metric in [simulation.metrics['compartment_count'], 
                          catalytic_activity]:
                if metric and any(metric):
                    max_value = max(max_value, max(metric))
            self.metrics_axes.set_ylim(0, max_value * 1.2)
        else:
            self.metrics_axes.set_ylim(0, max(max(entropy_reduction or [0]), 
                                       max(catalytic_activity or [0]), 
                                       max(complexity or [0])) * 1.1)
    
    def _update_information(self, simulation, environment):
        """Update the information panel with key insights and system state."""
        self.info_axes.clear()
        self.info_axes.set_title("Information")
        self.info_axes.set_xticks([])
        self.info_axes.set_yticks([])
        
        # Count total molecules
        total_molecules = sum(simulation.molecules.values())
        
        # Get molecule diversity (unique types)
        molecule_diversity = sum(1 for _, count in simulation.molecules.items() if count > 0)
        
        # Get compartment count
        compartment_count = len(simulation.compartments)
        
        # Calculate catalytic ratio
        catalyst_count = sum(1 for reaction in simulation.reactions if reaction.is_catalyzed)
        catalytic_ratio = catalyst_count / max(1, len(simulation.reactions))
        
        # Calculate entropy reduction efficiency
        if simulation.metrics['entropy_reduction']:
            avg_entropy_reduction = np.mean(simulation.metrics['entropy_reduction'][-10:])
        else:
            avg_entropy_reduction = 0
            
        # Create information text
        info_text = (
            f"Time Step: {simulation.time_step}\n"
            f"Total Molecules: {total_molecules}\n"
            f"Molecule Types: {molecule_diversity}\n"
            f"Compartments: {compartment_count}\n"
            f"Catalyzed Reactions: {catalyst_count}\n"
            f"Catalytic Ratio: {catalytic_ratio:.2f}\n"
            f"Entropy Reduction: {avg_entropy_reduction:.2f}\n"
            f"Feedback Coef: {simulation.calculate_feedback_coefficient():.2f}\n"
        )
        
        # Highlight key insights
        insights = []
        
        # Check for emergence of catalysis
        if catalyst_count > 0 and simulation.time_step < 100:
            insights.append("Early catalysis emerged!")
            
        # Check for emergence of compartments
        if compartment_count > 0:
            if len(simulation.metrics['compartment_count']) > 10:
                if np.mean(simulation.metrics['compartment_count'][-10:-5]) < compartment_count:
                    insights.append("Compartments increasing!")
                    
        # Check for increasing molecular complexity
        if len(simulation.metrics['molecular_complexity']) > 10:
            recent_complexity = np.mean(simulation.metrics['molecular_complexity'][-5:])
            earlier_complexity = np.mean(simulation.metrics['molecular_complexity'][-10:-5])
            if recent_complexity > earlier_complexity * 1.2:
                insights.append("Complexity increasing!")
                
        # Check for strong feedback loop formation
        feedback = simulation.calculate_feedback_coefficient()
        if feedback > 0.7:
            insights.append("Strong feedback detected!")
            
        # Add insights to the text
        if insights:
            info_text += "\nKey Insights:\n- " + "\n- ".join(insights)
        
        # Draw as text block with color based on complexity
        if np.mean(simulation.metrics['molecular_complexity'][-5:] if simulation.metrics['molecular_complexity'] else [0]) > 5:
            box_color = 'lightgreen'
            edge_color = 'green'
        else:
            box_color = 'white'
            edge_color = 'gray'
            
        self.info_axes.text(0.5, 0.5, info_text, 
                         ha='center', va='center', 
                         bbox=dict(boxstyle="round,pad=0.5", 
                                 fc=box_color, 
                                 ec=edge_color, 
                                 lw=1))
    
    def start_animation(self, simulation, environment, frames=100, interval=200):
        """
        Start the animation of the simulation.
        
        Args:
            simulation: The simulation object
            environment: The environment object
            frames (int): Number of frames to run
            interval (int): Interval between frames in milliseconds
        """
        self.animation = animation.FuncAnimation(
            self.fig, 
            self.update_animation,
            frames=frames,
            interval=interval,
            fargs=(simulation, environment),
            init_func=self.init_animation,
            blit=False
        )
        plt.show()
    
    def save_animation(self, filename, fps=5):
        """
        Save the animation to a file.
        
        Args:
            filename (str): Output filename
            fps (int): Frames per second
        """
        if self.animation:
            self.animation.save(filename, fps=fps)
            print(f"Animation saved to {filename}")
        else:
            print("No animation to save. Run start_animation first.")
    
    def save_current_frame(self, filename, dpi=300):
        """
        Save the current frame as an image.
        
        Args:
            filename (str): Output filename
            dpi (int): DPI for the output image
        """
        self.fig.savefig(filename, dpi=dpi, bbox_inches='tight')
        print(f"Current frame saved to {filename}")
        
    def generate_compartment_evolution_animation(self, output_filename=None):
        """
        Generate an animation showing the evolution of compartments over time.
        """
        if not self.compartment_tracking or not any(t['compartment_count'] > 0 for t in self.compartment_tracking):
            print("No compartment data to visualize")
            return
            
        # Create a new figure for the animation
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_title("Compartment Evolution Over Time")
        
        # Function to update the animation
        def update(frame):
            ax.clear()
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            
            data = self.compartment_tracking[frame]
            time_step = data['time_step']
            compartment_count = data['compartment_count']
            
            ax.set_title(f"Compartment Evolution - Step {time_step}, Count: {compartment_count}")
            
            # Draw compartments
            for comp in data['compartment_positions']:
                circle = plt.Circle(comp['position'], comp['radius'], 
                                  color=self.compartment_cmap(comp['stability']), 
                                  fill=False, linewidth=2, alpha=0.8)
                ax.add_patch(circle)
                
                # Add stability text
                ax.text(comp['position'][0], comp['position'][1], 
                      f"{comp['stability']:.2f}", ha='center', va='center',
                      fontsize=8)
            
            # Add feedback coefficient indicator
            feedback = data['feedback_coefficient']
            ax.text(0.02, 0.98, f"Feedback: {feedback:.2f}", 
                  transform=ax.transAxes, fontsize=10,
                  verticalalignment='top', color='black',
                  bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
            
            # Add amphiphilic count
            ax.text(0.98, 0.98, f"Amphiphilic: {data['amphiphilic_count']}", 
                  transform=ax.transAxes, fontsize=10, ha='right',
                  verticalalignment='top', color='blue',
                  bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
            
            return []
        
        # Create the animation
        anim = animation.FuncAnimation(
            fig, update, frames=len(self.compartment_tracking),
            interval=200, blit=False
        )
        
        # Save if filename provided
        if output_filename:
            anim.save(output_filename, writer='ffmpeg', fps=5, dpi=200)
            print(f"Compartment evolution animation saved to {output_filename}")
            plt.close(fig)
        else:
            plt.show()


class MetricsVisualizer:
    """
    Static class to generate detailed visualizations of simulation metrics
    after the simulation has completed.
    """
    
    @staticmethod
    def plot_all_metrics(simulation, environment, output_prefix="", show=True):
        """
        Generate comprehensive plots of all metrics from the simulation.
        
        Args:
            simulation: Completed simulation object
            environment: Environment object
            output_prefix (str): Prefix for output filenames
            show (bool): Whether to display the plots
        """
        # Create figure with 2x3 subplots
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        
        # Plot entropy and catalysis metrics
        MetricsVisualizer._plot_entropy_catalysis(simulation, axes[0, 0])
        
        # Plot molecular complexity
        MetricsVisualizer._plot_molecular_complexity(simulation, axes[0, 1])
        
        # Plot compartment metrics
        MetricsVisualizer._plot_compartment_metrics(simulation, axes[0, 2])
        
        # Plot environmental conditions
        MetricsVisualizer._plot_environmental_conditions(environment, axes[1, 0])
        
        # Plot feedback coefficients
        MetricsVisualizer._plot_feedback_analysis(simulation, axes[1, 1])
        
        # Plot molecule diversity
        MetricsVisualizer._plot_molecule_diversity(simulation, axes[1, 2])
        
        # Adjust layout
        fig.tight_layout()
        
        # Save if output prefix is given
        if output_prefix:
            filename = f"{output_prefix}_metrics.png"
            fig.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"Metrics plot saved to {filename}")
        
        if show:
            plt.show()
        else:
            plt.close(fig)
    
    @staticmethod
    def _plot_entropy_catalysis(simulation, ax):
        """Plot entropy reduction and catalytic activity metrics."""
        time_steps = range(len(simulation.metrics['entropy_reduction']))
        
        ax.plot(time_steps, simulation.metrics['entropy_reduction'], 'g-', 
             label='Entropy Reduction', alpha=0.7)
        ax.plot(time_steps, simulation.metrics['catalytic_activity'], 'r-', 
             label='Catalytic Activity', alpha=0.7)
        
        # Calculate moving correlation
        if len(time_steps) > 10:
            window_size = min(20, len(time_steps) // 5)
            correlations = []
            
            for i in range(len(time_steps) - window_size):
                er = simulation.metrics['entropy_reduction'][i:i+window_size]
                ca = simulation.metrics['catalytic_activity'][i:i+window_size]
                
                if np.std(er) > 0 and np.std(ca) > 0:
                    corr = np.corrcoef(er, ca)[0, 1]
                    if not np.isnan(corr):
                        correlations.append(corr)
                else:
                    correlations.append(0)
            
            # Pad correlations array to match time steps
            correlations = [0] * window_size + correlations
            ax.plot(time_steps, correlations, 'b--', 
                  label='Moving Correlation', alpha=0.5)
        
        ax.set_title("Entropy Reduction & Catalytic Activity")
        ax.set_xlabel("Time Steps")
        ax.set_ylabel("Value")
        ax.legend(loc='upper right')
    
    @staticmethod
    def _plot_molecular_complexity(simulation, ax):
        """Plot molecular complexity over time."""
        time_steps = range(len(simulation.metrics['molecular_complexity']))
        
        ax.plot(time_steps, simulation.metrics['molecular_complexity'], 'b-', 
             label='Avg. Complexity', linewidth=2)
        
        # Calculate the rate of change of complexity (first derivative)
        if len(time_steps) > 5:
            complexity = np.array(simulation.metrics['molecular_complexity'])
            # Use gradient to calculate derivative
            complexity_rate = np.gradient(complexity)
            
            ax.plot(time_steps, complexity_rate, 'r--', 
                  label='Rate of Change', alpha=0.6)
            
            # Add annotations for significant complexity jumps
            threshold = np.std(complexity_rate) * 2
            for i, rate in enumerate(complexity_rate):
                if i > 0 and rate > threshold:
                    ax.annotate("Jump", 
                              xy=(i, complexity[i]),
                              xytext=(-20, 20),
                              textcoords="offset points",
                              arrowprops=dict(arrowstyle="->", 
                                           connectionstyle="arc3,rad=.2"))
        
        ax.set_title("Molecular Complexity Over Time")
        ax.set_xlabel("Time Steps")
        ax.set_ylabel("Complexity")
        ax.legend(loc='best')
    
    @staticmethod
    def _plot_compartment_metrics(simulation, ax):
        """Plot compartment-related metrics."""
        time_steps = range(len(simulation.metrics['compartment_count']))
        
        ax.plot(time_steps, simulation.metrics['compartment_count'], 'b-', 
             label='Compartment Count')
        
        if simulation.metrics['avg_stability']:
            ax.plot(time_steps, simulation.metrics['avg_stability'], 'g-', 
                  label='Avg. Stability', alpha=0.7)
        
        # Add annotations for first compartment
        if any(count > 0 for count in simulation.metrics['compartment_count']):
            first_compartment = next(i for i, count in enumerate(
                simulation.metrics['compartment_count']) if count > 0)
            
            ax.annotate("First Compartment", 
                      xy=(first_compartment, simulation.metrics['compartment_count'][first_compartment]),
                      xytext=(10, 20),
                      textcoords="offset points",
                      arrowprops=dict(arrowstyle="->"))
        
        ax.set_title("Compartment Metrics")
        ax.set_xlabel("Time Steps")
        ax.set_ylabel("Value")
        ax.legend(loc='best')
    
    @staticmethod
    def _plot_environmental_conditions(environment, ax):
        """Plot environmental conditions over time."""
        time_steps = range(len(environment.history['temperature']))
        
        # Normalize values for better comparison
        temp_norm = [t/100 for t in environment.history['temperature']]  # Assume max temp = 100
        ph_norm = [p/14 for p in environment.history['ph']]  # pH scale is 0-14
        uv_norm = environment.history['uv_intensity']
        wet_phase = environment.history['wet_phase']
        
        ax.plot(time_steps, temp_norm, 'r-', label='Temperature (norm.)')
        ax.plot(time_steps, ph_norm, 'g-', label='pH (norm.)')
        ax.plot(time_steps, uv_norm, 'y-', label='UV Intensity')
        ax.plot(time_steps, wet_phase, 'b-', label='Wet Phase')
        
        ax.set_title("Environmental Conditions")
        ax.set_xlabel("Time Steps")
        ax.set_ylabel("Normalized Value")
        ax.legend(loc='best')
    
    @staticmethod
    def _plot_feedback_analysis(simulation, ax):
        """Plot analysis of entropy-catalysis feedback mechanism."""
        time_steps = range(len(simulation.metrics['entropy_reduction']))
        
        if len(time_steps) < 10:
            ax.text(0.5, 0.5, "Insufficient data for feedback analysis", 
                  ha='center', va='center')
            ax.set_title("Feedback Analysis")
            return
        
        # Calculate feedback coefficients over different windows
        feedback_data = []
        window_sizes = [10, 20, 50, 100]
        window_sizes = [w for w in window_sizes if w < len(time_steps)]
        
        for window in window_sizes:
            coefficients = []
            
            for i in range(0, len(time_steps) - window, window // 2):
                er = simulation.metrics['entropy_reduction'][i:i+window]
                ca = simulation.metrics['catalytic_activity'][i:i+window]
                
                if np.std(er) > 0 and np.std(ca) > 0:
                    corr = np.corrcoef(er, ca)[0, 1]
                    if not np.isnan(corr):
                        coefficients.append((i + window//2, corr))
            
            if coefficients:
                xs, ys = zip(*coefficients)
                ax.plot(xs, ys, '-', label=f'Window={window}')
        
        # Calculate overall feedback trend
        if simulation.metrics['entropy_ratio'] and simulation.metrics['catalytic_ratio']:
            entropy_ratio = simulation.metrics['entropy_ratio']
            catalytic_ratio = simulation.metrics['catalytic_ratio']
            
            if len(entropy_ratio) > 10 and len(catalytic_ratio) > 10:
                # Fit a line to the relationship
                valid_indices = [i for i in range(len(entropy_ratio)) 
                                if entropy_ratio[i] > 0 and catalytic_ratio[i] > 0]
                
                if valid_indices:
                    er_valid = [entropy_ratio[i] for i in valid_indices]
                    cr_valid = [catalytic_ratio[i] for i in valid_indices]
                    
                    # Insert a small subplot
                    subax = ax.inset_axes([0.6, 0.1, 0.35, 0.35])
                    subax.scatter(er_valid, cr_valid, alpha=0.5, s=10)
                    subax.set_xlabel('Entropy Ratio')
                    subax.set_ylabel('Catalytic Ratio')
                    subax.set_title('Relationship', fontsize=8)
        
        ax.set_title("Entropy-Catalysis Feedback Analysis")
        ax.set_xlabel("Time Steps")
        ax.set_ylabel("Feedback Coefficient")
        if window_sizes:
            ax.legend(loc='best')
    
    @staticmethod
    def _plot_molecule_diversity(simulation, ax):
        """Plot molecule diversity metrics over time."""
        # We'll reconstruct molecule diversity from the data
        time_steps = range(len(simulation.metrics['molecular_complexity']))
        
        # For simplicity, we'll use complexity as a proxy for diversity
        complexity = simulation.metrics['molecular_complexity']
        
        # Create a heatmap-style plot to show the evolution of complexity
        # We'll create bands of complexity levels
        
        levels = [1, 3, 5, 10, 20]  # Complexity levels
        level_labels = ['Simple', 'Basic', 'Intermediate', 'Complex', 'Very Complex']
        
        # For each level, calculate how many molecules are at or above that level
        level_counts = []
        
        # Get the latest molecule counts
        molecules = list(simulation.molecules.items())
        molecules.sort(key=lambda x: x[0].complexity)
        
        # Group molecules by complexity level
        level_molecules = [[] for _ in range(len(levels) + 1)]
        for molecule, count in molecules:
            if count > 0:
                level_idx = 0;
                for i, level in enumerate(levels):
                    if molecule.complexity >= level:
                        level_idx = i + 1
                level_molecules[level_idx].append((molecule.name, count))
        
        # Create a horizontal stacked bar chart of molecule types by complexity level
        y_pos = np.arange(len(level_labels))
        counts = [sum(count for _, count in level) for level in level_molecules[1:]]
        
        # If we have data, plot it
        if any(counts):
            ax.barh(y_pos, counts, align='center', alpha=0.5)
            ax.set_yticks(y_pos)
            ax.set_yticklabels(level_labels)
            
            # Add labels with counts
            for i, count in enumerate(counts):
                if count > 0:
                    ax.text(count + 0.5, i, str(count), va='center')
                    
            # Add the most prevalent molecule at each level
            for i, molecules in enumerate(level_molecules[1:]):
                if molecules:
                    top_molecule = max(molecules, key=lambda x: x[1])
                    ax.text(5, i, f"Top: {top_molecule[0]} ({top_molecule[1]})", 
                          va='center', fontsize=8)
        else:
            ax.text(0.5, 0.5, "No molecules present", ha='center', va='center')
                
        ax.set_title("Molecular Diversity")
        ax.set_xlabel("Count")


class AnimationController:
    """Controller for creating and managing simulation animations."""
    
    @staticmethod
    def run_animation(simulation, environment, frames=100, interval=200,
                    output_file=None, save_metrics=True, metrics_prefix="",
                    focus_compartments=False, detailed_visualization=False):
        """
        Run an animation of the simulation with streamlined options.
        
        Args:
            simulation: Simulation object
            environment: Environment object
            frames (int): Number of frames to run
            interval (int): Time between frames in milliseconds
            output_file (str): File to save animation to (optional)
            save_metrics (bool): Whether to save metrics plots after simulation
            metrics_prefix (str): Prefix for metrics files
            focus_compartments (bool): Whether to focus on compartment visualization
            detailed_visualization (bool): Whether to use detailed visualization
        """
        # Create visualization with optimized parameters
        viz = SimulationVisualization()
        
        # Setup the plot layout based on visualization focus
        viz.setup_plot_layout(focus_compartments=focus_compartments, 
                             detailed_visualization=detailed_visualization)
        
        # Run animation with appropriate parameters
        viz.start_animation(simulation, environment, frames, interval, 
                          focus_compartments=focus_compartments)
        
        # Save animation if requested
        if output_file:
            viz.save_animation(output_file)
            
        # Save metrics if requested with streamlined interface
        if save_metrics:
            MetricsVisualizer.plot_all_metrics(
                simulation, environment, output_prefix=metrics_prefix, show=True)