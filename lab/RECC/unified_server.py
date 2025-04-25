#!/usr/bin/env python3
# RECC MVP 1.5: Unified Server
# Combines RECC core functionality and visualization in a single server

import os
import sys
import json
import time
import threading
import argparse
from datetime import datetime

from flask import Flask, render_template, send_from_directory, request
from flask_socketio import SocketIO

# Import RECC components
from event_bus import global_event_bus, EventTypes
from recc import RECC, ConceptNetwork, Memory, Me
from visualization_utils import draw_concept_map, visualize_emotions

class UnifiedRECCServer:
    """
    Unified server that combines RECC core functionality with visualization
    capabilities in a single process
    """
    def __init__(self, port=5000, llm_function=None, initial_agent=None):
        # Create Flask app and SocketIO for communication
        self.app = Flask(__name__, 
                         static_folder='static',
                         template_folder='templates')
        self.socketio = SocketIO(self.app, cors_allowed_origins="*")
        self.port = port
        
        # Initialize RECC with the provided LLM function or use a default
        from llmentor import AI
        
        def default_llm(prompt, reset_history=False):
            ai = AI()
            return ai.answer(prompt, reset_history=reset_history)
            
        self.llm_function = llm_function or default_llm
        
        # Create the RECC instance integrated with our event system
        # If an initial agent is provided, use it instead of creating a new one
        if initial_agent:
            self.recc = initial_agent
        else:
            self.recc = RECC(self.llm_function, global_event_bus)
            
            # Automatically load the latest state file when starting up
            import glob
            import os
            
            if os.path.exists("./state"):
                state_files = glob.glob("./state/recc_state_*.json")
                if state_files:
                    print(f"Found {len(state_files)} existing state files.")
                    latest_state = max(state_files, key=os.path.getctime)
                    state = self.recc.state_manager.load_state(filepath=latest_state)
                    if state:
                        self.recc = self.recc.state_manager.apply_state(self.recc, state)
                        print(f"Loaded state from: {latest_state}")
                    else:
                        print("Failed to load state.")
        
        # Simulation control
        self.simulation_running = False
        self.simulation_thread = None
        self.stop_simulation = False
        self.learning_mode = False  # Track whether learning mode is active
        self.learning_paused = False  # Track whether learning is paused
        self.auto_step_delay = 3  # Delay between autonomous steps in seconds
        
        # Register routes and event handlers
        self._register_routes()
        self._register_socket_events()
        self._register_recc_event_handlers()
        
        # # Ensure necessary directories exist
        # os.makedirs("static", exist_ok=True)
        # os.makedirs("templates", exist_ok=True)
        
    def _register_routes(self):
        """Register HTTP routes for the Flask app"""
        
        @self.app.route('/')
        def index():
            """Serve the main visualization dashboard"""
            return render_template('index.html')
        
        @self.app.route('/static/<path:path>')
        def serve_static(path):
            """Serve static files"""
            return send_from_directory('static', path)
            
        @self.app.route('/api/status')
        def api_status():
            """Get RECC status information"""
            return {
                'status': 'learning' if self.simulation_running else 'idle',
                'learning_mode': self.learning_mode,
                'learning_paused': self.learning_paused,
                'memory_entries': len(self.recc.memory.entries),
                'concepts': len(self.recc.memory.concept_network.concepts),
                'emotional_state': self.recc.me.emotional_state
            }
            
    def _register_socket_events(self):
        """Register SocketIO events for real-time communication"""
        
        @self.socketio.on('connect')
        def handle_connect():
            """Handle client connection"""
            print('Client connected to RECC server')
            self.socketio.emit('status', {'status': 'Connected to RECC server'})
            
            # Send initial state if RECC has data
            if len(self.recc.memory.entries) > 0:
                self.send_current_state()
        
        @self.socketio.on('toggle_learning_mode')
        def handle_toggle_learning_mode(data):
            """Toggle autonomous learning mode on/off"""
            enable = data.get('enable', False)
            
            if enable and not self.learning_mode:
                # Start learning mode
                self.learning_mode = True
                self.learning_paused = False
                
                # Start simulation in a separate thread if not already running
                if not self.simulation_running:
                    self._start_learning_mode(data.get('steps', 100), data.get('delay', self.auto_step_delay))
                    
                self.socketio.emit('status', {'status': 'Learning mode activated'})
                self.socketio.emit('learning_mode_update', {
                    'active': True,
                    'paused': False
                })
                
            elif not enable and self.learning_mode:
                # Stop learning mode
                self.learning_mode = False
                self.learning_paused = False
                
                # Stop the simulation if it's running
                if self.simulation_running:
                    self.stop_simulation = True
                    
                self.socketio.emit('status', {'status': 'Learning mode deactivated'})
                self.socketio.emit('learning_mode_update', {
                    'active': False,
                    'paused': False
                })
        
        @self.socketio.on('pause_learning')
        def handle_pause_learning(data):
            """Pause or resume the learning process"""
            if not self.learning_mode:
                self.socketio.emit('error', {'message': 'Learning mode is not active'})
                return
                
            pause = data.get('pause', True)
            
            if pause and not self.learning_paused:
                # Pause learning
                self.learning_paused = True
                if self.simulation_running:
                    self.stop_simulation = True
                self.socketio.emit('status', {'status': 'Learning paused'})
                
            elif not pause and self.learning_paused:
                # Resume learning
                self.learning_paused = False
                if not self.simulation_running:
                    # Restart the paused learning process
                    self._start_learning_mode(data.get('steps', 100), data.get('delay', self.auto_step_delay))
                self.socketio.emit('status', {'status': 'Learning resumed'})
                
            self.socketio.emit('learning_mode_update', {
                'active': self.learning_mode,
                'paused': self.learning_paused
            })
            
        @self.socketio.on('start_simulation')
        def handle_start_simulation(data):
            """Start a RECC simulation - legacy method, redirects to toggle_learning_mode"""
            if self.simulation_running:
                self.socketio.emit('status', {'status': 'Simulation already running'})
                return
                
            # Get parameters with defaults
            steps = data.get('steps', 20)
            mode = data.get('mode', 'autonomous')
            
            # Update learning mode settings
            self.learning_mode = True
            self.learning_paused = False
            
            # Start learning mode
            self._start_learning_mode(steps, self.auto_step_delay)
            
            self.socketio.emit('status', {'status': 'Learning mode started'})
            self.socketio.emit('learning_mode_update', {
                'active': True,
                'paused': False
            })
        
        @self.socketio.on('stop_simulation')
        def handle_stop_simulation():
            """Stop the running simulation - legacy method, redirects to toggle_learning_mode"""
            if not self.simulation_running:
                self.socketio.emit('status', {'status': 'No simulation running'})
                return
                
            self.stop_simulation = True
            self.learning_mode = False
            self.learning_paused = False
            
            self.socketio.emit('status', {'status': 'Stopping learning mode...'})
            self.socketio.emit('learning_mode_update', {
                'active': False,
                'paused': False
            })
        
        @self.socketio.on('send_prompt')
        def handle_send_prompt(data):
            """Process a user-provided prompt in interactive dialogue mode"""
            prompt = data.get('prompt', '')
            if not prompt:
                self.socketio.emit('error', {'message': 'Empty prompt'})
                return
            
            # If in learning mode, check if it's paused first
            if self.learning_mode and not self.learning_paused:
                self.socketio.emit('error', {'message': 'Cannot send manual prompts while learning mode is active. Please pause learning first.'})
                return
                
            # Process prompt in a separate thread
            threading.Thread(target=self._process_prompt, args=(prompt, True)).start()
            self.socketio.emit('status', {'status': f'Processing prompt: "{prompt}"'})
            
        @self.socketio.on('adjust_parameter')
        def handle_adjust_parameter(data):
            """Adjust RECC parameters like emotional state"""
            param_type = data.get('type', '')
            param_name = data.get('name', '')
            param_value = data.get('value')
            
            if not param_type or not param_name or param_value is None:
                self.socketio.emit('error', {'message': 'Invalid parameter adjustment'})
                return
                
            # Handle emotional state adjustments
            if param_type == 'emotional_state' and param_name in self.recc.me.emotional_state:
                try:
                    value = float(param_value)
                    if 0.0 <= value <= 1.0:
                        self.recc.me.emotional_state[param_name] = value
                        self.socketio.emit('parameter_adjusted', {
                            'type': param_type,
                            'name': param_name,
                            'value': value
                        })
                        
                        # Also update the emotion history
                        self.recc.me.emotion_history.append({
                            'timestamp': datetime.now().isoformat(),
                            'state': self.recc.me.emotional_state.copy(),
                            'cycle': len(self.recc.memory.entries),
                            'user_adjusted': True
                        })
                    else:
                        self.socketio.emit('error', {'message': 'Emotion values must be between 0 and 1'})
                except ValueError:
                    self.socketio.emit('error', {'message': 'Invalid value format'})
            elif param_type == 'auto_step_delay':
                try:
                    value = float(param_value)
                    if value >= 0.5:  # At least 0.5 seconds between steps
                        self.auto_step_delay = value
                        self.socketio.emit('parameter_adjusted', {
                            'type': param_type,
                            'name': 'auto_step_delay',
                            'value': value
                        })
                    else:
                        self.socketio.emit('error', {'message': 'Delay must be at least 0.5 seconds'})
                except ValueError:
                    self.socketio.emit('error', {'message': 'Invalid value format'})
            else:
                self.socketio.emit('error', {'message': f'Unknown parameter: {param_type}.{param_name}'})
                
        @self.socketio.on('save_state')
        def handle_save_state():
            """Save RECC state to disk"""
            try:
                filepath = self.recc.state_manager.save_state(self.recc)
                self.socketio.emit('state_saved', {'filepath': filepath})
            except Exception as e:
                self.socketio.emit('error', {'message': f'Failed to save state: {str(e)}'})
                
        @self.socketio.on('load_state')
        def handle_load_state(data):
            """Load RECC state from disk"""
            session_id = data.get('session_id')
            
            try:
                state = self.recc.state_manager.load_state(session_id=session_id)
                if state:
                    self.recc = self.recc.state_manager.apply_state(self.recc, state)
                    self.send_current_state()
                    self.socketio.emit('state_loaded', {'success': True})
                else:
                    self.socketio.emit('error', {'message': 'Failed to load state'})
            except Exception as e:
                self.socketio.emit('error', {'message': f'Error loading state: {str(e)}'})
                
    def _start_learning_mode(self, steps, delay):
        """Start the autonomous learning mode in a separate thread"""
        if self.simulation_running:
            return
            
        # Start simulation in a separate thread
        self.stop_simulation = False
        self.simulation_thread = threading.Thread(
            target=self._run_learning_loop,
            args=(steps, delay)
        )
        self.simulation_running = True
        self.simulation_thread.start()
                
    def _register_recc_event_handlers(self):
        """Register handlers for RECC events to send updates to clients"""
        
        def on_cycle_complete(data):
            """Handle cycle completion events"""
            self.socketio.emit('cycle_complete', data)
            
            # Also send a comprehensive update
            self.send_current_state()
            
        def on_threshold_crossed(data):
            """Handle threshold crossing events"""
            self.socketio.emit('threshold_crossed', data)
            
        def on_concept_created(data):
            """Handle new concept creation events"""
            self.socketio.emit('concept_created', data)
            
        def on_emotional_change(data):
            """Handle emotional state changes"""
            self.socketio.emit('emotional_change', data)
            
        def on_prompt_generated(data):
            """Handle prompt generation events"""
            self.socketio.emit('prompt_generated', data)
            
        # Register with the event bus
        global_event_bus.subscribe(EventTypes.CYCLE_COMPLETE, on_cycle_complete)
        global_event_bus.subscribe(EventTypes.THRESHOLD_CROSSED, on_threshold_crossed)
        global_event_bus.subscribe(EventTypes.CONCEPT_CREATED, on_concept_created)
        global_event_bus.subscribe(EventTypes.EMOTIONAL_CHANGE, on_emotional_change)
        global_event_bus.subscribe(EventTypes.PROMPT_GENERATED, on_prompt_generated)
        
    def _run_learning_loop(self, steps, delay):
        """Run RECC autonomous learning cycle for a specified number of steps"""
        try:
            for step in range(steps):
                if self.stop_simulation or not self.learning_mode or self.learning_paused:
                    break
                    
                # Generate autonomous prompt
                prompt = self.recc.generate_prompt()
                self.socketio.emit('prompt_generated', {'prompt': prompt, 'step': step})
                
                # Process the prompt and get response
                self._process_prompt(prompt, False)  # False = not user-generated
                    
                # Small delay between autonomous cycles
                time.sleep(delay)
                
        except Exception as e:
            import traceback
            traceback.print_exc()
            self.socketio.emit('error', {'message': f'Learning cycle error: {str(e)}'})
            
        finally:
            self.simulation_running = False
            if self.learning_mode and not self.learning_paused:
                self.socketio.emit('status', {'status': 'Learning cycle complete'})
            else:
                self.socketio.emit('status', {'status': 'Learning cycle stopped'})
            
    def _process_prompt(self, prompt, user_generated=False):
        """Process a single prompt through the RECC system"""
        try:
            # If this is the first prompt or if a reset is needed, reset conversation history
            reset_history = False
            if (len(self.recc.memory.entries) == 0) or self.recc.reset_conversation_history:
                reset_history = True
                self.recc.reset_conversation_history = False
            
            # Handle the prompt differently based on whether it's user-generated or not
            if user_generated:
                # For user-generated prompts, use the dedicated method that ensures
                # the baby agent processes the input with its unique characteristics
                result = self.recc.process_user_input(prompt, reset_history)
                response = result['response']
                entry_id = result['entry_id']
                decision = result['decision']
            else:
                # For autonomous mode, continue using the same approach
                response = self.recc.llm(prompt, reset_history=reset_history)
                
                # Add to RECC memory and reflect
                entry = self.recc.memory.add(prompt, response, self.recc.state.copy())
                entry_id = entry['id']
                decision = self.recc.me.reflect()
            
            # Create update with core information
            update = {
                'prompt': prompt,
                'response': response,
                'entry_id': entry_id,
                'cycle': len(self.recc.memory.entries),
                'user_generated': user_generated,
                'timestamp': datetime.now().isoformat()
            }
            
            # Send the update to all clients
            self.socketio.emit('recc_response', update)
            
            # Save visualizations periodically (not on every prompt)
            if len(self.recc.memory.entries) % 5 == 0:
                self._save_visualizations()
                
            # Save state periodically to ensure persistence
            if len(self.recc.memory.entries) % 10 == 0:
                self.recc.state_manager.save_state(self.recc)
            
        except Exception as e:
            import traceback
            traceback.print_exc()
            self.socketio.emit('error', {'message': f'Error processing prompt: {str(e)}'})
            
    def _save_visualizations(self):
        """Generate and save visualization images"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        try:
            # Save concept network visualization
            os.makedirs("static/visualizations", exist_ok=True)
            concept_map_path = f"static/visualizations/concept_map_{timestamp}.png"
            draw_concept_map(concept_network=self.recc.memory.concept_network, save_path=concept_map_path)
            
            # Save emotional state visualization if we have enough history
            emotion_path = None
            if len(self.recc.me.emotion_history) > 2:
                emotion_path = f"static/visualizations/emotions_{timestamp}.png"
                visualize_emotions(self.recc.me, save_path=emotion_path)
                
            # Notify clients about new visualizations
            self.socketio.emit('visualization_saved', {
                'concept_map': concept_map_path,
                'emotions': emotion_path
            })
            
        except Exception as e:
            print(f"Error saving visualizations: {e}")
            
    def send_current_state(self):
        """Send the current state of RECC to clients"""
        # Extract metrics
        metrics = self._extract_metrics()
        
        # Extract concept network
        concept_network = self._extract_concept_network()
        
        # Create state update
        update = {
            'timestamp': datetime.now().isoformat(),
            'metrics': metrics,
            'concept_network': concept_network,
            'emotional_state': self.recc.me.emotional_state,
            'memory_size': len(self.recc.memory.entries),
            'theories': self.recc.me.personal_theories,
            'learning_mode': self.learning_mode,
            'learning_paused': self.learning_paused
        }
        
        # Send to all clients
        self.socketio.emit('recc_state_update', update)
        
    def _extract_metrics(self):
        """Extract key metrics from RECC for reporting"""
        memory = self.recc.memory
        
        # Get basic metrics
        novelty_gradient, reuse_gradient = memory.compute_gradients()
        recent = memory.get_recent(5)
        avg_novelty = sum(e.get('novelty', 0) for e in recent) / max(len(recent), 1)
        
        # Get network statistics
        network_stats = memory.concept_network.get_network_stats()
        
        return {
            'memory_size': len(memory.entries),
            'concept_count': network_stats['concept_count'],
            'relation_count': network_stats['relation_count'],
            'avg_connections': round(network_stats['avg_connections'], 2),
            'network_density': round(network_stats['density'], 3),
            'novelty_gradient': novelty_gradient,
            'reuse_gradient': reuse_gradient,
            'avg_novelty': round(avg_novelty, 3),
            'theory_count': len(self.recc.me.personal_theories)
        }
        
    def _extract_concept_network(self):
        """Extract concept network data for visualization"""
        network = self.recc.memory.concept_network
        
        # Performance optimization: pre-filter concepts and relations here
        # rather than sending the entire network to the client
        
        # Get total counts for metrics
        total_concepts = len(network.concepts)
        total_relations = len(network.relations)
        
        # If network is smaller than threshold, send everything
        # Otherwise, filter to most important nodes
        MAX_NODES_TO_SEND = 150  # Limit nodes to prevent UI freezing
        
        if total_concepts <= MAX_NODES_TO_SEND:
            # For small networks, send everything
            concept_ids = list(network.concepts.keys())
        else:
            # For large networks, get the most important concepts
            # First try to get central concepts by betweenness or activation
            try:
                # Combine centrality and activation for importance
                importance_dict = {}
                
                # Get central concepts (up to 75)
                central_concepts = network.get_central_concepts(n=75)
                
                # Also include frequently reused concepts
                reused_concepts = []
                for concept_id, concept in network.concepts.items():
                    reuse_count = concept.get('reuse_count', 0)
                    if reuse_count > 1:
                        reused_concepts.append((concept_id, reuse_count))
                
                # Sort and get top reused concepts
                reused_concepts.sort(key=lambda x: x[1], reverse=True)
                top_reused = [c[0] for c in reused_concepts[:75]]
                
                # Get active concepts
                active_concepts = network.get_active_concepts(threshold=0.5)
                
                # Combine all important concepts, prioritizing diversity
                combined_concepts = []
                for concept_id in central_concepts:
                    if concept_id not in combined_concepts:
                        combined_concepts.append(concept_id)
                        
                for concept_id in top_reused:
                    if concept_id not in combined_concepts:
                        combined_concepts.append(concept_id)
                
                for concept_id in active_concepts:
                    if concept_id not in combined_concepts:
                        combined_concepts.append(concept_id)
                
                # Cap at MAX_NODES_TO_SEND
                concept_ids = combined_concepts[:MAX_NODES_TO_SEND]
            except Exception as e:
                # Fallback: just take the first MAX_NODES_TO_SEND concepts
                print(f"Error selecting important concepts: {e}")
                concept_ids = list(network.concepts.keys())[:MAX_NODES_TO_SEND]
        
        # Create a set for faster lookups
        concept_id_set = set(concept_ids)
        
        # Extract nodes (concepts)
        nodes = []
        for concept_id in concept_ids:
            if concept_id in network.concepts:  # Safety check
                concept = network.concepts[concept_id]
                nodes.append({
                    'id': concept_id,
                    'name': concept['name'],
                    'activation': concept.get('activation', 0.5),
                    'reuse_count': concept.get('reuse_count', 0),
                    'created': concept.get('created', '')
                })
            
        # Extract only edges that connect the selected concepts
        edges = []
        for relation in network.relations:
            source = relation.get('source', '')
            target = relation.get('target', '')
            if source in concept_id_set and target in concept_id_set:
                edges.append({
                    'id': relation.get('id', ''),
                    'source': source,
                    'target': target,
                    'type': relation.get('type', 'association'),
                    'weight': relation.get('weight', 0.5)
                })
        
        # Include metadata about filtering for UI awareness
        return {
            'nodes': nodes,
            'edges': edges,
            'metadata': {
                'total_concepts': total_concepts,
                'total_relations': total_relations,
                'filtered_concepts': len(nodes),
                'filtered_relations': len(edges)
            }
        }
        
    def run(self):
        """Start the unified RECC server"""
        print(f"Starting Unified RECC Server at http://localhost:{self.port}")
        print("Press Ctrl+C to stop the server")
        
        self.socketio.run(self.app, host='0.0.0.0', port=self.port, debug=False, allow_unsafe_werkzeug=True)

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Start the Unified RECC Server')
    parser.add_argument('--port', type=int, default=5000, help='Port to run the server on')
    parser.add_argument('--load-state', help='Load a saved state by session ID')
    args = parser.parse_args()
    
    # Create and run the server
    server = UnifiedRECCServer(port=args.port)
    
    # Load state if requested
    if args.load_state:
        state = server.recc.state_manager.load_state(session_id=args.load_state)
        if state:
            server.recc = server.recc.state_manager.apply_state(server.recc, state)
            print(f"Loaded state from session: {args.load_state}")
        else:
            print(f"Failed to load state: {args.load_state}")
            
    # Run the server
    server.run()