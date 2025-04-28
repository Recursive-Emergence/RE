#!/usr/bin/env python3
# RECC MVP 1.6: Unified Server
# Combines RECC core functionality, recursive reflection, and visualization in a single server

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
from components.recc_integration import RECC_MVP16
from visualization_utils import draw_concept_map, visualize_emotions

class UnifiedRECCServer:
    """
    Unified server that combines RECC core functionality with visualization
    capabilities in a single process
    """
    def __init__(self, port=5000, llm_function=None, initial_agent=None, use_mvp16=True):
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
            # Choose between MVP 1.5 and MVP 1.6 implementations
            if use_mvp16:
                print("Initializing with MVP 1.6 integration...")
                self.recc = RECC_MVP16(self.llm_function, global_event_bus)
                self.is_mvp16 = True
            else:
                self.recc = RECC(self.llm_function, global_event_bus)
                self.is_mvp16 = False
            
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
        
        @self.app.route('/recursive')
        def recursive():
            """Serve the recursive reflection visualization (MVP 1.6)"""
            return render_template('recursive.html')
        
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
                'memory_entries': len(self.recc.memory.entries) if hasattr(self.recc, 'memory') else len(self.recc.hybrid_memory.components['reference'].entries) if hasattr(self.recc, 'hybrid_memory') else 0,
                'concepts': len(self.recc.memory.concept_network.concepts) if hasattr(self.recc, 'memory') and hasattr(self.recc.memory, 'concept_network') else 0,
                'emotional_state': self.recc.me.emotional_state if hasattr(self.recc, 'me') else self.recc.state.get('emotional_state', {}) if hasattr(self.recc, 'state') else {},
                'mvp_version': '1.6' if self.is_mvp16 else '1.5'
            }
            
    def _register_socket_events(self):
        """Register SocketIO events for real-time communication"""
        
        @self.socketio.on('connect')
        def handle_connect():
            """Handle client connection"""
            print('Client connected to RECC server')
            self.socketio.emit('status', {'status': 'Connected to RECC server'})
            
            # Send initial state if RECC has data
            if (hasattr(self.recc, 'memory') and len(self.recc.memory.entries) > 0) or \
               (hasattr(self.recc, 'hybrid_memory') and len(self.recc.hybrid_memory.components['reference'].entries) > 0):
                self.send_current_state()
                
                # For MVP 1.6, also send recursive reflection data
                if self.is_mvp16 and hasattr(self.recc, 'reflection'):
                    self.send_recursive_data()
        
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

        # ... [rest of existing socket events remain unchanged]
        
        @self.socketio.on('run_cycles')
        def handle_run_cycles(data):
            """Run a specific number of recursive reflection cycles (MVP 1.6)"""
            if not self.is_mvp16:
                self.socketio.emit('error', {'message': 'This function is only available in MVP 1.6'})
                return
                
            steps = data.get('steps', 10)
            
            # Run the cycles in a separate thread
            threading.Thread(target=self._run_recursive_cycles, args=(steps,)).start()
            self.socketio.emit('status', {'status': f'Running {steps} recursive cycles...'})
        
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

    def _run_recursive_cycles(self, steps):
        """Run recursive reflection cycles for MVP 1.6"""
        if not hasattr(self.recc, 'autonomous_cycle'):
            self.socketio.emit('error', {'message': 'Recursive autonomous cycle not available'})
            return
            
        try:
            # Run the autonomous cycles
            results = self.recc.autonomous_cycle(steps=steps)
            
            # Emit results and update visualization
            self.socketio.emit('cycles_complete', {
                'steps': steps,
                'results': results.get('results', []),
                'metrics': self.recc.get_performance_metrics() if hasattr(self.recc, 'get_performance_metrics') else {}
            })
            
            # Send updated recursive data
            self.send_recursive_data()
            
        except Exception as e:
            import traceback
            traceback.print_exc()
            self.socketio.emit('error', {'message': f'Error running recursive cycles: {str(e)}'})

    def send_recursive_data(self):
        """Send recursive reflection data for visualization (MVP 1.6)"""
        if not self.is_mvp16 or not hasattr(self.recc, 'reflection'):
            return
            
        try:
            # Get reflection visualization data
            viz_data = self.recc.visualize_recursive_depth()
            
            # Get performance metrics
            metrics = self.recc.get_performance_metrics()
            
            # Send to clients
            self.socketio.emit('recursive_reflection_update', viz_data)
            self.socketio.emit('performance_update', metrics)
            
            # Also send concept hierarchy data if available
            if hasattr(self.recc.hybrid_memory, 'components') and 'reference' in self.recc.hybrid_memory.components:
                ref_memory = self.recc.hybrid_memory.components['reference']
                if hasattr(ref_memory, 'concept_hierarchy'):
                    self.socketio.emit('concept_hierarchy_update', {
                        'hierarchy': ref_memory.concept_hierarchy,
                        'depth': self.recc.hybrid_memory.emergent_properties.get('concept_hierarchy_depth', 1)
                    })
            
        except Exception as e:
            print(f"Error sending recursive data: {e}")
    
    def _process_prompt(self, prompt, user_generated=False):
        """Process a single prompt through the RECC system"""
        try:
            # Process differently based on MVP version
            if self.is_mvp16:
                # For MVP 1.6, use the integrated process_input method
                result = self.recc.process_input({
                    'prompt': prompt,
                    'user_input': True
                })
                
                response = result.get('memory_result', {}).get('response', 'No response generated')
                entry_id = result.get('memory_result', {}).get('id', 'unknown')
                
                # Send the reflection data update
                self.send_recursive_data()
            else:
                # MVP 1.5 processing (existing code)
                # If this is the first prompt or if a reset is needed, reset conversation history
                reset_history = False
                if (len(self.recc.memory.entries) == 0) or self.recc.reset_conversation_history:
                    reset_history = True
                    self.recc.reset_conversation_history = False
                
                # Handle the prompt differently based on whether it's user-generated or not
                if user_generated:
                    # For user-generated prompts, use the dedicated method
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
                'cycle': len(self.recc.memory.entries) if hasattr(self.recc, 'memory') else len(self.recc.hybrid_memory.components['reference'].entries) if hasattr(self.recc, 'hybrid_memory') else 0,
                'user_generated': user_generated,
                'timestamp': datetime.now().isoformat()
            }
            
            # Send the update to all clients
            self.socketio.emit('recc_response', update)
            
            # Send current state
            self.send_current_state()
                
        except Exception as e:
            import traceback
            traceback.print_exc()
            self.socketio.emit('error', {'message': f'Error processing prompt: {str(e)}'})
            
    def _run_learning_loop(self, steps, delay):
        """Run RECC autonomous learning cycle for a specified number of steps"""
        try:
            if self.is_mvp16:
                # For MVP 1.6, use the autonomous_cycle method directly
                results = self.recc.autonomous_cycle(steps=steps)
                
                # Send recursive data update
                self.send_recursive_data()
                
                # Send current state
                self.send_current_state()
            else:
                # For MVP 1.5, use the original implementation
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
            
    def send_current_state(self):
        """Send the current state of RECC to clients"""
        if self.is_mvp16:
            # For MVP 1.6, use the hybrid memory and reflection system
            metrics = self._extract_mvp16_metrics()
        else:
            # For MVP 1.5, use the original implementation
            metrics = self._extract_metrics()
        
        # Create state update
        update = {
            'timestamp': datetime.now().isoformat(),
            'metrics': metrics,
            'mvp_version': '1.6' if self.is_mvp16 else '1.5',
            'learning_mode': self.learning_mode,
            'learning_paused': self.learning_paused
        }
        
        # Add version-specific information
        if self.is_mvp16:
            if hasattr(self.recc, 'reflection'):
                reflection_metrics = self.recc.reflection.get_meta_cognition_report()
                update['reflection_metrics'] = reflection_metrics
                
            if hasattr(self.recc, 'get_performance_metrics'):
                update['performance_metrics'] = self.recc.get_performance_metrics()
                
            if hasattr(self.recc, 'hybrid_memory'):
                # Send concept data from hybrid memory
                if 'reference' in self.recc.hybrid_memory.components:
                    ref_memory = self.recc.hybrid_memory.components['reference']
                    update['concept_network'] = self._extract_mvp16_concept_network(ref_memory)
                
                # Send emergent properties
                update['emergent_properties'] = self.recc.hybrid_memory.emergent_properties
        else:
            # Original MVP 1.5 concept network extraction
            update['concept_network'] = self._extract_concept_network()
            update['emotional_state'] = self.recc.me.emotional_state
            update['theories'] = self.recc.me.personal_theories
        
        # Send to all clients
        self.socketio.emit('recc_state_update', update)
        
    def _extract_mvp16_metrics(self):
        """Extract key metrics from RECC MVP 1.6 for reporting"""
        metrics = {}
        
        try:
            # Get hybrid memory metrics
            if hasattr(self.recc, 'hybrid_memory'):
                hybrid = self.recc.hybrid_memory
                
                # Get reference memory metrics
                if 'reference' in hybrid.components:
                    ref_memory = hybrid.components['reference']
                    metrics['memory_size'] = len(ref_memory.entries) if hasattr(ref_memory, 'entries') else 0
                    metrics['concept_count'] = len(ref_memory.concepts) if hasattr(ref_memory, 'concepts') else 0
                    metrics['relation_count'] = len(ref_memory.relations) if hasattr(ref_memory, 'relations') else 0
                
                # Get emergent property metrics
                metrics['concept_hierarchy_depth'] = hybrid.emergent_properties.get('concept_hierarchy_depth', 0)
                metrics['strategy_sophistication'] = hybrid.emergent_properties.get('strategy_sophistication', 0)
            
            # Get reflection metrics
            if hasattr(self.recc, 'reflection'):
                reflection = self.recc.reflection
                metrics['effective_recursive_depth'] = reflection.metrics.get('effective_depth', 0)
                metrics['cross_level_modifications'] = reflection.metrics.get('cross_level_modifications', 0)
                metrics['active_reflection_levels'] = sum(1 for level in reflection.reflection_levels if level['state'] == 'active')
            
            # Get performance metrics
            if hasattr(self.recc, 'get_performance_metrics'):
                perf = self.recc.get_performance_metrics()
                metrics.update(perf)
                
        except Exception as e:
            print(f"Error extracting MVP 1.6 metrics: {e}")
            import traceback
            traceback.print_exc()
            
        return metrics
        
    def _extract_mvp16_concept_network(self, ref_memory):
        """Extract concept network data from MVP 1.6 reference memory"""
        try:
            # Define a reasonable limit for nodes to visualize
            MAX_NODES = 50
            
            # Get concepts
            if not hasattr(ref_memory, 'concepts'):
                return {'nodes': [], 'edges': [], 'metadata': {'filtered_concepts': 0}}
                
            concepts = ref_memory.concepts
            
            # Get active concepts first
            active_concepts = ref_memory.get_active_concepts(threshold=0.6) if hasattr(ref_memory, 'get_active_concepts') else []
            
            # Get central concepts if active list is too small
            if len(active_concepts) < 10 and hasattr(ref_memory, 'get_central_concepts'):
                central = ref_memory.get_central_concepts(n=20)
                for c in central:
                    if c not in active_concepts:
                        active_concepts.append(c)
            
            # Limit to max nodes
            concept_ids = active_concepts[:MAX_NODES]
            concept_id_set = set(concept_ids)
            
            # Extract nodes
            nodes = []
            for concept_id in concept_ids:
                if concept_id in concepts:
                    concept = concepts[concept_id]
                    nodes.append({
                        'id': concept_id,
                        'name': concept.get('name', 'Unnamed'),
                        'activation': concept.get('activation', 0.5),
                        'level': concept.get('abstraction_level', 0),
                        'isRecent': concept.get('is_recent', False)
                    })
            
            # Extract edges
            edges = []
            if hasattr(ref_memory, 'relations'):
                for relation in ref_memory.relations:
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
            
            # Include metadata
            return {
                'nodes': nodes,
                'edges': edges,
                'metadata': {
                    'total_concepts': len(concepts),
                    'total_relations': len(ref_memory.relations) if hasattr(ref_memory, 'relations') else 0,
                    'filtered_concepts': len(nodes),
                    'filtered_relations': len(edges),
                    'focus_type': 'active_concepts'
                }
            }
            
        except Exception as e:
            print(f"Error extracting MVP 1.6 concept network: {e}")
            return {'nodes': [], 'edges': [], 'metadata': {'error': str(e)}}

    # ... [keep the rest of the existing methods]
        
    def run(self):
        """Start the unified RECC server"""
        version = "1.6" if self.is_mvp16 else "1.5"
        print(f"Starting Unified RECC Server (MVP {version}) at http://localhost:{self.port}")
        print("Press Ctrl+C to stop the server")
        
        self.socketio.run(self.app, host='0.0.0.0', port=self.port, debug=False, allow_unsafe_werkzeug=True)

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Start the Unified RECC Server')
    parser.add_argument('--port', type=int, default=5000, help='Port to run the server on')
    parser.add_argument('--load-state', help='Load a saved state by session ID')
    parser.add_argument('--mvp15', action='store_true', help='Use MVP 1.5 implementation instead of 1.6')
    args = parser.parse_args()
    
    # Create and run the server
    server = UnifiedRECCServer(port=args.port, use_mvp16=not args.mvp15)
    
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