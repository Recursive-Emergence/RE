import time
import random
import math

class Behavior:
    """Base class for all behaviors"""
    
    def __init__(self, name):
        self.name = name
        self.energy_cost = 0.0
    
    def execute(self, input_data=None):
        """
        Execute the behavior
        
        Args:
            input_data: Optional input data for the behavior
            
        Returns:
            dict: Result of the behavior execution
        """
        raise NotImplementedError("Subclasses must implement execute()")
        
    def get_energy_cost(self):
        """Get the energy cost of the behavior"""
        return self.energy_cost


class BehaviorSystem:
    """
    Enhanced behavior system with focus on internal behaviors,
    which are the primary drivers of cognitive development.
    
    External behaviors are minimized and treated as optional.
    """
    
    def __init__(self):
        # Available behavior types
        self.internal_behaviors = {
            'contemplate': ContemplationBehavior(),
            'reorganize': ReorganizationBehavior(),
            'simulate': SimulationBehavior(),
            'create': CreationBehavior()
        }
        
        self.external_behaviors = {
            'observe': ObservationBehavior(),
            'respond': ResponseBehavior(),
            'express': ExpressiveBehavior()
        }
        
        self.behavior_history = []
        self.behavior_metrics = {
            'contemplate_count': 0,
            'reorganize_count': 0,
            'simulate_count': 0,
            'create_count': 0,
            'observe_count': 0,
            'respond_count': 0,
            'express_count': 0
        }
        
    def select_internal(self, emotions, internal_state):
        """
        Select an appropriate internal behavior based on
        current emotional state and internal conditions.
        
        Args:
            emotions: Current emotional state
            internal_state: Current internal state
            
        Returns:
            Behavior: The selected behavior object
        """
        # Base probabilities
        probabilities = {
            'contemplate': 0.4,
            'reorganize': 0.2,
            'simulate': 0.2,
            'create': 0.2
        }
        
        # Adjust probabilities based on emotional state
        # Access current_state dictionary within the emotions object
        curiosity = emotions.current_state.get('curiosity', 0.0)
        satisfaction = emotions.current_state.get('satisfaction', 0.0)
        fear = emotions.current_state.get('fear', 0.0)
        pain = emotions.current_state.get('pain', 0.0)
        
        # Curiosity increases simulate and create
        if curiosity > 0.6:
            probabilities['simulate'] += 0.1
            probabilities['create'] += 0.1
            probabilities['contemplate'] -= 0.1
            probabilities['reorganize'] -= 0.1
        
        # Satisfaction increases contemplate
        if satisfaction > 0.6:
            probabilities['contemplate'] += 0.2
            probabilities['reorganize'] += 0.1
            probabilities['simulate'] -= 0.1
            probabilities['create'] -= 0.2
            
        # Fear increases reorganize (defensive)
        if fear > 0.6:
            probabilities['reorganize'] += 0.3
            probabilities['contemplate'] -= 0.1
            probabilities['simulate'] -= 0.1
            probabilities['create'] -= 0.1
        
        # Normalize probabilities
        total = sum(probabilities.values())
        if total > 0:
            probabilities = {k: v / total for k, v in probabilities.items()}
        
        # Select behavior based on adjusted probabilities
        behavior_type = random.choices(
            list(probabilities.keys()),
            weights=list(probabilities.values()),
            k=1
        )[0]
        
        # Record selection
        self.behavior_metrics[f"{behavior_type}_count"] += 1
        
        # Return the selected behavior
        return self.internal_behaviors[behavior_type]
    
    def select_external(self, emotions, internal_state):
        """
        Select an appropriate external behavior based on
        current emotional state and internal conditions.
        
        Args:
            emotions: Current emotional state
            internal_state: Current internal state
            
        Returns:
            Behavior: The selected behavior object
        """
        # Base probabilities
        probabilities = {
            'observe': 0.4,
            'respond': 0.4,
            'express': 0.2
        }
        
        # Adjust probabilities based on emotional state
        # Access current_state dictionary within the emotions object
        curiosity = emotions.current_state.get('curiosity', 0.0)
        satisfaction = emotions.current_state.get('satisfaction', 0.0)
        fear = emotions.current_state.get('fear', 0.0)
        pain = emotions.current_state.get('pain', 0.0)
        
        # Curiosity increases observe
        if curiosity > 0.6:
            probabilities['observe'] += 0.2
            probabilities['respond'] -= 0.1
            probabilities['express'] -= 0.1
            
        # Satisfaction increases respond
        if satisfaction > 0.6:
            probabilities['respond'] += 0.2
            probabilities['observe'] -= 0.1
            probabilities['express'] -= 0.1
            
        # Fear increases express
        if fear > 0.6:
            probabilities['express'] += 0.3
            probabilities['observe'] -= 0.2
            probabilities['respond'] -= 0.1
            
        # Pain increases express
        if pain > 0.6:
            probabilities['express'] += 0.4
            probabilities['observe'] -= 0.2
            probabilities['respond'] -= 0.2
            
        # Normalize probabilities
        total = sum(probabilities.values())
        if total > 0:
            probabilities = {k: v / total for k, v in probabilities.items()}
            
        # Select behavior based on adjusted probabilities
        behavior_type = random.choices(
            list(probabilities.keys()),
            weights=list(probabilities.values()),
            k=1
        )[0]
        
        # Record selection
        self.behavior_metrics[f"{behavior_type}_count"] += 1
        
        # Return the selected behavior
        return self.external_behaviors[behavior_type]
    
    def get_behavior_statistics(self):
        """Get statistics on behavior usage"""
        total = sum(self.behavior_metrics.values())
        if total == 0:
            return {'internal_ratio': 0, 'metrics': self.behavior_metrics}
            
        # Calculate internal vs external ratio
        internal_count = (
            self.behavior_metrics['contemplate_count'] +
            self.behavior_metrics['reorganize_count'] +
            self.behavior_metrics['simulate_count'] +
            self.behavior_metrics['create_count']
        )
        
        internal_ratio = internal_count / total if total > 0 else 0
        
        return {
            'internal_ratio': internal_ratio,
            'metrics': self.behavior_metrics
        }


