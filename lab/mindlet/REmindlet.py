# ReMindlet v3.0: Modular Recursive Emergence Agent
from threading import Thread
import math, random, time
from collections import Counter, deque
import logging
import pickle
import os
import random # Needed for retry logic
import sys # Needed for path manipulation and exit

# Import module classes and helpers
from rme import RecursiveMemoryEngine, echo_score, motif_resonates, cluster_motifs, summarize_memory
from ee import EmotionEngine
from il import InteractionLoop
from sms import SelfModelSimulator
from ipl import IntentPlanningLayer

# === Agent Class ===
class REMindlet:
    def __init__(self):
        # Instantiate modules
        self.rme = RecursiveMemoryEngine("Memory", {('I',), ('am',)}) # Initial memory, "Cogito, Ergo sum"
        self.ee = EmotionEngine({'panic': 0, 'joy': 0})
        self.il = InteractionLoop(buffer_maxlen=20) # Increased buffer size slightly
        self.sms = SelfModelSimulator(history_length=10)
        self.ipl = IntentPlanningLayer()

        # --- Logging Setup ---
        # Use absolute path for log file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.log_file = os.path.join(current_dir, "log.txt")
        
        # Configure root logger first
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.INFO)
        
        # Create handlers
        fh = logging.FileHandler(self.log_file, mode='a') # Append mode
        fh.setLevel(logging.DEBUG)  # Set file handler to DEBUG level to capture all messages
        # Console handler - controlled by verbose_logging flag
        self.ch = logging.StreamHandler() # Outputs to stderr by default (like print)
        self.ch.setLevel(logging.CRITICAL + 1) # Default to hiding console logs
        
        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.ch.setFormatter(formatter)
        
        # Configure all module loggers
        module_loggers = {
            "REMindlet": logging.getLogger("REMindlet"),
            "RME": logging.getLogger("RME"),
            "IL": logging.getLogger("IL"),
            "IPL": logging.getLogger("IPL"),
            "SMS": logging.getLogger("SMS"),
            "EE": logging.getLogger("EE")
        }
        
        # Set up each module logger
        for name, logger in module_loggers.items():
            logger.setLevel(logging.DEBUG)
            # Clear existing handlers to avoid duplicates
            if logger.hasHandlers():
                logger.handlers.clear()
            # Add the same handlers
            logger.addHandler(fh)
            logger.addHandler(self.ch)
            # Make sure loggers don't propagate to the root logger
            logger.propagate = False
        
        # Store the main logger for convenience
        self.logger = module_loggers["REMindlet"]
        self.verbose_logging = False # Default to non-verbose console
        self._update_console_log_level() # Set initial console level

        # Metrics tracking
        self.metrics = {
            "cycle_count": 0,
            "entropy_flow": [], # Store (before, after, reduction) tuples
            "buffer_merge_attempts": 0,
            "buffer_merges": 0,
            "emotion_counts": Counter(), # Will be updated each cycle
            # "max_depth_reached": 0, # RME internal detail now
            # "derived_sets_created": 0, # RME internal detail now
            "avg_echo_score": 0.0,
            "avg_buffer_latency": 0.0,
            "motif_reuse": 0,
            "actions_chosen": Counter(),
            "merge_outcomes": Counter(), # Track success/fail
        }
        # self.verbose_logging = True # Removed, controlled by toggle

        # Store motifs associated with recent merge outcomes (can be used by EE/IPL)
        self.recently_positive_motifs = deque(maxlen=20)
        self.recently_negative_motifs = deque(maxlen=20)

        self.last_output = None # Add attribute to store last output

        # Start the main agent processing loop in a separate thread
        self.thought_thread = MetaCycle(self)
        self.thought_thread.daemon = True
        self.thought_thread.start()

    def _update_console_log_level(self):
        """Updates the console handler's log level based on verbose_logging."""
        if self.verbose_logging:
            self.ch.setLevel(logging.INFO) # Show INFO and above on console
        else:
            # Set level higher than CRITICAL to effectively disable console output via handler
            self.ch.setLevel(logging.CRITICAL + 1)

    def toggle_verbose_logging(self):
        """Toggles verbose logging and updates the console handler."""
        self.verbose_logging = not self.verbose_logging
        self._update_console_log_level()
        # Log the change itself to the file
        self.logger.info(f"Verbose console logging {'enabled' if self.verbose_logging else 'disabled'}")
        # Also print status to the console for immediate user feedback
        print(f"Verbose console logging {'enabled' if self.verbose_logging else 'disabled'}")

    def save_checkpoint(self, filepath="default_checkpoint.pkl"):
        """Saves the agent's state to a file."""
        # Ensure the thought thread has access to the blocked motifs buffer
        blocked_motifs = []
        if hasattr(self.thought_thread, 'blocked_motifs_buffer'):
             blocked_motifs = list(self.thought_thread.blocked_motifs_buffer)

        state = {
            'rme_elements': self.rme.elements,
            'rme_derived_sets': self.rme.subsets,  # Fixed: using subsets instead of derived_sets
            'rme_last_entropy': self.rme.last_entropy,
            'ee_state': self.ee.state,  # Fixed: using state instead of emotions
            'ee_positive_assoc': self.ee.positive_associated_motifs,
            'ee_negative_assoc': self.ee.negative_associated_motifs,
            'il_buffer': list(self.il.input_buffer), # Convert deque
            'sms_history': list(self.sms.state_history), # Convert deque
            'sms_self_model': self.sms.get_self_model(),
            # IPL state (if any - currently stateless)
            'metrics': self.metrics,
            'recently_positive_motifs': list(self.recently_positive_motifs), # Convert deque
            'recently_negative_motifs': list(self.recently_negative_motifs), # Convert deque
            'blocked_motifs_buffer': blocked_motifs # Use the fetched list
            # Note: Does not save thread state, logger state, or verbose flag itself
        }
        try:
            with open(filepath, 'wb') as f:
                pickle.dump(state, f)
            self.logger.info(f"Checkpoint saved to {filepath}")
            print(f"Checkpoint saved to {filepath}") # Keep confirmation on console
        except Exception as e:
            self.logger.error(f"Error saving checkpoint to {filepath}: {e}")
            print(f"Error saving checkpoint: {e}") # Keep error on console

    def _restore_memory_if_empty(self):
        """
        Seeds the memory with foundational motifs if memory is empty.
        Called after checkpoint loading to ensure continuity.
        """
        if not self.rme.elements or len(self.rme.elements) < 5:
            print("[REmindlet] Memory appears empty after load, seeding with foundational motifs.")
            # Basic identity and cognitive seed motifs
            seed_motifs = {
                ("I",), 
                ("am",), 
                ("think",),
                ("I", "am"),
                ("I", "think"),
                ("I", "am", "thinking"),
                ("want",),
                ("safe",),
                ("learn",),
                ("help",),
                ("you",)
            }
            
            # Add the seed motifs to memory
            for motif in seed_motifs:
                self.rme.elements.add(motif)
                
            # Also seed the self-model with core identity motifs
            self.sms.current_self_model.add(("I", "am"))
            self.sms.current_self_model.add(("I", "think"))
            
            print(f"[REmindlet] Seeded memory with {len(seed_motifs)} foundational motifs")
            
            # Recalculate entropy
            self.rme.last_entropy = self.rme.compute_entropy()

    def load_checkpoint(self, filepath="default_checkpoint.pkl"):
        """Loads the agent's state from a file."""
        if not os.path.exists(filepath):
            self.logger.warning(f"Checkpoint file not found: {filepath}")
            print(f"Checkpoint file not found: {filepath}") # Keep warning on console
            return False
        try:
            with open(filepath, 'rb') as f:
                state = pickle.load(f)

            # Restore RME state
            self.rme.elements = state.get('rme_elements', {('I',), ('am',)})
            self.rme.subsets = state.get('rme_derived_sets', [])  # Fixed: using subsets instead of derived_sets
            self.rme.last_entropy = state.get('rme_last_entropy', self.rme.compute_entropy()) # Recompute if missing

            # Restore EE state
            self.ee.state = state.get('ee_state', Counter({'panic': 0, 'joy': 0}))
            self.ee.positive_associated_motifs = state.get('ee_positive_assoc', Counter())
            self.ee.negative_associated_motifs = state.get('ee_negative_assoc', Counter())

            # Restore IL buffer
            self.il.input_buffer = deque(state.get('il_buffer', []), maxlen=self.il.input_buffer.maxlen)

            # Restore SMS state
            self.sms.state_history = deque(state.get('sms_history', []), maxlen=self.sms.state_history.maxlen)
            self.sms.self_model = state.get('sms_self_model', {})

            # Restore Metrics (selectively, cycle count might reset depending on philosophy)
            loaded_metrics = state.get('metrics', {})
            # Keep current cycle count or reset? Let's reset for now.
            loaded_metrics['cycle_count'] = 0
            self.metrics.update(loaded_metrics) # Update existing dict

            # Restore other state
            self.recently_positive_motifs = deque(state.get('recently_positive_motifs', []), maxlen=self.recently_positive_motifs.maxlen)
            self.recently_negative_motifs = deque(state.get('recently_negative_motifs', []), maxlen=self.recently_negative_motifs.maxlen)

            # Restore blocked motifs buffer in the thought thread
            if hasattr(self.thought_thread, 'blocked_motifs_buffer'):
                 self.thought_thread.blocked_motifs_buffer = deque(state.get('blocked_motifs_buffer', []), maxlen=self.thought_thread.blocked_motifs_buffer.maxlen)

            self.logger.info(f"Checkpoint loaded from {filepath}")
            print(f"Checkpoint loaded from {filepath}") # Keep confirmation on console
            # Recalculate entropy after loading RME state
            self.rme.last_entropy = self.rme.compute_entropy()
            print(f"Memory summary after load: {summarize_memory(self.rme.get_motifs())}") # Keep summary on console
            self._restore_memory_if_empty()
            return True
        except Exception as e:
            self.logger.error(f"Error loading checkpoint from {filepath}: {e}")
            print(f"Error loading checkpoint: {e}") # Keep error on console
            return False

