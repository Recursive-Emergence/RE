\
import time
import math

class EntropySystem:
    """
    Manages the calculation of internal system entropy based on memory,
    concept graph structure, and emotional state. Drives behavior based
    on entropy levels, reflecting the system's internal disorder and
    need for structure.
    """

    def __init__(self, alpha=0.4, beta=0.3, gamma=0.3):
        """
        Initializes the EntropySystem.

        Args:
            alpha: Weight for memory reuse factor.
            beta: Weight for graph sparsity factor.
            gamma: Weight for emotional deviation factor.
        """
        self.current_entropy = 0.0  # Start with zero entropy
        self.entropy_history = []   # Track entropy over time

        # Weights for entropy components (ensure they sum to 1 or normalize)
        total_weight = alpha + beta + gamma
        self.alpha = alpha / total_weight
        self.beta = beta / total_weight
        self.gamma = gamma / total_weight

        self.last_calculation_time = time.time()

    def compute_entropy(self, memory_system, emotional_system):
        """
        Computes the current internal entropy H_self(t).

        H_self(t) = α * (1 - memory reuse ratio) +
                    β * (graph sparsity) +
                    γ * (emotional equilibrium deviation)

        Args:
            memory_system: The MemorySystem instance.
            emotional_system: The EmotionalSystem instance.

        Returns:
            float: The calculated system entropy (typically 0.0 to 1.0+).
        """
        # 1. Memory Reuse Ratio
        # Needs MemorySystem to provide this metric
        reuse_ratio = memory_system.calculate_memory_reuse_ratio()
        memory_factor = 1.0 - reuse_ratio # Higher entropy if less reuse

        # 2. Graph Sparsity
        # Needs MemorySystem (concept graph part) to provide this
        graph_sparsity = memory_system.calculate_graph_sparsity() # 1 - avg degree / max possible degree?

        # 3. Emotional Equilibrium Deviation
        # Needs EmotionalSystem to provide this
        emotional_deviation = emotional_system.calculate_equilibrium_deviation()

        # Combine factors using weights
        entropy = (self.alpha * memory_factor +
                   self.beta * graph_sparsity +
                   self.gamma * emotional_deviation)

        # Ensure entropy is non-negative
        self.current_entropy = max(0.0, entropy)

        # Record history
        self.entropy_history.append({
            'timestamp': time.time(),
            'entropy': self.current_entropy,
            'factors': {
                'memory_factor': memory_factor,
                'graph_sparsity': graph_sparsity,
                'emotional_deviation': emotional_deviation
            }
        })
        # Limit history size (optional)
        if len(self.entropy_history) > 500:
            self.entropy_history.pop(0)

        self.last_calculation_time = time.time()
        return self.current_entropy

    def get_status(self):
        """
        Returns the current status of the entropy system.
        """
        return {
            'current_entropy': self.current_entropy,
            'last_calculation_time': self.last_calculation_time,
            'weights': {'alpha': self.alpha, 'beta': self.beta, 'gamma': self.gamma}
        }

    def get_history(self):
        """
        Returns the historical entropy data.
        """
        return self.entropy_history.copy()

# --- Helper methods needed in other systems ---
# These methods would need to be implemented in the respective system classes

