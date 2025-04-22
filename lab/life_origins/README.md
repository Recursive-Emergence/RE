# Life Origins Simulations

This directory contains simulations focused on testing the Recursive Emergence framework in the context of prebiotic chemistry and the origins of life.

## Overview

The core theoretical framework is described in [../appendix_life_origins.md](../appendix_life_origins.md), which explores how the chemical-to-biological transition represents the first major emergence layer in our theory.

## Key Hypothesis

Our primary research focus is testing a bidirectional feedback loop between entropy reduction and autocatalysis in chemical systems:

1. **Forward Direction**: Chemical networks require initial entropy reduction to establish self-catalytic structures.
2. **Reverse Direction**: Once formed, self-catalytic structures actively accelerate further entropy reduction.
3. **Runaway Complexity**: This creates a self-reinforcing cycle that may explain the transition to living systems.

## Simulations

### 1. Entropy-Catalysis Feedback Loop

The `entropy_catalysis_feedback.py` simulation implements a binary polymer model based on Kauffman's RAF theory to test our key hypothesis. It demonstrates how:

- Initial entropy constraints affect the emergence of autocatalytic sets
- Catalytic networks create a runaway feedback loop of increasing complexity
- The strength of this feedback can be quantified and measured

#### Running the Simulation

```bash
python entropy_catalysis_feedback.py
```

This will:
1. Run a standard simulation with visualization
2. Test how different initial entropy constraints affect emergence
3. Generate graphs showing the relationship between initial constraints and runaway complexity

#### Key Outputs

- `entropy_catalysis_metrics.png`: Shows the time evolution of key metrics
- `reaction_network.png`: Visualizes the final chemical reaction network
- `constraint_hypothesis_results.png`: Shows how different initial constraints affect outcomes

#### Metrics Tracked

- **Entropy reduction**: How much entropy is reduced by reactions in each time step
- **Catalytic activity**: Proportion of reactions that are catalyzed
- **Molecular complexity**: Average complexity of molecules in the system
- **Memory persistence**: How well catalytic patterns persist over time
- **Entropy-Catalysis Feedback Coefficient**: Correlation between entropy reduction and subsequent catalytic activity

### 2. Original Pseudocode (For Reference)

#### Basic RAF Model
```python
# Pseudocode for RAF simulation
class Molecule:
    # Structure representation
    pass

class Reaction:
    # Reactants, products, catalysts, energetics
    pass

def calculate_emergence_potential(reaction_set):
    reusability = measure_reusability(reaction_set)
    entropy_reduction = measure_entropy_reduction(reaction_set)
    return reusability * entropy_reduction

def is_RAF(reaction_set, food_set):
    # Check if:
    # 1. Every reaction is catalyzed by a molecule in the set
    # 2. All molecules can be built from food set
    pass

def simulate_chemical_evolution(steps, food_set):
    molecules = initialize_with_food(food_set)
    reactions = []
    memory = {}
    
    for step in range(steps):
        # Allow reactions to occur
        # Track which structures persist
        # Update system memory based on P(E)
        # Check for emergence of RAF sets
        
        if persistence_threshold_reached():
            print(f"Biological emergence threshold crossed at step {step}")
            
    return analyze_results()
```

#### Formose Reaction Model
```python
# Pseudocode for formose reaction simulation
def formose_simulation(formaldehyde_concentration, catalyst_type):
    molecules = initialize_with_formaldehyde(formaldehyde_concentration)
    
    # Define specific reactions in formose pathway
    # Track formation of key intermediates (glycolaldehyde, etc.)
    # Monitor emergence of autocatalytic cycles
    
    for step in range(simulation_steps):
        # Update concentrations
        # Apply reaction rules
        # Calculate entropy at each step
        # Measure reusability of products
        
    return {
        'sugar_distribution': analyze_sugars(),
        'autocatalytic_efficiency': measure_autocatalysis(),
        'emergence_potential': calculate_P_values(),
    }
```

## Future Work

1. **Formose Reaction Implementation**: Create a more chemistry-specific simulation of the formose reaction
2. **Persistence Threshold Analysis**: Quantify the exact point at which chemical networks cross into self-sustaining patterns
3. **Reaction Energy Constraints**: Add thermodynamic constraints to more realistically model prebiotic conditions
4. **Environmental Cycling**: Simulate day/night or wet/dry cycles to test their effects on emergence
5. **Memory Effects**: More sophisticated tracking of how past reactions influence future reaction probabilities