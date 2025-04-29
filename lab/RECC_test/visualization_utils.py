#!/usr/bin/env python3
# RECC MVP 1.5: Visualization Utilities
# Provides visualization functions for RECC components

import os
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime

def draw_concept_map(symbols=None, links=None, emotions=None, concept_network=None, save_path=None):
    """Draw concept map using either traditional symbols or concept network"""
    # Create timestamp for filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Set default save path if none provided
    if save_path is None:
        save_path = f"./static/concept_network_{timestamp}.png"
    
    if (concept_network and hasattr(concept_network, 'graph') and len(concept_network.graph) > 0):
        # Use concept network for visualization
        
        # Get a visualization-friendly subgraph instead of the full graph
        # This limits the number of nodes to prevent memory issues
        G = concept_network.get_visualization_subgraph(max_nodes=75)
        
        plt.figure(figsize=(12, 10))
        
        # Get positions
        pos = nx.spring_layout(G, seed=42)
        
        # Get node sizes based on activation or centrality
        centrality = nx.betweenness_centrality(G)
        node_sizes = [1000 * (0.3 + centrality[n]) for n in G.nodes()]
        
        # Get node colors based on reuse count
        reuse_counts = [G.nodes[n].get('reuse_count', 0) + 1 for n in G.nodes()]
        max_reuse = max(reuse_counts) if reuse_counts else 1
        node_colors = [(0.2, 0.4, 0.8, min(1.0, c/max_reuse)) for c in reuse_counts]
        
        # Draw nodes
        nx.draw_networkx_nodes(G, pos, 
                              node_size=node_sizes,
                              node_color=node_colors,
                              alpha=0.8)
        
        # Draw edges with weights affecting width
        edge_weights = [G.edges[e].get('weight', 0.1) * 2 for e in G.edges()]
        nx.draw_networkx_edges(G, pos, width=edge_weights, alpha=0.6, edge_color='gray')
        
        # Draw labels - only for the most important nodes
        # For smaller networks, show all labels
        labels = {}
        if len(G.nodes()) > 30:
            # For larger networks, only show labels for more important nodes
            central = nx.betweenness_centrality(G)
            important = sorted(central.items(), key=lambda x: x[1], reverse=True)[:25]
            for node, _ in important:
                if node in concept_network.concepts:
                    labels[node] = concept_network.concepts[node]['name']
        else:
            # For smaller networks, show all labels
            labels = {n: concept_network.concepts[n]['name'] for n in G.nodes() if n in concept_network.concepts}
            
        nx.draw_networkx_labels(G, pos, labels=labels, font_size=10, font_weight='bold')
        
        # Add information about size reduction
        total_concepts = len(concept_network.concepts)
        displayed_concepts = len(G.nodes())
        plt.title(f'RECC Concept Network (Showing {displayed_concepts}/{total_concepts} concepts)')
        plt.axis('off')
        
        # Ensure the visualization directory exists
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # Save figure with reduced DPI to decrease file size
        plt.savefig(save_path, dpi=80)
        print(f"📊 Concept network visualization saved to: {save_path}")
        
        # Close the figure immediately to free memory
        plt.close('all')
        
        return save_path
        
    elif symbols and links:
        # Fall back to traditional symbol visualization
        G = nx.Graph()

        # Add nodes with emotional data if available
        for symbol in symbols:
            G.add_node(symbol)

        # Add edges
        for source, target in links:
            G.add_edge(source, target)

        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(G, seed=42)
        
        # Use emotions to color nodes if available
        if (emotions and len(symbols) > 0):
            # Default coloring
            node_colors = ['lightblue'] * len(symbols)
            
            # If we have emotions, adjust colors
            if 'curiosity' in emotions and emotions['curiosity'] > 0.7:
                node_colors = ['#FFA500']  # Orange for curiosity
            elif 'satisfaction' in emotions and emotions['satisfaction'] > 0.7:
                node_colors = ['#90EE90']  # Light green for satisfaction
            elif 'frustration' in emotions and emotions['frustration'] > 0.7:
                node_colors = ['#FF6347']  # Tomato for frustration
            
            nx.draw(G, pos, with_labels=True, node_color=node_colors, 
                    node_size=1200, font_size=12, font_weight='bold', edge_color='gray')
        else:
            nx.draw(G, pos, with_labels=True, node_color='lightblue', 
                    node_size=1200, font_size=12, font_weight='bold', edge_color='gray')

        plt.title('RECC Concept Map')
        
        # Ensure the visualization directory exists
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # Save figure
        plt.savefig(save_path)
        print(f"📊 Symbol map visualization saved to: {save_path}")
        
        plt.close()  # Close the figure to free memory
        
        return save_path
    
    return None

