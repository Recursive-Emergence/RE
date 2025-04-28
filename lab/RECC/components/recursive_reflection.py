"""
Recursive Reflection Module
Implements multi-level self-modeling with configurable recursive depth

This module is the core of MVP 1.6, enabling RECC to develop true recursive 
self-reference capabilities with depth n ≥ 3 (the theoretical threshold for 
cognitive emergence as described in the neural layer theory).
"""

import time
import copy
import uuid
from datetime import datetime
import random

from event_bus import global_event_bus, EventTypes

class RecursiveReflection:
    """
    Core implementation of recursive reflection system with configurable depth.
    
    This class enables RECC to model its own modeling process at multiple levels,
    creating a recursive chain of self-models where each level can observe and
    modify lower levels.
    """
    
    def __init__(self, max_depth=3, event_bus=None):
        """Initialize the recursive reflection system with specified maximum depth"""
        self.max_depth = max_depth
        self.reflection_levels = []
        self.event_bus = event_bus or global_event_bus
        
        # Initialize reflection levels
        for depth in range(max_depth + 1):  # Include level 0
            self.reflection_levels.append({
                'depth': depth,
                'model': self._create_level_model(depth),
                'state': 'inactive' if depth > 0 else 'active',
                'history': []
            })
        
        # Track metrics about the recursive system
        self.metrics = {
            'effective_depth': 0.0,
            'cross_level_modifications': 0,
            'activation_history': []
        }
    
    def _create_level_model(self, depth):
        """Create an appropriate model for the specified reflection depth"""
        if depth == 0:
            return DirectExperienceModel()
        elif depth == 1:
            return BasicSelfModel()
        elif depth == 2:
            return MetaCognitiveModel()
        elif depth == 3:
            return RecursiveImprovementModel()
        else:
            return RecursiveImprovementModel()  # Default for higher levels
    
    def reflect(self, input_data=None):
        """
        Perform recursive reflection through all active levels.
        
        Each reflection level observes the level below it and potentially 
        modifies it based on its observations.
        
        Args:
            input_data: Optional input data to process at level 0
            
        Returns:
            List of reflection results from each active level
        """
        results = []
        reflection_start_time = time.time()
        
        # Level 0: Process direct experience (if input provided)
        if input_data is not None:
            level0_result = self.reflection_levels[0]['model'].process(input_data)
            self.reflection_levels[0]['history'].append({
                'time': time.time(),
                'input': input_data,
                'result': level0_result
            })
            results.append(level0_result)
            
            # Activate level 1 reflection immediately
            if self.reflection_levels[1]['state'] != 'active':
                self.reflection_levels[1]['state'] = 'active'
                self.metrics['activation_history'].append({
                    'time': time.time(),
                    'level': 1,
                    'action': 'activated'
                })
        
        # Process higher reflection levels
        for depth in range(1, self.max_depth + 1):
            if self.reflection_levels[depth]['state'] != 'active':
                continue
                
            # Get the lower level to reflect on
            lower_level_data = {
                'model': self.reflection_levels[depth-1]['model'],
                'history': self.reflection_levels[depth-1]['history'],
                'state': self.reflection_levels[depth-1]['state']
            }
            
            # Perform reflection
            reflection_result = self.reflection_levels[depth]['model'].reflect(lower_level_data)
            
            # Store result in history
            self.reflection_levels[depth]['history'].append({
                'time': time.time(),
                'input': copy.deepcopy(lower_level_data),
                'result': reflection_result
            })
            
            # Apply modifications to lower level if needed
            if 'modifications' in reflection_result and reflection_result['modifications']:
                self._apply_modifications(depth-1, reflection_result['modifications'])
                self.metrics['cross_level_modifications'] += len(reflection_result['modifications'])
                
                # Emit event about cross-level modification
                self.event_bus.publish(EventTypes.RECURSIVE_MODIFICATION, {
                    'source_level': depth,
                    'target_level': depth-1,
                    'modifications': reflection_result['modifications'],
                    'timestamp': datetime.now().isoformat()
                })
            
            results.append(reflection_result)
            
            # Enhanced activation logic: Activate next level more aggressively
            next_level = depth + 1
            if next_level <= self.max_depth:  # Ensure we don't exceed max_depth
                # Activate next level after just 2 history entries (was 3 before)
                if len(self.reflection_levels[depth]['history']) >= 2:
                    if self.reflection_levels[next_level]['state'] != 'active':
                        self.reflection_levels[next_level]['state'] = 'active'
                        self.metrics['activation_history'].append({
                            'time': time.time(),
                            'level': next_level,
                            'action': 'activated'
                        })
                        
                        # Emit event about level activation
                        self.event_bus.publish(EventTypes.RECURSIVE_LEVEL_ACTIVATED, {
                            'level': next_level,
                            'timestamp': datetime.now().isoformat()
                        })
        
        # Update metrics
        self._update_metrics()
        
        # Emit reflection complete event with duration
        self.event_bus.publish(EventTypes.REFLECTION_COMPLETE, {
            'duration': time.time() - reflection_start_time,
            'active_levels': self._count_active_levels(),
            'effective_depth': self.metrics['effective_depth'],
            'timestamp': datetime.now().isoformat()
        })
        
        return results
    
    def _apply_modifications(self, target_level, modifications):
        """
        Apply modifications from a higher reflection level to a lower one
        
        Args:
            target_level: The level to modify
            modifications: List of modification objects
        """
        model = self.reflection_levels[target_level]['model']
        
        for mod in modifications:
            try:
                if hasattr(model, mod['attribute']):
                    if mod['operation'] == 'update':
                        setattr(model, mod['attribute'], mod['value'])
                    elif mod['operation'] == 'adjust':
                        current_value = getattr(model, mod['attribute'])
                        # Handle different types of adjustments
                        if isinstance(current_value, (int, float)):
                            setattr(model, mod['attribute'], current_value + mod['delta'])
                        elif isinstance(current_value, dict) and isinstance(mod['delta'], dict):
                            # For dictionaries, update keys specified in delta
                            current_value.update(mod['delta'])
                            setattr(model, mod['attribute'], current_value)
                        elif isinstance(current_value, list) and isinstance(mod['delta'], list):
                            # For lists, append new items
                            current_value.extend(mod['delta'])
                            setattr(model, mod['attribute'], current_value)
            except Exception as e:
                print(f"Error applying modification: {e}")
    
    def get_meta_cognition_report(self):
        """
        Generate a comprehensive report on the current state of meta-cognition
        
        Returns:
            Dictionary containing detailed metrics about each reflection level
        """
        report = []
        
        for depth in range(self.max_depth + 1):
            level = self.reflection_levels[depth]
            level_report = {
                'depth': depth,
                'state': level['state'],
                'history_entries': len(level['history']),
                'active_since': level['history'][0]['time'] if level['history'] else None,
                'metrics': level['model'].get_metrics() if hasattr(level['model'], 'get_metrics') else {}
            }
            report.append(level_report)
            
        return {
            'levels': report,
            'effective_depth': self.metrics['effective_depth'],
            'cross_level_modifications': self.metrics['cross_level_modifications'],
            'active_levels': self._count_active_levels(),
            'timestamp': datetime.now().isoformat()
        }
    
    def _count_active_levels(self):
        """Count the number of active reflection levels"""
        return sum(1 for level in self.reflection_levels if level['state'] == 'active')
    
    def _update_metrics(self):
        """Update metrics about the recursive reflection system"""
        # Count active levels with meaningful history
        meaningful_levels = sum(1 for level in self.reflection_levels 
                              if level['state'] == 'active' and len(level['history']) >= 3)
        
        # Calculate effective recursive depth
        if meaningful_levels >= 3 and self.metrics['cross_level_modifications'] > 0:
            self.metrics['effective_depth'] = 3.0
        elif meaningful_levels >= 2 and self.metrics['cross_level_modifications'] > 0:
            self.metrics['effective_depth'] = 2.0
        elif meaningful_levels >= 1:
            self.metrics['effective_depth'] = 1.0
        else:
            self.metrics['effective_depth'] = 0.0

