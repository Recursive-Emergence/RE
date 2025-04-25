#!/usr/bin/env python3
"""
Environment module for Life Origins Simulation.

This module implements the environmental conditions that affect chemical reactions
and compartment formation in the simulation, including temperature, pH,
wet-dry cycles, and energy input rates.
"""

import random
import math
import numpy as np
from collections import defaultdict

class Environment:
    """
    Represents the physical and chemical environment for the simulation.
    Controls temperature, pH, wet-dry cycles, and other conditions.
    """
    
    def __init__(self):
        """Initialize the environment with default parameters."""
        # Physical parameters
        self.temperature = 85.0       # Temperature in Celsius
        self.temperature_K = 273.15 + self.temperature  # Temperature in Kelvin
        self.ph = 8.0                 # pH value
        self.uv_intensity = 0.2       # UV radiation intensity (0-1)
        self.wet_dry_cycle = True     # Whether wet-dry cycles are active
        self.wet_phase = 1.0          # Current phase of wet-dry cycle (0=dry, 1=wet)
        self.cycle_period = 20        # Steps per full wet-dry cycle
        self.metal_catalysts = False  # Presence of metal catalysts
        
        # Energy parameters
        self.energy_input = "medium"  # Energy input level
        self.energy_input_rates = {   # Energy input multipliers
            "very_low": 0.2,
            "low": 0.5,
            "medium": 1.0,
            "high": 2.0,
            "very_high": 5.0
        }
        
        # Advanced parameters
        self.temperature_gradient = False  # Whether temperature gradient is present
        self.temperature_range = 10.0      # Range of temperature gradient
        self.concentrated = False          # Whether reactants are concentrated
        self.concentration_factor = 1.0    # Factor for concentration
        
        # Tracking history
        self.time_step = 0
        self.history = defaultdict(list)
        
        # Environment type
        self.environment_type = "prebiotic_ocean"
        
        # Constraint level (1-5, with 5 being most constrained)
        self.constraint_level = 3
    
    def update(self):
        """Update the environment for the current time step."""
        self.time_step += 1
        
        # Update wet-dry cycle if enabled
        if self.wet_dry_cycle:
            self._update_wet_dry_cycle()
            
        # Update temperature with small fluctuations
        self._update_temperature()
        
        # Update history
        self._update_history()
    
    def _update_wet_dry_cycle(self):
        """Update the wet-dry cycle phase."""
        if self.cycle_period > 0:
            cycle_position = self.time_step % self.cycle_period
            cycle_fraction = cycle_position / self.cycle_period
            
            # Use a cosine wave to model wet-dry cycles
            self.wet_phase = 0.5 + 0.5 * math.cos(cycle_fraction * 2 * math.pi)
    
    def _update_temperature(self):
        """Update temperature with small random fluctuations."""
        # Add small random fluctuations to temperature
        fluctuation = random.uniform(-0.5, 0.5)
        self.temperature += fluctuation
        self.temperature_K = 273.15 + self.temperature
        
        # Add temperature gradient effects if enabled
        if self.temperature_gradient:
            # Not implemented in this simplified version
            pass
    
    def _update_history(self):
        """Update the history tracking data."""
        self.history['temperature'].append(self.temperature)
        self.history['ph'].append(self.ph)
        self.history['uv_intensity'].append(self.uv_intensity)
        self.history['wet_phase'].append(self.wet_phase)
        
        # Energy input rate based on current setting
        energy_rate = self.energy_input_rates.get(self.energy_input, 1.0)
        self.history['energy_input'].append(energy_rate)
    
    def affect_reaction(self, reaction):
        """
        Calculate how the environment affects a specific reaction's rate.
        
        Args:
            reaction: Reaction object to evaluate
            
        Returns:
            float: Multiplier for reaction rate due to environmental factors
        """
        # Base multiplier starts at 1.0
        rate_multiplier = 1.0
        
        # Temperature effects (simple Arrhenius-like effect)
        # Higher temperatures generally speed up reactions
        temp_factor = 1.0 + (self.temperature - 85) / 100
        rate_multiplier *= max(0.1, min(3.0, temp_factor))
        
        # pH effects (reactions work best at specific pH values)
        # Assume most prebiotic reactions work best at slightly alkaline pH
        optimal_ph = getattr(reaction, 'optimal_ph', 8.0)
        ph_diff = abs(self.ph - optimal_ph)
        ph_factor = 1.0 - (ph_diff / 10.0)  # Linear decrease with pH difference
        rate_multiplier *= max(0.1, min(1.0, ph_factor))
        
        # Wet-dry cycle effects
        if self.wet_dry_cycle:
            # Different reactions prefer different wetness levels
            prefers_wet = getattr(reaction, 'prefers_wet', True)
            if prefers_wet:
                # Reactions that need water work better in wet conditions
                rate_multiplier *= 0.2 + 0.8 * self.wet_phase
            else:
                # Condensation reactions work better in dry conditions
                rate_multiplier *= 0.2 + 0.8 * (1.0 - self.wet_phase)
        
        # Energy input effects
        energy_factor = self.energy_input_rates.get(self.energy_input, 1.0)
        rate_multiplier *= energy_factor
        
        # Metal catalyst effects
        if self.metal_catalysts and getattr(reaction, 'metal_catalyzed', False):
            rate_multiplier *= 3.0  # Strong boost for reactions catalyzed by metals
        
        # Concentration effects
        if self.concentrated:
            rate_multiplier *= self.concentration_factor
        
        return rate_multiplier
    
    def get_visualization_data(self):
        """Get data for visualization purposes."""
        return {
            'type': self.environment_type,
            'temperature': self.temperature,
            'ph': self.ph,
            'uv': self.uv_intensity,
            'is_wet': self.wet_phase > 0.5,
            'wet_phase': self.wet_phase,
            'energy_input': self.energy_input,
            'constraint_level': self.constraint_level,
            'metal_catalysts': self.metal_catalysts,
            'gradient': self.temperature_gradient
        }
    
    def reset(self):
        """Reset the environment to initial state."""
        self.time_step = 0
        self.history = defaultdict(list)
    
    def set_environment_type(self, env_type):
        """
        Set the environment type to one of the predefined types.
        
        Args:
            env_type (str): One of 'prebiotic_ocean', 'hydrothermal_vent', 
                           'tidal_pool', 'clay_surfaces', 'hot_spring'
        """
        self.environment_type = env_type
        
        # Set parameters based on environment type
        if env_type == 'prebiotic_ocean':
            self.temperature = 25.0
            self.ph = 8.0
            self.uv_intensity = 0.2
            self.wet_dry_cycle = False
            self.metal_catalysts = False
            self.energy_input = "low"
            
        elif env_type == 'hydrothermal_vent':
            self.temperature = 90.0
            self.ph = 5.0
            self.uv_intensity = 0.0
            self.wet_dry_cycle = False
            self.metal_catalysts = True
            self.energy_input = "high"
            
        elif env_type == 'tidal_pool':
            self.temperature = 30.0
            self.ph = 7.5
            self.uv_intensity = 0.4
            self.wet_dry_cycle = True
            self.cycle_period = 15
            self.metal_catalysts = False
            self.concentrated = True
            self.concentration_factor = 2.0
            self.energy_input = "medium"
            
        elif env_type == 'clay_surfaces':
            self.temperature = 40.0
            self.ph = 6.5
            self.uv_intensity = 0.3
            self.wet_dry_cycle = True
            self.cycle_period = 25
            self.metal_catalysts = True
            self.concentrated = True
            self.concentration_factor = 3.0
            self.energy_input = "medium"
            
        elif env_type == 'hot_spring':
            self.temperature = 70.0
            self.ph = 9.0
            self.uv_intensity = 0.5
            self.wet_dry_cycle = False
            self.metal_catalysts = True
            self.temperature_gradient = True
            self.temperature_range = 20.0
            self.energy_input = "high"
            
        # Update Kelvin temperature
        self.temperature_K = 273.15 + self.temperature

    def set_constraint_level(self, level):
        """
        Set the constraint level for the environment.
        Higher constraint levels represent more structured, constrained environments.
        
        Args:
            level (int): Constraint level from 1 (low) to 5 (high)
        """
        self.constraint_level = max(1, min(5, level))
        
        # Adjust parameters based on constraint level
        if level == 1:  # Low constraint
            self.temperature = 70.0
            self.ph = 7.0
            self.wet_dry_cycle = False
            self.energy_input = "high"
            self.metal_catalysts = False
            self.concentrated = False
            
        elif level == 2:  # Medium-low constraint
            self.temperature = 80.0
            self.ph = 7.5
            self.wet_dry_cycle = True
            self.cycle_period = 25
            self.energy_input = "medium"
            self.metal_catalysts = False
            self.concentrated = False
            
        elif level == 3:  # Medium constraint
            self.temperature = 85.0
            self.ph = 8.0
            self.wet_dry_cycle = True
            self.cycle_period = 20
            self.energy_input = "medium"
            self.metal_catalysts = True
            self.concentrated = False
            
        elif level == 4:  # Medium-high constraint
            self.temperature = 90.0
            self.ph = 8.5
            self.wet_dry_cycle = True
            self.cycle_period = 15
            self.energy_input = "low"
            self.metal_catalysts = True
            self.temperature_gradient = True
            self.concentrated = False
            
        elif level == 5:  # High constraint
            self.temperature = 95.0
            self.ph = 9.0
            self.wet_dry_cycle = True
            self.cycle_period = 10
            self.energy_input = "very_low"
            self.metal_catalysts = True
            self.temperature_gradient = True
            self.concentrated = True
            self.concentration_factor = 5.0
            
        # Update Kelvin temperature
        self.temperature_K = 273.15 + self.temperature