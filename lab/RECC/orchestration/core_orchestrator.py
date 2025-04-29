import sys
import os
import time
import json
import argparse
import threading
import random
from datetime import datetime
from collections import deque

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.mind_kernel import MindKernel

# Import for terminal UI
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.layout import Layout
    from rich.live import Live
    from rich.text import Text
    from rich.table import Table
    from rich import box
    RICH_AVAILABLE = True
except ImportError:
    print("For the best experience, install the rich package: pip install rich")
    RICH_AVAILABLE = False

class CoreOrchestrator:
    """
    Orchestrates the RECC system and provides a CLI interface for interaction.
    
    This is a minimal implementation that allows:
    1. Running the RECC system with basic monitoring
    2. Interaction through simple text commands
    3. Monitoring of system status
    """
    
    def __init__(self, auto_save=True, save_interval=300, dynamic_ui=True):
        self.mind = MindKernel()
        self.auto_save = auto_save
        self.save_interval = save_interval  # seconds
        self.last_save_time = time.time()
        self.running = False
        self.cycle_count = 0
        self.session_start = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.session_data = []
        self.dynamic_ui = dynamic_ui and RICH_AVAILABLE
        self.interface = None
    
    def start(self, interactive=True):
        """
        Start the RECC system
        
        Args:
            interactive: If True, start an interactive CLI session
        """
        self.running = True
        print(f"Starting RECC system - Session {self.session_start}")
        print("Baby Mind initializing...")
        print("Energy Level:", self.mind.energy_level)
        print("Emotional State:", self.mind.emotional_system.get_state())
        
        try:
            if interactive:
                if self.dynamic_ui:
                    self._run_dynamic_session()
                else:
                    self._run_interactive_session()
            else:
                self._run_background_session()
        except KeyboardInterrupt:
            print("\nReceived interrupt signal. Shutting down gracefully...")
            self.stop()
    
    def _run_dynamic_session(self):
        """Run an interactive session with the rich dynamic UI"""
        # Initialize and start the dynamic interface
        self.interface = DynamicInterface(self)
        if not self.interface.start():
            # Fall back to the simple CLI if the dynamic interface couldn't start
            self._run_interactive_session()
            return
            
        try:
            # Main loop
            while self.running:
                # Run a processing cycle
                cycle_results = self._process_cycle()
                
                # Update the interface with current state
                self.interface.update()
                
                # Check for user input
                cmd = self.interface.get_and_clear_input()
                if cmd is None:
                    # No input, just continue the cycle
                    time.sleep(0.1)  # Small delay to prevent CPU hogging
                    continue
                    
                # Process special commands
                if cmd.lower() == 'exit':
                    self.stop()
                    break
                elif cmd.lower() == 'help':
                    self.interface.add_message("System", "Available commands: help, status, feed, give <num>, concepts, experiences, save, exit")
                elif cmd.lower() == 'status':
                    status = self.mind.get_state_summary()
                    status_text = f"Cycles: {self.cycle_count}, Uptime: {status['uptime']:.1f}s, Energy: {status['energy']:.1f}, Experiences: {status['experience_count']}"
                    self.interface.add_message("System", status_text)
                elif cmd.lower() == 'feed':
                    self.mind.update_energy(10)
                    self.interface.add_message("System", f"Energy +10. Current level: {self.mind.energy_level}")
                elif cmd.startswith('give '):
                    # Extract energy amount
                    try:
                        amount = float(cmd[5:])
                        self.mind.update_energy(amount)
                        self.interface.add_message("System", f"Energy {amount:+}. Current level: {self.mind.energy_level}")
                    except ValueError:
                        self.interface.add_message("System", "Invalid amount. Use 'give <number>'")
                elif cmd.lower() == 'concepts':
                    concepts = self.mind.memory_bank.get_concepts_by_strength(min_strength=0.3)
                    concept_text = "Top concepts: " + ", ".join([c['label'] for c in concepts[:5]]) if concepts else "No concepts formed yet."
                    self.interface.add_message("System", concept_text)
                elif cmd.lower() == 'experiences':
                    experiences = self.mind.memory_bank.get_recent_experiences(3)
                    exp_text = "Recent experiences: " + "; ".join([e.get('input', '')[:20] for e in experiences]) if experiences else "No experiences yet."
                    self.interface.add_message("System", exp_text)
                elif cmd.lower() == 'save':
                    self._save_state()
                    self.interface.add_message("System", f"State saved for session {self.session_start}")
                elif cmd:
                    # Any other input is treated as interaction with the baby mind
                    # Record the user's input in the chat
                    self.interface.add_message("You", cmd)
                    
                    # Process the input through a mind cycle
                    result = self.interact(cmd)
                    output = result.get('output', 'processed input')
                    
                    # Add baby's response to the chat
                    self.interface.add_message("Baby", output)
                
                # Auto-save if enabled
                if self.auto_save and time.time() - self.last_save_time > self.save_interval:
                    self._save_state()
        finally:
            # Stop the dynamic interface
            if self.interface:
                self.interface.stop()
    
    def _run_interactive_session(self):
        """Run an interactive CLI session"""
        print("\nStarting interactive session. Type 'help' for commands or 'exit' to quit.")
        
        while self.running:
            # Run a processing cycle
            self._process_cycle()
            
            # Display prompt
            cmd = input("\n> ").strip()
            
            # Process command
            if cmd.lower() == 'exit':
                self.stop()
                break
            elif cmd.lower() == 'help':
                self._show_help()
            elif cmd.lower() == 'status':
                self._show_status()
            elif cmd.lower() == 'emotions':
                self._show_emotions()
            elif cmd.lower() == 'energy':
                self._show_energy()
            elif cmd.lower() == 'feed':
                self.mind.update_energy(10)
                print("Energy +10. Current level:", self.mind.energy_level)
            elif cmd.lower() == 'concepts':
                self._show_concepts()
            elif cmd.lower() == 'experiences':
                self._show_recent_experiences()
            elif cmd.lower() == 'save':
                self._save_state()
            elif cmd.startswith('give '):
                # Extract energy amount
                try:
                    amount = float(cmd[5:])
                    self.mind.update_energy(amount)
                    print(f"Energy {amount:+}. Current level: {self.mind.energy_level}")
                except ValueError:
                    print("Invalid amount. Use 'give <number>'")
            elif cmd:
                # Any other input is treated as interaction with the baby mind
                result = self.interact(cmd)
                print(f"Baby Mind: {result.get('output', 'processed input')}")
    
    def _run_background_session(self):
        """Run a non-interactive background session"""
        print("Running in background mode. Press Ctrl+C to stop.")
        
        while self.running:
            # Run a processing cycle
            self._process_cycle()
            
            # Display minimal status updates
            if self.cycle_count % 10 == 0:
                print(f"Cycle {self.cycle_count}: Energy={self.mind.energy_level:.1f}, " +
                      f"Dominant emotion: {self.mind.emotional_system.get_dominant_emotion()[0]}")
            
            # Auto-save if enabled
            if self.auto_save and time.time() - self.last_save_time > self.save_interval:
                self._save_state()
                
            # Brief pause to not consume all CPU
            time.sleep(0.1)
    
    def _process_cycle(self):
        """Run a single processing cycle"""
        # Process a cycle in the mind kernel
        cycle_results = self.mind.process_cycle()
        self.cycle_count += 1
        
        # Record cycle data
        self.session_data.append({
            'cycle': self.cycle_count,
            'timestamp': time.time(),
            'energy': self.mind.energy_level,
            'emotions': self.mind.emotional_system.get_state(),
            'results': cycle_results
        })
        
        # Handle cry events
        if cycle_results.get('cry_emitted'):
            cry_details = cycle_results.get('cry_details', {})
            cry_event = cry_details.get('cry_event', {})
            print("\n[CRYING]", cry_event.get('reason', 'Baby is crying!'))
            print(f"Urgency: {cry_event.get('urgency', 0):.1f}, Type: {cry_event.get('type', 'unknown')}")
        
        return cycle_results
    
    def interact(self, input_text):
        """
        Interact with the baby mind
        
        Args:
            input_text: Text input for the baby mind
            
        Returns:
            dict: Interaction results
        """
        # Process input through a mind cycle
        cycle_results = self.mind.process_cycle(input_text)
        
        # Track the interaction
        self.session_data.append({
            'cycle': self.cycle_count,
            'timestamp': time.time(),
            'input': input_text,
            'energy': self.mind.energy_level,
            'emotions': self.mind.emotional_system.get_state(),
            'results': cycle_results
        })
        
        return cycle_results
    
    def stop(self):
        """Stop the system and save state"""
        self.running = False
        print("\nStopping RECC system...")
        
        # Final save
        if self.auto_save:
            self._save_state()
            
        print("System stopped.")
    
    def _save_state(self):
        """Save the current system state"""
        try:
            # Create directories if they don't exist
            save_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'sessions')
            os.makedirs(save_dir, exist_ok=True)
            
            # Save session data
            filename = os.path.join(save_dir, f"session_{self.session_start}.json")
            with open(filename, 'w') as f:
                json.dump({
                    'session_id': self.session_start,
                    'cycles': self.cycle_count,
                    'data': self.session_data
                }, f, indent=2)
                
            print(f"State saved to {filename}")
            self.last_save_time = time.time()
        except Exception as e:
            print(f"Error saving state: {e}")
    
    def _show_help(self):
        """Display available commands"""
        print("\nAvailable commands:")
        print("  help       - Show this help message")
        print("  status     - Show overall system status")
        print("  emotions   - Show emotional state details")
        print("  energy     - Show energy level details")
        print("  feed       - Give +10 energy to the system")
        print("  give <num> - Give specified amount of energy")
        print("  concepts   - Show top concepts in memory")
        print("  experiences - Show recent experiences")
        print("  save       - Save current state")
        print("  exit       - Exit the program")
        print("\nAny other input will be processed as interaction with the baby mind.")
    
    def _show_status(self):
        """Display system status"""
        status = self.mind.get_state_summary()
        
        print("\n=== RECC System Status ===")
        print(f"Cycles completed: {self.cycle_count}")
        print(f"Uptime: {status['uptime']:.1f} seconds")
        print(f"Energy level: {status['energy']:.1f}/100")
        print(f"Dominant emotion: {self.mind.emotional_system.get_dominant_emotion()[0]} " +
              f"({self.mind.emotional_system.get_dominant_emotion()[1]:.2f})")
        print(f"Experiences: {status['experience_count']}")
        print(f"Concepts: {status['concept_count']}")
        
        # Show active states
        print("\nCurrent state:")
        for state, active in status['status'].items():
            if active:
                print(f"  - {state}")
    
    def _show_emotions(self):
        """Display detailed emotional state"""
        emotions = self.mind.emotional_system.get_state()
        
        print("\n=== Emotional State ===")
        for emotion, value in emotions.items():
            print(f"{emotion}: {'|' * int(value * 20)} {value:.2f}")
            
        # Show emotional trends if possible
        for emotion in emotions:
            trend = self.mind.emotional_system.get_emotion_trend(emotion)
            direction = "↑" if trend > 0.05 else "↓" if trend < -0.05 else "→"
            print(f"{emotion} trend: {direction} ({trend:.2f})")
    
    def _show_energy(self):
        """Display energy details"""
        print("\n=== Energy Status ===")
        print(f"Current level: {self.mind.energy_level:.1f}/100")
        
        # Show energy history if available
        if hasattr(self.mind, 'energy_history') and self.mind.energy_history:
            history = self.mind.energy_history[-5:] if len(self.mind.energy_history) > 5 else self.mind.energy_history
            print("\nRecent energy changes:")
            for entry in history:
                print(f"  {datetime.fromtimestamp(entry['timestamp']).strftime('%H:%M:%S')}: {entry['level']:.1f}")
    
    def _show_concepts(self):
        """Display top concepts in memory"""
        print("\n=== Top Concepts ===")
        concepts = self.mind.memory_bank.get_concepts_by_strength(min_strength=0.3)
        
        if not concepts:
            print("No concepts formed yet.")
            return
            
        # Display top 10 concepts by strength
        for i, concept in enumerate(concepts[:10]):
            print(f"{i+1}. {concept['label']} (strength: {concept['strength']:.2f})")
            
            # Show emotional associations
            if 'emotional_tags' in concept:
                emotions = concept['emotional_tags']
                dominant = max(emotions.items(), key=lambda x: x[1]) if emotions else (None, 0)
                if dominant[0]:
                    print(f"   → Main emotion: {dominant[0]} ({dominant[1]:.2f})")
            
            # Show related concepts if available
            related = self.mind.memory_bank.get_concept_connections(concept['id'])
            if related:
                related_labels = [r['source'] if r['target'] == concept['id'] else r['target'] for r in related[:3]]
                print(f"   → Related: {', '.join(related_labels)}")
    
    def _show_recent_experiences(self):
        """Display recent experiences"""
        experiences = self.mind.memory_bank.get_recent_experiences(5)
        
        print("\n=== Recent Experiences ===")
        if not experiences:
            print("No experiences recorded yet.")
            return
            
        for i, exp in enumerate(experiences):
            print(f"{i+1}. Input: {exp.get('input', '')[:30]}{'...' if len(exp.get('input', '')) > 30 else ''}")
            if exp.get('output'):
                print(f"   Output: {exp.get('output')[:30]}{'...' if len(exp.get('output', '')) > 30 else ''}")
            if exp.get('tags'):
                print(f"   Tags: {', '.join(exp.get('tags', []))}")