class DirectExperienceModel:
    """
    Level 0: Direct processing of experiences without self-reflection
    
    This model represents the base layer of cognitive processing
    that simply handles incoming data without self-awareness.
    """
    def __init__(self):
        self.experiences = []
        self.patterns = {}
        self.attention_focus = 'default'
    
    def process(self, input_data):
        """
        Process incoming experience data
        
        Args:
            input_data: Dictionary containing experience information
            
        Returns:
            Dictionary with processing results
        """
        # Extract patterns from input
        detected_patterns = self._detect_patterns(input_data)
        
        # Store experience
        experience = {
            'id': str(uuid.uuid4()),
            'time': time.time(),
            'input': input_data,
            'patterns': detected_patterns
        }
        self.experiences.append(experience)
        
        # Update pattern statistics
        for pattern in detected_patterns:
            if pattern not in self.patterns:
                self.patterns[pattern] = {
                    'count': 0,
                    'first_seen': time.time(),
                    'contexts': set()
                }
            self.patterns[pattern]['count'] += 1
            
            # Track contexts where this pattern appears
            if 'context' in input_data:
                self.patterns[pattern]['contexts'].add(input_data['context'])
            
        return {
            'processed': True,
            'patterns_detected': len(detected_patterns),
            'patterns': detected_patterns
        }
    
    def _detect_patterns(self, input_data):
        """
        Detect patterns in input data
        
        This is a simplified implementation. In practice, this would use
        more sophisticated pattern recognition techniques.
        
        Args:
            input_data: Dictionary containing experience data
            
        Returns:
            List of detected pattern identifiers
        """
        patterns = []
        
        # Extract simple patterns based on data type
        if isinstance(input_data, dict):
            # For memory entries, look at response content
            if 'response' in input_data:
                text = input_data['response'].lower()
                
                # Check for emotional content
                if any(word in text for word in ['happy', 'glad', 'joy', 'excited']):
                    patterns.append('positive_emotion')
                elif any(word in text for word in ['sad', 'upset', 'angry', 'frustrated']):
                    patterns.append('negative_emotion')
                
                # Check for question patterns
                if '?' in text:
                    patterns.append('question')
                    
                # Check for specific domains
                if any(word in text for word in ['recursive', 'self', 'reflect', 'think']):
                    patterns.append('self_reference')
                    
                # Check for pattern references
                if any(word in text for word in ['pattern', 'structure', 'system', 'organize']):
                    patterns.append('pattern_recognition')
        
        # Ensure we always return at least one pattern
        if not patterns:
            patterns.append('generic_pattern')
            
        return patterns
    
    def get_metrics(self):
        """Get model metrics"""
        return {
            'experience_count': len(self.experiences),
            'unique_patterns': len(self.patterns),
            'attention_focus': self.attention_focus
        }