# === Thought Process Thread ===
class MetaCycle(Thread):
    def __init__(self, agent):
        super().__init__()
        self.agent = agent
        # Buffer for motifs that failed to merge below threshold, to retry later
        self.blocked_motifs_buffer = deque(maxlen=10)
        # Track the source of the content currently being processed ('external', 'internal_action', 'self')
        self.current_buffer_source = "external" # Default

    def run(self):
        while True:
            self.agent.metrics["cycle_count"] += 1
            # Use logger for verbose cycle start
            self.agent.logger.info(f"--- Cycle {self.agent.metrics['cycle_count']} ---")

            # --- Initialize cycle variables ---
            candidate_motifs = None
            merge_result = None
            retry_source = "unknown" # Track if processing buffer or retry
            echo = 0.0
            current_threshold = 0.0 # Will be set by RME
            entropy_before = self.agent.rme.last_entropy # Capture entropy before potential merge
            actual_entropy_reduction = 0.0 # Initialize reduction
            buffer_source_for_this_cycle = self.current_buffer_source # Capture source for this cycle

            # --- Perception Phase (Check IL buffer & Blocked Retry Buffer) ---
            # Prioritize retrying blocked motifs if buffer is full or randomly
            should_retry = len(self.blocked_motifs_buffer) > 0 and \
                           (len(self.agent.il.input_buffer) == self.agent.il.input_buffer.maxlen or random.random() < 0.2)

            if should_retry:
                candidate_motifs = self.blocked_motifs_buffer.popleft()
                retry_source = "blocked_retry" # Override source if retrying
                # Use logger for verbose output
                self.agent.logger.info(f"[RME Retry] Attempting merge for previously blocked: {candidate_motifs}")
            elif len(self.agent.il.input_buffer) > 0:
                candidate_motifs = self.agent.il.input_buffer.popleft()
                retry_source = "input" # Source is fresh input buffer
                # Use logger for verbose output
                self.agent.logger.info(f"[RME] Processing {retry_source} buffer: {candidate_motifs}")
            else:
                retry_source = "none" # No input this cycle

            # --- RME Processing (Merge Attempt) ---
            if candidate_motifs:
                self.agent.metrics["buffer_merge_attempts"] += 1

                # --- Prepare arguments for RME.merge ---
                known_motifs = self.agent.rme.get_motifs()
                emotional_state = self.agent.ee.get_state()
                # Calculate echo score before calling merge
                echo = echo_score(candidate_motifs, known_motifs)
                # Define a base threshold (can be tuned)
                base_threshold = 0.05

                # Perform the merge attempt using RME's method with all required arguments
                merge_result = self.agent.rme.merge(
                    candidate_set=candidate_motifs,
                    echo_score=echo,
                    threshold=base_threshold, 
                    known_motifs=known_motifs,
                    emotional_state=emotional_state
                )

                # Calculate entropy reduction *after* the attempt
                # If merge succeeded, RME updated its last_entropy internally
                # If failed, calculate potential entropy if it *had* been added (for EE)
                entropy_after_attempt = self.agent.rme.last_entropy if merge_result else self.agent.rme.compute_entropy(self.agent.rme.elements.union(candidate_motifs))
                actual_entropy_reduction = entropy_before - entropy_after_attempt

                # Log entropy flow
                self.agent.metrics["entropy_flow"].append((entropy_before, self.agent.rme.last_entropy if merge_result else entropy_before, actual_entropy_reduction))
                if len(self.agent.metrics["entropy_flow"]) > 50: # Keep history manageable
                     self.agent.metrics["entropy_flow"].pop(0)

                # --- Emotion Adjustment (Post-Merge) ---
                emotion_event_info = {
                    "motifs": candidate_motifs,
                    "entropy_reduction": actual_entropy_reduction,
                    "echo_score": echo,
                    "source": retry_source # Pass source info to EE
                }
                if merge_result:
                    self.agent.metrics["buffer_merges"] += 1
                    self.agent.metrics["merge_outcomes"]["success"] += 1
                    # Adjust emotion based on success
                    joy_boost = 0
                    if actual_entropy_reduction > 0: joy_boost += min(2, int(actual_entropy_reduction * 10))
                    if echo > 0.3: joy_boost += 1
                    if joy_boost > 0:
                        emotion_event_info["type"] = "merge_success"
                        emotion_event_info["joy_boost"] = joy_boost
                        self.agent.ee.adjust(emotion_event_info)
                    # Use logger for verbose output
                    self.agent.logger.info(f"[RME Merged ({retry_source})] ΔH={actual_entropy_reduction:.2f}, Echo={echo:.2f}, Thr={current_threshold:.2f}")
                    # Keep self-narration on console periodically
                    if self.agent.metrics["buffer_merges"] % 5 == 0:
                         print("[Self-Narration] " + summarize_memory(self.agent.rme.get_motifs()))
                    # Clear any older blocked motifs if a retry succeeded
                    # if retry_source == "blocked_retry": pass # Already popped

                else: # Merge Blocked
                    self.agent.metrics["merge_outcomes"]["fail"] += 1
                    # Add to blocked buffer only if it came from fresh input
                    if retry_source == "input":
                        self.blocked_motifs_buffer.append(candidate_motifs)

                    # Adjust emotion based on failure
                    panic_boost = 0
                    if actual_entropy_reduction < -0.1: panic_boost += min(2, int(abs(actual_entropy_reduction * 5)))
                    if panic_boost > 0:
                         emotion_event_info["type"] = "merge_fail"
                         emotion_event_info["panic_boost"] = panic_boost
                         self.agent.ee.adjust(emotion_event_info)
                    # Use logger for verbose output
                    self.agent.logger.info(f"[RME Blocked ({retry_source})] ΔH={actual_entropy_reduction:.2f}, Echo={echo:.2f}, Thr={current_threshold:.2f}")
            else:
                 # No input in buffer, no retry triggered
                 # Use logger for verbose output
                 self.agent.logger.info("[Cycle] No input buffer content or retry triggered.")
                 # Apply internal emotion dynamics even if no input processed
                 self.agent.ee.adjust({"source": buffer_source_for_this_cycle}) # Pass the source context

            # --- Self-Model Update ---
            current_memory = self.agent.rme.get_motifs()
            current_emotion = self.agent.ee.get_state()
            new_reflections = self.agent.sms.update_self_model(current_memory, current_emotion)
            # Use logger for verbose output
            if new_reflections:
                self.agent.logger.info(f"[SMS Update] New reflections: {new_reflections}")
            # Feed new reflections back into RME
            if new_reflections:
                added_by_reflection = self.agent.rme.update(new_reflections)
                if added_by_reflection:
                    # Use logger for verbose output
                    self.agent.logger.info(f"[RME <- SMS] Added reflections to memory: {added_by_reflection}")
                    # Recalculate entropy after adding reflections
                    self.agent.rme.last_entropy = self.agent.rme.compute_entropy()
                # else: # Log if reflections already existed (optional)
                #     self.agent.logger.info("[RME <- SMS] Reflections already present in memory.")


            # --- Intent & Planning ---
            current_memory = self.agent.rme.get_motifs() # Re-fetch memory after potential reflection update
            current_emotion = self.agent.ee.get_state() # Re-fetch emotion state
            ipl_context = {
                "rme_state": {"elements": current_memory, "entropy": self.agent.rme.last_entropy},
                "ee_state": current_emotion,
                "sms_state": {"self_model": self.agent.sms.get_self_model(), "history": self.agent.sms.state_history},
                "positive_assoc": self.agent.ee.positive_associated_motifs,
                "negative_assoc": self.agent.ee.negative_associated_motifs,
                "last_buffer_content": candidate_motifs, # Content processed this cycle
                "last_merge_result": merge_result, # Outcome of merge attempt
                "last_actual_entropy_reduction": actual_entropy_reduction, # Entropy change
                "sms_instance": self.agent.sms,
                "ee_valence_func": self.agent.ee.valence,
                "current_buffer_source": buffer_source_for_this_cycle # Source of content
            }
            action_space = self.agent.ipl.generate_action_space(**ipl_context)
            chosen_action = self.agent.ipl.choose(action_space, **ipl_context)

            self.agent.metrics["actions_chosen"][chosen_action.get("type", "unknown")] += 1

            # --- Action Execution ---
            act_context = {
                "memory_elements": current_memory,
                "emotion_state": current_emotion,
                "positive_assoc": self.agent.ee.positive_associated_motifs,
                "negative_assoc": self.agent.ee.negative_associated_motifs,
                "buffer_content": candidate_motifs, # Content that led to this action
                "chosen_action_raw": chosen_action
            }
            action_result_output = self.agent.il.act(act_context)
            self.agent.last_output = action_result_output # Store the output

            # --- Post-Action Adjustments & Internal Re-perception ---
            # Feed action result back into perception (Inner Speech)
            if action_result_output and isinstance(action_result_output, str) and action_result_output != "...":
                # Use logger for verbose output
                self.agent.logger.info(f"[IL -> Perceive] Re-perceiving output: '{action_result_output}'")
                # Set the source before calling perceive for internal output
                self.current_buffer_source = "internal_action" # Set source for next cycle if this is perceived
                repercieved_motifs = self.agent.il.perceive(action_result_output, source="internal_action")
                # Use logger for verbose output
                if repercieved_motifs:
                    self.agent.logger.info(f"[IL -> Perceive] Generated motifs: {repercieved_motifs}")

            # Update metrics
            self.agent.metrics["emotion_counts"] = self.agent.ee.get_state()

            # --- Loop Delay ---
            time.sleep(10) 

