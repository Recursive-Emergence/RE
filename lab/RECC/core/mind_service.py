import sys
import os
import time
import json
import random
import glob
import argparse
import threading
import logging
from flask import Flask, request, jsonify

# Ensure the core modules can be found
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.independent_mind import IndependentMind

# Configuration
CHECKPOINT_DIR = "./data/checkpoints"  # Directory for saving checkpoints
CHECKPOINT_INTERVAL = 5  # Save state every 5 cycles
MAX_CHECKPOINTS = 5  # Maximum number of regular checkpoints to keep
LOG_DIR = "./data/logs"  # Directory for logs
DEFAULT_CYCLES = 1000  # Default number of cycles to run in autonomous mode
WEB_PORT = 5000  # Default port for web service

# Setup logging
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(f"{LOG_DIR}/mind_service.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("mind_service")

# Create Flask app for web service mode
app = Flask(__name__)

# Global mind instance
mind = None
mind_lock = threading.Lock()
mind_thread = None
mind_running = False
stats = {
    "total_cycles": 0,
    "start_time": None,
    "last_save_time": None
}

def cleanup_old_checkpoints(keep_count=MAX_CHECKPOINTS):
    """
    Removes old checkpoint files, keeping only the most recent ones.
    Final checkpoints are always preserved.
    
    Args:
        keep_count: Number of regular checkpoints to keep (not counting finals)
    """
    if not os.path.exists(CHECKPOINT_DIR):
        return
    
    # Get all checkpoint files
    checkpoint_files = glob.glob(os.path.join(CHECKPOINT_DIR, "mind_state_cycle_*.pkl"))
    
    # Separate regular and final checkpoints
    regular_checkpoints = [f for f in checkpoint_files if "_final.pkl" not in f]
    final_checkpoints = [f for f in checkpoint_files if "_final.pkl" in f]
    
    # Extract cycle number for sorting
    def extract_cycle_number(filename):
        parts = filename.split('_cycle_')[-1].split('.')[0]
        numeric_part = ''.join(c for c in parts.split('_')[0] if c.isdigit())
        return int(numeric_part) if numeric_part else 0
    
    # Sort regular checkpoints by cycle number
    regular_checkpoints.sort(key=extract_cycle_number)
    
    checkpoints_to_remove = []
    # If we have more than keep_count, remove the oldest ones
    if len(regular_checkpoints) > keep_count:
        checkpoints_to_remove = regular_checkpoints[:-keep_count]
        for checkpoint in checkpoints_to_remove:
            try:
                os.remove(checkpoint)
                logger.info(f"Removed old checkpoint: {os.path.basename(checkpoint)}")
            except Exception as e:
                logger.error(f"Error removing checkpoint {os.path.basename(checkpoint)}: {e}")
                
    # Report status
    remaining_checkpoints = len(regular_checkpoints) - len(checkpoints_to_remove) if len(regular_checkpoints) > keep_count else len(regular_checkpoints)
    logger.info(f"Checkpoint maintenance: Keeping {remaining_checkpoints} regular checkpoints and {len(final_checkpoints)} final checkpoints")

def find_latest_checkpoint(directory):
    """Finds the latest checkpoint file based on cycle number."""
    pattern = os.path.join(directory, "mind_state_cycle_*.pkl")
    checkpoints = glob.glob(pattern)
    if not checkpoints:
        return None
    
    # Extract cycle number more carefully to handle filenames like "mind_state_cycle_20_final.pkl"
    def extract_cycle_number(filename):
        # Extract the part after 'mind_state_cycle_'
        parts = filename.split('_cycle_')[-1].split('.')[0]
        # Extract just the numeric part from this string
        numeric_part = ''.join(c for c in parts.split('_')[0] if c.isdigit())
        return int(numeric_part) if numeric_part else 0
        
    latest_checkpoint = max(checkpoints, key=extract_cycle_number)
    return latest_checkpoint

def initialize_mind(load_latest=True):
    """Initialize the mind, optionally loading from a checkpoint."""
    global mind, stats
    
    # Ensure checkpoint directory exists
    if not os.path.exists(CHECKPOINT_DIR):
        os.makedirs(CHECKPOINT_DIR)
        logger.info(f"Created checkpoint directory: {CHECKPOINT_DIR}")
    
    # Clean up old checkpoints before loading
    cleanup_old_checkpoints(MAX_CHECKPOINTS)

    # Attempt to load the latest checkpoint
    latest_checkpoint_path = find_latest_checkpoint(CHECKPOINT_DIR) if load_latest else None
    
    if load_latest and latest_checkpoint_path:
        logger.info(f"Loading latest checkpoint: {os.path.basename(latest_checkpoint_path)}")
        mind = IndependentMind.load_state(latest_checkpoint_path)
    else:
        if load_latest:
            logger.info("No checkpoint found or loading disabled. Initializing fresh mind.")
        mind = IndependentMind()
        logger.info(f"Mind initialized. Birth time: {mind.internal_state['birth_time']:.2f}")
    
    # Initialize stats
    stats["total_cycles"] = mind.cycle_counter if hasattr(mind, "cycle_counter") else 0
    stats["start_time"] = time.time()
    stats["last_save_time"] = time.time()
    
    return mind

def save_checkpoint(mind, force_final=False):
    """Save a checkpoint of the current mind state."""
    global stats
    
    if not os.path.exists(CHECKPOINT_DIR):
        os.makedirs(CHECKPOINT_DIR)
    
    if force_final:
        checkpoint_filename = os.path.join(CHECKPOINT_DIR, f"mind_state_cycle_{mind.cycle_counter}_final.pkl")
    else:
        checkpoint_filename = os.path.join(CHECKPOINT_DIR, f"mind_state_cycle_{mind.cycle_counter}.pkl")
    
    mind.save_state(checkpoint_filename)
    stats["last_save_time"] = time.time()
    logger.info(f"Saved checkpoint: {os.path.basename(checkpoint_filename)}")

def run_single_cycle(external_input=None):
    """Run a single mind cycle with optional external input."""
    global mind, stats
    
    with mind_lock:
        # Select random emoji if external_input is None but we want to provide input (30% chance)
        emoji_inputs = ["😊", "🤔", "😊", "🤔", "😢", "😊", "🤔", "😢", "🔥", "💡"]
        provide_input = external_input is not None or (random.random() < 0.3)
        
        if provide_input and external_input is None:
            external_input = random.choice(emoji_inputs)
            logger.info(f"Providing random external input: {external_input}")
        elif external_input:
            logger.info(f"Providing external input: {external_input}")
        else:
            logger.info("No external input provided")
        
        # Run the cycle
        start_time = time.time()
        cycle_results = mind.autonomous_cycle(external_input)
        end_time = time.time()
        
        # Log cycle information
        logger.info(f"--- Cycle {mind.cycle_counter} --- (Duration: {end_time - start_time:.4f}s)")
        logger.info(f"  Computed Entropy: {cycle_results.get('computed_entropy', 'N/A'):.4f}")
        logger.info(f"  Behavior: {cycle_results.get('behavior_type', 'N/A')} - {cycle_results.get('selected_behavior', 'N/A')}")
        
        # Save checkpoint if needed
        if mind.cycle_counter % CHECKPOINT_INTERVAL == 0:
            save_checkpoint(mind)
            
        # Update stats
        stats["total_cycles"] = mind.cycle_counter
        
        return cycle_results

def mind_process(cycles=DEFAULT_CYCLES):
    """Run the mind as a continuous autonomous process for a specified number of cycles."""
    global mind_running
    
    logger.info(f"Starting autonomous mind process for {cycles} cycles")
    mind_running = True
    
    try:
        for _ in range(cycles):
            if not mind_running:
                break
            run_single_cycle()
            time.sleep(0.1)  # Small delay between cycles to prevent CPU overload
    
    except KeyboardInterrupt:
        logger.info("Mind process interrupted by user")
    
    except Exception as e:
        logger.error(f"Error in mind process: {e}")
    
    finally:
        # Save final state
        if mind:
            save_checkpoint(mind, force_final=True)
        mind_running = False
        logger.info("Mind process stopped")

# Flask routes for web service mode
@app.route('/status', methods=['GET'])
def get_status():
    """Get the current status of the mind."""
    global mind, stats
    
    if not mind:
        return jsonify({"error": "Mind not initialized"}), 500
    
    with mind_lock:
        uptime = time.time() - stats["start_time"] if stats["start_time"] else 0
        
        return jsonify({
            "status": "running" if mind_running else "idle",
            "total_cycles": stats["total_cycles"],
            "uptime_seconds": uptime,
            "last_checkpoint": stats["last_save_time"],
            "birth_time": mind.internal_state.get('birth_time', 0)
        })

@app.route('/state', methods=['GET'])
def get_state():
    """Get the current state of the mind."""
    global mind
    
    if not mind:
        return jsonify({"error": "Mind not initialized"}), 500
    
    with mind_lock:
        return jsonify(mind.get_state_summary())

@app.route('/cycle', methods=['POST'])
def trigger_cycle():
    """Trigger a single mind cycle with optional external input."""
    global mind
    
    if not mind:
        return jsonify({"error": "Mind not initialized"}), 500
    
    data = request.json or {}
    external_input = data.get('input')
    
    try:
        results = run_single_cycle(external_input)
        return jsonify({
            "success": True,
            "cycle": mind.cycle_counter,
            "results": results
        })
    except Exception as e:
        logger.error(f"Error during cycle: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/save', methods=['POST'])
def trigger_save():
    """Manually trigger a checkpoint save."""
    global mind
    
    if not mind:
        return jsonify({"error": "Mind not initialized"}), 500
    
    with mind_lock:
        try:
            save_checkpoint(mind)
            return jsonify({
                "success": True,
                "checkpoint": f"mind_state_cycle_{mind.cycle_counter}.pkl"
            })
        except Exception as e:
            logger.error(f"Error saving checkpoint: {e}")
            return jsonify({"error": str(e)}), 500

@app.route('/start', methods=['POST'])
def start_mind_process():
    """Start the autonomous mind process."""
    global mind_thread, mind_running
    
    if mind_running:
        return jsonify({"message": "Mind process already running"}), 400
    
    data = request.json or {}
    cycles = data.get('cycles', DEFAULT_CYCLES)
    
    mind_thread = threading.Thread(target=mind_process, args=(cycles,))
    mind_thread.daemon = True
    mind_thread.start()
    
    return jsonify({
        "success": True,
        "message": f"Mind process started for {cycles} cycles"
    })

@app.route('/stop', methods=['POST'])
def stop_mind_process():
    """Stop the autonomous mind process."""
    global mind_running
    
    if not mind_running:
        return jsonify({"message": "Mind process not running"}), 400
    
    mind_running = False
    return jsonify({
        "success": True,
        "message": "Mind process stopping"
    })

def run_web_service(host='0.0.0.0', port=WEB_PORT):
    """Run the mind as a web service."""
    logger.info(f"Starting mind web service on {host}:{port}")
    app.run(host=host, port=port, debug=False, threaded=True)

# Main entry point
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Independent Mind Service")
    parser.add_argument('--mode', choices=['autonomous', 'web'], default='autonomous',
                      help='Run mode: autonomous process or web service')
    parser.add_argument('--cycles', type=int, default=DEFAULT_CYCLES,
                      help='Number of cycles to run in autonomous mode')
    parser.add_argument('--port', type=int, default=WEB_PORT,
                      help='Port to use for web service mode')
    parser.add_argument('--fresh', action='store_true',
                      help='Start with a fresh mind instead of loading from checkpoint')
    
    args = parser.parse_args()
    
    # Initialize the mind
    initialize_mind(load_latest=not args.fresh)
    
    try:
        if args.mode == 'autonomous':
            # Run as autonomous process
            mind_process(args.cycles)
        else:
            # Run as web service
            run_web_service(port=args.port)
    
    except KeyboardInterrupt:
        logger.info("Service interrupted by user")
    
    finally:
        # Save final state if necessary
        if mind and not args.mode == 'web':  # In web mode, saves are handled by API
            save_checkpoint(mind, force_final=True)