class BasicSelfModel:
    """
    Level 1: Basic awareness of internal states and patterns
    
    This model represents the first level of self-awareness, where the
    system begins to monitor its own states and recognize patterns in
    its processing.
    """
    def __init__(self):
        self.observations = []
        self.state_awareness = {
            'pattern_recognition': 0.5,
            'memory_utilization': 0.5,
            'attention_focus': 'default'
        }
        self.learning_rate = 0.1
    
    def reflect(self, lower_level_data):
        """
        Reflect on the direct experience level
        
        Args:
            lower_level_data: Data about the lower level (L0) processing
            
        Returns:
            Dictionary containing reflection results
        """
        model = lower_level_data['model']
        history = lower_level_data['history']
        
        if not history:
            return {'status': 'insufficient_data'}
        
        # Analyze recent experiences
        recent_entries = history[-5:] if len(history) >= 5 else history
        patterns_seen = set()
        
        for entry in recent_entries:
            if 'result' in entry and 'patterns' in entry['result']:
                patterns_seen.update(entry['result']['patterns'])
        
        # Update self-awareness based on direct level statistics
        pattern_recognition = min(1.0, len(model.patterns) / max(100, len(model.patterns) * 2))
        memory_utilization = min(1.0, len(model.experiences) / max(1000, len(model.experiences) * 2))
        
        # Gradually update awareness (moving average)
        self.state_awareness = {
            'pattern_recognition': (1 - self.learning_rate) * self.state_awareness['pattern_recognition'] + 
                                   self.learning_rate * pattern_recognition,
            'memory_utilization': (1 - self.learning_rate) * self.state_awareness['memory_utilization'] + 
                                  self.learning_rate * memory_utilization,
            'attention_focus': model.attention_focus
        }
        
        # Check if focus should shift based on patterns
        if 'self_reference' in patterns_seen:
            self.state_awareness['attention_focus'] = 'self_monitoring'
        elif 'pattern_recognition' in patterns_seen:
            self.state_awareness['attention_focus'] = 'pattern_detection'
        
        # Record this observation
        observation = {
            'time': time.time(),
            'patterns_count': len(patterns_seen),
            'patterns': list(patterns_seen),
            'state_awareness': copy.deepcopy(self.state_awareness)
        }
        self.observations.append(observation)
        
        # At this level, we only observe, not modify
        modifications = []
        
        # Potential focus shift modification
        if model.attention_focus != self.state_awareness['attention_focus']:
            modifications.append({
                'attribute': 'attention_focus',
                'operation': 'update',
                'value': self.state_awareness['attention_focus']
            })
        
        return {
            'status': 'observation_recorded',
            'observation_id': len(self.observations),
            'self_awareness': copy.deepcopy(self.state_awareness),
            'modifications': modifications
        }
    
    def get_metrics(self):
        """Get model metrics"""
        return {
            'observation_count': len(self.observations),
            'self_awareness_level': sum(v for k, v in self.state_awareness.items() 
                                       if isinstance(v, (int, float))) / 
                                  sum(1 for v in self.state_awareness.values() 
                                     if isinstance(v, (int, float)))
        }