class DynamicInterface:
    """
    Provides a real-time dynamic interface for the baby mind using the Rich library.
    This displays current status, emotions, and activities in an interactive dashboard.
    """
    
    def __init__(self, orchestrator):
        self.orchestrator = orchestrator
        self.console = Console()
        self.layout = Layout()
        self.message_history = deque(maxlen=10)  # Store recent messages
        self.thought_history = deque(maxlen=5)   # Store recent thoughts
        self.last_update = time.time()
        self.status_message = "Baby is waking up..."
        self.thinking_messages = [
            "I wonder...", 
            "What is this?", 
            "Interesting...",
            "That feels nice",
            "I remember this",
            "This is new",
            "I like this",
            "I'm not sure about this",
            "This connects to...",
            "I feel something"
        ]
        
        # Configure layout
        self.layout.split(
            Layout(name="header", size=3),
            Layout(name="main", ratio=1),
            Layout(name="input", size=3)
        )
        
        # Split the main area into status and chat
        self.layout["main"].split_row(
            Layout(name="status", ratio=2),
            Layout(name="chat", ratio=3)
        )
        
        # Split status into emotions and thinking
        self.layout["status"].split(
            Layout(name="emotions", ratio=2),
            Layout(name="thinking", ratio=3)
        )
        
        # Initialize the live display
        self.live = Live(self.layout, refresh_per_second=4, screen=True)
        self.input_thread = None
        self.user_input = None
        
    def start(self):
        """Start the dynamic interface"""
        if not RICH_AVAILABLE:
            print("Rich library not available. Falling back to simple CLI.")
            return False
            
        # Start input thread
        self.input_thread = threading.Thread(target=self._input_loop)
        self.input_thread.daemon = True
        self.input_thread.start()
        
        # Start the live display
        self.live.start()
        return True
        
    def stop(self):
        """Stop the dynamic interface"""
        if hasattr(self, 'live') and self.live:
            self.live.stop()
    
    def update(self):
        """Update the interface with current state"""
        now = time.time()
        mind = self.orchestrator.mind
        cycle_results = self.orchestrator.session_data[-1]['results'] if self.orchestrator.session_data else {}
        
        # Update status message based on state
        if cycle_results.get('cry_emitted'):
            cry_event = cycle_results.get('cry_details', {}).get('cry_event', {})
            self.status_message = f"Baby is crying! [{cry_event.get('type', 'distress')}]"
        elif cycle_results.get('interaction'):
            self.status_message = "Baby is interacting with you"
        elif cycle_results.get('reflection'):
            self.status_message = "Baby is reflecting on experiences"
        elif cycle_results.get('idle_thinking'):
            self.status_message = "Baby is thinking..."
        
        # Add a thought bubble occasionally when thinking
        if now - self.last_update > 2 and (cycle_results.get('idle_thinking') or cycle_results.get('reflection')):
            thought = random.choice(self.thinking_messages)
            # Add emotional context to thoughts based on dominant emotion
            dominant_emotion, strength = mind.emotional_system.get_dominant_emotion()
            if dominant_emotion == 'curiosity' and strength > 0.6:
                thought = f"{thought} [curious]"
            elif dominant_emotion == 'satisfaction' and strength > 0.6:
                thought = f"{thought} [content]"
            elif dominant_emotion == 'fear' and strength > 0.6:
                thought = f"{thought} [fearful]"
            elif dominant_emotion == 'pain' and strength > 0.6:
                thought = f"{thought} [pained]"
            
            self.thought_history.append(thought)
            self.last_update = now
        
        # Update the layout
        self._update_header()
        self._update_emotions()
        self._update_thinking()
        self._update_chat()
        self._update_input_area()
    
    def add_message(self, sender, message):
        """Add a message to the chat history"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.message_history.append((timestamp, sender, message))
        
    def _input_loop(self):
        """Background thread to get user input without blocking"""
        while True:
            try:
                user_input = input()
                self.user_input = user_input
                time.sleep(0.1)  # Small pause to prevent CPU hogging
            except (EOFError, KeyboardInterrupt):
                break
    
    def _update_header(self):
        """Update the header panel with system status"""
        energy_level = self.orchestrator.mind.energy_level
        energy_color = "green" if energy_level > 70 else "yellow" if energy_level > 30 else "red"
        
        header_content = Text()
        header_content.append("💭 RECC Baby Mind ", style="bold blue")
        header_content.append(f"[Energy: ", style="dim")
        header_content.append(f"{energy_level:.1f}/100", style=energy_color)
        header_content.append("] ", style="dim")
        header_content.append(f"Status: {self.status_message}", style="italic")
        
        self.layout["header"].update(Panel(header_content))
    
    def _update_emotions(self):
        """Update the emotions panel with current emotional state"""
        emotions = self.orchestrator.mind.emotional_system.get_state()
        
        # Create a table for emotions
        emotion_table = Table(box=box.SIMPLE)
        emotion_table.add_column("Emotion")
        emotion_table.add_column("Level")
        emotion_table.add_column("Trend")
        
        # Color map for emotions
        emotion_colors = {
            'curiosity': 'bright_blue',
            'satisfaction': 'bright_green',
            'fear': 'yellow',
            'pain': 'red'
        }
        
        # Add emotions to table
        for emotion, value in emotions.items():
            bar = "■" * int(value * 10)
            color = emotion_colors.get(emotion, 'white')
            trend = self.orchestrator.mind.emotional_system.get_emotion_trend(emotion)
            trend_icon = "↑" if trend > 0.05 else "↓" if trend < -0.05 else "→"
            
            emotion_table.add_row(
                Text(emotion.capitalize(), style=color),
                Text(f"{bar} {value:.2f}", style=color),
                Text(trend_icon, style=color)
            )
        
        # Add emotions panel
        self.layout["emotions"].update(Panel(emotion_table, title="Emotions"))
    
    def _update_thinking(self):
        """Update the thinking panel with thought bubbles"""
        thinking_content = Text()
        
        if self.thought_history:
            thinking_content.append("Baby's thoughts:\n\n", style="bold")
            
            for i, thought in enumerate(reversed(self.thought_history)):
                if "[curious]" in thought:
                    thinking_content.append(f"💭 {thought.replace('[curious]', '')}\n", style="bright_blue")
                elif "[content]" in thought:
                    thinking_content.append(f"😊 {thought.replace('[content]', '')}\n", style="bright_green")
                elif "[fearful]" in thought:
                    thinking_content.append(f"😨 {thought.replace('[fearful]', '')}\n", style="yellow")
                elif "[pained]" in thought:
                    thinking_content.append(f"😣 {thought.replace('[pained]', '')}\n", style="red")
                else:
                    thinking_content.append(f"💭 {thought}\n", style="bright_white")
        else:
            thinking_content.append("Baby hasn't had any thoughts yet...", style="dim italic")
        
        self.layout["thinking"].update(Panel(thinking_content, title="Thinking"))
    
    def _update_chat(self):
        """Update the chat panel with message history"""
        chat_content = Text()
        
        if self.message_history:
            for timestamp, sender, message in self.message_history:
                chat_content.append(f"[{timestamp}] ", style="dim")
                
                if sender == "Baby":
                    chat_content.append("Baby: ", style="bold blue")
                    chat_content.append(f"{message}\n", style="blue")
                elif sender == "Mentor":
                    chat_content.append("Mentor: ", style="bold green")
                    chat_content.append(f"{message}\n", style="green")
                else:  # User
                    chat_content.append("You: ", style="bold")
                    chat_content.append(f"{message}\n")
        else:
            chat_content.append("No conversations yet. Say hello to baby!", style="italic")
        
        self.layout["chat"].update(Panel(chat_content, title="Conversation"))
    
    def _update_input_area(self):
        """Update the input area with prompt"""
        input_text = Text("Type your message to the baby (or 'help' for commands):")
        self.layout["input"].update(Panel(input_text))
    
    def get_and_clear_input(self):
        """Get user input and clear the buffer"""
        if self.user_input is not None:
            input_value = self.user_input
            self.user_input = None
            return input_value
        return None


def main():
    """Main entry point for the CLI"""
    parser = argparse.ArgumentParser(description="RECC System CLI")
    parser.add_argument('-i', '--interactive', action='store_true', default=True,
                        help='Run in interactive mode (default)')
    parser.add_argument('-b', '--background', action='store_true',
                        help='Run in background mode')
    parser.add_argument('-s', '--save-interval', type=int, default=300,
                        help='Auto-save interval in seconds (default: 300)')
    parser.add_argument('-n', '--no-autosave', action='store_true',
                        help='Disable auto-saving')
    parser.add_argument('-c', '--classic-ui', action='store_true',
                        help='Use classic CLI interface instead of dynamic UI')
    
    args = parser.parse_args()
    
    # Check if Rich is available for dynamic UI
    if not RICH_AVAILABLE and not args.classic_ui:
        print("Rich library not available. Installing it will provide a better experience.")
        print("You can install it with: pip install rich")
        print("Falling back to classic CLI interface.")
        dynamic_ui = False
    else:
        dynamic_ui = not args.classic_ui
    
    orchestrator = CoreOrchestrator(
        auto_save=not args.no_autosave,
        save_interval=args.save_interval,
        dynamic_ui=dynamic_ui
    )
    
    # Start in the selected mode
    orchestrator.start(interactive=not args.background)


if __name__ == "__main__":
    main()