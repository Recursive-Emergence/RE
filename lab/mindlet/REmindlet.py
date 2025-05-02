# ReMindlet v3.0: Modular Recursive Emergence Agent
from threading import Thread
import math, random, time
from collections import Counter, deque

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
        self.verbose_logging = True
        
        # Store motifs associated with recent merge outcomes (can be used by EE/IPL)
        # Consider moving this logic into EE or making it part of state snapshots
        self.recently_positive_motifs = deque(maxlen=20) 
        self.recently_negative_motifs = deque(maxlen=20)

        self.last_output = None # Add attribute to store last output

        # Start the main agent processing loop
        self.thought_thread = ThoughtThread(self)
        self.thought_thread.daemon = True
        self.thought_thread.start()

    # Methods like process_input, express, emotion_face, emotional_threshold are removed
    # as their logic is now within the modules IL, EE.

# === Thought Thread ===
class ThoughtThread(Thread):
    def __init__(self, agent):
        super().__init__()
        self.agent = agent
        self.base_merge_threshold = 0.05 # Base threshold for entropy reduction merge

    def run(self):
        while True:
            self.agent.metrics["cycle_count"] += 1
            if self.agent.verbose_logging:
                print(f"\n--- Cycle {self.agent.metrics['cycle_count']} ---")

            # --- Perception Phase (Handled by IL externally, check buffer here) ---
            # Get buffered input motifs from the Interaction Loop
            candidate_motifs, latency = self.agent.il.get_buffered_input()
            merge_result = None
            entropy_reduction = 0
            echo = 0

            if candidate_motifs:
                if self.agent.verbose_logging:
                    print(f"[RME] Processing buffer: {candidate_motifs}")
                
                self.agent.metrics["buffer_merge_attempts"] += 1
                if latency > 0:
                     self.agent.metrics["avg_buffer_latency"] = (
                         self.agent.metrics["avg_buffer_latency"] * (self.agent.metrics["buffer_merge_attempts"] -1) + latency
                         ) / self.agent.metrics["buffer_merge_attempts"]


                # --- RME Merge Attempt ---
                # Calculate potential merge impact
                entropy_before = self.agent.rme.compute_entropy()
                combined_potential = self.agent.rme.get_motifs().union(candidate_motifs)
                
                # Temp calculation for entropy_after (RME merge should ideally return this)
                tokens = [token for tup in combined_potential if isinstance(tup, tuple) for token in tup]
                total = len(tokens)
                if total > 0:
                    freq = Counter(tokens)
                    entropy_after = -sum((c/total) * math.log2(c/total) for c in freq.values() if c > 0)
                else:
                    entropy_after = 0
                entropy_reduction = entropy_before - entropy_after
                
                echo = echo_score(candidate_motifs, self.agent.rme.get_motifs())
                self.agent.metrics["avg_echo_score"] = (
                    self.agent.metrics["avg_echo_score"] * (self.agent.metrics["buffer_merge_attempts"] -1) + echo
                    ) / self.agent.metrics["buffer_merge_attempts"]
                
                reuse_count = sum(1 for e in candidate_motifs if e in self.agent.rme.get_motifs())
                self.agent.metrics["motif_reuse"] += reuse_count

                # Get emotional modifier for threshold
                emo_threshold_mod = self.agent.ee.get_emotional_threshold_modifier()
                current_threshold = self.base_merge_threshold + emo_threshold_mod

                # Call RME merge
                merge_result = self.agent.rme.merge(
                    candidate_set=candidate_motifs,
                    entropy_reduction=entropy_reduction,
                    echo_score=echo,
                    threshold=current_threshold,
                    known_motifs=self.agent.rme.get_motifs() # Pass known motifs for resonance check
                )

                self.agent.metrics["entropy_flow"].append((entropy_before, self.agent.rme.last_entropy, entropy_reduction))
                if len(self.agent.metrics["entropy_flow"]) > 50: # Keep history manageable
                     self.agent.metrics["entropy_flow"].pop(0)

                # --- Emotion Adjustment (Post-Merge) ---
                if merge_result:
                    self.agent.metrics["buffer_merges"] += 1
                    self.agent.metrics["merge_outcomes"]["success"] += 1
                    self.agent.recently_positive_motifs.extend(candidate_motifs)
                    # Adjust emotion based on success (e.g., joy boost scaled by reduction/echo)
                    joy_boost = 0
                    if entropy_reduction > 0: joy_boost += min(2, int(entropy_reduction * 10))
                    if echo > 0.3: joy_boost += 1
                    if joy_boost > 0:
                        self.agent.ee.adjust({"type": "merge_success", "joy_boost": joy_boost})
                    if self.agent.verbose_logging:
                        print(f"[RME Merged] ΔH={entropy_reduction:.2f}, Echo={echo:.2f}, Thr={current_threshold:.2f}")
                    if self.agent.metrics["buffer_merges"] % 5 == 0:
                         print("[Self-Narration] " + summarize_memory(self.agent.rme.get_motifs()))

                else:
                    self.agent.metrics["merge_outcomes"]["fail"] += 1
                    self.agent.recently_negative_motifs.extend(candidate_motifs)
                    # Adjust emotion based on failure (e.g., panic boost scaled by negative reduction)
                    panic_boost = 0
                    if entropy_reduction < -0.1: panic_boost += min(2, int(abs(entropy_reduction * 5)))
                    if panic_boost > 0:
                         self.agent.ee.adjust({"type": "merge_fail", "panic_boost": panic_boost})
                    if self.agent.verbose_logging:
                        print(f"[RME Blocked] ΔH={entropy_reduction:.2f}, Echo={echo:.2f}, Thr={current_threshold:.2f}")
            else:
                 # No input in buffer, still run internal dynamics
                 if self.agent.verbose_logging:
                     print("[Cycle] No input buffer content.")
                 # Apply internal emotion dynamics even if no input processed
                 self.agent.ee.adjust(None) # Pass None or {} to trigger internal dynamics

            # --- Self-Model Update ---
            current_memory = self.agent.rme.get_motifs()
            current_emotion = self.agent.ee.get_state()
            new_reflections = self.agent.sms.update_self_model(current_memory, current_emotion)
            if new_reflections and self.agent.verbose_logging:
                print(f"[SMS Update] New reflections: {new_reflections}")
            # Optionally merge new reflections back into RME?
            # if new_reflections:
            #     self.agent.rme.update(new_reflections) # Direct update, bypass merge logic?

            # --- Intent & Planning ---
            # Package current state for IPL
            ipl_context = {
                "rme_state": {"elements": current_memory, "entropy": self.agent.rme.last_entropy},
                "ee_state": current_emotion,
                "sms_state": {"self_model": self.agent.sms.get_self_model(), "history": self.agent.sms.state_history},
                "positive_assoc": set(self.agent.recently_positive_motifs),
                "negative_assoc": set(self.agent.recently_negative_motifs),
                "last_buffer_content": candidate_motifs # Pass the input that was just processed
            }
            action_space = self.agent.ipl.generate_action_space(**ipl_context)
            chosen_action = self.agent.ipl.choose(action_space, **ipl_context)
            self.agent.metrics["actions_chosen"][chosen_action.get("type", "unknown")] += 1

            # --- Action Execution ---
            # Prepare context needed for the action (specifically for the placeholder 'act')
            act_context = {
                "memory_elements": current_memory,
                "emotion_state": current_emotion,
                "positive_assoc": set(self.agent.recently_positive_motifs),
                "negative_assoc": set(self.agent.recently_negative_motifs),
                "buffer_content": candidate_motifs, # Content that led to this action
                "chosen_action_raw": chosen_action # Pass the chosen action itself
            }
            # IL.act executes the action (currently prints output via placeholder logic)
            action_result_output = self.agent.il.act(act_context)
            self.agent.last_output = action_result_output # Store the output

            # action_result_output contains the string that was printed by il.act

            # --- Post-Action Adjustments ---
            # Adjust Emotion based on action result (Placeholder)
            # TODO: Define how action results affect emotion
            # self.agent.ee.adjust({"type": "action_result", "result": action_result_output})

            # Merge action result back into memory? (Placeholder)
            # TODO: Decide if/how action outputs become memory motifs
            # result_motifs = self.agent.il.perceive(action_result_output, source="internal_action") # Process output like input?
            # if result_motifs:
            #     self.agent.rme.merge(result_motifs, ...) # Use merge logic again?

            # --- Self-Model Simulation (Placeholder) ---
            # Simulate the effects of the chosen action (optional, for future refinement)
            # predicted_outcome = self.agent.sms.simulate(chosen_action, ipl_context)
            # if self.agent.verbose_logging:
            #      print(f"[SMS Simulate] Predicted outcome: {predicted_outcome}")


            # Update metrics
            self.agent.metrics["emotion_counts"] = self.agent.ee.get_state()

            # --- Loop Delay ---
            time.sleep(2) # Reduced sleep time

