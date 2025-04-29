import sys
import os
import time
import json

# Ensure the core modules can be found
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.independent_mind import IndependentMind

def run_simulation(cycles=10):
    """
    Initializes and runs the IndependentMind for a specified number of cycles.
    """
    print("Initializing Independent Mind...")
    mind = IndependentMind()
    print(f"Mind initialized. Birth time: {mind.internal_state['birth_time']:.2f}")
    print("-" * 30)

    results_history = []

    for i in range(cycles):
        print(f"--- Cycle {i+1}/{cycles} ---")
        
        # In this simple run, we provide no external input
        external_input = None 
        
        start_time = time.time()
        cycle_results = mind.autonomous_cycle(external_input)
        end_time = time.time()
        
        print(f"Cycle Duration: {end_time - start_time:.4f} seconds")
        
        # Print a summary of the cycle results
        print(f"  Computed Entropy: {cycle_results.get('computed_entropy', 'N/A'):.4f}")
        print(f"  Emotions Before: {cycle_results.get('emotions_before', {})}")
        print(f"  Emotions After: {cycle_results.get('emotions_after', {})}")
        print(f"  Behavior: {cycle_results.get('behavior_type', 'N/A')} - {cycle_results.get('selected_behavior', 'N/A')}")
        print(f"  Reflection Occurred: {cycle_results.get('reflection_occurred', False)}")
        if cycle_results.get('cognitive_metrics'):
             print(f"  Cognitive Complexity: {cycle_results['cognitive_metrics'].get('memory_complexity', 'N/A'):.4f}")

        results_history.append(cycle_results)
        
        # Optional: Add a small delay between cycles if needed
        # time.sleep(0.1) 

    print("-" * 30)
    print("Simulation Complete.")
    
    # Print final state summary
    final_summary = mind.get_state_summary()
    print("\nFinal Mind State Summary:")
    print(json.dumps(final_summary, indent=2, default=str)) # Use default=str for non-serializable types like deque

    # Optionally save results history to a file
    # with open("mind_run_history.json", "w") as f:
    #     json.dump(results_history, f, indent=2, default=str)
    # print("\nResults history saved to mind_run_history.json")

if __name__ == "__main__":
    num_cycles = 20 # Run for 20 cycles
    run_simulation(num_cycles)
