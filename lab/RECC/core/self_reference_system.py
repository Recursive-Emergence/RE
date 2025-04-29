import time
import math
import random
import uuid
from collections import defaultdict, deque

class SelfReferenceSystem:
    """
    Self-reference system that enables the mind to observe, model
    and modify itself. This system is the core of recursive emergence
    as it tracks and enhances the mind's ability to reference its own
    states and processes.
    
    The system manages:
    1. Self-model of the mind's components and states
    2. Self-reference events and their tracking
    3. Recursive depth monitoring
    4. Internal representation evolution
    """
    
    def __init__(self):
        # Self-model of the mind (representational)
        self.self_model = {
            'components': {
                'energy': {'status': 'initialized', 'representation': 0.1},
                'emotion': {'status': 'initialized', 'representation': 0.1},
                'memory': {'status': 'initialized', 'representation': 0.1},
                'behavior': {'status': 'initialized', 'representation': 0.1},
                'reflection': {'status': 'initialized', 'representation': 0.1},
                'self_reference': {'status': 'initialized', 'representation': 0.1}
            },
            'processes': {
                'perception': {'status': 'active', 'representation': 0.1},
                'integration': {'status': 'active', 'representation': 0.1},
                'reflection': {'status': 'active', 'representation': 0.1},
                'consolidation': {'status': 'inactive', 'representation': 0.1},
                'self_observation': {'status': 'active', 'representation': 0.1}
            },
            'states': {
                'overall': 'initializing',
                'coherence': 0.3,
                'complexity': 0.2
            }
        }
        
        # Self-reference tracking
        self.self_references = []
        self.reference_counts = {
            'depth_1': 0,  # Direct self-references
            'depth_2': 0,  # References to self-references
            'depth_3+': 0  # Deeper recursive references
        }
        
        # Recursive depth tracking
        self.max_depth_achieved = 1
        self.current_recursion = {
            'depth': 1,
            'path': [],
            'start_time': time.time()
        }
        
        # Internal representation quality
        self.representation_quality = {
            'overall': 0.2,  # Overall quality of self-model
            'by_component': {},  # Quality by component
            'coherence': 0.3,  # How well components integrate
            'abstraction': 0.1   # Level of abstract representation
        }
        
        # Meta-cognitive capabilities
        self.meta_capabilities = {
            'self_observation': 0.2,  # Ability to observe own states
            'self_modification': 0.1,  # Ability to modify own processes
            'self_explanation': 0.1,   # Ability to explain own functioning
            'abstraction': 0.1         # Ability to form abstract self-concepts
        }
        
        # History of self-model evolution
        self.model_evolution = []
        
        # Initialize representation quality for each component
        for component in self.self_model['components']:
            self.representation_quality['by_component'][component] = 0.1
    
    # Add the missing process_cycle method
    def process_cycle(self, memory_system, emotional_system, internal_state):
        """
        Process a cycle of self-reference, examining current and past
        states to build a more complex understanding of self.
        
        Args:
            memory_system: Memory system to reference
            emotional_system: Emotional state to reference
            internal_state: Current internal state (e.g., entropy, complexity)
            
        Returns:
            dict: Results of self-reference processing, including events.
        """
        events = []
        insights = []
        
        # 1. Basic Self-Observation: Record a reference to the current state
        current_entropy = internal_state.get('current_entropy', 0.0)
        insight_text = f"Observed internal state. Entropy: {current_entropy:.3f}"
        ref = self.record_reference(
            source_type='self_reference_system', 
            target_type='internal_state', 
            insight=insight_text,
            energy_impact=-0.05 # Minimal cost for observation
        )
        events.append(ref)
        insights.append(insight_text)

        # 2. Reference recent memory/experience (simple example)
        recent_exps = memory_system.get_recent_experiences(1)
        if recent_exps:
            exp = recent_exps[0]
            insight_text = f"Referencing recent experience {exp['id'][:8]} with entropy {exp.get('entropy_at_experience', 'N/A'):.3f}"
            ref = self.record_reference(
                source_type='self_reference_system',
                target_type='memory_experience',
                insight=insight_text,
                energy_impact=-0.05
            )
            events.append(ref)
            insights.append(insight_text)
            # Potentially trigger deeper analysis based on this reference...

        # 3. Reference emotional state
        dominant_emotion, strength = emotional_system.get_dominant_emotion()
        insight_text = f"Referencing dominant emotion: {dominant_emotion} ({strength:.3f})"
        ref = self.record_reference(
            source_type='self_reference_system',
            target_type='emotional_state',
            insight=insight_text,
            energy_impact=-0.05
        )
        events.append(ref)
        insights.append(insight_text)

        # 4. Consolidate self-model periodically
        # (Could be triggered by specific conditions, e.g., high curiosity, low entropy)
        if random.random() < 0.1: # Consolidate 10% of the time
             consolidation_results = self.consolidate_self_model()
             insights.append(f"Consolidated self-model. Quality improved by {consolidation_results['improvements'].get('overall_quality', 0):.4f}")

        # Update internal state based on self-reference activity
        # (e.g., increase complexity slightly)
        # internal_state['cognitive_complexity'] += 0.001 * len(events) 
        # ^ This should ideally be done within IndependentMind based on results

        return {
            'events': events,
            'insights': insights,
            'current_depth': self.current_recursion['depth'], # Return current depth
            # Add other relevant results as needed
        }

    def record_reference(self, source_type, target_type, insight=None, energy_impact=-0.1):
        """
        Record a self-reference event
        
        Args:
            source_type: Component making the reference
            target_type: Component being referenced
            insight: Optional insight gained from reference
            energy_impact: Energy impact of the reference
            
        Returns:
            dict: The recorded self-reference
        """
        # Generate reference ID
        ref_id = str(uuid.uuid4())
        
        # Determine depth based on target
        depth = 1  # Default: direct reference
        
        if target_type == 'self_reference':
            # Reference to self-reference system is depth 2
            depth = 2
        elif 'ref_' in str(target_type):
            # Reference to another reference is deeper
            depth = 3
            
        # Create default insight if none provided
        if insight is None:
            insight = f"{source_type} referencing {target_type}"
            
        # Record timestamp
        timestamp = time.time()
        
        # Create reference object
        reference = {
            'id': ref_id,
            'timestamp': timestamp,
            'source_type': source_type,
            'target_type': target_type,
            'depth': depth,
            'insight': insight,
            'energy_impact': energy_impact,
            'reused': 0  # Count of times this reference is referenced
        }
        
        # Store reference
        self.self_references.append(reference)
        
        # Update counts
        if depth == 1:
            self.reference_counts['depth_1'] += 1
        elif depth == 2:
            self.reference_counts['depth_2'] += 1
        else:
            self.reference_counts['depth_3+'] += 1
            
        # Update max depth if needed
        if depth > self.max_depth_achieved:
            self.max_depth_achieved = depth
            
        # Update current recursion path
        self.current_recursion['path'].append(f"{source_type}->{target_type}")
        self.current_recursion['depth'] = max(self.current_recursion['depth'], depth)
        
        # If this is a significant insight, improve representation quality
        if len(insight) > 30:
            self._improve_representation(target_type, 0.01)
            
        return reference
    
    def begin_recursive_reference(self, initial_source):
        """
        Begin tracking a new recursive reference chain
        
        Args:
            initial_source: Component starting the reference chain
        """
        # Reset the current recursion tracking
        self.current_recursion = {
            'depth': 1,
            'path': [initial_source],
            'start_time': time.time()
        }
    
    def end_recursive_reference(self):
        """
        End tracking of current recursive reference chain
        
        Returns:
            dict: Summary of the completed recursive reference
        """
        # Calculate duration
        duration = time.time() - self.current_recursion['start_time']
        
        # Create summary
        summary = {
            'depth': self.current_recursion['depth'],
            'path': self.current_recursion['path'].copy(),
            'duration': duration,
            'timestamp': time.time()
        }
        
        # If this was a deep recursion, improve meta-capabilities
        if self.current_recursion['depth'] >= 2:
            improvement = 0.005 * self.current_recursion['depth']
            self._improve_meta_capability('self_observation', improvement)
            
        # Reset current recursion
        self.current_recursion = {
            'depth': 1,
            'path': [],
            'start_time': time.time()
        }
        
        return summary
    
    def update_component_status(self, component_name, status, representation_delta=0):
        """
        Update status of a component in the self-model
        
        Args:
            component_name: Name of component to update
            status: New status value
            representation_delta: Change in representation quality
        """
        if component_name in self.self_model['components']:
            self.self_model['components'][component_name]['status'] = status
            
            # Apply representation delta if provided
            if representation_delta != 0:
                current_rep = self.self_model['components'][component_name]['representation']
                new_rep = max(0.0, min(1.0, current_rep + representation_delta))
                self.self_model['components'][component_name]['representation'] = new_rep
    
    def update_process_status(self, process_name, status, representation_delta=0):
        """
        Update status of a process in the self-model
        
        Args:
            process_name: Name of process to update
            status: New status value
            representation_delta: Change in representation quality
        """
        if process_name in self.self_model['processes']:
            self.self_model['processes'][process_name]['status'] = status
            
            # Apply representation delta if provided
            if representation_delta != 0:
                current_rep = self.self_model['processes'][process_name]['representation']
                new_rep = max(0.0, min(1.0, current_rep + representation_delta))
                self.self_model['processes'][process_name]['representation'] = new_rep
    
    def update_overall_state(self, state_name, value=None):
        """
        Update overall state in the self-model
        
        Args:
            state_name: Name of state to update
            value: New value (optional)
        """
        if state_name == 'overall' and isinstance(value, str):
            self.self_model['states']['overall'] = value
        elif state_name in self.self_model['states'] and value is not None:
            # For numerical states, ensure value is in range 0-1
            if isinstance(value, (int, float)):
                self.self_model['states'][state_name] = max(0.0, min(1.0, value))
    
    def _improve_representation(self, component_name, amount):
        """
        Improve representation quality for a component
        
        Args:
            component_name: Component to improve
            amount: Amount to improve by
        """
        # Update component-specific quality
        if component_name in self.representation_quality['by_component']:
            current = self.representation_quality['by_component'][component_name]
            self.representation_quality['by_component'][component_name] = min(1.0, current + amount)
        
        # Update overall quality (average of components)
        total = sum(self.representation_quality['by_component'].values())
        count = len(self.representation_quality['by_component'])
        if count > 0:
            self.representation_quality['overall'] = total / count
    
    def _improve_meta_capability(self, capability, amount):
        """
        Improve a meta-cognitive capability
        
        Args:
            capability: Capability to improve
            amount: Amount to improve by
        """
        if capability in self.meta_capabilities:
            current = self.meta_capabilities[capability]
            
            # Apply improvement with diminishing returns
            self.meta_capabilities[capability] = min(
                1.0, 
                current + (amount * (1.0 - current))
            )
            
            # If abstraction improves, improve coherence
            if capability == 'abstraction' and amount > 0:
                self.representation_quality['coherence'] = min(
                    1.0, 
                    self.representation_quality['coherence'] + (amount * 0.5)
                )
    
    def consolidate_self_model(self):
        """
        Consolidate and evolve the self-model based on accumulated references
        
        Returns:
            dict: Consolidation results
        """
        # Store current model state before changes
        previous_model = {
            'overall_quality': self.representation_quality['overall'],
            'coherence': self.representation_quality['coherence'],
            'abstraction': self.representation_quality['abstraction']
        }
        
        # Count references by component
        component_references = defaultdict(int)
        
        # Analyze recent self-references
        recent_count = min(30, len(self.self_references))
        if recent_count > 0:
            recent_refs = self.self_references[-recent_count:]
            
            # Count references by target type
            for ref in recent_refs:
                target = ref['target_type']
                component_references[target] += 1
        
        # Improve representation for frequently referenced components
        for component, count in component_references.items():
            if count > 1:
                # Larger improvements for more frequent references
                improvement = 0.01 * math.log(1 + count)
                self._improve_representation(component, improvement)
        
        # Improve abstraction based on reference depth
        depth_2_count = self.reference_counts['depth_2']
        depth_3_count = self.reference_counts['depth_3+']
        
        if depth_2_count + depth_3_count > 0:
            # Higher depths contribute more to abstraction
            abstraction_improvement = 0.005 * (depth_2_count + 2 * depth_3_count)
            self._improve_meta_capability('abstraction', abstraction_improvement)
            self.representation_quality['abstraction'] = min(
                1.0, 
                self.representation_quality['abstraction'] + abstraction_improvement
            )
        
        # Calculate coherence based on component representation balance
        if self.representation_quality['by_component']:
            values = list(self.representation_quality['by_component'].values())
            mean = sum(values) / len(values)
            
            # Calculate standard deviation
            variance = sum((x - mean) ** 2 for x in values) / len(values)
            std_dev = math.sqrt(variance)
            
            # Higher coherence when representation is more balanced
            coherence = 1.0 - min(1.0, std_dev * 2)
            self.representation_quality['coherence'] = coherence
            
            # Update overall state
            self.self_model['states']['coherence'] = coherence
            
            # Calculate complexity based on number and quality of representations
            complexity = min(1.0, (len(values) / 10) * (mean + 0.2))
            self.self_model['states']['complexity'] = complexity
        
        # Record model evolution
        self.model_evolution.append({
            'timestamp': time.time(),
            'overall_quality': self.representation_quality['overall'],
            'coherence': self.representation_quality['coherence'],
            'abstraction': self.representation_quality['abstraction'],
            'max_depth': self.max_depth_achieved
        })
        
        # Calculate improvements
        improvements = {
            'overall_quality': self.representation_quality['overall'] - previous_model['overall_quality'],
            'coherence': self.representation_quality['coherence'] - previous_model['coherence'],
            'abstraction': self.representation_quality['abstraction'] - previous_model['abstraction']
        }
        
        # Update overall state based on quality
        quality = self.representation_quality['overall']
        if quality < 0.2:
            state = 'primitive'
        elif quality < 0.4:
            state = 'developing'
        elif quality < 0.6:
            state = 'functional'
        elif quality < 0.8:
            state = 'refined'
        else:
            state = 'advanced'
            
        self.self_model['states']['overall'] = state
        
        return {
            'improvements': improvements,
            'reference_counts': self.reference_counts.copy(),
            'max_depth': self.max_depth_achieved,
            'model_state': state
        }
    
    def get_self_model(self):
        """
        Get the current self-model
        
        Returns:
            dict: Current self-model
        """
        return self.self_model.copy()
    
    def get_recent_references(self, count=10):
        """
        Get most recent self-references
        
        Args:
            count: Number of references to retrieve
            
        Returns:
            list: Recent self-references
        """
        return self.self_references[-count:]
    
    def get_reference_statistics(self):
        """
        Get statistics about self-references
        
        Returns:
            dict: Reference statistics
        """
        return {
            'total': len(self.self_references),
            'by_depth': self.reference_counts.copy(),
            'max_depth': self.max_depth_achieved
        }
    
    def get_representation_quality(self):
        """
        Get representation quality metrics
        
        Returns:
            dict: Representation quality
        """
        return self.representation_quality.copy()
    
    def get_meta_capabilities(self):
        """
        Get meta-cognitive capabilities
        
        Returns:
            dict: Meta-cognitive capabilities
        """
        return self.meta_capabilities.copy()
    
    def get_model_evolution(self):
        """
        Get history of model evolution
        
        Returns:
            list: Model evolution history
        """
        return self.model_evolution.copy()
    
    def detect_recursive_patterns(self):
        """
        Analyze self-references to detect recurring patterns
        
        Returns:
            list: Detected patterns
        """
        patterns = []
        
        # Need sufficient history
        if len(self.self_references) < 10:
            return patterns
        
        # Extract the latest reference chains
        chains = []
        current_chain = []
        
        for ref in self.self_references[-50:]:  # Analyze the last 50 references
            if not current_chain:
                current_chain.append(ref)
            elif ref['timestamp'] - current_chain[-1]['timestamp'] < 1.0:
                # Add to current chain if within 1 second
                current_chain.append(ref)
            else:
                # Start new chain
                if len(current_chain) > 1:
                    chains.append(current_chain)
                current_chain = [ref]
        
        # Add the final chain if not empty
        if len(current_chain) > 1:
            chains.append(current_chain)
        
        # Analyze chains for patterns
        for chain in chains:
            if len(chain) < 2:
                continue
                
            # Look for cycles (A->B->A)
            sources = [ref['source_type'] for ref in chain]
            targets = [ref['target_type'] for ref in chain]
            
            # Check for source-target cycles
            for i in range(len(chain) - 1):
                if sources[i] == targets[i+1] and targets[i] == sources[i+1]:
                    patterns.append({
                        'type': 'cycle',
                        'components': [sources[i], targets[i]],
                        'references': [chain[i]['id'], chain[i+1]['id']],
                        'depth': max(chain[i]['depth'], chain[i+1]['depth'])
                    })
            
            # Check for depth increases
            depths = [ref['depth'] for ref in chain]
            increasing = True
            for i in range(len(depths) - 1):
                if depths[i+1] <= depths[i]:
                    increasing = False
                    break
                    
            if increasing and len(chain) >= 3:
                patterns.append({
                    'type': 'increasing_depth',
                    'start_depth': depths[0],
                    'end_depth': depths[-1],
                    'length': len(chain)
                })
                
        return patterns
    
    def reference_quality_score(self, min_references=10):
        """
        Calculate overall quality score for self-reference capability
        
        Args:
            min_references: Minimum references needed for accurate score
            
        Returns:
            float: Quality score (0-1)
        """
        if len(self.self_references) < min_references:
            return 0.3  # Base score for early development
            
        # Calculate based on multiple factors
        depth_score = min(1.0, self.max_depth_achieved * 0.25)
        volume_score = min(1.0, len(self.self_references) / 100)
        quality_score = self.representation_quality['overall']
        coherence_score = self.representation_quality['coherence']
        abstraction_score = self.representation_quality['abstraction']
        
        # Weighted average
        return (depth_score * 0.3 + 
                volume_score * 0.1 + 
                quality_score * 0.2 + 
                coherence_score * 0.2 + 
                abstraction_score * 0.2)