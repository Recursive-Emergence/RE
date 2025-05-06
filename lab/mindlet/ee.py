import random
from collections import Counter, deque # Added deque

class EmotionEngine:
    """
    Manages the agent's emotional state, assigning valence and tracking homeostasis.
    """
    def __init__(self, initial_state=None):
        # Using Counter for easier state management
        self.state = Counter(initial_state or {'panic': 0, 'joy': 0})
        # Parameters for dynamics (can be tuned)
        self.balance_factor = 2.0 # How much imbalance triggers correction
        self.balance_correction_prob = 0.25
        self.decay_prob_panic = 0.2
        self.decay_prob_joy = 0.15
        self.max_level = 10 # Max level for each emotion
        self.decay_rate = 0.1 # Decay 10% towards 0 each cycle
        # Track motifs associated with recent strong emotional changes
        self.positive_associated_motifs = Counter() # motif -> positive association score
        self.negative_associated_motifs = Counter() # motif -> negative association score
        self.association_decay = 0.95 # Decay factor for associations over time
        self.motif_association_history = deque(maxlen=50) # Track (motif, valence_change) pairs

    def _decay_associations(self):
        # Periodically decay the association scores
        for motif in list(self.positive_associated_motifs.keys()):
            self.positive_associated_motifs[motif] *= self.association_decay
            if self.positive_associated_motifs[motif] < 0.1:
                del self.positive_associated_motifs[motif]
        for motif in list(self.negative_associated_motifs.keys()):
            self.negative_associated_motifs[motif] *= self.association_decay
            if self.negative_associated_motifs[motif] < 0.1:
                del self.negative_associated_motifs[motif]

    def _internal_dynamics(self):
        """
        Applies natural balancing and decay to emotions.
        Migrated from the original emotion_dynamics function.
        """
        new_changes = Counter()
        panic = self.state.get('panic', 0)
        joy = self.state.get('joy', 0)

        # Natural balancing
        if panic > joy * self.balance_factor and random.random() < self.balance_correction_prob:
            new_changes['panic'] -= 1
            new_changes['joy'] += 1
        elif joy > panic * self.balance_factor and random.random() < self.balance_correction_prob:
            new_changes['joy'] -= 1
            new_changes['panic'] += 1

        # Natural decay
        if panic > 0 and random.random() < self.decay_prob_panic:
            new_changes['panic'] -= 1
        if joy > 0 and random.random() < self.decay_prob_joy:
            new_changes['joy'] -= 1

        # Apply changes, ensuring counts don't go below zero
        self.state.update(new_changes)
        self.state = Counter({k: max(0, v) for k, v in self.state.items()})

        # Decay associations as part of internal dynamics
        self._decay_associations()


    def adjust(self, state_change_info):
        """
        Adjusts emotional state based on external events or internal signals.
        'state_change_info' could be input data, action results, entropy changes, etc.
        Also updates motif-emotion associations.
        Enhanced to handle source-tagged motifs differently and recognize desire motifs.
        """
        # 1. Apply decay first
        for emotion in list(self.state.keys()):
            decay_amount = int(self.state[emotion] * self.decay_rate)
            if decay_amount > 0:
                 self.state[emotion] -= decay_amount
            # Ensure emotion doesn't go below 0 due to decay
            if self.state[emotion] < 0: self.state[emotion] = 0

        # 2. Process event
        if state_change_info:
            event_type = state_change_info.get("type")
            # Get motifs involved, default to empty set if not provided
            associated_motifs = state_change_info.get("motifs", set()) 
            # Get source information (user/self/environment)
            source = state_change_info.get("source", "unknown")
            # Get valence modifier based on source (self-generated motifs get higher valence)
            valence_modifier = state_change_info.get("valence_modifier", 1.0)
            
            if event_type == "merge_success":
                joy_boost = state_change_info.get("joy_boost", 1)
                # Apply source-based valence modification
                joy_boost = int(joy_boost * valence_modifier)
                
                self.state['joy'] += joy_boost
                self.state['panic'] -= joy_boost // 2 # Reduce panic on success
                
                # Strengthen positive associations for involved motifs
                for motif in associated_motifs:
                    if isinstance(motif, tuple):
                        self.positive_associated_motifs[motif] += joy_boost
                        self.motif_association_history.append((motif, joy_boost)) # Track positive change
                        # Weaken negative association if it existed
                        if motif in self.negative_associated_motifs:
                            self.negative_associated_motifs[motif] *= 0.5
                
                # NEW: Special handling for identity and desire motifs
                for motif in associated_motifs:
                    if isinstance(motif, tuple):
                        # Check if this is an identity motif ("I am", "I think")
                        if len(motif) > 1 and motif[0] == "I":
                            # Identity motifs get stronger joy boost
                            self.state['joy'] += 1
                            # Add double strength to positive association
                            self.positive_associated_motifs[motif] += 1
                        
                        # Check if this is a desire motif ("want", "learn", "safe")
                        if "want" in motif or "learn" in motif or "safe" in motif:
                            # Desire motifs get stronger joy boost when successfully merged
                            self.state['joy'] += 1
                            # Desire fulfillment reduces panic
                            self.state['panic'] = max(0, self.state['panic'] - 1)

            elif event_type == "merge_fail":
                panic_boost = state_change_info.get("panic_boost", 1)
                # Apply source-based modification (self-failures might be more impactful)
                if source == "self":
                    panic_boost += 1  # Higher panic when self-generated content fails to merge
                
                self.state['panic'] += panic_boost // 2 + 1 # Less sensitive panic increase
                self.state['joy'] -= panic_boost // 3 # Reduce joy slightly on failure
                
                # Strengthen negative associations for involved motifs
                for motif in associated_motifs:
                     if isinstance(motif, tuple):
                        self.negative_associated_motifs[motif] += panic_boost
                        self.motif_association_history.append((motif, -panic_boost)) # Track negative change
                        # Weaken positive association if it existed
                        if motif in self.positive_associated_motifs:
                            self.positive_associated_motifs[motif] *= 0.5

            elif state_change_info.get("type") == "input_keyword":
                 # Example: Adjust based on keywords in input
                 keywords = state_change_info.get("keywords", set())
                 if "help" in keywords or "pain" in keywords:
                     self.state['panic'] += 1
                 if "good" in keywords or "happy" in keywords:
                     self.state['joy'] += 1
                     
            elif state_change_info.get("type") == "perceive":
                # NEW: Handle perception events directly
                # This allows emotional response to perceived input based on source
                source = state_change_info.get("source", "user")
                valence_modifier = state_change_info.get("valence_modifier", 1.0)
                
                # Self-perception can trigger different emotional responses
                if source == "self":
                    # Self-generated content that gets re-perceived can generate small joy
                    # This creates a positive feedback loop for self-expression
                    self.state['joy'] += 1
                    
                # Special token detection for emotional response
                motifs = state_change_info.get("motifs", set())
                for motif in motifs:
                    if isinstance(motif, tuple):
                        # Joy triggers
                        if any(token in ["good", "happy", "joy", "safe", "help"] for token in motif):
                            self.state['joy'] += 1 * valence_modifier
                        # Panic triggers    
                        if any(token in ["bad", "sad", "panic", "fear", "scary"] for token in motif):
                            self.state['panic'] += 1 * valence_modifier

        # 3. Clamp values
        for emotion in self.state:
            if self.state[emotion] > self.max_level:
                self.state[emotion] = self.max_level
            elif self.state[emotion] < 0:
                self.state[emotion] = 0

        # Apply internal dynamics after adjustments
        self._internal_dynamics()
        
    def valence(self, motif):
        """
        Assigns an emotional valence score to a motif based on past associations.
        Positive score = positive association, Negative score = negative association.
        Enhanced with special case handling for identity and desire motifs.
        """
        if not isinstance(motif, tuple):
            return 0 # Only score tuple motifs

        pos_score = self.positive_associated_motifs.get(motif, 0)
        neg_score = self.negative_associated_motifs.get(motif, 0)
        
        # Base valence: difference between positive and negative associations
        valence = pos_score - neg_score
        
        # NEW: Special case handling
        # Identity motifs get an inherent positive bias
        if len(motif) > 1 and motif[0] == "I":
            valence += 1
            
        # Desire motifs get a small positive bias
        desire_tokens = {"want", "learn", "safe", "help", "think"}
        if any(token in desire_tokens for token in motif):
            valence += 0.5
            
        # Motifs with high emotional words get direct valence
        if any(token in ["good", "happy", "joy"] for token in motif):
            valence += 1
        if any(token in ["bad", "sad", "panic", "fear"] for token in motif):
            valence -= 1
            
        return valence

    def homeostasis_check(self):
        """
        Checks if the emotional state is significantly out of balance.
        Returns a signal that might influence IPL or other modules.
        """
        panic = self.state.get('panic', 0)
        joy = self.state.get('joy', 0)
        if panic > joy * (self.balance_factor + 1): # More extreme imbalance
            return "high_panic"
        if joy > panic * (self.balance_factor + 1):
            return "high_joy"
        return "balanced"

    def get_state(self):
        """Returns the current emotional state."""
        return self.state

    def get_emotional_threshold_modifier(self):
        """
        Provides a value based on emotion state to modify thresholds (e.g., for RME merge).
        Simplified version of the original emotional_threshold.
        """
        # Example: Higher joy makes agent more open (lower threshold), higher panic more closed (higher threshold)
        panic = self.state.get('panic', 0)
        joy = self.state.get('joy', 0)
        # Base threshold modifier (e.g., 0) + bonus for joy - penalty for panic
        modifier = (joy * 0.05) - (panic * 0.05)
        return modifier # This value can be added to a base threshold in RME

    def get_emotion_face(self):
        """
        Generates a facial expression based on the current emotional state.
        Migrated from REmindlet.py.
        """
        panic = self.state.get('panic', 0)
        joy = self.state.get('joy', 0)
        total = panic + joy
        if total == 0: return '😐'

        if panic > joy * 3: return '😱'
        elif panic > joy * 1.5: return '😖'
        elif joy > panic * 3: return '😄'
        elif joy > panic * 1.5: return '🙂' # Using consistent happy face
        elif panic > joy: return '😕'
        elif joy > panic: return '🙂' # Using consistent happy face
        else: return '😐'

