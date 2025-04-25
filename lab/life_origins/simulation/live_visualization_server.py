#!/usr/bin/env python3
import os
import json
import threading
import time
from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO
import sys
import importlib.util
import numpy as np

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Direct import from realistic_chemistry.py in the same directory
from realistic_chemistry import run_simulation, test_entropy_constraint_hypothesis

app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')
app.config['SECRET_KEY'] = 'entropy_catalysis_visualization'
socketio = SocketIO(app, cors_allowed_origins="*")

# Global variables to track simulation state
simulation_running = False
simulation_thread = None
stop_simulation = False

# Threshold constants for emergence detection
THRESHOLDS = {
    'negentropy': 0.15,
    'feedback': 0.10,
    'resilience': 0.75,
    'compartment': 0.50
}

@app.route('/')
def index():
    """Serve the main visualization page"""
    return render_template('index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    """Serve static files"""
    return send_from_directory('static', path)

@socketio.on('connect')
def handle_connect():
    """Handle client connection"""
    print('Client connected')
    socketio.emit('status', {'status': 'Connected to server'})

@socketio.on('disconnect')
def handle_disconnect():
    """Handle client disconnection"""
    print('Client disconnected')

@socketio.on('start_simulation')
def handle_start_simulation(data):
    """Start a new simulation based on client parameters"""
    global simulation_running, simulation_thread, stop_simulation
    
    if simulation_running:
        socketio.emit('status', {'status': 'Simulation already running'})
        return
    
    # Reset stop flag
    stop_simulation = False
    
    # Get parameters from client
    steps = data.get('steps', 100)
    simulation_type = data.get('type', 'standard')
    
    # Start simulation in a separate thread
    simulation_thread = threading.Thread(
        target=run_visualization_simulation,
        args=(steps, simulation_type)
    )
    simulation_running = True
    simulation_thread.start()
    
    socketio.emit('status', {'status': 'Simulation started'})

@socketio.on('stop_simulation')
def handle_stop_simulation():
    """Stop the running simulation"""
    global stop_simulation
    stop_simulation = True
    socketio.emit('status', {'status': 'Stopping simulation...'})

def run_visualization_simulation(steps, simulation_type):
    """Run simulation with periodic updates to the client"""
    global simulation_running, stop_simulation
    
    try:
        if simulation_type == 'constraint_hypothesis':
            # For hypothesis testing, we run multiple simulations with different constraints
            for constraint_level in range(1, 6):
                if stop_simulation:
                    break
                
                socketio.emit('status', {'status': f'Running constraint level {constraint_level}/5'})
                
                env_params = get_constraint_environment(constraint_level)
                network = run_monitored_simulation(steps // 5, env_params, constraint_level)
                
                # Send final results for this constraint level
                analysis = network.get_final_analysis()
                socketio.emit('constraint_results', {
                    'constraint_level': constraint_level,
                    'feedback_coef': analysis['entropy_catalysis_feedback'],
                    'complexity_score': analysis['complexity_score'],
                    'molecule_count': network.get_statistics()['molecules'],
                    'autocatalytic_cycles': analysis['autocatalytic_cycles'],
                    'resilience_score': calculate_resilience(network)
                })
                
                # Short pause between constraint levels
                time.sleep(1)
                
        else:  # standard simulation
            network = run_monitored_simulation(steps)
            
            # Detect compartmentalization probability
            compartment_prob = calculate_compartmentalization_probability(network)
            
            # Send final summary when complete
            socketio.emit('simulation_complete', {
                'final_molecules': network.get_statistics()['molecules'],
                'final_reactions': len(network.active_reactions),
                'complexity_score': network.get_final_analysis()['complexity_score'],
                'compartmentalization_probability': compartment_prob,
                'resilience_score': calculate_resilience(network)
            })
    
    except Exception as e:
        socketio.emit('error', {'message': str(e)})
    
    finally:
        simulation_running = False
        socketio.emit('status', {'status': 'Simulation complete'})

def run_monitored_simulation(steps, env_params=None, constraint_level=None):
    """Run a simulation with periodic updates to the client"""
    # Updated imports to match the direct imports at the top of the file
    from src.environment import Environment
    from src.chemistry import ChemicalNetwork, create_prebiotic_food_set
    from src.emergence_detector import analyze_complexity_emergence
    
    # Set up environment
    env = Environment()
    if env_params:
        for key, value in env_params.items():
            setattr(env, key, value)
    else:
        env.temperature = 85
        env.temperature_K = env.temperature + 273.15
        env.ph = 8.0
        env.wet_dry_cycle = True
    
    # Create network
    food_molecules = create_prebiotic_food_set()
    network = ChemicalNetwork(food_molecules, env)
    
    # Store history for threshold detection
    complexity_history = []
    molecule_history = []
    reaction_history = []
    energy_history = []
    
    # Run simulation with periodic updates
    update_interval = max(1, steps // 20)  # Send ~20 updates during the simulation
    
    for step in range(steps):
        if stop_simulation:
            break
        
        network.update()
        
        stats = network.get_statistics()
        analysis = analyze_complexity_emergence(network)
        
        # Store data for threshold detection
        complexity_history.append(analysis['complexity_score'])
        molecule_history.append(stats['molecules'])
        reaction_history.append(len(network.active_reactions))
        energy_history.append(stats['energy_currency'])
        
        if step % update_interval == 0 or step == steps - 1:
            # Detect emergence thresholds
            negentropy = calculate_negentropy(complexity_history)
            feedback = calculate_feedback_coefficient(complexity_history, energy_history)
            resilience = calculate_resilience(network, complexity_history)
            functional_phase = detect_functional_phase(stats, analysis)
            
            # Generate molecular network data for visualization
            molecular_network = extract_molecular_network_data(network)
            
            # Send update to client
            update_data = {
                'step': step,
                'total_steps': steps,
                'molecules': stats['molecules'],
                'reactions': len(network.active_reactions),
                'energy': stats['energy_currency'],
                'complexity': analysis['complexity_score'],
                'constraint_level': constraint_level,
                
                # Emergence threshold metrics
                'negentropy': negentropy,
                'feedback': feedback,
                'resilience': resilience,
                'functional_phase': functional_phase,
                'compartment_probability': calculate_compartmentalization_probability(network),
                
                # Molecular network data for visualization
                'molecular_network': molecular_network
            }
            socketio.emit('simulation_update', update_data)
            time.sleep(0.1)  # Small delay to prevent flooding the client
    
    return network

def extract_molecular_network_data(network):
    """
    Extract molecule and reaction data from the chemical network for visualization
    
    Args:
        network: ChemicalNetwork instance
        
    Returns:
        dict: Structured data for network visualization
    """
    try:
        # Extract molecules with their properties
        molecules = {}
        for molecule, count in network.molecules.items():
            # Skip molecules with zero count
            if count <= 0:
                continue
                
            # Extract key properties
            molecule_data = {
                'name': molecule.name,
                'count': count,
                'complexity': molecule.complexity,
                'is_amphiphilic': molecule.is_amphiphilic,
                'position': [molecule.position[0], molecule.position[1]] if hasattr(molecule, 'position') else None
            }
            
            molecules[molecule.name] = molecule_data
            
        # Extract active reactions
        reactions = []
        for reaction in network.active_reactions:
            reaction_data = {
                'reactants': [reactant.name for reactant in reaction.reactants],
                'products': [product.name for product in reaction.products],
                'is_catalyzed': reaction.is_catalyzed,
                'catalysts': [mol.name for mol in reaction.catalysts] if reaction.catalysts else []
            }
            reactions.append(reaction_data)
            
        return {
            'molecules': molecules,
            'reactions': reactions
        }
    except Exception as e:
        print(f"Error extracting molecular network data: {e}")
        return {'molecules': {}, 'reactions': []}

def calculate_negentropy(complexity_history):
    """Calculate the negentropy (order increase) from complexity history"""
    if len(complexity_history) < 2:
        return 0.0
    
    # Look at the rate of complexity increase 
    current = complexity_history[-1]
    previous = complexity_history[-2]
    
    # Calculate the normalized rate of increase
    increase = current - previous
    normalized = increase / max(previous, 0.1)  # Avoid division by zero
    
    return max(0.0, normalized)  # Only consider positive increases

def calculate_feedback_coefficient(complexity_history, energy_history):
    """Calculate entropy-catalysis feedback coefficient"""
    if len(complexity_history) < 3 or len(energy_history) < 3:
        return 0.0
    
    # Calculate complexity trend
    complexity_trend = complexity_history[-1] - complexity_history[-3]
    
    # Calculate energy efficiency (how much complexity per unit of energy)
    if energy_history[-1] == 0:
        energy_efficiency = 0
    else:
        energy_efficiency = complexity_history[-1] / energy_history[-1]
    
    # Calculate feedback coefficient
    feedback = max(0.0, complexity_trend * energy_efficiency / 5.0)
    
    # Cap at a reasonable value
    return min(1.0, feedback)

def detect_functional_phase(stats, analysis):
    """Detect which functional phase the system is in"""
    # Simple detection based on complexity and molecule counts
    complexity = analysis['complexity_score']
    molecules = stats['molecules']
    autocatalytic = analysis.get('autocatalytic_cycles', 0)
    
    if autocatalytic > 0 and complexity > 5:
        return "Catalytic Networks"
    elif complexity > 3:
        return "Reaction Cycles"
    elif molecules > 8:
        return "Molecular Diversity"
    else:
        return "None"

def calculate_resilience(network, complexity_history=None):
    """Calculate the resilience of the system to perturbations"""
    # In a full simulation this would involve actual perturbation testing
    # Here we'll use a simplified approach based on:
    # 1. Network connectivity (more connections = more resilient)
    # 2. Complexity stability (lower volatility in complexity = more resilient)
    
    try:
        # Calculate network connectivity
        stats = network.get_statistics()
        if stats['molecules'] == 0:
            return 0.0
        
        reactions_per_molecule = len(network.active_reactions) / stats['molecules']
        connectivity = min(1.0, reactions_per_molecule / 2.0)
        
        # Calculate complexity stability if history is available
        stability = 0.5  # Default mid-range value
        if complexity_history and len(complexity_history) >= 5:
            recent = complexity_history[-5:]
            mean = np.mean(recent)
            if mean > 0:
                std_dev = np.std(recent)
                coefficient_of_variation = std_dev / mean
                stability = max(0, min(1.0, 1.0 - coefficient_of_variation))
        
        # Combine the metrics (equal weighting for now)
        resilience = 0.5 * connectivity + 0.5 * stability
        
        return resilience
    
    except Exception as e:
        print(f"Error calculating resilience: {e}")
        return 0.0

def calculate_compartmentalization_probability(network):
    """Calculate the probability of compartmentalization using the formula:
    P(compartment) = P(amphiphilic molecules) × P(self-assembly | amphiphilic molecules)
    """
    try:
        stats = network.get_statistics()
        analysis = network.get_final_analysis()
        
        # In a full simulation, we would check for actual amphiphilic molecules
        # Here we use a simplified approach based on molecule count and diversity
        molecules_count = stats['molecules']
        complexity = analysis['complexity_score']
        
        # Simplified probability of amphiphilic molecules
        p_amphiphilic = min(0.8, molecules_count / 20)
        
        # Simplified probability of self-assembly given amphiphilic molecules exist
        p_self_assembly = min(0.9, complexity / 10)
        
        # Final compartmentalization probability
        p_compartment = p_amphiphilic * p_self_assembly
        
        return {
            'p_amphiphilic': p_amphiphilic,
            'p_self_assembly': p_self_assembly,
            'p_compartment': p_compartment
        }
    
    except Exception as e:
        print(f"Error calculating compartmentalization probability: {e}")
        return {
            'p_amphiphilic': 0.0,
            'p_self_assembly': 0.0,
            'p_compartment': 0.0
        }

def get_constraint_environment(constraint_level):
    """Get environment parameters for a specific constraint level"""
    params = {
        1: {  # Low constraint
            "temperature": 70,
            "ph": 7.0,
            "wet_dry_cycle": False,
            "energy_input": "high"
        },
        2: {  # Medium-low constraint
            "temperature": 80,
            "ph": 7.5,
            "wet_dry_cycle": True,
            "energy_input": "medium"
        },
        3: {  # Medium constraint
            "temperature": 85, 
            "ph": 8.0,
            "wet_dry_cycle": True,
            "energy_input": "medium",
            "metal_catalysts": True
        },
        4: {  # Medium-high constraint
            "temperature": 90,
            "ph": 8.5, 
            "wet_dry_cycle": True,
            "energy_input": "low",
            "temperature_gradient": True
        },
        5: {  # High constraint
            "temperature": 95,
            "ph": 9.0,
            "wet_dry_cycle": True,
            "energy_input": "very_low",
            "concentrated": True
        }
    }
    
    result = params[constraint_level]
    result["temperature_K"] = result["temperature"] + 273.15
    return result

def check_for_emergence_thresholds(data):
    """Check if any emergence thresholds have been crossed"""
    thresholds_crossed = []
    
    # Check each threshold metric
    if data.get('negentropy', 0) >= THRESHOLDS['negentropy']:
        thresholds_crossed.append('negentropy')
    
    if data.get('feedback', 0) >= THRESHOLDS['feedback']:
        thresholds_crossed.append('feedback')
    
    if data.get('resilience', 0) >= THRESHOLDS['resilience']:
        thresholds_crossed.append('resilience')
    
    if data.get('compartment_probability', {}).get('p_compartment', 0) >= THRESHOLDS['compartment']:
        thresholds_crossed.append('compartmentalization')
    
    # Emit event if any thresholds crossed
    if thresholds_crossed:
        socketio.emit('threshold_detection', {
            'step': data['step'],
            'thresholds': thresholds_crossed
        })
    
    return thresholds_crossed

if __name__ == "__main__":
    # Create template and static directories if they don't exist
    os.makedirs("templates", exist_ok=True)
    os.makedirs("static", exist_ok=True)
    
    # Run the server
    print("Starting visualization server at http://localhost:5000")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, allow_unsafe_werkzeug=True)