"""
RECC: Recursive Emergent Conscious Core - MVP 1.5
Main entry point for the RECC system

This file serves as the entry point for the RECC system, importing the components from
their respective modules and providing convenient access to the main RECC class.
"""
import os
import glob
import argparse
from datetime import datetime

# Import components from modularized structure
from components.concept_network import ConceptNetwork
from components.memory import Memory
from components.reflective_core import Me
from components.state_manager import StateManager
from components.recc_agent import RECC

# Import event bus for global access
from event_bus import global_event_bus, EventTypes

# Import visualization utilities
try:
    from visualization_utils import draw_concept_map, visualize_emotions
except ImportError:
    print("Warning: Visualization utilities not found. Visualizations will be disabled.")

# Default LLM implementation
def openai_llm(prompt, reset_history=False):
    """Default LLM implementation using OpenAI via llmentor"""
    from llmentor import AI
    ai = AI()
    return ai.answer(prompt, reset_history=reset_history)

def launch_unified_server(agent, port=5000):
    """Launch the unified visualization server with the initialized agent"""
    try:
        from unified_server import UnifiedRECCServer
        server = UnifiedRECCServer(port=port, initial_agent=agent)
        print(f"🌐 Starting RECC Web UI on http://localhost:{port}")
        server.run()
        return True
    except ImportError as e:
        print(f"Error: Could not launch unified server: {e}")
        print("Make sure 'flask' and 'flask_socketio' are installed")
        return False

# --- Main Execution ---
if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Start RECC agent system')
    parser.add_argument('--web-ui', action='store_true', help='Launch with web UI')
    parser.add_argument('--port', type=int, default=5000, help='Web UI port (if --web-ui is enabled)')
    parser.add_argument('--steps', type=int, default=15, help='Number of autonomous steps to run')
    parser.add_argument('--delay', type=int, default=3, help='Delay between autonomous steps')
    parser.add_argument('--save-interval', type=int, default=10, help='Save interval for state')
    args = parser.parse_args()
    
    # Initialize agent
    agent = RECC(openai_llm, global_event_bus)
    
    # Check for existing state
    if os.path.exists("./state"):
        state_files = glob.glob("./state/recc_state_*.json")
        if state_files:
            print(f"Found {len(state_files)} existing state files.")
            latest_state = max(state_files, key=os.path.getctime)
            state = agent.state_manager.load_state(filepath=latest_state)
            if state:
                agent = agent.state_manager.apply_state(agent, state)
                print(f"Loaded state from: {latest_state}")
            else:
                print("Failed to load state.")
    
    if args.web_ui:
        # Launch with web UI for both autonomous and interactive modes
        launch_unified_server(agent, port=args.port)
    else:
        # Run traditional autonomous loop
        print("🧠 Starting RECC MVP 1.5 autonomous loop...")
        agent.autonomous_loop(steps=args.steps, delay=args.delay, save_interval=args.save_interval)
