"""
Reflective Core Module
Handles self-reflection, emotional processing, and theory formation
"""
import copy
from datetime import datetime

from event_bus import global_event_bus, EventTypes

class Me:
    def __init__(self, memory, event_bus=None):
        self.memory = memory
        self.introspection_log = []
        self.self_model = {
            'ideal_avg_novelty': 0.2,
            'ideal_reuse_balance': 0.1,
            'adaptiveness': 0.05
        }
        self.personal_theories = []
        # New in MVP 1.4: Emotional state
        self.emotional_state = {
            'curiosity': 0.5,      # Drives exploration of novel concepts
            'frustration': 0.0,    # Rises with stagnation/repetition  
            'satisfaction': 0.3,   # Rises with successful theory formation
            'uncertainty': 0.7     # Modulates mutation aggressiveness
        }
        self.emotion_history = []  # Track emotional trajectory
        # Store recent prompts to better detect repetition patterns
        self.recent_prompts = []
        self.last_mutation_cycle = 0  # Track when we last mutated to prevent too-frequent mutations
        
        # Store reference to event bus (or use global)
        self.event_bus = event_bus or global_event_bus

    def reflect(self):
        """Reflect on current state and make decisions"""
        self.memory.update_scores()
        high_value = [e for e in self.memory.entries if e['reuse_score'] > 0.2]
        avg_novelty = sum(e['novelty'] for e in self.memory.entries[-3:]) / 3 if len(self.memory.entries) >= 3 else 0
        novelty_gradient, reuse_gradient = self.memory.compute_gradients()

        # Get previous emotional state for comparison
        prev_emotional_state = copy.deepcopy(self.emotional_state) if self.emotion_history else None

        # Update emotional state before making decision
        self.update_emotions()

        # New in MVP 1.5: Detect significant emotional changes
        if prev_emotional_state:
            for emotion, value in self.emotional_state.items():
                prev_value = prev_emotional_state.get(emotion, 0.5)
                # Check for significant changes (>25%)
                if abs(value - prev_value) > 0.25:
                    self.event_bus.publish(EventTypes.EMOTIONAL_CHANGE, {
                        'emotion': emotion,
                        'previous': prev_value,
                        'current': value,
                        'delta': value - prev_value,
                        'cycle': len(self.memory.entries)
                    })
                
                # Check for threshold crossings
                if emotion == 'frustration' and value > 0.8 and prev_value <= 0.8:
                    self.event_bus.publish(EventTypes.FRUSTRATION_THRESHOLD, {
                        'value': value,
                        'cycle': len(self.memory.entries)
                    })
                    
                if emotion == 'curiosity' and value > 0.8 and prev_value <= 0.8:
                    self.event_bus.publish(EventTypes.CURIOSITY_THRESHOLD, {
                        'value': value,
                        'cycle': len(self.memory.entries)
                    })

        decision = {
            'cycle': len(self.memory.entries),
            'keep': len(high_value),
            'discarded': len(self.memory.entries) - len(high_value),
            'avg_novelty': round(avg_novelty, 3),
            'novelty_gradient': novelty_gradient,
            'reuse_gradient': reuse_gradient,
            'symbols_learned': self.memory.symbols,
            'symbol_links': self.memory.symbol_links,
            'personal_theories': self.personal_theories,
            'note': 'compressed' if len(high_value) < len(self.memory.entries) else 'stable',
            'emotional_state': copy.deepcopy(self.emotional_state)
        }

        if len(self.introspection_log) >= 5:
            last_cycles = self.introspection_log[-5:]
            if all(d['avg_novelty'] == 0.0 for d in last_cycles):
                decision['signal'] = 'stagnation_detected'
                
                # New in MVP 1.5: Emit threshold crossed event
                self.event_bus.publish(EventTypes.THRESHOLD_CROSSED, {
                    'type': 'stagnation',
                    'description': 'Zero novelty detected across multiple cycles',
                    'cycle': len(self.memory.entries),
                    'severity': 'high'
                })

        # Detect theory-like sentences
        for entry in self.memory.get_recent(2):
            theory_indicators = ['law', 'principle', 'rule', 'truth', 'theory', 'hypothesis']
            if any(word in entry['response'].lower() for word in theory_indicators):
                self.personal_theories.append(entry['response'])
                
                # New in MVP 1.5: Emit theory formed event
                self.event_bus.publish(EventTypes.THEORY_FORMED, {
                    'theory': entry['response'],
                    'cycle': len(self.memory.entries),
                    'source_entry_id': entry.get('id')
                })

        # Self-adjust if far from ideal model
        if abs(avg_novelty - self.self_model['ideal_avg_novelty']) > self.self_model['adaptiveness']:
            decision['self_adjust'] = 'encourage_mutation' if avg_novelty < self.self_model['ideal_avg_novelty'] else 'encourage_compression'

        self.introspection_log.append(decision)
        return decision
    
    def update_emotions(self):
        """Update emotional states based on recent memory and reflection"""
        # Get metrics
        novelty_gradient, reuse_gradient = self.memory.compute_gradients()
        recent_entries = self.memory.get_recent(5)
        theory_count = len([t for t in self.personal_theories if recent_entries and t not in [e['response'] for e in recent_entries]])
        
        # Check for repetition and increase frustration if detected
        repetition_detected = self.memory.detect_repetition()
        if repetition_detected:
            self.emotional_state['frustration'] = min(1.0, self.emotional_state['frustration'] + 0.35)  # Stronger frustration rise
            self.emotional_state['satisfaction'] = max(0.0, self.emotional_state['satisfaction'] - 0.3)  # Stronger satisfaction drop
            self.emotional_state['curiosity'] = min(1.0, self.emotional_state['curiosity'] + 0.2)  # Frustration should spark curiosity
        else:
            # Only reduce frustration if we're not in a repetition state
            self.emotional_state['frustration'] = max(0.0, self.emotional_state['frustration'] - 0.15)
        
        # Update emotional states
        self.emotional_state['curiosity'] = min(1.0, max(0.1, # Never let curiosity drop below 0.1
            self.emotional_state['curiosity'] + (0.15 * novelty_gradient) - 
            (0.05 * len(self.memory.symbols) / max(1, 20)) +
            (0.1 if len(self.memory.concept_network.get_most_connected_concepts(3)) > 0 else 0)  # Boost curiosity based on network richness
        ))
        
        # Make satisfaction more dynamic - it should rise and fall more dramatically
        self.emotional_state['satisfaction'] = min(0.85, max(0.1,  # Range between 0.1 and 0.85
            self.emotional_state['satisfaction'] + 
            (0.2 if theory_count > len(self.personal_theories) - 3 else -0.1) +
            (0.15 * novelty_gradient) - 
            (0.2 if repetition_detected else 0)
        ))
        
        self.emotional_state['uncertainty'] = min(1.0, max(0.2, 
            0.5 + (0.3 * novelty_gradient) - (0.2 * reuse_gradient) +
            (0.3 if repetition_detected else 0)  # Increase uncertainty when stuck
        ))
        
        # Track cycles since last strong emotional change
        current_cycle = len(self.introspection_log)
        if len(self.emotion_history) > 5:
            # If emotions have been static for too long, introduce a random perturbation
            last_5_emotions = self.emotion_history[-5:]
            avg_emotion_change = sum(abs(e1['state']['curiosity'] - e2['state']['curiosity']) + 
                                   abs(e1['state']['frustration'] - e2['state']['frustration']) + 
                                   abs(e1['state']['satisfaction'] - e2['state']['satisfaction'])
                                   for e1, e2 in zip(last_5_emotions[:-1], last_5_emotions[1:])) / 4
            
            # If average change is very small, emotions are stagnant
            if avg_emotion_change < 0.05:
                # Introduce a significant random perturbation
                import random
                emotion_boost = random.choice(['curiosity', 'frustration', 'uncertainty'])
                self.emotional_state[emotion_boost] = min(1.0, self.emotional_state[emotion_boost] + 0.4)
                print(f"🔄 Emotions stagnant - boosting {emotion_boost} to break pattern")
        
        # Save emotional snapshot
        self.emotion_history.append({
            'timestamp': datetime.now().isoformat(),
            'state': copy.deepcopy(self.emotional_state),
            'cycle': current_cycle
        })
        
        return self.emotional_state