class MemorySystem: # Example additions needed
    # ... existing methods ...

    def calculate_memory_reuse_ratio(self):
        """Calculates the ratio of reused concepts/experiences recently."""
        # Placeholder logic: Needs actual tracking of reuse
        # Example: (# repeated concepts in last N experiences) / N
        # Or: (Sum of reuse_count for recent experiences) / (Total concepts accessed recently)
        # For MVP, could be simpler:
        if not hasattr(self, 'metrics') or self.metrics['total_experiences'] == 0:
             return 0.0 # Avoid division by zero, assume no reuse initially
        
        # Example: Track total accesses vs unique accesses
        total_accesses = self.metrics.get('total_concept_accesses', 0)
        unique_accesses = len(self.metrics.get('unique_concepts_accessed', set()))
        
        if total_accesses == 0:
            return 0.0 # No accesses yet
        if total_accesses == unique_accesses:
             return 0.0 # All unique, no reuse

        # Ratio of non-unique accesses to total accesses
        reuse_count = total_accesses - unique_accesses
        return reuse_count / total_accesses if total_accesses > 0 else 0.0


    def calculate_graph_sparsity(self):
        """Calculates the sparsity of the concept graph."""
        # Placeholder logic: Needs actual graph analysis
        # Sparsity = 1 - density
        # Density = 2 * num_edges / (num_nodes * (num_nodes - 1))
        num_nodes = len(self.concept_graph['nodes'])
        num_edges = len(self.concept_graph['edges'])

        if num_nodes < 2:
            return 1.0 # Max sparsity if less than 2 nodes

        max_possible_edges = num_nodes * (num_nodes - 1)
        if max_possible_edges == 0:
             return 1.0 # Avoid division by zero

        density = (2.0 * num_edges) / max_possible_edges
        sparsity = 1.0 - density
        return max(0.0, min(1.0, sparsity)) # Clamp between 0 and 1

class EmotionalSystem: # Example additions needed
    # ... existing methods ...

    def calculate_equilibrium_deviation(self):
        """Calculates the deviation from an emotional equilibrium state."""
        # Placeholder logic: Needs definition of equilibrium
        # Example: Equilibrium = all emotions at 0.5 or some baseline
        # Calculate standard deviation from this baseline
        equilibrium_point = 0.5 # Example baseline
        emotion_values = [
            self.current_state.get('curiosity', 0.0),
            self.current_state.get('satisfaction', 0.0),
            self.current_state.get('fear', 0.0),
            self.current_state.get('pain', 0.0)
        ]

        if not emotion_values:
            return 0.0

        mean_deviation = sum(abs(e - equilibrium_point) for e in emotion_values) / len(emotion_values)
        
        # Alternative: Standard Deviation
        # mean = sum(emotion_values) / len(emotion_values)
        # variance = sum((e - mean) ** 2 for e in emotion_values) / len(emotion_values)
        # std_dev = math.sqrt(variance)
        # Normalize std_dev to 0-1 range (e.g. max possible std dev depends on emotion range)
        
        # Using mean absolute deviation from equilibrium, normalized assuming max deviation is 0.5 per emotion
        # Max possible mean deviation is 0.5 if all are 0 or 1.
        normalized_deviation = mean_deviation / 0.5 
        
        return max(0.0, min(1.0, normalized_deviation)) # Clamp between 0 and 1

    def update(self, entropy_value, memory_system):
         """
         Update emotional state based on current entropy and memory context.
         (Signature changed from taking energy to entropy)
         """
         # Existing logic needs refactoring to use entropy triggers
         # Example trigger logic based on prompt:
         entropy_change = entropy_value - self.previous_entropy if hasattr(self, 'previous_entropy') else 0

         if entropy_change > 0.1: # Sharp rise
             self.current_state['fear'] = min(1.0, self.current_state.get('fear', 0.0) + 0.2)
         elif entropy_value > 0.7 and entropy_change > 0.01: # Mild growth in high entropy state
             self.current_state['curiosity'] = min(1.0, self.current_state.get('curiosity', 0.0) + 0.1)
         elif entropy_change < -0.05: # Entropy recently dropped
             self.current_state['satisfaction'] = min(1.0, self.current_state.get('satisfaction', 0.0) + 0.15)
         elif entropy_value > 0.85: # Prolonged high entropy
             self.current_state['pain'] = min(1.0, self.current_state.get('pain', 0.0) + 0.1)

         # Add decay/momentum logic as before
         # ...

         self.previous_entropy = entropy_value # Store for next cycle's change calculation
         # ... rest of update logic ...

