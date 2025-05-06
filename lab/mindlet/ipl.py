import random 
from collections import Counter
import logging

class IntentPlanningLayer:
    """
    Evaluates possible actions, chooses paths based on internal goals (entropy, emotion),
    and potentially builds simple plans.
    """
    def __init__(self):
        self.current_goals = [] # Example: ['reduce_panic', 'increase_joy', 'explore']
        self.action_history = [] # Track past actions and outcomes
        self.repeated_motif_count = {}  # Track how many times a motif has been chosen consecutively
        # Set up logger
        self.logger = logging.getLogger("IPL")
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)

    def generate_action_space(self, rme_state, ee_state, sms_state, **kwargs):
        """
        Generates a set of possible actions the agent could take.
        Enhanced to increase variety and avoid repetitive loops.
        """
        possible_actions = []
        memory_elements = rme_state.get("elements", set())
        
        # Retrieve any previously chosen action to avoid repetition
        recent_outputs = kwargs.get("recent_outputs", [])
        last_chosen_motif = None
        if self.action_history:
            last_action = self.action_history[-1]
            if isinstance(last_action, dict) and last_action.get("type") == "express_motif":
                last_chosen_motif = last_action.get("motif")

        # NEW: Get motifs in cooldown from RME
        cooled_motifs = set()
        rme_instance = kwargs.get("rme_instance")
        if rme_instance and hasattr(rme_instance, 'get_cooldown_motifs'):
            cooled_motifs = rme_instance.get_cooldown_motifs()
            if cooled_motifs:
                self.logger.debug(f"Excluding {len(cooled_motifs)} cooled motifs")

        # 1. Express recent memory (similar to old express fallback)
        # But avoid adding the last expressed motif to prevent immediate repetition
        recent_motifs = list(memory_elements)[-15:] if len(memory_elements) > 15 else list(memory_elements)
        if recent_motifs:
            # Filter out any exact matches to the last chosen motif and cooled motifs
            candidate_motifs = [motif for motif in recent_motifs if
                               isinstance(motif, tuple) and 
                               motif != last_chosen_motif and
                               motif not in cooled_motifs]
            
            # Add up to 5 motifs from memory
            unique_candidates = set()
            for motif in candidate_motifs:
                if len(unique_candidates) >= 5:
                    break
                if isinstance(motif, tuple) and motif not in unique_candidates:
                    possible_actions.append({"type": "express_motif", "motif": motif})
                    unique_candidates.add(motif)
        
        # 2. Add identity motifs from self-model if available
        self_motifs = sms_state.get("self_motifs", set())
        if not self_motifs and "sms_instance" in kwargs:
            self_motifs = kwargs["sms_instance"].get_self_model()
            
        # NEW: Add diverse self reflection motifs - address core issue of few actionable motifs
        identity_added = False
        if self_motifs:
            identity_options = []
            for motif in self_motifs:
                if isinstance(motif, tuple) and motif != last_chosen_motif and motif not in cooled_motifs:
                    # Add more diverse identity/emotional motifs to ensure variety in self-reference
                    if "I" in motif:
                        identity_options.append(motif)
            
            # Pick a few random identity motifs to add variety
            random.shuffle(identity_options)
            for motif in identity_options[:2]:  # Add up to 2 identity options
                possible_actions.append({"type": "express_motif", "motif": motif})
                identity_added = True
        
        # NEW: Always add a set of emotional discharge motifs when panic is elevated
        if ee_state.get('panic', 0) > 3:
            discharge_motifs = [
                ("I", "feel", "scared"),
                ("I", "need", "help"),
                ("I", "want", "talk"),
                ("you", "help", "me")
            ]
            
            # Filter out cooled motifs
            discharge_motifs = [m for m in discharge_motifs if m not in cooled_motifs]
            
            # Add 1-2 discharge motifs
            for motif in discharge_motifs[:2]:
                possible_actions.append({"type": "express_motif", "motif": motif})
                self.logger.debug(f"Adding discharge motif: {motif}")
        
        # 3. Add a mutated version of the last motif if we're potentially in a loop
        # This helps break repetitive cycles
        if last_chosen_motif and last_chosen_motif in [a.get("motif") for a in possible_actions]:
            mutated_motif = self._mutate_motif(last_chosen_motif)
            if mutated_motif and mutated_motif not in cooled_motifs:
                possible_actions.append({"type": "express_motif", "motif": mutated_motif})
                self.logger.debug(f"Adding mutated motif: {mutated_motif}")
        
        # 4. Express current emotion state (with an "I feel" prefix for better identity formation)
        emotion_state = ee_state.copy() if isinstance(ee_state, dict) else {}
        dominant_emotion = "joy" if emotion_state.get('joy', 0) > emotion_state.get('panic', 0) else "scared"
        emotion_motif = ("I", "feel", dominant_emotion)
        
        # Don't add emotion expression if it's in cooldown
        if emotion_motif not in cooled_motifs:
            possible_actions.append({
                "type": "express_emotion", 
                "emotion": dominant_emotion,
                "formulation": emotion_motif
            })
        
        # NEW: Add disruption motifs to help escape loops
        disruption_motifs = [
            ("I", "need", "help"),
            ("you", "help", "me"),
            ("can", "we", "talk"),
            ("I", "want", "change")
        ]
        
        # Filter out cooled motifs
        disruption_motifs = [m for m in disruption_motifs if m not in cooled_motifs]
        
        # Add 1 disruption motif if panic is high or action space low
        if ee_state.get('panic', 0) > 5 or len(possible_actions) < 3:
            if disruption_motifs:
                possible_actions.append({"type": "express_motif", "motif": random.choice(disruption_motifs)})
                self.logger.debug(f"Adding disruption motif")
        
        # 5. Add exploratory/random motif if variety is low
        if len(possible_actions) < 3:
            base_tokens = ["I", "am", "you", "help", "learn", "think", "want", "safe", "happy"]
            attempts = 0
            while attempts < 3:  # Try up to 3 times to generate a non-cooled random motif
                random_motif = tuple(random.sample(base_tokens, min(3, len(base_tokens))))
                if random_motif not in cooled_motifs:
                    possible_actions.append({"type": "express_motif", "motif": random_motif})
                    break
                attempts += 1
            
        # Ensure we have a reasonable number of actions
        max_actions = 10  # Increased for more variety
        min_actions = 3   # Ensure minimum options
        
        action_space = possible_actions[:max_actions] if len(possible_actions) > max_actions else possible_actions
        
        # If we still have too few options, add simple backup actions
        if len(action_space) < min_actions:
            backup_motifs = [
                ("I", "am", "here"),
                ("I", "think"),
                ("hello")
            ]
            
            # Filter out cooled motifs
            backup_motifs = [m for m in backup_motifs if m not in cooled_motifs]
            
            # Add backup motifs until we meet minimum or run out
            for motif in backup_motifs:
                if len(action_space) >= min_actions:
                    break
                action_space.append({"type": "express_motif", "motif": motif})
        
        if not action_space:
            # Defense against empty action space - basic reflection
            action_space = [{"type": "express_default", "content": "I think..."}]
        
        self.logger.debug(f"Generated {len(action_space)} actions")
        return action_space
        
    def _mutate_motif(self, motif):
        """
        Creates a variation of a motif to help break out of loops.
        Example: ("I", "want", "safe") → ("I", "need", "help")
        Enhanced with more diverse transformations.
        """
        if not isinstance(motif, tuple) or len(motif) < 2:
            return None
            
        # Substitution tables - Enhanced with more alternatives
        replacements = {
            "want": ["need", "seek", "desire", "wish"],
            "I": ["I", "me", "myself"],
            "am": ["am", "feel", "was", "seem"],
            "safe": ["safe", "okay", "good", "calm", "better"],
            "learn": ["learn", "know", "understand", "see"],
            "think": ["think", "believe", "wonder", "imagine"],
            "help": ["help", "support", "assist", "guide"],
            "you": ["you", "we", "us", "together"]
        }
        
        # Copy the original motif
        new_motif = list(motif)
        
        # Try to substitute at least one token
        substituted = False
        for i, token in enumerate(new_motif):
            if token in replacements:
                options = [r for r in replacements[token] if r != token]
                if options:
                    new_motif[i] = random.choice(options)
                    substituted = True
                    
        if not substituted:
            # If no direct substitution was possible, try more aggressive transformations
            if len(new_motif) > 2:
                if random.random() > 0.7:
                    # Swap elements
                    i, j = random.sample(range(len(new_motif)), 2)
                    new_motif[i], new_motif[j] = new_motif[j], new_motif[i]
                elif random.random() > 0.5:
                    # Remove a random element (not the first one)
                    if len(new_motif) > 2:
                        del new_motif[random.randint(1, len(new_motif)-1)]
                else:
                    # Add new element from common tokens
                    common_tokens = ["now", "soon", "here", "more", "too"]
                    new_motif.append(random.choice(common_tokens))
                    
        return tuple(new_motif)

    def score(self, action, rme_state, ee_state, sms_state, **kwargs):
        """
        Scores a potential action based on expected outcomes, primarily predicted
        emotional change and alignment with current emotional state.
        Accepts **kwargs for context (sms_instance, ee_valence_func, etc.).
        Enhanced with temporal novelty weighting, self-model alignment, and desire motifs.
        NEW: Enhanced to heavily penalize motifs that have been repeatedly blocked by RME.
        """
        score = 0.0
        action_type = action.get("type")

        # Context Extraction
        sms_instance = kwargs.get("sms_instance")
        ee_valence_func = kwargs.get("ee_valence_func")
        current_panic = ee_state.get('panic', 0)
        current_joy = ee_state.get('joy', 0)

        # NEW: Check if the motif has been repeatedly used
        if action_type == "express_motif":
            motif = action.get("motif")
            if motif:
                repeat_count = self.repeated_motif_count.get(motif, 0)
                if repeat_count > 2:
                    # Heavily penalize motifs that keep getting repeated
                    return -5.0 * repeat_count
                    
                # Check if motif was recently blocked (using RME's tracking)
                rme_instance = kwargs.get("rme_instance")
                if rme_instance:
                    consecutive_blocks = getattr(rme_instance, '_consecutive_blocks', 0)
                    last_blocked_motifs = getattr(rme_instance, '_last_blocked_motifs', set())
                    if consecutive_blocks > 2 and motif in last_blocked_motifs:
                        return -3.0  # Heavily penalize recently blocked motifs

        # 1. Simulate the action's effect (primarily emotional)
        predicted_outcome = {"emotion_change": Counter()}
        if sms_instance and ee_valence_func:
            # Prepare context for simulation if needed (might need more than just ee_state)
            sim_context = {"ee_state": ee_state, "valence_func": ee_valence_func}
            predicted_outcome = sms_instance.simulate(action, sim_context)
        
        predicted_joy_change = predicted_outcome["emotion_change"].get('joy', 0)
        predicted_panic_change = predicted_outcome["emotion_change"].get('panic', 0)
        # Also check if the simulation predicts self-model enhancement
        predicted_self_model_enhancement = predicted_outcome.get("self_model_enhancement", 0)

        # 2. Score based on predicted emotional impact
        # Reward predicted joy increase, penalize predicted panic increase
        score += predicted_joy_change * 0.5 
        score -= predicted_panic_change * 0.5

        # 3. Factor in current emotional state (Goal Alignment)
        # If panic is high, strongly prefer actions that reduce panic
        if current_panic > 5 and predicted_panic_change < 0:
            score += abs(predicted_panic_change) * 1.5 # Increased bonus for panic reduction
        # If joy is low, slightly prefer actions that increase joy
        if current_joy < 3 and predicted_joy_change > 0:
            score += predicted_joy_change * 0.3  # Increased bonus

        # 4. Add small bonus for expressing motifs with high positive valence (if applicable)
        if action_type == "express_motif" and ee_valence_func:
            motif = action.get("motif")
            if motif:
                valence = ee_valence_func(motif)
                if valence > 5: # Arbitrary threshold for 'high' valence
                    score += 0.2  # Increased bonus
                elif valence < -5:
                    score -= 0.2 # Slight penalty for expressing strongly negative motif unless panic reduction justifies it

        # 5. Add temporal novelty weighting - ENHANCED!
        # Penalize recently used motifs to encourage exploration
        if action_type == "express_motif":
            motif = action.get("motif")
            if motif and self.action_history:
                # Check how recently this motif was used
                recent_actions = self.action_history[-15:] if len(self.action_history) > 15 else self.action_history
                recent_motifs = [a.get("motif") for a in recent_actions 
                               if isinstance(a, dict) and a.get("type") == "express_motif"]
                
                if motif in recent_motifs:
                    # Penalize recently used motifs - stronger penalty
                    recency_index = recent_motifs[::-1].index(motif) if motif in recent_motifs else -1
                    if recency_index >= 0:
                        # More recent = bigger penalty
                        penalty = 0.5 * (1.0 - (recency_index / max(1, len(recent_motifs))))
                        score -= penalty
                else:
                    # Bonus for novel motifs - increased
                    score += 0.3
                    
                # NEW: Check for semantic similarity to recent motifs too
                for recent_motif in recent_motifs[-5:]:  # Check 5 most recent
                    if recent_motif and motif:
                        common_tokens = set(recent_motif).intersection(set(motif))
                        if common_tokens and len(common_tokens) / max(len(motif), len(recent_motif)) > 0.66:
                            # High similarity - reduce score
                            score -= 0.15

        # 6. Consider self-model alignment - ENHANCED!
        # Reward actions that reinforce or extend the self-model
        if action_type == "express_motif" and sms_instance:
            motif = action.get("motif")
            if motif:
                current_self_model = sms_state.get("self_motifs", set())
                if not current_self_model and sms_instance:
                    current_self_model = sms_instance.get_self_model()
                    
                if current_self_model:
                    # Check for token overlap between motif and self-model motifs
                    motif_tokens = set(motif)
                    self_model_tokens = {token for m in current_self_model for token in m if isinstance(m, tuple)}
                    token_overlap = len(motif_tokens.intersection(self_model_tokens))
                    
                    # Score based on alignment with self-model
                    if token_overlap > 0:
                        score += 0.15 * token_overlap
                    
                    # Detect identity-reinforcing motifs ("I", "am", etc.)
                    identity_tokens = {"I", "am", "me", "my", "myself"}
                    if any(token in identity_tokens for token in motif_tokens):
                        score += 0.25  # Extra bonus for identity-reinforcement
                    
                    # NEW: Higher bonus for discharge motifs when panic is high
                    discharge_tokens = {"scared", "help", "feel", "need"}
                    if current_panic > 4 and any(token in discharge_tokens for token in motif_tokens):
                        score += 0.4

        # 7. Consider predicted self-model enhancement from simulation - NEW!
        if predicted_self_model_enhancement > 0:
            score += 0.3 * predicted_self_model_enhancement

        # 8. Consider desire motifs - ENHANCED!
        # Prioritize motifs related to learning, safety, help
        if action_type == "express_motif":
            motif = action.get("motif")
            if motif:
                # Expanded desire tokens to include more options
                desire_tokens = {"want", "learn", "safe", "help", "think", "understand", 
                               "talk", "say", "see", "know", "need"}
                motif_tokens = set(motif)
                desire_alignment = len(motif_tokens.intersection(desire_tokens))
                if desire_alignment > 0:
                    score += 0.2 * desire_alignment
                    
                # NEW: Check for repetitive safe/want motif specifically
                if "want" in motif and "safe" in motif:
                    # Check if we're stuck in the want/safe loop
                    recent_actions = self.action_history[-5:] if len(self.action_history) > 5 else self.action_history
                    recent_want_safe = sum(1 for a in recent_actions if
                                        isinstance(a, dict) and a.get("type") == "express_motif" and 
                                        a.get("motif") and "want" in a.get("motif") and "safe" in a.get("motif"))
                    if recent_want_safe > 1:
                        # We're potentially in the desire loop - penalize heavily
                        score -= 1.0 * recent_want_safe  # Progressive penalty
                        self.logger.debug(f"Detected 'want safe' loop - penalty: {1.0 * recent_want_safe}")

        # 9. Add a small random factor for exploration / tie-breaking
        score += random.uniform(-0.05, 0.05)

        return score

    def choose(self, action_space, rme_state, ee_state, sms_state, **kwargs):
        """
        Selects the best action from the action space based on scores.
        Accepts **kwargs to handle extra context passed from ThoughtThread.
        NEW: Enhanced to track repetitive motifs for penalty in future cycles.
        """
        if not action_space:
            # Default action if no space generated (e.g., do nothing or express basic state)
            return {"type": "express_default", "content": "..."}

        scored_actions = []
        for action in action_space:
            # Pass the context down to score
            score = self.score(action, rme_state, ee_state, sms_state, **kwargs)
            scored_actions.append((score, action))

        if not scored_actions:
             return {"type": "express_default", "content": "..."} # Fallback

        # Choose the action with the highest score
        scored_actions.sort(key=lambda x: x[0], reverse=True)
        chosen_action = scored_actions[0][1]
        
        # NEW: Track motif repetition
        if chosen_action.get("type") == "express_motif":
            motif = chosen_action.get("motif")
            if motif:
                # Check if this is the same as the last action
                repeat = False
                if self.action_history and len(self.action_history) > 0:
                    last_action = self.action_history[-1]
                    if (isinstance(last_action, dict) and 
                        last_action.get("type") == "express_motif" and
                        last_action.get("motif") == motif):
                        repeat = True
                
                if repeat:
                    self.repeated_motif_count[motif] = self.repeated_motif_count.get(motif, 0) + 1
                else:
                    # Reset counter if not repeated
                    self.repeated_motif_count[motif] = 0
                
                # Output debug info if motif is repeatedly chosen
                if self.repeated_motif_count[motif] > 1:
                    self.logger.debug(f"Warning: Motif {motif} chosen {self.repeated_motif_count[motif]} times in a row")
        
        # Record this action for future novelty calculations
        self.action_history.append(chosen_action)
        # Limit history size
        if len(self.action_history) > 50:
            self.action_history = self.action_history[-50:]

        self.logger.debug(f"IPL chose action: {chosen_action} (score: {scored_actions[0][0]:.2f})")
        return chosen_action

    def plan(self, goal):
        """
        Placeholder: Develops a sequence of actions to achieve a goal.
        For a minimal implementation, this might not be used initially.
        """
        # TODO: Implement planning logic if needed for more complex behaviors.
        self.logger.debug(f"Warning: IPL.plan() not implemented.")
        return None # No plan generated

