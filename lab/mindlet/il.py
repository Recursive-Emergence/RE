\
# filepath: /media/im2/plus/lab4/ACI/lab/mindlet/il.py
import time
from collections import deque, Counter
import random # Needed for fallback in act

class InteractionLoop:
    """
    Handles the interface between the agent and the external environment (or mentor).
    Manages input perception and action execution.
    """
    def __init__(self, buffer_maxlen=20):
        # Input buffer stores processed input motifs before RME merge attempt
        self.input_buffer = deque(maxlen=buffer_maxlen)
        self.buffer_timestamps = deque() # Track arrival time for latency metrics
        self.last_interaction_log = None

    def perceive(self, input_data, source="user"):
        """
        Processes raw input data (e.g., text) into motifs and stores in buffer.
        Migrated from REmindlet.process_input.
        Returns the motifs added to the buffer.
        """
        added_motifs = set()
        if isinstance(input_data, str):
            line = input_data.strip()
            if line:
                # Simple tokenization (can be improved)
                tokens = line.split()
                # Create 1-grams and 2-grams
                for i in range(len(tokens)):
                    motif1 = (tokens[i],)
                    self.input_buffer.append(motif1)
                    self.buffer_timestamps.append(time.time())
                    added_motifs.add(motif1)
                    if i < len(tokens) - 1:
                        motif2 = (tokens[i], tokens[i+1])
                        self.input_buffer.append(motif2)
                        self.buffer_timestamps.append(time.time())
                        added_motifs.add(motif2)
        else:
            # Handle other potential input types if necessary
            print(f"Warning: IL.perceive received non-string input: {type(input_data)}")
            
        # Log the perception event
        self.log_interaction(event_type="perceive", data={"source": source, "raw": input_data, "motifs": added_motifs})
        return added_motifs # Return the set of motifs generated from this input

    def get_buffered_input(self):
        """Returns the current content of the input buffer and clears it."""
        buffered = set(self.input_buffer)
        timestamps = list(self.buffer_timestamps)
        self.input_buffer.clear()
        self.buffer_timestamps.clear()
        # Calculate average latency if timestamps exist
        latency = (time.time() - timestamps[0]) if timestamps else 0.0
        return buffered, latency

    def act(self, action_details):
        """
        Executes an action chosen by the IPL.
        Placeholder: Currently uses the old 'express' logic to generate output directly.
        In the final architecture, 'action_details' should specify what to do.
        """
        # TODO: Refine this. 'action_details' should come from IPL.
        # For now, assume action_details contains necessary context (memory, emotion state)
        # to run the old express logic as a placeholder for generating output.

        memory_elements = action_details.get("memory_elements", set())
        emotion_state = action_details.get("emotion_state", Counter())
        positive_assoc = action_details.get("positive_assoc", set())
        negative_assoc = action_details.get("negative_assoc", set())
        buffer_content = action_details.get("buffer_content", set()) # Content of buffer *before* it was cleared

        if not memory_elements:
            output = "..."
        else:
            # --- Start of migrated 'express' logic ---
            panic = emotion_state.get('panic', 0)
            joy = emotion_state.get('joy', 0)
            is_positive = joy > panic

            memory_list = list(memory_elements)
            # Look back at recent memory
            recent_memory = [m for m in memory_list if isinstance(m, tuple)][-min(len(memory_list), 30):]

            candidates = []
            for motif in recent_memory:
                score = 0
                motif_words = set(motif)

                # Relevance to input buffer (that triggered this cycle)
                overlap = len(motif_words.intersection(buffer_content))
                if overlap > 0: score += overlap * 2

                # Relevance to emotional context
                if is_positive and motif in positive_assoc: score += 1
                elif not is_positive and motif in negative_assoc: score += 1
                
                # Recency boost
                if score == 0 and motif in recent_memory[-10:]: score += 0.1

                if score > 0: candidates.append((score, motif))

            if not candidates:
                # Fallback
                sample_pool = [m for m in memory_list if isinstance(m, tuple)][-min(len(memory_list), 10):]
                actual_sample_size = min(3, len(sample_pool))
                if actual_sample_size > 0:
                    sample = random.sample(sample_pool, actual_sample_size)
                    output = " ".join(" ".join(t) for t in sample)
                else:
                    output = "..."
            else:
                # Select top N candidates
                candidates.sort(key=lambda x: x[0], reverse=True)
                num_to_express = min(3, len(candidates))
                chosen_motifs = [motif for score, motif in candidates[:num_to_express]]
                output = " ".join(" ".join(t) for t in chosen_motifs)
            # --- End of migrated 'express' logic ---

        # Log the action event
        self.log_interaction(event_type="act", data={"chosen_action": action_details.get("chosen_action_raw", "express_placeholder"), "output": output})
        
        # In a real scenario, this would perform the action (e.g., print to console, send API request)
        # For now, it just returns the generated text.
        return output # Return the result of the action (e.g., the text expressed)


    def log_interaction(self, event_type, data):
        """Logs key details about perception and action events."""
        log_entry = {
            "timestamp": time.time(),
            "event": event_type,
            "details": data
        }
        self.last_interaction_log = log_entry
        # In a real implementation, this might write to a file or database.
        # print(f"[IL Log] {log_entry}") # Optional: print log

