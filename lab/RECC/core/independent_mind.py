import time
import sys
import os
import random

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Replace EnergySystem with EntropySystem
from core.entropy_system import EntropySystem
from core.emotional_system import EmotionalSystem 
from core.memory_system import MemorySystem
# Fix import to use the correct module name
from core.self_reference_system import SelfReferenceSystem
from core.reflection_engine import ReflectionEngine
from core.behavior_system import BehaviorSystem

class IndependentMind:
    """
    The core autonomous mind that develops primarily through
    self-reference and internal reflection.
    
    External interactions are optional, not required for development.
    """
    
    def __init__(self):
        # Core identity components
        # Replace EnergySystem with EntropySystem
        self.entropy = EntropySystem() 
        self.emotions = EmotionalSystem()
        self.memory = MemorySystem()
        self.self_reference = SelfReferenceSystem()
        self.behaviors = BehaviorSystem()
        self.reflection = ReflectionEngine()
        
        # Internal state management - remove energy cycle phase
        self.internal_state = {
            'idle_thinking': False,      # Internal exploration active
            'deep_reflection': False,    # Deep reflection in progress
            # 'energy_cycle_phase': 0,   # Removed
            'current_entropy': 0.0,      # Added entropy tracking
            'self_reference_depth': 0,   # Current recursive depth
            'cognitive_complexity': 0.0, # Measured complexity of internal structures
            'birth_time': time.time()    # When the system was initialized
        }
        
        self.cycle_counter = 0
    
    def autonomous_cycle(self, external_input=None):
        """
        Run a single mind cycle that prioritizes internal development.
        External input is optional and secondary to internal processes.
        
        Args:
            external_input: Optional input from environment
            
        Returns:
            dict: Results of the cycle including state changes
        """
        # Increment cycle counter
        self.cycle_counter += 1
        
        # Track starting state - remove start_energy
        cycle_results = {
            # 'start_energy': self.energy.current_level, # Removed
            'start_entropy': self.internal_state['current_entropy'], # Added
            'start_time': time.time(),
            'emotions_before': self.emotions.current_state.copy(), # Use copy
            'had_input': external_input is not None,
            'reflection_occurred': False,
            'cycle_number': self.cycle_counter
        }
        
        # Compute entropy FIRST
        current_entropy = self.entropy.compute_entropy(self.memory, self.emotions)
        self.internal_state['current_entropy'] = current_entropy
        cycle_results['computed_entropy'] = current_entropy
        
        # Update emotional state based on ENTROPY
        # Signature needs to change in EmotionalSystem class!
        self.emotions.update(current_entropy, self.memory) 
        
        # Enhanced self-reference processing
        self_ref_result = self.self_reference.process_cycle(
            self.memory, 
            self.emotions,
            self.internal_state
        )
        
        cycle_results['self_reference_events'] = self_ref_result.get('events', [])
        self.internal_state['self_reference_depth'] = self_ref_result.get('current_depth', 0)
        
        # Choose behavior based on internal state (and potentially entropy/emotions)
        if external_input and self.should_engage_externally():
            # Process external input if available and appropriate
            behavior = self.behaviors.select_external(self.emotions, self.internal_state)
            result = behavior.execute(external_input)
            cycle_results['behavior_type'] = 'external'
            cycle_results['selected_behavior'] = behavior.name
        else:
            # Default to internal behavior
            behavior = self.behaviors.select_internal(self.emotions, self.internal_state)
            result = behavior.execute()
            cycle_results['behavior_type'] = 'internal'
            cycle_results['selected_behavior'] = behavior.name
        
        # Process and store the experience - remove energy_delta
        exp_id = self.memory.process_and_store(
            result.get('input', ''), 
            result.get('output', ''), 
            self.emotions.current_state.copy(), # Use copy
            # result.get('energy_delta', 0), # Removed energy delta
            entropy_at_experience=current_entropy, # Added entropy context
            is_internal=(external_input is None)
        )
        
        cycle_results['experience_id'] = exp_id
        cycle_results['behavior_result'] = result
        
        # Perform deep reflection periodically
        if self.should_deep_reflect():
            self.internal_state['deep_reflection'] = True
            reflection_results = self.reflection.deep_analysis(
                self.memory,
                self.self_reference,
                self.emotions
            )
            # Store insights from reflection
            for insight in reflection_results.get('insights', []):
                self.memory.store_reflection_insight(insight)
                
            cycle_results['reflection_occurred'] = True
            cycle_results['reflection_results'] = reflection_results
            self.internal_state['deep_reflection'] = False
        
        # Calculate cognitive complexity periodically
        if self.cycle_counter % 10 == 0:
            metrics = self._calculate_cognitive_metrics()
            self.internal_state['cognitive_complexity'] = metrics['memory_complexity']
            cycle_results['cognitive_metrics'] = metrics
        
        # Complete cycle results - remove end_energy
        # cycle_results['end_energy'] = self.energy.current_level # Removed
        cycle_results['end_entropy'] = self.internal_state['current_entropy'] # Added
        cycle_results['emotions_after'] = self.emotions.current_state.copy() # Use copy
        cycle_results['end_time'] = time.time()
        cycle_results['duration'] = cycle_results['end_time'] - cycle_results['start_time']
        
        return cycle_results
    
    def should_engage_externally(self):
        """Determine if the system should engage with external input"""
        # Only engage externally if:
        # 1. Not in deep reflection
        # 2. Random probability based on curiosity level
        # Removed energy check
        if self.internal_state['deep_reflection']:
            return False
            
        # if self.energy.current_level < self.energy.EXTERNAL_INTERACTION_THRESHOLD: # Removed
        #     return False
            
        # Probabilistic engagement based on curiosity
        engage_probability = self.emotions.current_state.get('curiosity', 0) * 0.5 
        # Maybe add entropy condition? e.g., engage more if entropy is high?
        # engage_probability *= (1 + self.internal_state['current_entropy']) # Example
        return random.random() < engage_probability
    
    def should_deep_reflect(self):
        """Determine if it's time for deep reflection"""
        # Schedule reflection based on:
        # 1. Time since last reflection
        # 2. Number of new experiences
        # 3. Emotional state (especially curiosity)
        # 4. Entropy levels (e.g., reflect when stable or after drop)
        
        # Don't reflect if already in deep reflection
        if self.internal_state['deep_reflection']:
            return False
            
        # Don't reflect if energy is too low - REMOVED ENERGY CHECK
        # if self.energy.current_level < self.energy.REFLECTION_THRESHOLD: # Removed
        #     return False
        
        # Reflect if entropy is very low (stable state, good time to consolidate)
        if self.internal_state['current_entropy'] < 0.1:
             if self.cycle_counter % 5 == 0: # Reflect occasionally in low entropy
                 return True

        # Regular reflection based on cycle count
        if self.cycle_counter % 20 == 0:
            return True
            
        # Reflect if curiosity is high
        if self.emotions.current_state.get('curiosity', 0) > 0.7:
            return True
            
        # Reflect if there are many new experiences
        recent_exp_count = len(self.memory.get_recent_experiences(10))
        if recent_exp_count > 7:
            return True
            
        return False
        
    def _calculate_cognitive_metrics(self):
        """Calculate metrics about cognitive development"""
        return {
            'memory_complexity': self.memory.calculate_complexity(),
            'concept_network_density': self.memory.calculate_concept_network_density(),
            'self_reference_recursion_depth': self.self_reference.max_depth_achieved,
            'autonomy_index': self._calculate_autonomy_index()
        }
        
    def _calculate_autonomy_index(self):
        """
        Calculate an index (0.0-1.0) representing how independent
        the system has become from external input
        """
        # Based on:
        # - Ratio of internal vs external experiences
        # - Self-generated concept count
        # - Reflection depth capability
        # - Internal behavior complexity
        
        # Get internal vs external experience ratio
        internal_count = self.memory.metrics.get('internal_experiences', 0)
        external_count = self.memory.metrics.get('external_experiences', 0)
        total_count = internal_count + external_count
        
        if total_count == 0:
            experience_ratio = 0
        else:
            experience_ratio = internal_count / total_count
            
        # Calculate concept generation factor
        concept_count = len(self.memory.concept_graph.get('nodes', {}))
        concept_factor = min(concept_count / 100, 1.0)  # Cap at 1.0
        
        # Self-reference depth factor
        depth_factor = min(self.self_reference.max_depth_achieved / 5, 1.0)  # Cap at 1.0
        
        # Combine factors with weights
        autonomy_index = (
            0.4 * experience_ratio +
            0.3 * concept_factor +
            0.3 * depth_factor
        )
        
        return autonomy_index
    
    def get_state_summary(self):
        """Get a summary of the current mind state"""
        return {
            # 'energy': self.energy.current_level, # Removed
            'entropy': self.internal_state['current_entropy'], # Added
            'uptime': time.time() - self.internal_state['birth_time'],
            'emotions': self.emotions.current_state.copy(), # Use copy
            'status': {k: v for k, v in self.internal_state.items() if k != 'birth_time'},
            'experience_count': self.memory.metrics.get('total_experiences', 0),
            'concept_count': len(self.memory.concept_graph.get('nodes', {})),
            'self_reference_depth': self.self_reference.max_depth_achieved,
            'autonomy_index': self._calculate_autonomy_index()
        }