class MetaCognitiveModel:
    """
    Level 2: Awareness of the process of self-modeling
    
    This model represents meta-cognitive awareness, where the system
    not only monitors itself but also recognizes patterns in how it 
    monitors itself and can adjust its monitoring strategies.
    """
    def __init__(self):
        self.meta_observations = []
        self.strategy_effectiveness = {}
        self.learning_rate = 0.1
        self.meta_model = {
            'optimal_pattern_recognition': 0.7,
            'optimal_memory_utilization': 0.6,
            'strategy_adaptation_rate': 0.2
        }
    
    def reflect(self, lower_level_data):
        """
        Reflect on the basic self-model level
        
        Args:
            lower_level_data: Data about the lower level (L1) processing
            
        Returns:
            Dictionary containing reflection results
        """
        model = lower_level_data['model']
        history = lower_level_data['history']
        
        if len(history) < 3:
            return {'status': 'insufficient_data'}
        
        # Analyze trend in self-awareness
        awareness_trend = []
        for entry in history[-3:]:
            if 'result' in entry and 'self_awareness' in entry['result']:
                awareness_trend.append(entry['result']['self_awareness'])
        
        if not awareness_trend:
            return {'status': 'insufficient_awareness_data'}
        
        # Detect patterns in self-awareness changes
        pattern_recognition_trend = [a.get('pattern_recognition', 0) for a in awareness_trend]
        memory_utilization_trend = [a.get('memory_utilization', 0) for a in awareness_trend]
        
        # Calculate trends
        pr_trend = self._calculate_trend(pattern_recognition_trend)
        mu_trend = self._calculate_trend(memory_utilization_trend)
        
        # Determine if strategies need adjustment based on meta-model
        modifications = []
        
        # Check if pattern recognition is below optimal and declining
        if (awareness_trend[-1]['pattern_recognition'] < self.meta_model['optimal_pattern_recognition'] and
            pr_trend < -0.05):
            modifications.append({
                'attribute': 'attention_focus',
                'operation': 'update',
                'value': 'pattern_detection'
            })
            
        # Check if memory utilization is too high
        if awareness_trend[-1]['memory_utilization'] > self.meta_model['optimal_memory_utilization'] + 0.1:
            modifications.append({
                'attribute': 'learning_rate',
                'operation': 'adjust',
                'delta': 0.05  # Increase learning rate to adapt faster
            })
        
        # Record this meta-observation
        meta_observation = {
            'time': time.time(),
            'awareness_trends': {
                'pattern_recognition': pr_trend,
                'memory_utilization': mu_trend
            },
            'modifications': modifications
        }
        self.meta_observations.append(meta_observation)
        
        # Update strategy effectiveness based on past modifications
        if len(self.meta_observations) >= 2:
            previous_mods = self.meta_observations[-2].get('modifications', [])
            for prev_mod in previous_mods:
                # Check if this modification improved the situation
                attribute = prev_mod['attribute']
                if attribute == 'attention_focus':
                    # Did focusing on pattern detection improve pattern recognition?
                    if prev_mod['value'] == 'pattern_detection' and pr_trend > 0:
                        self._update_strategy_effectiveness('focus_on_patterns', True)
                    elif prev_mod['value'] == 'pattern_detection' and pr_trend <= 0:
                        self._update_strategy_effectiveness('focus_on_patterns', False)
        
        return {
            'status': 'meta_observation_recorded',
            'meta_observation_id': len(self.meta_observations),
            'awareness_trends': {
                'pattern_recognition': pr_trend,
                'memory_utilization': mu_trend
            },
            'modifications': modifications,
            'meta_model': copy.deepcopy(self.meta_model)
        }
    
    def _calculate_trend(self, values):
        """Calculate trend in a series of values"""
        if len(values) < 2:
            return 0
        return (values[-1] - values[0]) / (len(values) - 1)
    
    def _update_strategy_effectiveness(self, strategy, success):
        """Update the effectiveness record of a strategy"""
        if strategy not in self.strategy_effectiveness:
            self.strategy_effectiveness[strategy] = {'success': 0, 'total': 0}
            
        self.strategy_effectiveness[strategy]['total'] += 1
        if success:
            self.strategy_effectiveness[strategy]['success'] += 1
    
    def get_metrics(self):
        """Get model metrics"""
        strategy_success_rates = {}
        for strategy, stats in self.strategy_effectiveness.items():
            if stats['total'] > 0:
                strategy_success_rates[strategy] = stats['success'] / stats['total']
            
        return {
            'meta_observation_count': len(self.meta_observations),
            'strategy_count': len(self.strategy_effectiveness),
            'strategy_success_rates': strategy_success_rates,
            'learning_rate': self.learning_rate
        }