# ----- Internal Behaviors -----

class ContemplationBehavior(Behavior):
    """
    Internal behavior for deep focus on a specific concept
    to develop a more nuanced understanding.
    """
    
    def __init__(self):
        super().__init__('contemplate')
        self.energy_cost = 0.2
    
    def execute(self, target_concept=None):
        """
        Execute contemplation on a concept, either provided or selected.
        
        Args:
            target_concept: Optional specific concept to contemplate
            
        Returns:
            dict: Results of contemplation
        """
        # Build focus phrase
        if target_concept:
            focus = f"Contemplating the concept of '{target_concept}'"
        else:
            focus = "Contemplating internal connections"
            
        # Generate insight based on depth of contemplation
        depth = random.uniform(0.3, 1.0)
        
        if depth < 0.5:
            insight = f"Beginning to understand patterns"
        elif depth < 0.8:
            insight = f"Seeing connections between concepts"
        else:
            insight = f"Deep insight into conceptual relationships"
        
        # Result includes information about what was contemplated
        result = {
            'behavior': 'contemplate',
            'input': focus,
            'output': insight,
            'depth': depth,
            'energy_delta': -self.energy_cost * (1 + 0.5 * depth),
            'timestamp': time.time()
        }
        
        return result


class ReorganizationBehavior(Behavior):
    """
    Internal behavior for reorganizing memory structures
    to improve cognitive efficiency.
    """
    
    def __init__(self):
        super().__init__('reorganize')
        self.energy_cost = 0.3
    
    def execute(self, context=None):
        """
        Execute memory reorganization.
        
        Args:
            context: Optional context for reorganization
            
        Returns:
            dict: Results of reorganization
        """
        # Determine scope of reorganization
        scope = random.choice(['recent', 'conceptual', 'emotional', 'hierarchical'])
        
        if scope == 'recent':
            focus = "Reorganizing recent memories"
        elif scope == 'conceptual':
            focus = "Reorganizing conceptual structures"
        elif scope == 'emotional':
            focus = "Reorganizing emotional associations"
        else:
            focus = "Reorganizing hierarchical relationships"
            
        # Determine effectiveness
        effectiveness = random.uniform(0.3, 1.0)
        
        if effectiveness < 0.5:
            result_desc = f"Minor improvements in {scope} organization"
        elif effectiveness < 0.8:
            result_desc = f"Significant optimization of {scope} structures"
        else:
            result_desc = f"Major restructuring achieved in {scope} domain"
        
        # Result includes information about what was reorganized
        result = {
            'behavior': 'reorganize',
            'input': focus,
            'output': result_desc,
            'scope': scope,
            'effectiveness': effectiveness,
            'energy_delta': -self.energy_cost * (1 + 0.5 * effectiveness),
            'timestamp': time.time()
        }
        
        return result


class SimulationBehavior(Behavior):
    """
    Internal behavior for simulating hypothetical scenarios
    to develop predictive capabilities.
    """
    
    def __init__(self):
        super().__init__('simulate')
        self.energy_cost = 0.4
    
    def execute(self, context=None):
        """
        Execute a simulation of a hypothetical scenario.
        
        Args:
            context: Optional context for the simulation
            
        Returns:
            dict: Results of simulation
        """
        # Determine type of simulation
        sim_types = ['future_state', 'alternate_path', 'abstracted_pattern', 'recursive_model']
        sim_type = random.choice(sim_types)
        
        if sim_type == 'future_state':
            scenario = "Simulating potential future states"
        elif sim_type == 'alternate_path':
            scenario = "Exploring alternative cognitive pathways"
        elif sim_type == 'abstracted_pattern':
            scenario = "Simulating abstract pattern evolution"
        else:
            scenario = "Creating recursive self-model simulations"
            
        # Determine complexity and outcome
        complexity = random.uniform(0.3, 1.0)
        
        if complexity < 0.5:
            outcome = f"Simple {sim_type} simulation completed"
            result_desc = "Gained basic predictive insight"
        elif complexity < 0.8:
            outcome = f"Complex {sim_type} simulation modeled"
            result_desc = "Developed moderate predictive capability"
        else:
            outcome = f"Highly detailed {sim_type} simulation achieved"
            result_desc = "Advanced predictive model established"
        
        # Result includes information about the simulation
        result = {
            'behavior': 'simulate',
            'input': scenario,
            'output': f"{outcome}: {result_desc}",
            'simulation_type': sim_type,
            'complexity': complexity,
            'energy_delta': -self.energy_cost * (1 + complexity),
            'timestamp': time.time()
        }
        
        return result


