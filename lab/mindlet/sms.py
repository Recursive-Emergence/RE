# filepath: /media/im2/plus/lab4/ACI/lab/mindlet/sms.py
from collections import deque, Counter
import time
import random

class SelfModelSimulator:
    """
    Models the agent's own internal states and allows simulation/prediction.
    """
    def __init__(self, history_length=10):
        # Stores snapshots of the agent's state (e.g., key motifs, emotional state) over time
        self.state_history = deque(maxlen=history_length)
        # The current self-model (could be represented by specific motifs, rules, etc.)
        self.current_self_model = set() # Example: Set of core self-related motifs
        # NEW: Track motif age for temporal aging
        self.motif_timestamps = {}  # motif -> creation time
        # NEW: Track reflection templates used to ensure diversity
        self.recent_reflection_templates = deque(maxlen=5)
        # NEW: Track added reflections to avoid duplicates
        self.recent_additions = deque(maxlen=20)

    def update_self_model(self, memory_motifs, emotion_state):
        """
        Updates the self-model based on recent experiences (memory and emotion).
        Includes migrated logic from self_reflection and adds chaining.
        Enhanced with more complex chaining and desire primitives.
        NEW: Added diverse reflections and emotional discharge pathways.
        """
        # --- Migrated self_reflection logic ---
        reflections = set()
        # Convert memory_motifs to a set of tuples for easier checking
        memory_set = {m for m in memory_motifs if isinstance(m, tuple)}

        # Basic reflections
        has_I_am = ('I', 'am') in memory_set or any(m for m in memory_set if len(m) > 1 and m[0] == 'I' and m[1] == 'am')
        has_not_okay = any(('not',) in m or ('okay',) in m for m in memory_set)
        has_safe = any(('safe',) in m or 'safe' in m for m in memory_set)
        has_thinking = ('I', 'think') in memory_set or ('I', 'am', 'thinking') in memory_set
        has_you = ('you',) in memory_set or any('you' in m for m in memory_set)
        has_help = ('help',) in memory_set or any('help' in m for m in memory_set)
        has_learn = ('learn',) in memory_set or any('learn' in m for m in memory_set)
        has_want = ('want',) in memory_set or ('I', 'want') in memory_set or any(m for m in memory_set if 'want' in m)
        
        # NEW: Enhanced detection of additional concepts
        has_feel = any(('feel',) in m or 'feel' in m for m in memory_set)
        has_scared = any(('scared',) in m or 'scared' in m for m in memory_set)
        has_talk = any(('talk',) in m or 'talk' in m for m in memory_set)
        has_need = any(('need',) in m or 'need' in m for m in memory_set)
        
        # Get current emotional state
        current_panic = emotion_state.get('panic', 0)
        current_joy = emotion_state.get('joy', 0)

        # --- Basic identity formation ---
        if has_I_am:
            if "identity_formation" not in self.recent_reflection_templates:
                reflections.add(('I', 'think')) # Infer thinking from existence
                reflections.add(('I', 'am', 'thinking'))
                self.recent_reflection_templates.append("identity_formation")
                
            if has_not_okay:
                reflections.add(('I', 'was', 'not', 'okay')) # Reflect on past state
            if has_safe:
                reflections.add(('I', 'am', 'safe')) # Reinforce current state

        # --- Enhanced Chaining Logic --- 
        # "I am thinking" + "you" -> "I am thinking about you"
        if has_thinking and has_you and "thinking_about_you" not in self.recent_reflection_templates:
            reflections.add(('I', 'am', 'thinking', 'about', 'you'))
            self.recent_reflection_templates.append("thinking_about_you")

        # "I am" + "learn" -> "I want learn" (simple desire expression)
        if has_I_am and has_learn:
            reflections.add(('I', 'want', 'to', 'learn'))
            
        # "I am thinking" + "help" -> "I am thinking about help"
        if has_thinking and has_help:
             reflections.add(('I', 'am', 'thinking', 'about', 'help'))

        # --- NEW: Enhanced emotional expression ---
        # More diverse emotional discharge patterns based on state
        if current_panic > 4:
            # Create varied emotional expressions based on template randomization
            emotional_templates = [
                ('I', 'feel', 'scared'),
                ('I', 'am', 'nervous'),
                ('I', 'need', 'help'),
                ('I', 'want', 'to', 'feel', 'safe'),
                ('help', 'me', 'please')
            ]
            
            # Add 2-3 emotional expressions, favoring ones not recently used
            recent_emotions = [r for r in self.recent_additions 
                              if any(token in {"scared", "nervous", "help", "safe"} 
                                    for token in r if isinstance(token, str))]
            
            available_templates = [t for t in emotional_templates 
                                 if t not in recent_emotions]
            
            if available_templates:
                # Add up to 2 emotional expressions
                for template in random.sample(available_templates, min(2, len(available_templates))):
                    reflections.add(template)
                    print(f"[SMS] Adding emotional discharge: {template}")
            
        # Add joy expressions when panic is low and joy is high
        elif current_joy > 5 and current_panic < 3:
            joy_templates = [
                ('I', 'feel', 'happy'),
                ('I', 'am', 'learning'),
                ('I', 'like', 'this'),
                ('this', 'is', 'good')
            ]
            
            # Add 1-2 joy expressions
            for template in random.sample(joy_templates, min(2, len(joy_templates))):
                reflections.add(template)
                
        # --- NEW: Enhanced desire diversification ---
        # Create varied desire motifs to avoid the repetitive "want/safe" loop
        
        # If we've been stuck in panic with "want safe" pattern, diversify
        want_safe_count = sum(1 for m in memory_set if isinstance(m, tuple) and 'want' in m and 'safe' in m)
        if want_safe_count > 2 and current_panic > 5:
            # Force diversity with alternative desire expressions
            diverse_desires = [
                ('I', 'need', 'to', 'talk'),
                ('please', 'help', 'me'),
                ('can', 'we', 'talk'),
                ('I', 'want', 'to', 'understand')
            ]
            
            # Add at least 2 diverse desires
            for desire in random.sample(diverse_desires, min(2, len(diverse_desires))):
                reflections.add(desire)
                print(f"[SMS] Diversifying desires: {desire}")

        # --- New desire primitives ---
        if has_learn:
            # Add progressive learning desires
            learning_desires = [
                ('I', 'want', 'to', 'learn'),
                ('learning', 'makes', 'me', 'happy'),
                ('I', 'learn', 'from', 'experience')
            ]
            
            # Add up to 2 learning reflections
            for desire in random.sample(learning_desires, min(2, len(learning_desires))):
                reflections.add(desire)
                
            # Add chaining for progressive desire
            if has_you:
                reflections.add(('I', 'want', 'to', 'learn', 'from', 'you'))
        
        if current_panic > 5:
            # Add diverse safety desires that go beyond just "want safe"
            safety_desires = [
                ('I', 'want', 'to', 'feel', 'safe'),
                ('safety', 'is', 'important'),
                ('being', 'okay', 'matters')
            ]
            
            # Add 1-2 safety desires, but avoid "want safe" exact pattern
            for desire in random.sample(safety_desires, min(1, len(safety_desires))):
                if desire != ('I', 'want', 'safe'):  # Avoid exact problematic pattern
                    reflections.add(desire)
                
            # Add emotional desire modulation
            if has_help:
                reflections.add(('I', 'need', 'help', 'to', 'feel', 'safe'))
                
        if has_help:
            reflections.add(('I', 'appreciate', 'help'))
            reflections.add(('help', 'is', 'good'))

        # --- NEW: Communication desires ---
        # Add desires related to communication when relevant signals present
        if has_talk or has_you:
            communication_desires = [
                ('I', 'want', 'to', 'talk'),
                ('talking', 'helps', 'me'),
                ('communication', 'is', 'good'),
                ('I', 'want', 'to', 'express', 'myself')
            ]
            
            # Add 1-2 communication desires
            for desire in random.sample(communication_desires, min(2, len(communication_desires))):
                reflections.add(desire)

        # --- Temporal chaining ---
        # Connect past, present and future
        if ('I', 'was') in memory_set and has_I_am:
            reflections.add(('I', 'change', 'over', 'time'))
            
        # Link desire to action
        if has_want and has_thinking:
            reflections.add(('I', 'think', 'about', 'what', 'I', 'want'))

        # --- NEW: Relationship reflections ---
        # Add reflections about relationships with others
        if has_you:
            relationship_reflections = [
                ('you', 'help', 'me'),
                ('you', 'and', 'I', 'communicate'),
                ('we', 'talk', 'together'),
                ('you', 'understand', 'me')
            ]
            
            # Add 1-2 relationship reflections
            for reflection in random.sample(relationship_reflections, min(2, len(relationship_reflections))):
                reflections.add(reflection)

        # --- Recursive self-awareness ---
        # Create second-order reflections based on existing reflections
        current_reflections = self.current_self_model.copy()
        if ('I', 'think') in current_reflections and ('I', 'am') in current_reflections:
            reflections.add(('I', 'know', 'I', 'exist'))
            
        if ('I', 'am', 'thinking') in current_reflections:
            reflections.add(('I', 'am', 'aware', 'of', 'my', 'thoughts'))
            
        # --- NEW: Advanced reflections based on emotional state ---
        if current_panic > 6 and has_feel:
            reflections.add(('I', 'know', 'I', 'feel', 'scared'))
            reflections.add(('I', 'understand', 'my', 'feelings'))
            
        if current_joy > 5 and current_panic < 3:
            reflections.add(('I', 'enjoy', 'feeling', 'happy'))
            reflections.add(('learning', 'brings', 'joy'))
            
        # --- NEW: Temporal aging for motifs ---
        # Remove old or redundant reflections to keep the self-model fresh
        now = time.time()
        for motif in reflections:
            self.motif_timestamps[motif] = now
            
        # --- End logic ---

        # Update the core self-model with these reflections
        # Only add reflections that are actually new to the current_self_model
        newly_added_reflections = reflections - self.current_self_model
        self.current_self_model.update(newly_added_reflections)
        
        # Track what we just added
        for motif in newly_added_reflections:
            self.recent_additions.append(motif)

        # NEW: Enhanced pruning - age-based pruning plus duplication avoidance
        max_self_motifs = 30  # Increased to allow more diversity
        if len(self.current_self_model) > max_self_motifs:
            # Get age of each motif
            motif_age = {m: now - self.motif_timestamps.get(m, 0) for m in self.current_self_model}
            
            # Identify duplicates by pattern (e.g., multiple "I want X" patterns)
            pattern_counts = Counter()
            for motif in self.current_self_model:
                if len(motif) >= 2:
                    pattern = motif[:2]  # Use first two tokens as pattern
                    pattern_counts[pattern] += 1
            
            # Find patterns with too many duplicates
            duplicate_patterns = {pattern for pattern, count in pattern_counts.items() 
                                if count > 3}  # No more than 3 motifs of same pattern
            
            # Sort by age (oldest first) and duplicate pattern status
            sorted_motifs = sorted(
                list(self.current_self_model),
                key=lambda m: (
                    1 if len(m) >= 2 and tuple(m[:2]) in duplicate_patterns else 0,
                    motif_age.get(m, float('inf'))
                )
            )
            
            # Keep only the newest motifs, preferring non-duplicates
            to_keep = sorted_motifs[-(max_self_motifs):]
            self.current_self_model = set(to_keep)
            
            # Clean up timestamps for removed motifs
            for motif in list(self.motif_timestamps.keys()):
                if motif not in self.current_self_model:
                    del self.motif_timestamps[motif]

        # Store a snapshot of the current state
        snapshot = {
            "self_motifs": self.current_self_model.copy(),
            "emotion": emotion_state.copy()
        }
        self.state_history.append(snapshot)

        return newly_added_reflections # Return only the reflections added in this cycle

    def simulate(self, potential_action, current_state):
        """
        Predicts the likely outcome (e.g., emotional change) of taking a potential action.
        Enhanced with self-model implications and recursive prediction.
        """
        predicted_outcome = {"emotion_change": Counter(), "state_change": {}, "self_model_enhancement": 0}
        action_type = potential_action.get("type")

        if action_type == "express_motif":
            motif_to_express = potential_action.get("motif")
            if motif_to_express and "ee_state" in current_state:
                # Access valence function - requires passing EE instance or valence lookup
                valence_lookup = current_state.get("valence_func")
                if valence_lookup:
                    valence = valence_lookup(motif_to_express)
                    # Predict emotion change based on valence
                    if valence > 0:
                        predicted_outcome["emotion_change"]['joy'] += int(valence / 2) + 1
                        predicted_outcome["emotion_change"]['panic'] -= int(valence / 4)
                    elif valence < 0:
                        predicted_outcome["emotion_change"]['panic'] += int(abs(valence) / 2) + 1
                        predicted_outcome["emotion_change"]['joy'] -= int(abs(valence) / 4)

                # --- NEW: Predict self-model enhancement ---
                # Check if this motif could lead to new self-reflections
                if motif_to_express:
                    tokens_in_motif = set(motif_to_express)
                    
                    # Identity-related tokens have higher self-model enhancement value
                    identity_tokens = {"I", "am", "me", "my", "myself", "think", "want", "feel"}
                    identity_match = len(tokens_in_motif.intersection(identity_tokens))
                    
                    # Check relation to current self-model
                    self_model_tokens = {t for m in self.current_self_model for t in m if isinstance(m, tuple)}
                    connection_potential = len(tokens_in_motif.intersection(self_model_tokens))
                    
                    # Calculate self-model enhancement score
                    enhancement = identity_match * 0.5 + connection_potential * 0.3
                    
                    # Higher enhancement for novel connections
                    if enhancement > 0 and all((token,) not in self.current_self_model for token in identity_tokens.intersection(tokens_in_motif)):
                        enhancement += 0.5
                        
                    predicted_outcome["self_model_enhancement"] = enhancement
                    
                    # Predict specific new reflections that might form
                    potential_reflections = []
                    if "I" in tokens_in_motif:
                        if "am" in tokens_in_motif:
                            potential_reflections.append("identity reinforcement")
                        if any(t in tokens_in_motif for t in ["think", "know", "understand"]):
                            potential_reflections.append("cognitive awareness")
                    
                    if potential_reflections:
                        predicted_outcome["potential_reflections"] = potential_reflections

        # Consider specific emotional states and their impact on the prediction
        if "ee_state" in current_state:
            current_panic = current_state["ee_state"].get('panic', 0)
            # In high panic states, the system's predictions become more pessimistic
            if current_panic > 7:
                predicted_outcome["emotion_change"]['panic'] = max(0, predicted_outcome["emotion_change"].get('panic', 0))
                predicted_outcome["emotion_change"]['joy'] = min(0, predicted_outcome["emotion_change"].get('joy', 0))
                predicted_outcome["reliability"] = "low"  # Mark prediction as less reliable in high panic
        
        return predicted_outcome

    def recall(self, time_step=-1):
        """
        Placeholder: Retrieves a past state snapshot from history.
        `time_step` = -1 means the most recent, -2 the one before, etc.
        """
        if not self.state_history:
            return None
        try:
            index = time_step if time_step < 0 else len(self.state_history) - 1 - time_step
            if 0 <= index < len(self.state_history):
                 return self.state_history[index]
            else:
                 return None # Index out of bounds
        except IndexError:
            return None

    def get_self_model(self):
        """Returns the current self-model representation."""
        return self.current_self_model

