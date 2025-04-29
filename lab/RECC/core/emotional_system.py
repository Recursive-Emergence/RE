import time
import math
import random

class EmotionalSystem:
    """
    Enhanced emotional system that manages the mind's emotional state
    with momentum, emotional blending, and self-regulation.
    
    Emotions serve as internal signals that guide behavior and reflection,
    forming a critical component of the recursive emergence process.
    """
    
    def __init__(self):
        # Primary emotional dimensions
        self.current_state = {
            'curiosity': 0.5,    # Desire to explore and learn
            'satisfaction': 0.3, # Contentment with current state
            'fear': 0.2,         # Aversion to potential harm
            'pain': 0.1          # Response to harmful conditions
        }
        
        # Emotional momentum (directional trends)
        self.momentum = {
            'curiosity': 0.0,
            'satisfaction': 0.0,
            'fear': 0.0,
            'pain': 0.0
        }
        
        # Blended emotional states (emerge from primary emotions)
        self.blended_states = {
            # No blended emotions initially
        }
        
        # Emotional regulation capabilities (develop over time)
        self.regulation = {
            'recovery_rate': 0.1,      # How quickly emotions return to baseline
            'stability': 0.2,          # Resistance to rapid fluctuations
            'self_awareness': 0.0,     # Understanding of own emotional state
            'baseline': {              # The system's natural resting state
                'curiosity': 0.5,
                'satisfaction': 0.3,
                'fear': 0.2,
                'pain': 0.1
            }
        }
        
        # Track emotional history
        self.history = []
        self.last_update = time.time()
        self.previous_entropy = 0.5 # Initialize previous entropy for change calculation
    
    # Change signature: remove energy_system, add entropy_value
    def update(self, entropy_value, memory_system):
        """
        Update emotional state based on current entropy, memories, and internal dynamics
        
        Args:
            entropy_value: The current system entropy value.
            memory_system: Reference to memory system
        """
        now = time.time()
        elapsed = now - self.last_update
        self.last_update = now
        
        # Store current state in history
        self.history.append({
            'timestamp': now,
            'state': self.current_state.copy(),
            'momentum': self.momentum.copy(),
            'blended_states': self.blended_states.copy()
        })
        
        # Trim history if needed
        if len(self.history) > 100:
            self.history = self.history[-100:]
        
        # 1. Apply momentum with temporal decay
        self._apply_momentum(elapsed)
        
        # 2. Apply ENTROPY effects (replaces energy effects)
        self._apply_entropy_effects(entropy_value)
        
        # 3. Apply memory effects
        recent_experiences = memory_system.get_recent_experiences(5)
        self._apply_memory_effects(recent_experiences)
        
        # 4. Apply self-regulation
        self._apply_self_regulation(elapsed)
        
        # 5. Update blended emotional states
        self._update_blended_states()

        # Store current entropy for next cycle's change calculation
        self.previous_entropy = entropy_value
    
    def _apply_momentum(self, elapsed):
        """
        Apply existing emotional momentum with temporal decay
        
        Args:
            elapsed: Time in seconds since last update
        """
        # Scale elapsed time to make updates smoother
        time_factor = min(1.0, elapsed / 5.0)
        
        # Apply momentum to each emotion
        for emotion in self.current_state:
            # Apply current momentum
            delta = self.momentum[emotion] * time_factor
            self.current_state[emotion] += delta
            
            # Decay momentum over time
            decay_rate = 0.1 * time_factor
            self.momentum[emotion] *= (1.0 - decay_rate)
            
            # Ensure emotion stays in valid range
            self.current_state[emotion] = max(0.0, min(1.0, self.current_state[emotion]))
    
    # Replace _apply_energy_effects with _apply_entropy_effects
    def _apply_entropy_effects(self, entropy_value):
        """
        Update emotions based on entropy level and its change.
        
        Args:
            entropy_value: Current entropy level (0.0+)
        """
        entropy_change = entropy_value - self.previous_entropy
        
        # Trigger emotions based on entropy state and change
        if entropy_change > 0.1: # Sharp rise -> Fear
            self.momentum['fear'] = min(1.0, self.momentum.get('fear', 0.0) + 0.2 * (entropy_change * 5)) # Scale effect by change magnitude
            self.momentum['curiosity'] *= 0.8 # Dampen curiosity during sharp fear increase
        elif entropy_value > 0.7 and entropy_change > 0.01: # Mild growth in high entropy -> Curiosity
            self.momentum['curiosity'] = min(1.0, self.momentum.get('curiosity', 0.0) + 0.1 * (entropy_change * 10))
        elif entropy_change < -0.05: # Significant drop -> Satisfaction
            self.momentum['satisfaction'] = min(1.0, self.momentum.get('satisfaction', 0.0) + 0.15 * abs(entropy_change * 3))
            self.momentum['fear'] *= 0.7 # Reduce fear when entropy drops
            self.momentum['pain'] *= 0.8 # Reduce pain when entropy drops
        elif entropy_value > 0.85: # Prolonged high entropy -> Pain
            # Increase pain slowly if entropy remains high
            self.momentum['pain'] = min(1.0, self.momentum.get('pain', 0.0) + 0.05 * (entropy_value - 0.85))
            self.momentum['satisfaction'] *= 0.9 # Dampen satisfaction in high pain state

        # General effect: High entropy tends to increase fear/pain, low entropy satisfaction
        self.momentum['fear'] += (entropy_value - 0.5) * 0.01 # Small push towards fear if entropy > 0.5
        self.momentum['pain'] += (entropy_value - 0.6) * 0.01 # Small push towards pain if entropy > 0.6
        self.momentum['satisfaction'] += (0.6 - entropy_value) * 0.01 # Small push towards satisfaction if entropy < 0.6
    
    def _apply_memory_effects(self, recent_experiences):
        """
        Update emotions based on recent experiences
        
        Args:
            recent_experiences: List of recent experiences
        """
        if not recent_experiences:
            return
        
        # Calculate emotional impact from recent experiences
        for exp in recent_experiences:
            # Extract emotional tags
            tags = exp.get('tags', [])
            emotional_tags = [t for t in tags if t in ['curious', 'satisfying', 'fearful', 'painful']]
            
            # Apply small momentum changes based on tags
            for tag in emotional_tags:
                if tag == 'curious':
                    self.momentum['curiosity'] += 0.05
                elif tag == 'satisfying':
                    self.momentum['satisfaction'] += 0.05
                elif tag == 'fearful':
                    self.momentum['fear'] += 0.05
                elif tag == 'painful':
                    self.momentum['pain'] += 0.05
            
            # Apply energy delta effects on emotions
            energy_delta = exp.get('energy_delta', 0)
            if energy_delta < -0.5:
                # Large energy loss increases pain
                self.momentum['pain'] += 0.03
                self.momentum['satisfaction'] -= 0.02
                
            elif energy_delta > 0.5:
                # Energy gain increases satisfaction
                self.momentum['satisfaction'] += 0.03
                self.momentum['pain'] -= 0.01
    
    def _apply_self_regulation(self, elapsed):
        """
        Apply emotional self-regulation based on regulation capabilities
        
        Args:
            elapsed: Time in seconds since last update
        """
        # Scale elapsed time to make updates smoother
        time_factor = min(1.0, elapsed / 10.0)
        recovery_rate = self.regulation['recovery_rate']
        stability = self.regulation['stability']
        
        # Apply recovery toward baseline (stronger for emotions far from baseline)
        for emotion, value in self.current_state.items():
            baseline = self.regulation['baseline'][emotion]
            distance = abs(value - baseline)
            
            # Direction of recovery
            direction = -1 if value > baseline else 1
            
            # Recovery strength increases with distance from baseline
            recovery_strength = direction * distance * recovery_rate * time_factor
            
            # Apply recovery, modulated by stability
            self.momentum[emotion] += recovery_strength * stability
    
    def _update_blended_states(self):
        """
        Update complex blended emotional states based on primary emotions
        """
        # Clear existing blended states
        self.blended_states = {}
        
        # Calculate hope (curiosity + satisfaction, low fear)
        if self.current_state['curiosity'] > 0.5 and self.current_state['satisfaction'] > 0.4 and self.current_state['fear'] < 0.3:
            hope_strength = (self.current_state['curiosity'] + self.current_state['satisfaction']) / 2
            self.blended_states['hope'] = hope_strength * 0.8  # Discounting factor
        
        # Calculate anxiety (fear + curiosity, low satisfaction)
        if self.current_state['fear'] > 0.4 and self.current_state['curiosity'] > 0.4 and self.current_state['satisfaction'] < 0.3:
            anxiety_strength = (self.current_state['fear'] + self.current_state['curiosity']) / 2
            self.blended_states['anxiety'] = anxiety_strength * 0.8
        
        # Calculate contentment (high satisfaction, low fear and pain)
        if self.current_state['satisfaction'] > 0.6 and self.current_state['fear'] < 0.3 and self.current_state['pain'] < 0.2:
            self.blended_states['contentment'] = self.current_state['satisfaction'] * 0.9
        
        # Calculate frustration (pain + curiosity, moderate satisfaction)
        if self.current_state['pain'] > 0.4 and self.current_state['curiosity'] > 0.3 and self.current_state['satisfaction'] < 0.6:
            frustration_strength = (self.current_state['pain'] + self.current_state['curiosity']) / 2
            self.blended_states['frustration'] = frustration_strength * 0.8
    
        # Calculate intrigue (high curiosity, low pain, moderate fear)
        if self.current_state['curiosity'] > 0.7 and self.current_state['pain'] < 0.3 and self.current_state['fear'] < 0.5:
            self.blended_states['intrigue'] = self.current_state['curiosity'] * 0.9
    
    def modify_emotion(self, emotion, delta):
        """
        Directly modify an emotional state with momentum impact
        
        Args:
            emotion: Name of emotion to modify
            delta: Amount to change emotion by
        """
        if emotion in self.current_state:
            # Add to momentum rather than directly changing state
            self.momentum[emotion] += delta
    
    def get_dominant_emotion(self):
        """
        Get the currently dominant emotion
        
        Returns:
            tuple: (emotion_name, strength)
        """
        # Check primary emotions first
        primary_dominant = max(self.current_state.items(), key=lambda x: x[1])
        
        # Then check blended emotions
        if self.blended_states:
            blended_dominant = max(self.blended_states.items(), key=lambda x: x[1])
            
            # Return whichever is stronger
            if blended_dominant[1] > primary_dominant[1]:
                return blended_dominant
        
        return primary_dominant
    
    def get_blended_states(self):
        """
        Get current blended emotional states
        
        Returns:
            dict: Blended emotional states
        """
        return self.blended_states.copy()
    
    def improve_regulation(self, amount=0.01):
        """
        Improve emotional regulation abilities
        
        Args:
            amount: Amount to improve by
        """
        # Improve recovery rate (with diminishing returns)
        current = self.regulation['recovery_rate']
        self.regulation['recovery_rate'] = min(0.5, current + amount)
        
        # Improve stability (with diminishing returns)
        current = self.regulation['stability']
        self.regulation['stability'] = min(0.8, current + amount * 0.5)
        
        # Improve self-awareness (with diminishing returns)
        current = self.regulation['self_awareness']
        self.regulation['self_awareness'] = min(1.0, current + amount * 0.8)
    
    def get_regulation_metrics(self):
        """
        Get emotional regulation metrics
        
        Returns:
            dict: Regulation metrics
        """
        return self.regulation.copy()
    
    def get_emotional_variance(self, time_window=5):
        """
        Calculate emotional variance over recent history
        
        Args:
            time_window: Number of history entries to analyze
            
        Returns:
            float: Average emotional variance
        """
        if len(self.history) < 2:
            return 0.0
            
        # Get recent history
        recent = self.history[-min(time_window, len(self.history)):]
        
        # Calculate variance for each emotion
        variances = {}
        for emotion in self.current_state:
            values = [h['state'][emotion] for h in recent]
            mean = sum(values) / len(values)
            variance = sum((x - mean) ** 2 for x in values) / len(values)
            variances[emotion] = variance
            
        # Return average variance
        return sum(variances.values()) / len(variances)
    
    # Add calculate_equilibrium_deviation method
    def calculate_equilibrium_deviation(self):
        """Calculates the deviation from an emotional equilibrium state."""
        # Equilibrium defined in self.regulation['baseline']
        equilibrium = self.regulation['baseline']
        emotion_values = self.current_state

        if not emotion_values:
            return 0.0

        deviations = []
        for emotion, value in emotion_values.items():
            if emotion in equilibrium:
                deviations.append(abs(value - equilibrium[emotion]))

        if not deviations:
            return 0.0

        # Calculate mean absolute deviation
        mean_deviation = sum(deviations) / len(deviations)
        
        # Normalize: Max possible mean deviation depends on range (0-1) and baseline.
        # If baseline is 0.5, max deviation per emotion is 0.5. Max mean deviation is 0.5.
        # If baseline varies, this needs adjustment. Assuming baseline values are reasonable (not 0 or 1).
        # For simplicity, normalize assuming max mean deviation is roughly 0.5.
        normalized_deviation = mean_deviation / 0.5 
        
        return max(0.0, min(1.0, normalized_deviation)) # Clamp between 0 and 1