# === Main Execution ===
if __name__ == '__main__':
    import sys
    # Ensure modules in the current directory can be imported
    sys.path.insert(0, '.') 
    # Assuming mentor.py is in the same directory or accessible via PYTHONPATH
    try:
        from mentor import AI
        mentor_available = True
    except ImportError:
        print("Warning: mentor.py not found. /train command will not work.")
        mentor_available = False
        AI = None # Define AI as None if import fails

    agent = REMindlet()
    if mentor_available:
        mentor = AI()
    else:
        mentor = None
        
    print("MindletRE v3 (Modular) born.")
    agent.verbose_logging = True # Default to verbose

    while True:
        try:
            line = input(f"You ({agent.ee.get_emotion_face()}): ").strip()
        except EOFError: # Handle Ctrl+D
             line = "/exit"
             
        if not line: continue

        if line == "/exit":
            print("\nShutting down MindletRE...")
            # TODO: Add any cleanup if needed (e.g., saving state)
            break
        elif line == "/narrate":
            print(summarize_memory(agent.rme.get_motifs()))
        elif line == "/clusters":
            clusters = cluster_motifs(agent.rme.get_motifs())
            if clusters:
                for head, tails in clusters.items():
                    print(f"{head} → {sorted(tails)}")
            else:
                print("(no clusters found)")
        elif line == "/metrics":
            print("--- Agent Metrics ---")
            for k, v in agent.metrics.items():
                if k == 'entropy_flow':
                     print(f"entropy_flow: [Last 10 reductions: {[f'{r:.2f}' for _,_,r in v[-10:]]}]")
                elif isinstance(v, Counter):
                     print(f"{k}: {dict(v)}")
                elif isinstance(v, float):
                     print(f"{k}: {v:.3f}")
                else:
                     print(f"{k}: {v}")
            print(f"Current Emotion: {dict(agent.ee.get_state())}")
            print(f"Current Self Model: {agent.sms.get_self_model()}")
            print("---------------------")
        elif line == "/toggle_logging":
            agent.verbose_logging = not agent.verbose_logging
            print(f"Verbose logging {'enabled' if agent.verbose_logging else 'disabled'}")
        elif (line == "/train" or line.startswith("/train ")) and mentor_available:
            parts = line.split()
            steps = 20
            train_verbose = True

            if len(parts) > 1:
                if parts[1].isdigit():
                    steps = int(parts[1])
                    if len(parts) > 2 and parts[2] == "quiet": train_verbose = False
                elif parts[1] == "quiet":
                    train_verbose = False

            print(f"Starting {steps}-step training with LLM mentor... ({'verbose' if train_verbose else 'quiet'} mode)")
            
            original_agent_logging = agent.verbose_logging
            agent.verbose_logging = train_verbose

            # Pass the agent instance to the mentor
            result = mentor.start_training(agent, steps) 
            print(result)

            while mentor.training_mode:
                result = mentor.continue_training()
                print(result)

            agent.verbose_logging = original_agent_logging
            print(f"Training finished. Verbose logging restored to: {'enabled' if agent.verbose_logging else 'disabled'}.")
        elif line.startswith("/"):
             print(f"Unknown command: {line}")
        else:
            # Process regular input via InteractionLoop
            agent.il.perceive(line)
            # Output is now generated and printed within the ThoughtThread via il.act()
            # We just wait for the next cycle implicitly.

    print("MindletRE has ceased.")