def visualize_emotions(me_instance, save_path=None):
    """Generate visualization of emotional state over time"""
    if not me_instance.emotion_history:
        print("No emotional history available for visualization.")
        return None
    
    # Create timestamp for filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Set default save path if none provided
    if save_path is None:
        save_path = f"./static/emotional_development_{timestamp}.png"
    
    # Extract data
    cycles = [h['cycle'] for h in me_instance.emotion_history]
    emotions = {e: [h['state'][e] for h in me_instance.emotion_history] for e in me_instance.emotional_state.keys()}
    
    # Plot
    plt.figure(figsize=(12, 6))
    for emotion, values in emotions.items():
        plt.plot(cycles, values, marker='o', label=emotion)
    
    plt.xlabel('Reflection Cycle')
    plt.ylabel('Emotional Intensity')
    plt.title('RECC Emotional Development')
    plt.legend()
    plt.grid(True)
    
    # Ensure the visualization directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Save figure
    plt.savefig(save_path)
    print(f"📊 Emotional development visualization saved to: {save_path}")
    
    plt.close()  # Close the figure to free memory
    
    return save_path

def create_interactive_concept_network_data(concept_network):
    """Create data structure for interactive concept network visualization"""
    # Extract nodes (concepts)
    nodes = []
    for concept_id, concept in concept_network.concepts.items():
        nodes.append({
            'id': concept_id,
            'name': concept['name'],
            'activation': concept.get('activation', 0.5),
            'reuse_count': concept.get('reuse_count', 0),
            'created': concept.get('created', ''),
            'source': concept.get('source', 'unknown')
        })
        
    # Extract edges (relations)
    edges = []
    for relation in concept_network.relations:
        edges.append({
            'id': relation.get('id', ''),
            'source': relation.get('source', ''),
            'target': relation.get('target', ''),
            'type': relation.get('type', 'association'),
            'weight': relation.get('weight', 0.5)
        })
        
    return {
        'nodes': nodes,
        'edges': edges
    }

def create_metric_summary(memory, me_instance):
    """Create a summary of key RECC metrics"""
    # Calculate basic metrics
    novelty_gradient, reuse_gradient = memory.compute_gradients()
    recent = memory.get_recent(5)
    avg_novelty = sum(e.get('novelty', 0) for e in recent) / max(len(recent), 1)
    
    # Get network statistics
    network_stats = memory.concept_network.get_network_stats()
    
    # Create the metric summary
    metrics = {
        'memory_size': len(memory.entries),
        'concept_count': network_stats['concept_count'],
        'relation_count': network_stats['relation_count'],
        'avg_connections': round(network_stats['avg_connections'], 2),
        'network_density': round(network_stats['density'], 3),
        'most_central_concept': network_stats.get('most_reused', 'unknown'),
        'novelty_gradient': novelty_gradient,
        'reuse_gradient': reuse_gradient,
        'avg_novelty': round(avg_novelty, 3),
        'emotional_state': me_instance.emotional_state,
        'theory_count': len(me_instance.personal_theories)
    }
    
    return metrics