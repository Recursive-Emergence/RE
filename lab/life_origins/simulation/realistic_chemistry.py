import random
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import datetime
import json

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Updated imports to match the actual directory structure
from src.chemistry import create_prebiotic_food_set
from src.environment import Environment
from src.chemistry import ChemicalNetwork
from src.emergence_detector import analyze_complexity_emergence
from src.visualization import visualize_stability_analysis

def run_simulation(steps=50, with_plots=True, output_dir=None):
    """
    Run a standard life origins simulation with the specified number of steps.
    
    Args:
        steps (int): Number of simulation steps to run
        with_plots (bool): Whether to generate visualization plots
        output_dir (str): Directory to save output files (None = don't save)
        
    Returns:
        ChemicalNetwork: The final simulation network state
    """
    # Start time for performance tracking
    start_time = time.time()
    
    # Create output directory if specified
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    # Initialize simulation components
    food_molecules = create_prebiotic_food_set()
    print(f"Created {len(food_molecules)} prebiotic molecules")
    
    env = Environment()
    env.temperature = 85
    env.temperature_K = env.temperature + 273.15
    env.ph = 8.0
    env.wet_dry_cycle = True
    
    network = ChemicalNetwork(food_molecules, env)
    
    # Track metrics over time for later analysis
    metrics = {
        'steps': [],
        'molecules': [],
        'reactions': [],
        'energy': [],
        'complexity': []
    }
    
    # Run simulation with periodic logging
    print(f"Running simulation for {steps} steps...")
    log_interval = max(1, steps // 10)  # Log approximately 10 times
    
    for step in range(steps):
        network.update()
        
        # Store metrics at each step
        stats = network.get_statistics()
        metrics['steps'].append(step)
        metrics['molecules'].append(stats['molecules'])
        metrics['reactions'].append(len(network.active_reactions))
        metrics['energy'].append(stats['energy_currency'])
        metrics['complexity'].append(network.get_average_complexity())
        
        # Log progress periodically
        if step % log_interval == 0 or step == steps - 1:
            print(f"Step {step}: {stats['molecules']} molecules, "
                  f"{len(network.active_reactions)} reactions, "
                  f"{stats['energy_currency']:.2f} energy")
    
    # Calculate final analysis
    analysis_results = analyze_complexity_emergence(network)
    
    # Print summary statistics
    print(f"\nSimulation completed in {time.time() - start_time:.2f} seconds")
    print(f"Final complexity score: {analysis_results['complexity_score']:.4f}")
    print(f"Entropy-catalysis feedback: {analysis_results['entropy_catalysis_feedback']:.4f}")
    
    # Generate and save plots if requested
    if with_plots:
        # Stability analysis visualization
        visualize_stability_analysis(analysis_results)
        
        # Generate time series plots of key metrics
        plot_simulation_metrics(metrics, output_dir)
    
    # Save results if output directory is specified
    if output_dir:
        # Save metrics as JSON
        with open(os.path.join(output_dir, 'results.json'), 'w') as f:
            json.dump({
                'final_analysis': {k: float(v) if isinstance(v, np.float32) else v 
                                for k, v in analysis_results.items()},
                'metrics': {k: [float(x) if isinstance(x, np.float32) else x for x in v] 
                          for k, v in metrics.items()}
            }, f, indent=2)
        
        print(f"Results saved to {output_dir}")
    
    return network

def test_entropy_constraint_hypothesis(steps=50, with_plots=True, output_dir=None):
    """
    Test the entropy constraint hypothesis with varying constraint levels.
    
    Args:
        steps (int): Number of steps per constraint level
        with_plots (bool): Whether to generate visualization plots
        output_dir (str): Directory to save output files
        
    Returns:
        dict: Results for each constraint level
    """
    # Start time for performance tracking
    start_time = time.time()
    
    # Create output directory if specified
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    # Initialize results container with optimized structure
    results = {
        'constraint_level': [],
        'feedback_coef': [],
        'final_complexity': [],
        'molecule_count': [],
        'catalyst_count': [],
        'energy_final': [],
        'autocatalytic_cycles': []
    }
    
    # Define the constraint levels with descriptive information
    constraint_descriptions = {
        1: "Low constraint - abundant simple food set, high water content",
        2: "Medium-low constraint - moderate food set, periodic drying",
        3: "Medium constraint - moderate food set with metal catalysts",
        4: "Medium-high constraint - limited food set, strong temperature gradient",
        5: "High constraint - highly specific food set, concentrated reactants"
    }
    
    # Run simulations for each constraint level
    for constraint_level in range(1, 6):
        print(f"\nRunning constraint level {constraint_level}/5: {constraint_descriptions[constraint_level]}")
        
        # Configure environment based on constraint level
        env = Environment()
        env.configure_constraint_level(constraint_level)
        
        # Create network with appropriate constraint level
        network = ChemicalNetwork(create_prebiotic_food_set(constraint_level), env)
        
        # Run simulation for this constraint level
        for step in range(steps):
            network.update()
            
            # Log progress at 25%, 50%, 75% and 100%
            if step in [steps//4, steps//2, 3*steps//4, steps-1]:
                print(f"  Step {step}/{steps}, molecules: {network.get_statistics()['molecules']}")
        
        # Analyze results
        analysis = analyze_complexity_emergence(network)
        stats = network.get_statistics()
        
        # Store results
        results['constraint_level'].append(constraint_level)
        results['feedback_coef'].append(analysis['entropy_catalysis_feedback'])
        results['final_complexity'].append(analysis['complexity_score'])
        results['molecule_count'].append(stats['molecules'])
        results['catalyst_count'].append(stats['catalysts'])
        results['energy_final'].append(stats['energy_currency'])
        results['autocatalytic_cycles'].append(analysis['autocatalytic_cycles'])
        
        # Print summary for this constraint level
        print(f"\nConstraint {constraint_level} Results:")
        print(f"  Feedback Coefficient: {analysis['entropy_catalysis_feedback']:.4f}")
        print(f"  Complexity Score: {analysis['complexity_score']:.4f}")
        print(f"  Molecules: {stats['molecules']}, Catalysts: {stats['catalysts']}")
    
    # Generate plots if requested
    if with_plots:
        plot_constraint_hypothesis_results(results, output_dir)
    
    # Save results if output directory is specified
    if output_dir:
        with open(os.path.join(output_dir, 'constraint_results.json'), 'w') as f:
            json.dump({k: [float(x) if isinstance(x, np.float32) else x for x in v] 
                     for k, v in results.items()}, f, indent=2)
    
    print(f"\nEntropy constraint hypothesis test completed in {time.time() - start_time:.2f} seconds")
    return results

def plot_simulation_metrics(metrics, output_dir=None):
    """
    Plot time series metrics from a simulation run.
    
    Args:
        metrics (dict): Dictionary of simulation metrics
        output_dir (str): Directory to save output files
    """
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    
    # Plot molecule count
    axs[0, 0].plot(metrics['steps'], metrics['molecules'], 'b-')
    axs[0, 0].set_title('Molecule Count')
    axs[0, 0].set_xlabel('Step')
    axs[0, 0].set_ylabel('Count')
    
    # Plot reaction count
    axs[0, 1].plot(metrics['steps'], metrics['reactions'], 'r-')
    axs[0, 1].set_title('Active Reactions')
    axs[0, 1].set_xlabel('Step')
    axs[0, 1].set_ylabel('Count')
    
    # Plot energy level
    axs[1, 0].plot(metrics['steps'], metrics['energy'], 'g-')
    axs[1, 0].set_title('Energy Currency')
    axs[1, 0].set_xlabel('Step')
    axs[1, 0].set_ylabel('Energy')
    
    # Plot molecular complexity
    axs[1, 1].plot(metrics['steps'], metrics['complexity'], 'm-')
    axs[1, 1].set_title('Average Complexity')
    axs[1, 1].set_xlabel('Step')
    axs[1, 1].set_ylabel('Complexity')
    
    plt.tight_layout()
    
    # Save if output directory specified
    if output_dir:
        plt.savefig(os.path.join(output_dir, 'simulation_metrics.png'), dpi=300)
    
    plt.show()

def plot_constraint_hypothesis_results(results, output_dir=None):
    """
    Plot results from the entropy constraint hypothesis test.
    
    Args:
        results (dict): Results from test_entropy_constraint_hypothesis
        output_dir (str): Directory to save output files
    """
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    
    x = results['constraint_level']
    
    # Plot feedback coefficient vs constraint level
    axs[0, 0].bar(x, results['feedback_coef'], color='blue', alpha=0.7)
    axs[0, 0].set_title('Feedback Coefficient vs Constraint Level')
    axs[0, 0].set_xlabel('Constraint Level')
    axs[0, 0].set_ylabel('Feedback Coefficient')
    
    # Add value labels on bars
    for i, v in enumerate(results['feedback_coef']):
        axs[0, 0].text(i + 1, v + 0.01, f"{v:.2f}", ha='center')
    
    # Plot final complexity vs constraint level
    axs[0, 1].bar(x, results['final_complexity'], color='green', alpha=0.7)
    axs[0, 1].set_title('Final Complexity vs Constraint Level')
    axs[0, 1].set_xlabel('Constraint Level')
    axs[0, 1].set_ylabel('Complexity Score')
    
    # Add value labels on bars
    for i, v in enumerate(results['final_complexity']):
        axs[0, 1].text(i + 1, v + 0.01, f"{v:.2f}", ha='center')
    
    # Plot molecule count vs constraint level
    axs[1, 0].bar(x, results['molecule_count'], color='red', alpha=0.7)
    axs[1, 0].set_title('Molecule Count vs Constraint Level')
    axs[1, 0].set_xlabel('Constraint Level')
    axs[1, 0].set_ylabel('Molecule Count')
    
    # Add value labels on bars
    for i, v in enumerate(results['molecule_count']):
        axs[1, 0].text(i + 1, v + 1, str(v), ha='center')
    
    # Plot autocatalytic cycles vs constraint level
    width = 0.35
    ax1 = axs[1, 1]
    ax1.bar(x, results['autocatalytic_cycles'], width, color='purple', alpha=0.7, label='Autocatalytic Cycles')
    ax1.set_xlabel('Constraint Level')
    ax1.set_ylabel('Autocatalytic Cycles', color='purple')
    ax1.tick_params(axis='y', labelcolor='purple')
    ax1.set_title('Autocatalytic Cycles & Catalysts vs Constraint')
    
    # Add value labels
    for i, v in enumerate(results['autocatalytic_cycles']):
        ax1.text(i + 1 - width/2, v + 0.1, str(v), ha='center')
    
    # Add catalyst count on secondary axis
    ax2 = ax1.twinx()
    ax2.bar([x + width for x in results['constraint_level']], results['catalyst_count'], 
           width, color='orange', alpha=0.7, label='Catalysts')
    ax2.set_ylabel('Catalyst Count', color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')
    
    # Add value labels
    for i, v in enumerate(results['catalyst_count']):
        ax2.text(i + 1 + width/2, v + 0.1, str(v), ha='center')
    
    # Add legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')
    
    plt.tight_layout()
    
    # Save if output directory specified
    if output_dir:
        plt.savefig(os.path.join(output_dir, 'constraint_hypothesis_results.png'), dpi=300)
    
    plt.show()

def run_batch_simulation(num_runs=5, steps=50, output_base_dir=None):
    """
    Run multiple simulations and analyze statistical significance of results.
    
    Args:
        num_runs (int): Number of simulations to run
        steps (int): Number of steps per simulation
        output_base_dir (str): Base directory for outputs
    
    Returns:
        dict: Aggregated statistics from all runs
    """
    # Create timestamp for output directory
    timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
    if output_base_dir:
        output_dir = os.path.join(output_base_dir, f"batch_simulation_{timestamp}")
        os.makedirs(output_dir, exist_ok=True)
    else:
        output_dir = None
    
    # Initialize results collection
    all_results = []
    
    # Run all simulations
    for run in range(num_runs):
        print(f"\nRun {run + 1}/{num_runs}")
        
        # Create run-specific output directory
        if output_dir:
            run_output_dir = os.path.join(output_dir, f"run_{run + 1}")
            os.makedirs(run_output_dir, exist_ok=True)
        else:
            run_output_dir = None
        
        # Run simulation with a different random seed for each run
        random.seed(42 + run)
        network = run_simulation(steps=steps, with_plots=False, output_dir=run_output_dir)
        
        # Analyze and store results
        analysis = analyze_complexity_emergence(network)
        stats = network.get_statistics()
        
        all_results.append({
            'run': run + 1,
            'complexity_score': analysis['complexity_score'],
            'feedback_coefficient': analysis['entropy_catalysis_feedback'],
            'autocatalytic_cycles': analysis['autocatalytic_cycles'],
            'molecules': stats['molecules'],
            'catalysts': stats['catalysts'],
            'energy': stats['energy_currency']
        })
    
    # Calculate aggregate statistics
    aggregated_stats = calculate_aggregate_statistics(all_results)
    
    # Generate summary plots
    if output_dir:
        plot_batch_statistics(all_results, aggregated_stats, output_dir)
        
        # Save aggregated results
        with open(os.path.join(output_dir, 'batch_results.json'), 'w') as f:
            json.dump({
                'individual_runs': all_results,
                'aggregated_stats': aggregated_stats
            }, f, indent=2)
        
        print(f"\nBatch results saved to {output_dir}")
    
    return aggregated_stats

def calculate_aggregate_statistics(results):
    """
    Calculate aggregate statistics from multiple simulation runs.
    
    Args:
        results (list): List of result dictionaries from multiple runs
        
    Returns:
        dict: Aggregated statistics
    """
    metrics = ['complexity_score', 'feedback_coefficient', 'autocatalytic_cycles', 
              'molecules', 'catalysts', 'energy']
    
    stats = {}
    
    for metric in metrics:
        values = [run[metric] for run in results]
        
        stats[metric] = {
            'mean': float(np.mean(values)),
            'std_dev': float(np.std(values)),
            'min': float(np.min(values)),
            'max': float(np.max(values)),
            'median': float(np.median(values)),
            'values': values
        }
    
    return stats

def plot_batch_statistics(results, stats, output_dir):
    """
    Plot statistical results from batch simulations.
    
    Args:
        results (list): List of result dictionaries from multiple runs
        stats (dict): Aggregated statistics
        output_dir (str): Directory to save output plots
    """
    # Plot key metrics across runs
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    
    run_nums = [r['run'] for r in results]
    
    # Plot complexity scores
    complexity_values = [r['complexity_score'] for r in results]
    axs[0, 0].plot(run_nums, complexity_values, 'bo-')
    axs[0, 0].axhline(y=stats['complexity_score']['mean'], color='r', linestyle='-', 
                     label=f"Mean: {stats['complexity_score']['mean']:.2f}")
    axs[0, 0].fill_between(run_nums, 
                         [stats['complexity_score']['mean'] - stats['complexity_score']['std_dev']] * len(run_nums),
                         [stats['complexity_score']['mean'] + stats['complexity_score']['std_dev']] * len(run_nums),
                         alpha=0.2, color='r', label=f"Std Dev: {stats['complexity_score']['std_dev']:.2f}")
    axs[0, 0].set_title('Complexity Score by Run')
    axs[0, 0].set_xlabel('Run')
    axs[0, 0].set_ylabel('Complexity Score')
    axs[0, 0].legend()
    
    # Plot feedback coefficients
    feedback_values = [r['feedback_coefficient'] for r in results]
    axs[0, 1].plot(run_nums, feedback_values, 'go-')
    axs[0, 1].axhline(y=stats['feedback_coefficient']['mean'], color='r', linestyle='-', 
                     label=f"Mean: {stats['feedback_coefficient']['mean']:.2f}")
    axs[0, 1].fill_between(run_nums, 
                         [stats['feedback_coefficient']['mean'] - stats['feedback_coefficient']['std_dev']] * len(run_nums),
                         [stats['feedback_coefficient']['mean'] + stats['feedback_coefficient']['std_dev']] * len(run_nums),
                         alpha=0.2, color='r', label=f"Std Dev: {stats['feedback_coefficient']['std_dev']:.2f}")
    axs[0, 1].set_title('Feedback Coefficient by Run')
    axs[0, 1].set_xlabel('Run')
    axs[0, 1].set_ylabel('Feedback Coefficient')
    axs[0, 1].legend()
    
    # Plot molecule counts
    molecule_values = [r['molecules'] for r in results]
    axs[1, 0].plot(run_nums, molecule_values, 'mo-')
    axs[1, 0].axhline(y=stats['molecules']['mean'], color='r', linestyle='-', 
                     label=f"Mean: {stats['molecules']['mean']:.1f}")
    axs[1, 0].fill_between(run_nums, 
                         [stats['molecules']['mean'] - stats['molecules']['std_dev']] * len(run_nums),
                         [stats['molecules']['mean'] + stats['molecules']['std_dev']] * len(run_nums),
                         alpha=0.2, color='r', label=f"Std Dev: {stats['molecules']['std_dev']:.1f}")
    axs[1, 0].set_title('Molecule Count by Run')
    axs[1, 0].set_xlabel('Run')
    axs[1, 0].set_ylabel('Molecule Count')
    axs[1, 0].legend()
    
    # Plot autocatalytic cycles
    cycle_values = [r['autocatalytic_cycles'] for r in results]
    axs[1, 1].plot(run_nums, cycle_values, 'co-')
    axs[1, 1].axhline(y=stats['autocatalytic_cycles']['mean'], color='r', linestyle='-', 
                     label=f"Mean: {stats['autocatalytic_cycles']['mean']:.1f}")
    axs[1, 1].fill_between(run_nums, 
                         [stats['autocatalytic_cycles']['mean'] - stats['autocatalytic_cycles']['std_dev']] * len(run_nums),
                         [stats['autocatalytic_cycles']['mean'] + stats['autocatalytic_cycles']['std_dev']] * len(run_nums),
                         alpha=0.2, color='r', label=f"Std Dev: {stats['autocatalytic_cycles']['std_dev']:.1f}")
    axs[1, 1].set_title('Autocatalytic Cycles by Run')
    axs[1, 1].set_xlabel('Run')
    axs[1, 1].set_ylabel('Cycles')
    axs[1, 1].legend()
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'batch_statistics.png'), dpi=300)
    plt.close()
    
    # Create correlation matrix heatmap
    metrics = ['complexity_score', 'feedback_coefficient', 'autocatalytic_cycles', 
              'molecules', 'catalysts', 'energy']
    
    correlation_data = np.zeros((len(metrics), len(metrics)))
    
    # Calculate correlations
    for i, metric1 in enumerate(metrics):
        for j, metric2 in enumerate(metrics):
            values1 = [r[metric1] for r in results]
            values2 = [r[metric2] for r in results]
            correlation = np.corrcoef(values1, values2)[0, 1]
            correlation_data[i, j] = correlation
    
    # Plot correlation heatmap
    plt.figure(figsize=(10, 8))
    plt.imshow(correlation_data, cmap='coolwarm', vmin=-1, vmax=1)
    
    # Add labels
    plt.colorbar(label='Correlation')
    plt.title('Correlation Matrix Between Metrics')
    plt.xticks(np.arange(len(metrics)), [m.replace('_', ' ').title() for m in metrics], rotation=45, ha='right')
    plt.yticks(np.arange(len(metrics)), [m.replace('_', ' ').title() for m in metrics])
    
    # Add correlation values
    for i in range(len(metrics)):
        for j in range(len(metrics)):
            plt.text(j, i, f"{correlation_data[i, j]:.2f}", 
                   ha="center", va="center", color="black" if abs(correlation_data[i, j]) < 0.7 else "white")
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'correlation_matrix.png'), dpi=300)
    plt.close()

if __name__ == "__main__":
    random.seed(42)
    
    # Get command-line arguments
    steps = 100
    simulation_type = "standard"
    
    if len(sys.argv) > 1:
        try:
            steps = int(sys.argv[1])
        except ValueError:
            print(f"Invalid steps argument: {sys.argv[1]}. Using default: 100")
            
        if len(sys.argv) > 2:
            simulation_type = sys.argv[2].lower()
    
    # Create output directory with timestamp
    timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
    output_dir = f"simulation_results_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    print(f"Output will be saved to: {output_dir}")
    
    # Run specified simulation type
    if simulation_type == "constraint":
        print("\nRunning entropy constraint hypothesis test...")
        constraint_results = test_entropy_constraint_hypothesis(steps=steps, output_dir=output_dir)
    elif simulation_type == "batch":
        print("\nRunning batch simulations...")
        batch_results = run_batch_simulation(num_runs=5, steps=steps, output_base_dir=output_dir)
    else:  # standard single run
        network = run_simulation(steps=steps, output_dir=output_dir)
    
    print("\nSimulation complete! All results saved as PNG files.")