class RecursiveImprovementModel:
    """
    Level 3: Ability to recognize and improve the meta-cognitive process itself
    
    This model represents the ability to reflect on and improve the process
    of reflection itself, creating a fully recursive self-improvement loop.
    This is the level at which true recursive self-reference emerges.
    """
    def __init__(self):
        self.improvement_history = []
        self.meta_strategies = {
            'adaptation_rate': 0.5,
            'exploration_vs_exploitation': 0.5,
            'recursive_depth_emphasis': 0.5
        }
        self.strategy_models = {}
        self.innovation_cycle = 0
        self.last_innovation_time = time.time()
    
    def reflect(self, lower_level_data):
        """
        Reflect on the meta-cognitive level
        
        Args:
            lower_level_data: Data about the lower level (L2) processing
            
        Returns:
            Dictionary containing reflection results
        """
        model = lower_level_data['model']
        history = lower_level_data['history']
        
        if len(history) < 2:  # Reduced requirement to start generating improvements sooner
            return {'status': 'insufficient_data'}
        
        # Analyze effectiveness of meta-cognitive strategies
        modification_count = 0
        improvement_count = 0
        
        for entry in history:
            if 'result' in entry:
                result = entry['result']
                mods = result.get('modifications', [])
                modification_count += len(mods)
                
                # Check if modifications led to improvements
                if ('awareness_trends' in result and 
                    result['awareness_trends'].get('pattern_recognition', 0) > 0):
                    improvement_count += 1
        
        # Calculate effectiveness ratio
        effectiveness = improvement_count / max(1, modification_count) if modification_count > 0 else 0
        
        # Increment innovation cycle and check if time for major changes
        self.innovation_cycle += 1
        time_since_innovation = time.time() - self.last_innovation_time
        major_innovation_due = self.innovation_cycle % 5 == 0 or time_since_innovation > 30
        
        # Adjust meta-strategies based on effectiveness
        if effectiveness < 0.3:  # Poor effectiveness
            self.meta_strategies['adaptation_rate'] *= 0.85  # More aggressive slowing
            self.meta_strategies['exploration_vs_exploitation'] += 0.15  # More aggressive exploration
            # Major shift in strategy when effectiveness is low
            if major_innovation_due:
                self.meta_strategies['recursive_depth_emphasis'] = min(0.9, self.meta_strategies['recursive_depth_emphasis'] + 0.2)
                self.last_innovation_time = time.time()
        elif effectiveness > 0.7:  # Good effectiveness
            self.meta_strategies['adaptation_rate'] *= 1.15  # More aggressive acceleration
            self.meta_strategies['exploration_vs_exploitation'] -= 0.1  # More exploitation
            if major_innovation_due:
                # Reward success with increased emphasis on recursion
                self.meta_strategies['recursive_depth_emphasis'] = min(0.9, self.meta_strategies['recursive_depth_emphasis'] + 0.1)
                self.last_innovation_time = time.time()
        else:  # Moderate effectiveness
            if major_innovation_due and random.random() < 0.7:  # 70% chance of innovation
                # Try something new
                strategy_keys = list(self.meta_strategies.keys())
                random_strategy = random.choice(strategy_keys)
                shift = 0.15 if random.random() < 0.5 else -0.15
                self.meta_strategies[random_strategy] += shift
                self.last_innovation_time = time.time()
        
        # Normalize values to appropriate ranges
        self.meta_strategies['adaptation_rate'] = max(0.1, min(0.9, self.meta_strategies['adaptation_rate']))
        self.meta_strategies['exploration_vs_exploitation'] = max(0.1, min(0.9, self.meta_strategies['exploration_vs_exploitation']))
        self.meta_strategies['recursive_depth_emphasis'] = max(0.1, min(0.9, self.meta_strategies['recursive_depth_emphasis']))
        
        # Update strategy models based on observations
        if hasattr(model, 'strategy_effectiveness') and model.strategy_effectiveness:
            for strategy, stats in model.strategy_effectiveness.items():
                if strategy not in self.strategy_models:
                    self.strategy_models[strategy] = {
                        'estimated_success': 0.5,
                        'confidence': 0.1,
                        'last_updated': time.time()
                    }
                
                # Update our model of this strategy's effectiveness
                if stats['total'] > 0:
                    success_rate = stats['success'] / stats['total']
                    confidence_factor = min(0.9, stats['total'] / 10)  # Confidence increases with more trials
                    
                    current_model = self.strategy_models[strategy]
                    # Bayesian-inspired update
                    current_model['estimated_success'] = (
                        (1 - confidence_factor) * current_model['estimated_success'] + 
                        confidence_factor * success_rate
                    )
                    current_model['confidence'] = min(0.9, current_model['confidence'] + 0.1)
                    current_model['last_updated'] = time.time()
        
        # Generate more substantial modifications - key enhancement!
        modifications = []
        
        # 1. Always update the learning rate based on adaptation rate
        modifications.append({
            'attribute': 'learning_rate',
            'operation': 'update',
            'value': self.meta_strategies['adaptation_rate']
        })
        
        # 2. Adjust the meta-model with higher probability
        if hasattr(model, 'meta_model') and random.random() < 0.8:  # 80% chance
            # Choose a parameter to adjust
            meta_model_params = list(model.meta_model.keys())
            param_to_adjust = random.choice(meta_model_params)
            
            # Determine adjustment magnitude based on exploration parameter
            adjust_magnitude = 0.05 + (self.meta_strategies['exploration_vs_exploitation'] * 0.1)
            
            # Apply the modification
            delta = {param_to_adjust: adjust_magnitude if random.random() < 0.6 else -adjust_magnitude}
            modifications.append({
                'attribute': 'meta_model',
                'operation': 'adjust',
                'delta': delta
            })
        
        # 3. Occasionally introduce entirely new strategies
        if major_innovation_due and random.random() < 0.5:  # 50% chance during innovation cycles
            # For example, introduce a new meta-model parameter or attention focus strategy
            if hasattr(model, 'meta_model') and len(model.meta_model) < 5:  # Limit to 5 parameters
                new_param_options = [
                    ('strategy_update_frequency', random.uniform(0.1, 0.5)),
                    ('attention_diversity', random.uniform(0.3, 0.7)),
                    ('memory_decay_rate', random.uniform(0.05, 0.2)),
                    ('cross_pattern_sensitivity', random.uniform(0.4, 0.8))
                ]
                
                # Filter out existing parameters
                available_params = [p for p in new_param_options if p[0] not in model.meta_model]
                
                if available_params:
                    new_param = random.choice(available_params)
                    modifications.append({
                        'attribute': 'meta_model',
                        'operation': 'adjust',
                        'delta': {new_param[0]: new_param[1]}
                    })
        
        # Record this improvement cycle
        improvement = {
            'time': time.time(),
            'effectiveness': effectiveness,
            'meta_strategies': copy.deepcopy(self.meta_strategies),
            'modifications': modifications,
            'innovation_cycle': self.innovation_cycle,
            'best_strategies': self._get_best_strategies(top_n=3)
        }
        self.improvement_history.append(improvement)
        
        return {
            'status': 'improvement_recorded',
            'improvement_id': len(self.improvement_history),
            'effectiveness': effectiveness,
            'meta_strategies': copy.deepcopy(self.meta_strategies),
            'modifications': modifications
        }
    
    def _get_best_strategies(self, top_n=3):
        """Get the top n most effective strategies"""
        if not self.strategy_models:
            return []
            
        # Filter for strategies with sufficient confidence
        reliable_strategies = {k: v for k, v in self.strategy_models.items() 
                              if v['confidence'] > 0.3}
        
        # Sort by estimated success
        sorted_strategies = sorted(
            reliable_strategies.items(),
            key=lambda x: x[1]['estimated_success'],
            reverse=True
        )
        
        # Return just the names of top strategies
        return [s[0] for s in sorted_strategies[:top_n]]
    
    def get_metrics(self):
        """Get model metrics"""
        effectiveness_values = [imp.get('effectiveness', 0) for imp in self.improvement_history]
        avg_effectiveness = sum(effectiveness_values) / max(1, len(effectiveness_values))
        
        # Calculate evolution of strategies over time
        strategy_evolution = 0
        if len(self.improvement_history) >= 4:
            start_strategies = self.improvement_history[0]['meta_strategies']
            current_strategies = self.improvement_history[-1]['meta_strategies']
            
            # Calculate Euclidean distance between strategy vectors
            squared_diffs = [
                (current_strategies[k] - start_strategies[k])**2
                for k in current_strategies.keys()
            ]
            strategy_evolution = (sum(squared_diffs) / len(squared_diffs))**0.5
        
        return {
            'improvement_cycles': len(self.improvement_history),
            'average_effectiveness': avg_effectiveness,
            'meta_strategy_balance': self.meta_strategies,
            'strategy_models_count': len(self.strategy_models),
            'strategy_evolution': strategy_evolution,
            'innovation_cycle': self.innovation_cycle
        }