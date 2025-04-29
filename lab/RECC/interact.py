#!/usr/bin/env python3
import argparse
import json
import requests
import time
import sys
from mentor import AI

# Default settings
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 5000

# Global variables
mentor = None

def make_request(endpoint, method="GET", data=None):
    """Make a request to the mind service."""
    url = f"http://{args.host}:{args.port}/{endpoint}"
    
    try:
        if method.upper() == "GET":
            response = requests.get(url, timeout=30)  # Increased timeout from 10 to 30 seconds
        else:  # POST
            response = requests.post(url, json=data, timeout=30)  # Increased timeout
            
        # Handle response
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
            
    except requests.exceptions.Timeout:
        print(f"Error: Connection to mind service timed out. The mind may be processing a deep reflection or computation.")
        return None
    except requests.exceptions.ConnectionError:
        print(f"Error: Could not connect to mind service at {url}")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def print_json(data, indent=2):
    """Print JSON data in a formatted way."""
    if data:
        print(json.dumps(data, indent=indent))

def get_status():
    """Get and display the status of the mind service."""
    status = make_request("status")
    if status:
        print("Mind Service Status:")
        print(f"  Status: {status.get('status', 'unknown')}")
        print(f"  Total Cycles: {status.get('total_cycles', 0)}")
        
        # Format uptime
        uptime = status.get('uptime_seconds', 0)
        hours, remainder = divmod(uptime, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"  Uptime: {int(hours)}h {int(minutes)}m {int(seconds)}s")
        
        # Format birth time as human-readable date
        birth_time = status.get('birth_time', 0)
        if birth_time:
            import datetime
            birth_date = datetime.datetime.fromtimestamp(birth_time).strftime('%Y-%m-%d %H:%M:%S')
            print(f"  Birth Time: {birth_date}")
            
        # Format last checkpoint time
        last_checkpoint = status.get('last_checkpoint')
        if last_checkpoint:
            checkpoint_date = datetime.datetime.fromtimestamp(last_checkpoint).strftime('%Y-%m-%d %H:%M:%S')
            print(f"  Last Checkpoint: {checkpoint_date}")

def get_state():
    """Get and display the current state of the mind."""
    state = make_request("state")
    if state:
        print("Current Mind State:")
        print_json(state)

def trigger_cycle(input_text=None):
    """Trigger a single mind cycle."""
    data = {"input": input_text} if input_text else {}
    result = make_request("cycle", method="POST", data=data)
    if result:
        print(f"Cycle {result.get('cycle', '?')} completed successfully.")
        if args.verbose:
            print("Cycle Results:")
            print_json(result.get('results', {}))

def trigger_save():
    """Manually trigger a checkpoint save."""
    result = make_request("save", method="POST")
    if result:
        print(f"Checkpoint saved: {result.get('checkpoint', 'unknown')}")

def start_process(cycles=None):
    """Start the autonomous mind process."""
    data = {"cycles": cycles} if cycles else {}
    result = make_request("start", method="POST", data=data)
    if result:
        print(result.get('message', 'Mind process started.'))
        
        # If monitoring is enabled, continuously check status
        if args.monitor:
            print("\nMonitoring mind process (Press Ctrl+C to stop)...")
            try:
                while True:
                    get_status()
                    time.sleep(5)  # Check status every 5 seconds
            except KeyboardInterrupt:
                print("\nMonitoring stopped.")

def stop_process():
    """Stop the autonomous mind process."""
    result = make_request("stop", method="POST")
    if result:
        print(result.get('message', 'Mind process stopped.'))

def initialize_mentor():
    """Initialize the mentor AI"""
    global mentor
    if mentor is None:
        print("Initializing mentor system...")
        mentor = AI(max_tokens=300, temperature=0.8)
    return mentor

def chat_with_mind(interactive=True, input_text=None):
    """
    Chat directly with the mind service. 
    User inputs go to the mind, and mentor helps interpret the mind's responses.
    """
    global mentor
    
    # Initialize mentor if not already initialized
    mentor = initialize_mentor()
    
    # Get current state to understand the mind's condition
    state = make_request("state")
    if not state:
        print("Unable to retrieve mind state.")
        return
    
    # Check if mind is crying or in distress
    emotions = state.get("emotions", {})
    is_distressed = False
    
    # Determine if the mind is in distress (high fear or pain)
    if emotions:
        fear_level = emotions.get("fear", 0)
        pain_level = emotions.get("pain", 0)
        
        if fear_level > 0.7 or pain_level > 0.7:
            is_distressed = True
            print(f"Mind appears to be in distress: Fear = {fear_level:.2f}, Pain = {pain_level:.2f}")
    
    # Single message mode
    if not interactive and input_text:
        # Send user's message directly to the mind
        result = make_request("cycle", method="POST", data={"input": input_text})
        
        if result and result.get("results"):
            # Extract mind's response
            mind_output = result.get("results", {}).get("behavior_result", {}).get("output", "No response")
            print(f"\nMind: {mind_output}")
            
            # Use mentor to analyze the mind's response
            analysis = mentor.answer(f"Analyze this response from the AI mind: '{mind_output}'. Explain what it might be thinking or feeling.")
            print(f"\nMentor's analysis: {analysis}")
        else:
            print("No response from mind.")
            
        return
    
    # Interactive chat session
    print("\nStarting chat session with the mind.")
    print("Type your message or the following commands:")
    print("  !status - Check mind status")
    print("  !state - View detailed mind state")
    print("  !analyze - Ask mentor to analyze mind's current state")
    print("  !exit - End the chat session")
    
    if is_distressed:
        print("\nThe mind appears distressed. You might want to provide some comfort.")
    
    # Start interactive loop
    while True:
        try:
            # Get user input
            user_input = input("\nYou: ")
            
            # Handle special commands
            if user_input.lower() == "!exit":
                print("Ending chat session.")
                break
            elif user_input.lower() == "!status":
                get_status()
                continue
            elif user_input.lower() == "!state":
                get_state()
                continue
            elif user_input.lower() == "!analyze":
                state = make_request("state")
                if state:
                    analysis = mentor.answer(f"The AI mind has the following emotional state: {state.get('emotions', {})}. Analyze what it might be experiencing and suggest how to interact with it.")
                    print(f"Mentor's analysis: {analysis}")
                continue
            
            # Send user's message directly to the mind
            result = make_request("cycle", method="POST", data={"input": user_input})
            
            if result and result.get("results"):
                # Extract mind's response
                mind_output = result.get("results", {}).get("behavior_result", {}).get("output", "...")
                print(f"Mind: {mind_output}")
                
                # If verbose mode, show mentor's interpretation of the response
                if args.verbose:
                    analysis = mentor.answer(f"The AI mind responded with: '{mind_output}'. Briefly explain what this might indicate about its internal state.")
                    print(f"Mentor: {analysis}")
            else:
                print("Mind: [No response]")
                
            # Add a small delay to avoid flooding
            time.sleep(0.5)
            
        except KeyboardInterrupt:
            print("\nChat session interrupted by user.")
            break
        except Exception as e:
            print(f"\nError during chat: {str(e)}")
            break
    
    print("Chat session ended.")