# === Main Execution ===
if __name__ == '__main__':
    # Ensure modules in the current directory can be imported
    # sys.path.insert(0, '.') # Not strictly needed if run from the directory
    try:
        from mentor import AI
        mentor_available = True
    except ImportError:
        print("Warning: mentor.py not found. /train command will not work.")
        mentor_available = False
        AI = None # Define AI as None if import fails

    agent = REMindlet()

    # --- Attempt to load default checkpoint ---
    agent.load_checkpoint() # Tries to load "default_checkpoint.pkl"

    if mentor_available:
        mentor = AI()
    else:
        mentor = None

    print(f"MindletRE v3 (Modular) born. Logging to {agent.log_file}. Type /exit to quit.")
    # Start with verbose logging disabled by default
    # agent.toggle_verbose_logging() # Call this if you want to start non-verbose

    while True:
        try:
            # Keep user input prompt on console
            line = input(f"You ({agent.ee.get_emotion_face()}): ").strip()
        except EOFError: # Handle Ctrl+D
             line = "/exit"
        except KeyboardInterrupt: # Handle Ctrl+C
             line = "/exit"


        if not line: continue

        if line == "/exit":
            # Keep exit message on console
            print("\nShutting down MindletRE...")
            # Optional: Save checkpoint on exit?
            agent.save_checkpoint()
            # Attempt to stop the thread gracefully (Python doesn't guarantee immediate stop)
            # No direct stop method for threads, rely on daemon=True and program exit
            print("Exiting...")
            sys.exit(0) # Exit the main script
            break # Should not be reached if sys.exit works

        elif line == "/narrate":
            # Keep command output on console
            print(summarize_memory(agent.rme.get_motifs()))
        elif line == "/clusters":
            # Keep command output on console
            clusters = cluster_motifs(agent.rme.get_motifs())
            if clusters:
                for head, tails in clusters.items():
                    print(f"{head} → {sorted(tails)}")
            else:
                print("(no clusters found)")
        elif line == "/metrics":
            # Keep command output on console
            print("--- Agent Metrics ---")
            print(f"Cycle Count: {agent.metrics['cycle_count']}")
            print(f"Merge Attempts: {agent.metrics['buffer_merge_attempts']}")
            print(f"Successful Merges: {agent.metrics['buffer_merges']}")
            print(f"Merge Outcomes: {dict(agent.metrics['merge_outcomes'])}")
            print(f"Actions Chosen: {dict(agent.metrics['actions_chosen'])}")
            # Calculate avg entropy reduction from flow
            reductions = [r for _, _, r in agent.metrics['entropy_flow']]
            avg_reduction = sum(reductions) / len(reductions) if reductions else 0
            print(f"Avg Entropy Reduction (last 50): {avg_reduction:.3f}")
            print(f"Current Emotion: {dict(agent.ee.get_state())}")
            print(f"Current Self Model: {agent.sms.get_self_model()}")
            print(f"IL Buffer Size: {len(agent.il.input_buffer)}")
            print(f"Blocked Retry Buffer Size: {len(agent.thought_thread.blocked_motifs_buffer)}")
            print("---------------------\n")

        elif line == "/toggle_logging":
            # Toggle function now handles printing/logging the status change
            agent.toggle_verbose_logging()
        elif line.startswith("/save"):
            parts = line.split(maxsplit=1)
            filename = parts[1] + ".pkl" if len(parts) > 1 else "default_checkpoint.pkl"
            agent.save_checkpoint(filename)
            # Confirmation is printed by save_checkpoint
        elif line.startswith("/load"):
            parts = line.split(maxsplit=1)
            filename = parts[1] + ".pkl" if len(parts) > 1 else "default_checkpoint.pkl"
            agent.load_checkpoint(filename)
            # Confirmation/error is printed by load_checkpoint
        elif (line == "/train" or line.startswith("/train ")) and mentor_available:
            # Keep training messages on console
            parts = line.split()
            steps = 10 # Default steps
            train_verbose = False # Default training verbosity (console)
            if len(parts) > 1:
                try:
                    steps = int(parts[1])
                except ValueError:
                    print("Invalid number of steps. Using default 10.")
            if len(parts) > 2 and parts[2].lower() == 'verbose':
                 train_verbose = True

            print(f"Starting {steps}-step training with LLM mentor... ({'verbose console' if train_verbose else 'quiet console'} mode)")

            original_agent_logging_flag = agent.verbose_logging # Store the flag state
            agent.verbose_logging = train_verbose # Set flag for console handler level
            agent._update_console_log_level() # Update console handler level

            # Pass the agent instance to the mentor
            result = mentor.start_training(agent, steps)
            print(result) # Keep mentor output on console

            while mentor.training_mode:
                result = mentor.continue_training()
                print(result) # Keep mentor output on console

            agent.verbose_logging = original_agent_logging_flag # Restore flag state
            agent._update_console_log_level() # Restore console handler level
            # Keep training finished message on console
            print(f"Training finished. Verbose console logging restored to: {'enabled' if agent.verbose_logging else 'disabled'}.")
        elif line.startswith("/"):
             # Keep unknown command message on console
             print(f"Unknown command: {line}")
        else:
            # Process regular input via InteractionLoop
            # Set source to external before perceiving user input
            agent.thought_thread.current_buffer_source = "external" # Mark source for next cycle
            agent.il.perceive(line, source="user")
            # Output is generated within the ThoughtThread via il.act()
            # and stored in agent.last_output. The main loop doesn't need to print it,
            # as il.act() handles printing the agent's response.

    # This part might not be reached if sys.exit() is called
    print("MindletRE has ceased.")
