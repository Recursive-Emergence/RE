"""
RECC: Recursive Emergent Conscious Core - MVP 1.5
Main entry point for the RECC system

This file serves as the entry point for the RECC system, importing the components from
their respective modules and providing convenient access to the main RECC class.
"""
import os
import glob
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

# --- Main Execution ---
if __name__ == '__main__':
    # Initialize agent
    agent = RECC(openai_llm)
    
    # Check for existing state
    if os.path.exists("./state"):
        state_files = glob.glob("./state/recc_state_*.json")
        if state_files:
            print(f"Found {len(state_files)} existing state files.")
            load_state = input("Load latest state? (y/n): ").lower() == 'y'
            if load_state:
                latest_state = max(state_files, key=os.path.getctime)
                state = agent.state_manager.load_state(filepath=latest_state)
                if state:
                    agent = agent.state_manager.apply_state(agent, state)
                    print(f"Loaded state from: {latest_state}")
                else:
                    print("Failed to load state.")
    
    # Run autonomous loop
    print("🧠 Starting RECC MVP 1.5 autonomous loop...")
    agent.autonomous_loop(steps=15, delay=3, save_interval=10)
