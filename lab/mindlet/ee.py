# filepath: /media/im2/plus/lab4/ACI/lab/mindlet/ee.py
import random
from collections import Counter

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


    def adjust(self, state_change_info):
        """
        Adjusts emotional state based on external events or internal signals.
        'state_change_info' could be input data, action results, entropy changes, etc.
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
            if event_type == "merge_success":
                # Increase joy, decrease panic
                joy_boost = state_change_info.get("joy_boost", 1)
                self.state['joy'] += joy_boost
                self.state['panic'] -= joy_boost // 2 # Reduce panic on success
            elif event_type == "merge_fail":
                # Increase panic slightly, decrease joy slightly
                # Reduced panic boost compared to before
                panic_boost = state_change_info.get("panic_boost", 1) 
                self.state['panic'] += panic_boost // 2 + 1 # Less sensitive panic increase
                self.state['joy'] -= panic_boost // 3 # Reduce joy slightly on failure
            elif state_change_info.get("type") == "input_keyword":
                 # Example: Adjust based on keywords in input
                 keywords = state_change_info.get("keywords", set())
                 if "help" in keywords or "pain" in keywords:
                     self.state['panic'] += 1
                 if "good" in keywords or "happy" in keywords:
                     self.state['joy'] += 1

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
        Placeholder: Assigns an emotional valence (e.g., joy/panic modifier) to a motif.
        This could be based on past associations.
        """
        # TODO: Implement valence assignment based on learned associations.
        # Could check against recently_positive/negative motifs stored here or passed in.
        return 0 # Neutral valence for now

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

