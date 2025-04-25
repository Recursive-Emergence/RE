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
    def __init__(self, port=5000, llm_function=None):
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
        self.recc = RECC(self.llm_function, global_event_bus)
        
        # Simulation control
        self.simulation_running = False
        self.simulation_thread = None
        self.stop_simulation = False
        
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
                'status': 'running' if self.simulation_running else 'idle',
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
        
        @self.socketio.on('start_simulation')
        def handle_start_simulation(data):
            """Start a RECC simulation"""
            if self.simulation_running:
                self.socketio.emit('status', {'status': 'Simulation already running'})
                return
                
            # Get parameters with defaults
            steps = data.get('steps', 20)
            mode = data.get('mode', 'autonomous')
            
            # Start simulation in a separate thread
            self.stop_simulation = False
            self.simulation_thread = threading.Thread(
                target=self._run_recc_simulation,
                args=(steps, mode)
            )
            self.simulation_running = True
            self.simulation_thread.start()
            
            self.socketio.emit('status', {'status': 'RECC simulation started'})
        
        @self.socketio.on('stop_simulation')
        def handle_stop_simulation():
            """Stop the running simulation"""
            if not self.simulation_running:
                self.socketio.emit('status', {'status': 'No simulation running'})
                return
                
            self.stop_simulation = True
            self.socketio.emit('status', {'status': 'Stopping simulation...'})
        
        @self.socketio.on('send_prompt')
        def handle_send_prompt(data):
            """Process a user-provided prompt"""
            prompt = data.get('prompt', '')
            if not prompt:
                self.socketio.emit('error', {'message': 'Empty prompt'})
                return
                
            # Process prompt in a separate thread
            threading.Thread(target=self._process_prompt, args=(prompt,)).start()
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
            
        # Register with the event bus
        global_event_bus.subscribe(EventTypes.CYCLE_COMPLETE, on_cycle_complete)
        global_event_bus.subscribe(EventTypes.THRESHOLD_CROSSED, on_threshold_crossed)
        global_event_bus.subscribe(EventTypes.CONCEPT_CREATED, on_concept_created)
        global_event_bus.subscribe(EventTypes.EMOTIONAL_CHANGE, on_emotional_change)
        
    def _run_recc_simulation(self, steps, mode):
        """Run RECC simulation for a specified number of steps"""
        try:
            for step in range(steps):
                if self.stop_simulation:
                    break
                    
                # In autonomous mode, RECC generates its own prompts
                if mode == 'autonomous':
                    prompt = self.recc.generate_prompt()
                    self.socketio.emit('prompt_generated', {'prompt': prompt, 'step': step})
                    self._process_prompt(prompt)
                else:
                    # In interactive mode, wait for the client to send prompts
                    self.socketio.emit('waiting_for_prompt', {'step': step})
                    # Just continue - prompts will be processed via socket events
                    time.sleep(2)
                    continue
                    
                # Small delay between autonomous cycles
                time.sleep(1)
                
        except Exception as e:
            import traceback
            traceback.print_exc()
            self.socketio.emit('error', {'message': f'Simulation error: {str(e)}'})
            
        finally:
            self.simulation_running = False
            self.socketio.emit('status', {'status': 'Simulation complete'})
            
    def _process_prompt(self, prompt):
        """Process a single prompt through the RECC system"""
        try:
            # Get response from LLM through RECC
            response = self.recc.llm(prompt)
            
            # Add to RECC memory and reflect
            entry = self.recc.memory.add(prompt, response, self.recc.state.copy())
            decision = self.recc.me.reflect()
            
            # Create update with core information
            update = {
                'prompt': prompt,
                'response': response,
                'entry_id': entry['id'],
                'cycle': len(self.recc.memory.entries),
                'timestamp': datetime.now().isoformat()
            }
            
            # Send the update to all clients
            self.socketio.emit('recc_response', update)
            
            # Save visualizations
            self._save_visualizations()
            
        except Exception as e:
            import traceback
            traceback.print_exc()
            self.socketio.emit('error', {'message': f'Error processing prompt: {str(e)}'})
            
    def _save_visualizations(self):
        """Generate and save visualization images"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        try:
            # Save concept network visualization
            concept_map_path = f"visualization/static/concept_map_{timestamp}.png"
            draw_concept_map(concept_network=self.recc.memory.concept_network, save_path=concept_map_path)
            
            # Save emotional state visualization if we have enough history
            emotion_path = None
            if len(self.recc.me.emotion_history) > 2:
                emotion_path = f"visualization/static/emotions_{timestamp}.png"
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
            'theories': self.recc.me.personal_theories
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
        
        # Extract nodes (concepts)
        nodes = []
        for concept_id, concept in network.concepts.items():
            nodes.append({
                'id': concept_id,
                'name': concept['name'],
                'activation': concept.get('activation', 0.5),
                'reuse_count': concept.get('reuse_count', 0),
                'created': concept.get('created', '')
            })
            
        # Extract edges (relations)
        edges = []
        for relation in network.relations:
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