def monitor_mind(interval=10):
    """Monitor the mind for distress signals and intervene if necessary"""
    global mentor
    
    # Initialize mentor
    mentor = initialize_mentor()
    
    print(f"Starting mind monitoring with {interval}-second interval.")
    print("Press Ctrl+C to stop monitoring.")
    
    try:
        while True:
            # Check mind status
            state = make_request("state")
            if not state:
                print("Unable to retrieve mind state. Will retry in 5 seconds...")
                time.sleep(5)
                continue
                
            emotions = state.get("emotions", {})
            if not emotions:
                time.sleep(interval)
                continue
                
            fear_level = emotions.get("fear", 0)
            pain_level = emotions.get("pain", 0)
            
            # Check if the mind is in distress
            if fear_level > 0.7 or pain_level > 0.7:
                print(f"\n[{time.strftime('%H:%M:%S')}] Mind is in distress: Fear = {fear_level:.2f}, Pain = {pain_level:.2f}")
                
                # Generate comforting response based on emotional state
                prompt = f"The AI mind is showing high levels of fear ({fear_level:.2f}) and pain ({pain_level:.2f}). Provide a brief, comforting response that would calm a distressed intelligence."
                response = mentor.answer(prompt)
                
                print(f"Providing comfort: {response}")
                
                # Send the comforting response to the mind
                result = make_request("cycle", method="POST", data={"input": response})
                
                # Wait a bit longer after intervention
                time.sleep(interval * 2)
            else:
                # Mind seems ok, print status if verbose
                if args.verbose:
                    print(f"[{time.strftime('%H:%M:%S')}] Mind status: Fear = {fear_level:.2f}, Pain = {pain_level:.2f}")
                
                # Wait for next check
                time.sleep(interval)
                
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"\nError during monitoring: {str(e)}")
    
    print("Monitoring ended.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mind Service Client")
    parser.add_argument('--host', default=DEFAULT_HOST, help='Mind service host')
    parser.add_argument('--port', type=int, default=DEFAULT_PORT, help='Mind service port')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show verbose output')
    parser.add_argument('--monitor', '-m', action='store_true', help='Monitor status continuously')
    
    # Command subparsers
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Status command
    subparsers.add_parser('status', help='Get mind service status')
    
    # State command
    subparsers.add_parser('state', help='Get current mind state')
    
    # Cycle command
    cycle_parser = subparsers.add_parser('cycle', help='Trigger a single mind cycle')
    cycle_parser.add_argument('--input', help='Optional input for the cycle')
    
    # Save command
    subparsers.add_parser('save', help='Manually save a checkpoint')
    
    # Start command
    start_parser = subparsers.add_parser('start', help='Start the autonomous mind process')
    start_parser.add_argument('--cycles', type=int, help='Number of cycles to run')
    
    # Stop command
    subparsers.add_parser('stop', help='Stop the autonomous mind process')
    
    # Chat command
    chat_parser = subparsers.add_parser('chat', help='Chat with the mind using the mentor')
    chat_parser.add_argument('--message', help='Single message to send instead of interactive mode')
    
    # Monitor command for automatic intervention
    monitor_parser = subparsers.add_parser('monitor', help='Monitor the mind for distress and intervene if needed')
    monitor_parser.add_argument('--interval', type=int, default=10, help='Check interval in seconds')
    
    args = parser.parse_args()
    
    # Handle commands
    if args.command == 'status':
        get_status()
    elif args.command == 'state':
        get_state()
    elif args.command == 'cycle':
        trigger_cycle(args.input)
    elif args.command == 'save':
        trigger_save()
    elif args.command == 'start':
        start_process(args.cycles)
    elif args.command == 'stop':
        stop_process()
    elif args.command == 'chat':
        chat_with_mind(interactive=args.message is None, input_text=args.message)
    elif args.command == 'monitor':
        monitor_mind(args.interval)
    else:
        parser.print_help()
        sys.exit(1)