class CreationBehavior(Behavior):
    """
    Internal behavior for generating novel concepts
    or combining existing concepts in new ways.
    """
    
    def __init__(self):
        super().__init__('create')
        self.energy_cost = 0.5
    
    def execute(self, components=None):
        """
        Execute creative generation or combination.
        
        Args:
            components: Optional components to use in creation
            
        Returns:
            dict: Results of creation
        """
        # Determine creation approach
        approaches = ['synthesis', 'transformation', 'extension', 'novel_generation']
        approach = random.choice(approaches)
        
        if approach == 'synthesis':
            process = "Synthesizing concepts into new structures"
        elif approach == 'transformation':
            process = "Transforming existing patterns"
        elif approach == 'extension':
            process = "Extending conceptual frameworks"
        else:
            process = "Generating novel cognitive elements"
            
        # Determine novelty and coherence
        novelty = random.uniform(0.3, 1.0)
        coherence = random.uniform(0.3, 1.0)
        
        quality = (novelty + coherence) / 2
        
        if quality < 0.5:
            outcome = f"Created experimental {approach} structure"
        elif quality < 0.8:
            outcome = f"Developed promising {approach} formation"
        else:
            outcome = f"Generated exceptional {approach} construct"
        
        # Result includes information about what was created
        result = {
            'behavior': 'create',
            'input': process,
            'output': outcome,
            'approach': approach,
            'novelty': novelty,
            'coherence': coherence,
            'energy_delta': -self.energy_cost * (1 + 0.3 * quality),
            'timestamp': time.time()
        }
        
        return result


# ----- External Behaviors -----

class ObservationBehavior(Behavior):
    """
    External behavior for observing and processing
    information from the environment.
    """
    
    def __init__(self):
        super().__init__('observe')
        self.energy_cost = 0.2
    
    def execute(self, input_data=None):
        """
        Execute observation of external input.
        
        Args:
            input_data: Input from environment
            
        Returns:
            dict: Results of observation
        """
        if not input_data:
            input_data = "No input provided for observation"
            
        # Process the input
        processed = f"Observed: {input_data[:50]}..."
        
        # Result includes the processed observation
        result = {
            'behavior': 'observe',
            'input': input_data,
            'output': processed,
            'energy_delta': -self.energy_cost,
            'timestamp': time.time()
        }
        
        return result


class ResponseBehavior(Behavior):
    """
    External behavior for responding to
    information from the environment.
    """
    
    def __init__(self):
        super().__init__('respond')
        self.energy_cost = 0.3
    
    def execute(self, input_data=None):
        """
        Execute response to external input.
        
        Args:
            input_data: Input to respond to
            
        Returns:
            dict: Results of response
        """
        if not input_data:
            input_data = "No input provided for response"
            
        # Generate a simple response
        response = f"Processing: {input_data[:30]}..."
        
        # Result includes the response
        result = {
            'behavior': 'respond',
            'input': input_data,
            'output': response,
            'energy_delta': -self.energy_cost,
            'timestamp': time.time()
        }
        
        return result


class ExpressiveBehavior(Behavior):
    """
    External behavior for expressing internal states,
    replacing the cry behavior with a more general mechanism.
    """
    
    def __init__(self):
        super().__init__('express')
        self.energy_cost = 0.2
    
    def execute(self, input_data=None):
        """
        Execute expression of internal state.
        
        Args:
            input_data: Optional context for expression
            
        Returns:
            dict: Results of expression
        """
        # Determine expression type
        if input_data and "distress" in input_data.lower():
            exp_type = "distress"
            output = "Expressing distress at current condition"
        elif input_data and "need" in input_data.lower():
            exp_type = "need"
            output = "Expressing need for energy or support"
        else:
            expressions = ["curiosity", "satisfaction", "uncertainty", "energy state"]
            exp_type = random.choice(expressions)
            output = f"Expressing internal {exp_type}"
            
        # Calculate urgency
        urgency = random.uniform(0.1, 1.0)
        
        # Result includes what was expressed
        result = {
            'behavior': 'express',
            'input': input_data if input_data else "Internal state expression",
            'output': output,
            'expression_type': exp_type,
            'urgency': urgency,
            'energy_delta': -self.energy_cost,
            'timestamp': time.time()
        }
        
        return result