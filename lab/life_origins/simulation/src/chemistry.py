#!/usr/bin/env python3
"""
Chemistry module for Life Origins Simulation.

This module implements the chemical reactions, molecules, and processes
including compartment formation and entropy-catalysis feedback loops.
Based on previous experimental findings.
"""

import random
import math
import numpy as np
from collections import defaultdict
import networkx as nx

# Add the missing required functions

def create_prebiotic_food_set():
    """
    Create an initial set of simple prebiotic food molecules.
    
    Returns:
        list: A list of Molecule objects representing the prebiotic food set
    """
    # Create simple prebiotic molecules
    molecules = []
    
    # Simple molecules
    molecules.append(Molecule("H2O", complexity=1))          # Water
    molecules.append(Molecule("CH4", complexity=1))          # Methane
    molecules.append(Molecule("NH3", complexity=1))          # Ammonia
    molecules.append(Molecule("H2", complexity=1))           # Hydrogen
    molecules.append(Molecule("CO2", complexity=1))          # Carbon dioxide
    molecules.append(Molecule("HCN", complexity=2))          # Hydrogen cyanide
    molecules.append(Molecule("CH2O", complexity=2))         # Formaldehyde
    
    # Some slightly more complex molecules
    molecules.append(Molecule("C2H4O2", complexity=3))       # Acetic acid
    molecules.append(Molecule("C2H5NO2", complexity=5))      # Glycine (simplest amino acid)
    
    # A few amphiphilic molecules as seed for potential compartmentalization
    molecules.append(Molecule("C8H16O2", complexity=10, is_amphiphilic=True))    # Caprylic acid
    molecules.append(Molecule("C10H18O8P", complexity=15, is_amphiphilic=True))  # Basic phospholipid
    
    return molecules

# Add ChemicalNetwork class
class ChemicalNetwork:
    """Represents a network of interacting chemical molecules and reactions."""
    
    def __init__(self, food_molecules, environment):
        """
        Initialize the chemical network with food molecules and environment.
        
        Args:
            food_molecules (list): List of initial food molecules
            environment: Environment object containing conditions
        """
        self.molecules = {}  # {molecule: count}
        self.active_reactions = []
        self.all_possible_reactions = []
        self.reaction_graph = nx.DiGraph()
        self.environment = environment
        self.time_step = 0
        self.history = {
            'molecule_counts': [],
            'reaction_counts': [],
            'complexity': [],
            'energy_currency': []
        }
        
        # Add a phase display counter to control output frequency
        self.phase_display_counter = 0
        self.phase_display_interval = 100  # Only show phase messages very rarely (increased from 10 to 100)
        self.verbose = False  # Set to False to disable most output messages
        
        # Initialize with food molecules
        for molecule in food_molecules:
            self.molecules[molecule] = 100  # Start with 100 of each food molecule
            
        # Generate initial reaction network
        self._generate_initial_reactions()
        
    def _generate_initial_reactions(self):
        """Generate the initial set of possible reactions from food molecules."""
        # Simple reactions between pairs of molecules
        molecules = list(self.molecules.keys())
        
        # Basic condensation reactions (A + B -> AB)
        for i, mol_a in enumerate(molecules):
            for j, mol_b in enumerate(molecules[i:]):
                # Skip if both molecules are too large (limit combinatorial explosion)
                if len(mol_a.name) > 4 and len(mol_b.name) > 4:
                    continue
                    
                # Create a condensation product with combined name
                # This is a simplified approach - real chemistry would be more complex
                product_name = self._combine_molecule_names(mol_a.name, mol_b.name)
                
                # Calculate new complexity (more than sum of parts if it creates something meaningful)
                base_complexity = mol_a.complexity + mol_b.complexity
                product_complexity = base_complexity * random.uniform(1.0, 1.2)
                
                # Determine if product is amphiphilic
                is_amphiphilic = mol_a.is_amphiphilic or mol_b.is_amphiphilic or \
                                (len(product_name) >= 7 and random.random() < 0.2)
                
                # Create the product molecule
                product = Molecule(product_name, complexity=product_complexity, 
                                  is_amphiphilic=is_amphiphilic)
                
                # Create the reaction
                reaction = Reaction([mol_a, mol_b], [product], 
                                   rate=0.01 / (1 + base_complexity/5))
                
                # Add to possible reactions
                self.all_possible_reactions.append(reaction)
        
        # Add decomposition reactions for complex molecules
        for molecule in molecules:
            if len(molecule.name) >= 5:  # Only for more complex molecules
                # Break into random fragments
                fragments = self._decompose_molecule(molecule)
                if len(fragments) >= 2:
                    reaction = Reaction([molecule], fragments, 
                                      rate=0.005)  # Slow decomposition rate
                    self.all_possible_reactions.append(reaction)
    
    def _combine_molecule_names(self, name_a, name_b):
        """
        Combine two molecule names into a new name.
        This is a simplified approach - real chemistry would follow specific rules.
        """
        # For basic molecules, use basic chemistry rules where possible
        if name_a == "H2O" and name_b == "CO2":
            return "H2CO3"  # Carbonic acid
        elif name_a == "H2" and name_b == "N2":
            return "NH3"  # Ammonia
        elif name_a == "CH4" and name_b == "O2":
            return "CH3OH"  # Methanol
            
        # For more complex molecules, do a simplified combination
        # Remove one H from first and one from second to simulate condensation
        # This is very simplified - real reactions would be more specific
        if len(name_a) > 1 and len(name_b) > 1:
            if "H" in name_a and "H" in name_b:
                # Count elements in both molecules
                elements_a = self._count_elements(name_a)
                elements_b = self._count_elements(name_b)
                
                # Combine elements, removing one H from each to simulate condensation
                elements_a["H"] = max(0, elements_a.get("H", 0) - 1)
                elements_b["H"] = max(0, elements_b.get("H", 0) - 1)
                
                # Add an O (oxygen) to represent the new bond
                elements_a["O"] = elements_a.get("O", 0) + 1
                
                # Combine the dictionaries
                combined = defaultdict(int)
                for element, count in elements_a.items():
                    combined[element] += count
                for element, count in elements_b.items():
                    combined[element] += count
                    
                # Generate new name
                return "".join(element + (str(count) if count > 1 else "") 
                              for element, count in combined.items())
        
        # Fallback - simple concatenation
        return name_a + name_b
    
    def _count_elements(self, formula):
        """Count elements in a chemical formula (simplified)."""
        elements = defaultdict(int)
        i = 0
        while i < len(formula):
            if i < len(formula) - 1 and formula[i].isalpha() and formula[i+1].islower():
                element = formula[i:i+2]
                i += 2
            else:
                element = formula[i]
                i += 1
                
            if i < len(formula) and formula[i].isdigit():
                count = 0
                while i < len(formula) and formula[i].isdigit():
                    count = count * 10 + int(formula[i])
                    i += 1
            else:
                count = 1
                
            elements[element] += count
            
        return elements
    
    def _decompose_molecule(self, molecule):
        """
        Decompose a complex molecule into simpler fragments.
        Very simplified - real decomposition would follow chemical rules.
        """
        fragments = []
        name = molecule.name
        
        # Skip simple molecules
        if len(name) < 5:
            return fragments
            
        # Try to split into reasonable chemical fragments
        if "C" in name and "H" in name:
            # Carbon-hydrogen molecules
            if "O" in name:
                # Carbohydrates and similar
                fragments.append(Molecule("CH2O", complexity=2))  # Formaldehyde
                fragments.append(Molecule("CO2", complexity=1))  # Carbon dioxide
            else:
                # Hydrocarbons
                fragments.append(Molecule("CH4", complexity=1))  # Methane
                
        elif "N" in name:
            # Nitrogen-containing compounds
            fragments.append(Molecule("NH3", complexity=1))  # Ammonia
            
        # If we couldn't generate fragments by chemical rules, use a random approach
        if not fragments:
            complexity = molecule.complexity / 2
            fragments = [
                Molecule(f"Fragment1_{name}", complexity=complexity),
                Molecule(f"Fragment2_{name}", complexity=complexity)
            ]
            
        return fragments
        
    def update(self):
        """Update the chemical network for one time step."""
        self.time_step += 1
        
        # Only print phase message at controlled intervals for longer runs
        if (self.time_step == 1 or self.phase_display_counter >= self.phase_display_interval) and self.verbose:
            print(f"Phase: Reaction Cycles")
            self.phase_display_counter = 0
        else:
            self.phase_display_counter += 1
        
        # Update active reactions
        self._update_active_reactions()
        
        # Execute each active reaction
        new_molecules = defaultdict(int)
        consumed_molecules = defaultdict(int)
        
        for reaction in self.active_reactions:
            # Check for available reactants
            min_available = float('inf')
            for reactant in reaction.reactants:
                if reactant in self.molecules:
                    min_available = min(min_available, self.molecules[reactant])
                else:
                    min_available = 0
                    break
                    
            if min_available <= 0:
                continue
                
            # Calculate how many reactions occur based on rate and availability
            reaction_count = self._calculate_reaction_events(reaction, min_available)
            
            if reaction_count > 0:
                # Consume reactants
                for reactant in reaction.reactants:
                    consumed_molecules[reactant] += reaction_count
                    
                # Produce products
                for product in reaction.products:
                    new_molecules[product] += reaction_count
        
        # Update molecule quantities
        for molecule, count in consumed_molecules.items():
            self.molecules[molecule] -= count
            if self.molecules[molecule] <= 0:
                del self.molecules[molecule]
                
        for molecule, count in new_molecules.items():
            if molecule in self.molecules:
                self.molecules[molecule] += count
            else:
                self.molecules[molecule] = count
        
        # Update history data
        self._update_history()
        
        # Periodically check for new possible reactions based on current molecules
        if self.time_step % 10 == 0:
            self._discover_new_reactions()
    
    def _update_active_reactions(self):
        """Update the list of active reactions based on available molecules."""
        self.active_reactions = []
        
        for reaction in self.all_possible_reactions:
            # A reaction is active if all reactants are available
            if all(reactant in self.molecules and self.molecules[reactant] > 0 
                  for reactant in reaction.reactants):
                self.active_reactions.append(reaction)
    
    def _calculate_reaction_events(self, reaction, available_reactants):
        """Calculate how many reaction events occur based on rate and availability."""
        # Get the reaction rate adjusted by environment
        env_factor = self.environment.affect_reaction(reaction) if hasattr(self.environment, 'affect_reaction') else 1.0
        adjusted_rate = reaction.effective_rate * env_factor
        
        # Calculate how many reaction events actually happen
        # Based on probability and available reactants
        # Limit maximum to prevent excessive resource consumption
        max_possible = min(available_reactants, 10)
        events = 0
        
        for _ in range(max_possible):
            if random.random() < adjusted_rate:
                events += 1
                
        return events
    
    def _update_history(self):
        """Update historical data for tracking simulation progress."""
        self.history['molecule_counts'].append(len(self.molecules))
        self.history['reaction_counts'].append(len(self.active_reactions))
        
        # Calculate current complexity and energy
        avg_complexity = 0
        total_molecules = sum(self.molecules.values())
        energy_currency = 0
        
        if total_molecules > 0:
            # Average molecular complexity
            avg_complexity = sum(mol.complexity * count 
                               for mol, count in self.molecules.items()) / total_molecules
                               
            # Simplified energy currency calculation based on phosphates
            energy_currency = sum(count for mol, count in self.molecules.items() 
                                if 'P' in mol.name or mol.complexity > 10)
        
        self.history['complexity'].append(avg_complexity)
        self.history['energy_currency'].append(energy_currency)
    
    def _discover_new_reactions(self):
        """Discover new possible reactions based on current molecules."""
        # Get all current molecule types
        current_molecules = list(self.molecules.keys())
        
        # Skip if too few molecules
        if len(current_molecules) < 2:
            return
            
        # Try random combinations to discover new reactions
        samples = min(5, len(current_molecules))  # Limit combinatorial explosion
        sample_molecules = random.sample(current_molecules, samples)
        
        for i, mol_a in enumerate(sample_molecules):
            for mol_b in sample_molecules[i+1:]:
                # Skip if this exact pair already has a reaction
                if any(set(r.reactants) == {mol_a, mol_b} for r in self.all_possible_reactions):
                    continue
                    
                # Small chance to discover a new reaction
                if random.random() < 0.3:
                    product_name = self._combine_molecule_names(mol_a.name, mol_b.name)
                    
                    # Skip if this would create a molecule that's too complex
                    if len(product_name) > 15:
                        continue
                        
                    base_complexity = mol_a.complexity + mol_b.complexity
                    product_complexity = base_complexity * random.uniform(1.0, 1.3)
                    
                    # Higher complexity molecules have higher chance to be amphiphilic
                    is_amphiphilic = (mol_a.is_amphiphilic or mol_b.is_amphiphilic or 
                                     (product_complexity > 8 and random.random() < 0.3))
                    
                    product = Molecule(product_name, complexity=product_complexity,
                                      is_amphiphilic=is_amphiphilic)
                    
                    # Create new reaction with low initial rate
                    new_reaction = Reaction([mol_a, mol_b], [product], 
                                          rate=0.005 / (1 + base_complexity/10))
                    
                    self.all_possible_reactions.append(new_reaction)
    
    def get_statistics(self):
        """Get current statistics about the chemical network."""
        total_molecules = sum(self.molecules.values())
        molecule_types = len(self.molecules)
        
        # Count catalysts
        catalysts = sum(1 for reaction in self.active_reactions if reaction.is_catalyzed)
        
        # Count amphiphilic molecules
        amphiphilic = sum(count for mol, count in self.molecules.items() if mol.is_amphiphilic)
        
        # Calculate average complexity
        avg_complexity = 0
        if total_molecules > 0:
            avg_complexity = sum(mol.complexity * count 
                               for mol, count in self.molecules.items()) / total_molecules
        
        # Energy currency (simplified)
        energy_currency = self.history['energy_currency'][-1] if self.history['energy_currency'] else 0
        
        return {
            'molecules': total_molecules,
            'types': molecule_types,
            'reactions': len(self.active_reactions),
            'catalysts': catalysts,
            'amphiphilic': amphiphilic,
            'complexity': avg_complexity,
            'energy_currency': energy_currency
        }
    
    def get_final_analysis(self):
        """Get comprehensive analysis of the chemical network evolution."""
        # Calculate autocatalytic cycles (simplified)
        autocatalytic_cycles = self._detect_autocatalytic_cycles()
        
        # Calculate entropy-catalysis feedback coefficient
        feedback = self._calculate_feedback_coefficient()
        
        # Calculate complexity score based on multiple factors
        complexity_score = self._calculate_complexity_score()
        
        # Calculate information metrics
        info_metrics = self._calculate_information_metrics()
        
        return {
            'autocatalytic_cycles': autocatalytic_cycles,
            'entropy_catalysis_feedback': feedback,
            'complexity_score': complexity_score,
            'information_metrics': info_metrics
        }
    
    def _detect_autocatalytic_cycles(self):
        """Detect autocatalytic cycles in the reaction network (simplified)."""
        # Build graph of reactions
        G = nx.DiGraph()
        
        # Add edges for reactions
        for reaction in self.active_reactions:
            for reactant in reaction.reactants:
                for product in reaction.products:
                    G.add_edge(reactant.name, product.name)
        
        # Count the number of simple cycles
        try:
            cycles = list(nx.simple_cycles(G))
            # Filter to cycles that are truly autocatalytic
            autocatalytic_cycles = 0
            for cycle in cycles:
                if len(cycle) > 2:  # Only count cycles with at least 3 components
                    autocatalytic_cycles += 1
            return autocatalytic_cycles
        except:
            # Simple_cycles can fail on complex networks
            return 0
    
    def _calculate_feedback_coefficient(self):
        """Calculate entropy-catalysis feedback coefficient."""
        # Need enough history data for meaningful calculation
        if len(self.history['complexity']) < 10:
            return 0
            
        # Use last 20 time steps (or all if less than 20)
        window = min(20, len(self.history['complexity']))
        
        # Calculate change in complexity
        complexity_values = self.history['complexity'][-window:]
        complexity_change = complexity_values[-1] - complexity_values[0]
        
        # Calculate percentage of reactions that are catalyzed
        reactions = len(self.active_reactions)
        catalyzed = sum(1 for reaction in self.active_reactions if reaction.is_catalyzed)
        catalysis_ratio = catalyzed / max(1, reactions)
        
        # Feedback coefficient combines how much complexity increases with catalysis
        # A positive value means catalysis is associated with complexity increase
        feedback = 0
        if window > 1:
            # Normalize to 0-1 range
            normalized_change = min(1, max(0, complexity_change / max(0.1, complexity_values[0])))
            feedback = normalized_change * catalysis_ratio
        
        return feedback
    
    def _calculate_complexity_score(self):
        """Calculate an overall complexity score for the system."""
        # Get statistics
        stats = self.get_statistics()
        total_molecules = stats['molecules']
        
        # Avoid division by zero
        if total_molecules == 0:
            return 0
        
        # Factors that contribute to complexity:
        # 1. Average molecular complexity
        avg_complexity = stats['complexity']
        
        # 2. Network diversity (types of molecules)
        diversity = stats['types'] / max(10, total_molecules/10)  # Normalize to reasonable range
        
        # 3. Reaction network complexity
        reaction_complexity = len(self.active_reactions) / max(10, stats['types'])
        
        # 4. Presence of catalysts
        catalyst_factor = stats['catalysts'] / max(1, stats['types'])
        
        # 5. Presence of amphiphilic molecules (important for compartmentalization)
        amphiphilic_factor = stats['amphiphilic'] / max(10, total_molecules/10)
        
        # Combine factors (weighted)
        complexity_score = (
            0.3 * avg_complexity +
            0.2 * diversity +
            0.2 * reaction_complexity +
            0.2 * catalyst_factor +
            0.1 * amphiphilic_factor
        )
        
        # Scale to a more intuitive range (0-10)
        return min(10, complexity_score * 2)
    
    def _calculate_information_metrics(self):
        """Calculate information-theoretic metrics of the chemical system."""
        # This is a simplified placeholder - real calculation would be more complex
        return {
            'chemical_diversity': len(self.molecules),
            'reaction_pathways': len(self.active_reactions),
            'network_connectivity': len(self.active_reactions) / max(1, len(self.molecules))
        }

class Molecule:
    """Represents a chemical molecule in the simulation."""
    
    def __init__(self, name, complexity=1, is_amphiphilic=False, hydrophobic_strength=0.5):
        """
        Initialize a molecule.
        
        Args:
            name (str): Molecule name/identifier
            complexity (float): Measure of molecular complexity
            is_amphiphilic (bool): Whether molecule can form compartment boundaries
            hydrophobic_strength (float): Strength of hydrophobic effect (0-1), relevant for amphiphilic molecules
        """
        self.name = name
        self.complexity = complexity
        self.is_amphiphilic = is_amphiphilic
        self.hydrophobic_strength = hydrophobic_strength if is_amphiphilic else 0.0
        self.concentration = 1.0  # Default concentration
        self.position = (random.random(), random.random())  # 2D position in simulation space
        self.velocity = (random.uniform(-0.01, 0.01), random.uniform(-0.01, 0.01))
        
    def __str__(self):
        return self.name
        
    def __hash__(self):
        return hash(self.name)
        
    def __eq__(self, other):
        if isinstance(other, Molecule):
            return self.name == other.name
        return False
        
    def update_position(self, bounds=(1.0, 1.0)):
        """Update the molecule's position based on velocity."""
        x, y = self.position
        dx, dy = self.velocity
        
        # Update position
        x += dx
        y += dy
        
        # Bounce off boundaries (elastic collision)
        if x < 0:
            x = -x
            dx = -dx
        elif x > bounds[0]:
            x = 2 * bounds[0] - x
            dx = -dx
            
        if y < 0:
            y = -y
            dy = -dy
        elif y > bounds[1]:
            y = 2 * bounds[1] - y
            dy = -dy
            
        # Apply random small changes to velocity (Brownian motion)
        dx += random.uniform(-0.005, 0.005)
        dy += random.uniform(-0.005, 0.005)
        
        # Limit maximum velocity
        max_velocity = 0.05
        magnitude = math.sqrt(dx*dx + dy*dy)
        if magnitude > max_velocity:
            dx = (dx / magnitude) * max_velocity
            dy = (dy / magnitude) * max_velocity
            
        self.position = (x, y)
        self.velocity = (dx, dy)
        
    def can_catalyze(self, reaction):
        """Check if this molecule can catalyze a specific reaction."""
        # Simple rule: molecule can catalyze reactions involving similar molecules
        # based on substring matching (a proxy for chemical similarity)
        for reactant in reaction.reactants:
            if len(self.name) >= 3 and len(reactant.name) >= 3:
                if self.name in reactant.name or reactant.name in self.name:
                    return True
                    
        for product in reaction.products:
            if len(self.name) >= 3 and len(product.name) >= 3:
                if self.name in product.name or product.name in self.name:
                    return True
        
        # More complex rules could be added here based on catalyst type
        return False


class Reaction:
    """Represents a chemical reaction with reactants, products, and catalysis."""
    
    def __init__(self, reactants, products, rate=0.01, energy=0):
        """
        Initialize a reaction.
        
        Args:
            reactants (list): List of reactant molecules
            products (list): List of product molecules
            rate (float): Base reaction rate
            energy (float): Energy change of reaction (negative = exergonic)
        """
        self.reactants = reactants
        self.products = products
        self.base_rate = rate
        self.energy = energy
        self.catalysts = set()
        
    def __str__(self):
        return " + ".join(str(r) for r in self.reactants) + " → " + " + ".join(str(p) for p in self.products)
    
    def add_catalyst(self, molecule):
        """Add a catalyst for this reaction."""
        self.catalysts.add(molecule)
    
    @property
    def is_catalyzed(self):
        """Check if the reaction has catalysts."""
        return len(self.catalysts) > 0
    
    @property
    def effective_rate(self):
        """Calculate the effective reaction rate with catalysis."""
        # Each catalyst increases the reaction rate
        catalyst_factor = 5.0
        
        if not self.catalysts:
            return self.base_rate
        
        # The more catalysts, the higher the rate, with diminishing returns
        return self.base_rate * (1 + catalyst_factor * math.log(1 + len(self.catalysts)))
    
    @property
    def entropy_reduction(self):
        """Calculate the entropy reduction achieved by this reaction."""
        # Calculate complexity before and after
        reactant_complexity = sum(r.complexity for r in self.reactants)
        product_complexity = sum(p.complexity for p in self.products)
        
        # Base entropy change (negative if complexity increases)
        base_entropy_change = reactant_complexity - product_complexity
        
        # Catalyzed reactions achieve more ordered outcomes
        catalyst_factor = 1.5 if self.is_catalyzed else 1.0
        
        # Return entropy reduction (so negate if complexity increases)
        return -base_entropy_change * catalyst_factor


class Compartment:
    """Represents a cell-like compartment with a boundary and internal chemistry."""
    
    def __init__(self, position, radius=0.05):
        """
        Initialize a compartment.
        
        Args:
            position (tuple): (x, y) position in simulation space
            radius (float): Initial radius of compartment
        """
        self.position = position
        self.radius = radius
        self.molecules = {}  # Molecules contained inside {molecule: count}
        self.boundary_molecules = []  # Molecules forming the boundary
        self.stability = 0.5  # Initial stability (0-1)
        self.age = 0  # Age in time steps
        self.division_threshold = 0.15  # Size threshold for division
        self.metabolic_activity = 0.0  # Measure of internal reactions
        
    def contains_point(self, point):
        """Check if a point is inside this compartment."""
        x, y = point
        cx, cy = self.position
        distance = math.sqrt((x - cx)**2 + (y - cy)**2)
        return distance <= self.radius
        
    def add_molecule(self, molecule, count=1):
        """Add molecules to the compartment interior."""
        if molecule in self.molecules:
            self.molecules[molecule] += count
        else:
            self.molecules[molecule] = count
            
    def add_to_boundary(self, molecule):
        """Add a molecule to the compartment boundary."""
        if molecule.is_amphiphilic:
            self.boundary_molecules.append(molecule)
            return True
        return False
        
    def update(self):
        """Update the compartment state."""
        # Age the compartment
        self.age += 1
        
        # Calculate stability based on boundary composition
        if self.boundary_molecules:
            # More amphiphilic molecules = more stable
            self.stability = min(0.9, 0.4 + 0.5 * (len(self.boundary_molecules) / (100 + self.radius * 1000)))
        else:
            # No boundary molecules means decreasing stability
            self.stability = max(0, self.stability - 0.05)
            
        # Grow if stable and has molecules
        if self.stability > 0.5 and self.molecules:
            growth_factor = 0.001 * self.stability * math.log(1 + sum(self.molecules.values()))
            self.radius += growth_factor
            
        # Calculate metabolic activity based on molecule diversity
        self.metabolic_activity = len(self.molecules) * math.log(1 + sum(self.molecules.values()))
        
    def can_divide(self):
        """Check if the compartment is ready to divide."""
        return (self.radius > self.division_threshold and 
                self.stability > 0.6 and 
                self.age > 10)
                
    def divide(self):
        """
        Divide the compartment into two daughter compartments.
        
        Returns:
            tuple: Two new compartments (parent, offspring)
        """
        # Create two daughter compartments
        angle = random.uniform(0, 2 * math.pi)
        offset_distance = self.radius * 0.5
        
        # Calculate new positions slightly offset from parent
        x, y = self.position
        pos1 = (x + offset_distance * math.cos(angle), y + offset_distance * math.sin(angle))
        pos2 = (x - offset_distance * math.cos(angle), y - offset_distance * math.sin(angle))
        
        daughter1 = Compartment(pos1, radius=self.radius * 0.6)
        daughter2 = Compartment(pos2, radius=self.radius * 0.6)
        
        # Distribute molecules somewhat randomly between daughters
        for molecule, count in self.molecules.items():
            # Slightly uneven split (60/40 on average with some randomness)
            split_ratio = random.uniform(0.4, 0.6)
            count1 = int(count * split_ratio)
            count2 = count - count1
            
            if count1 > 0:
                daughter1.add_molecule(molecule, count1)
            if count2 > 0:
                daughter2.add_molecule(molecule, count2)
                
        # Distribute boundary molecules
        for molecule in self.boundary_molecules:
            # Randomly assign to one of the daughters
            if random.random() < 0.5:
                daughter1.add_to_boundary(molecule)
            else:
                daughter2.add_to_boundary(molecule)
                
        # Inherit stability with small mutations
        stability_mutation = random.uniform(-0.1, 0.1)
        daughter1.stability = max(0.1, min(0.9, self.stability + stability_mutation))
        
        stability_mutation = random.uniform(-0.1, 0.1)
        daughter2.stability = max(0.1, min(0.9, self.stability + stability_mutation))
        
        return daughter1, daughter2


class ChemicalSystem:
    """Represents the entire chemical system with molecules, reactions, and compartments."""
    
    def __init__(self, width=1.0, height=1.0):
        """
        Initialize the chemical system.
        
        Args:
            width (float): Width of the simulation space
            height (float): Height of the simulation space
        """
        self.width = width
        self.height = height
        self.molecules = {}  # {molecule: count}
        self.reactions = []
        self.compartments = []
        self.reaction_network = nx.DiGraph()
        self.time_step = 0
        
        # Metrics tracking
        self.metrics = {
            'entropy_reduction': [],
            'catalytic_activity': [],
            'molecular_complexity': [],
            'compartment_count': [],
            'avg_stability': [],
            'entropy_ratio': [],
            'catalytic_ratio': []
        }
        
    def add_molecule(self, molecule, count=1, position=None):
        """Add molecules to the system."""
        if position:
            molecule.position = position
            
        if molecule in self.molecules:
            self.molecules[molecule] += count
        else:
            self.molecules[molecule] = count
            
    def add_reaction(self, reaction):
        """Add a reaction to the system."""
        self.reactions.append(reaction)
        
        # Update reaction network graph
        for reactant in reaction.reactants:
            for product in reaction.products:
                self.reaction_network.add_edge(reactant, product, reaction=reaction)
                
    def add_compartment(self, compartment):
        """Add a compartment to the system."""
        self.compartments.append(compartment)
        
    def identify_catalysts(self):
        """Identify molecules that can catalyze reactions."""
        for molecule in self.molecules:
            for reaction in self.reactions:
                if molecule.can_catalyze(reaction):
                    reaction.add_catalyst(molecule)
                    
    def create_initial_food_set(self):
        """Create an initial set of simple food molecules."""
        # Create simple molecules
        water = Molecule("H2O", complexity=1)
        methane = Molecule("CH4", complexity=1)
        ammonia = Molecule("NH3", complexity=1)
        hydrogen = Molecule("H2", complexity=1)
        carbon_dioxide = Molecule("CO2", complexity=1)
        
        # Add them to the system
        self.add_molecule(water, count=1000)
        self.add_molecule(methane, count=500)
        self.add_molecule(ammonia, count=300)
        self.add_molecule(hydrogen, count=800)
        self.add_molecule(carbon_dioxide, count=400)
        
        # Add some slightly more complex molecules
        formaldehyde = Molecule("CH2O", complexity=2)
        hydrogen_cyanide = Molecule("HCN", complexity=2)
        self.add_molecule(formaldehyde, count=50)
        self.add_molecule(hydrogen_cyanide, count=30)
        
        # Add a few amphiphilic molecules as seed
        fatty_acid = Molecule("C8H16O2", complexity=10, is_amphiphilic=True)
        phospholipid = Molecule("C10H18O8P", complexity=20, is_amphiphilic=True)
        self.add_molecule(fatty_acid, count=10)
        self.add_molecule(phospholipid, count=5)
        
    def create_initial_reactions(self):
        """Create an initial set of plausible prebiotic reactions."""
        # Get all molecules currently in the system
        molecules = list(self.molecules.keys())
        
        # Formose reaction (formaldehyde to sugars)
        # CH2O + CH2O → C2H4O2 (glycolaldehyde)
        if any(m.name == "CH2O" for m in molecules):
            formaldehyde = next(m for m in molecules if m.name == "CH2O")
            glycolaldehyde = Molecule("C2H4O2", complexity=4)
            formose_reaction = Reaction([formaldehyde, formaldehyde], [glycolaldehyde], rate=0.005)
            self.add_reaction(formose_reaction)
            self.add_molecule(glycolaldehyde, count=0)  # Add with count 0 so it's in the system
            
        # Further sugar formation
        # C2H4O2 + CH2O → C3H6O3 (glyceraldehyde)
        if any(m.name == "C2H4O2" for m in molecules):
            glycolaldehyde = next(m for m in molecules if m.name == "C2H4O2")
            if any(m.name == "CH2O" for m in molecules):
                formaldehyde = next(m for m in molecules if m.name == "CH2O")
                glyceraldehyde = Molecule("C3H6O3", complexity=6)
                sugar_reaction = Reaction([glycolaldehyde, formaldehyde], [glyceraldehyde], rate=0.003)
                self.add_reaction(sugar_reaction)
                self.add_molecule(glyceraldehyde, count=0)
                
        # HCN polymerization
        # HCN + HCN → C2H2N2 (cyanide dimer)
        if any(m.name == "HCN" for m in molecules):
            hcn = next(m for m in molecules if m.name == "HCN")
            cyanide_dimer = Molecule("C2H2N2", complexity=4)
            hcn_reaction = Reaction([hcn, hcn], [cyanide_dimer], rate=0.002)
            self.add_reaction(hcn_reaction)
            self.add_molecule(cyanide_dimer, count=0)
            
        # Amino acid formation
        # C2H2N2 + H2O → C2H5NO2 (glycine)
        if any(m.name == "C2H2N2" for m in molecules) and any(m.name == "H2O" for m in molecules):
            cyanide_dimer = next(m for m in molecules if m.name == "C2H2N2")
            water = next(m for m in molecules if m.name == "H2O")
            glycine = Molecule("C2H5NO2", complexity=8)
            amino_reaction = Reaction([cyanide_dimer, water], [glycine], rate=0.001)
            self.add_reaction(amino_reaction)
            self.add_molecule(glycine, count=0)
            
        # Fatty acid formation
        # CH4 + CO2 → C2H4O2 (acetic acid)
        if any(m.name == "CH4" for m in molecules) and any(m.name == "CO2" for m in molecules):
            methane = next(m for m in molecules if m.name == "CH4")
            co2 = next(m for m in molecules if m.name == "CO2")
            acetic_acid = Molecule("C2H4O2", complexity=5)
            acetic_reaction = Reaction([methane, co2], [acetic_acid], rate=0.001)
            self.add_reaction(acetic_reaction)
            self.add_molecule(acetic_acid, count=0)
            
        # Acetic acid to fatty acids
        # C2H4O2 + C2H4O2 → C4H8O2 (butyric acid)
        if any(m.name == "C2H4O2" for m in molecules):
            acetic_acid = next(m for m in molecules if m.name == "C2H4O2")
            butyric_acid = Molecule("C4H8O2", complexity=7, is_amphiphilic=True)
            fatty_reaction = Reaction([acetic_acid, acetic_acid], [butyric_acid], rate=0.0005)
            self.add_reaction(fatty_reaction)
            self.add_molecule(butyric_acid, count=0)
            
        # More complex amphiphilic molecules
        # C4H8O2 + C4H8O2 → C8H16O2 (caprylic acid, amphiphilic)
        if any(m.name == "C4H8O2" for m in molecules):
            butyric_acid = next(m for m in molecules if m.name == "C4H8O2")
            caprylic_acid = Molecule("C8H16O2", complexity=12, is_amphiphilic=True)
            amphiphilic_reaction = Reaction([butyric_acid, butyric_acid], [caprylic_acid], rate=0.0003)
            self.add_reaction(amphiphilic_reaction)
            self.add_molecule(caprylic_acid, count=0)
        
    def update(self, environment):
        """
        Update the chemical system for one time step.
        
        Args:
            environment: Current environmental state
        """
        self.time_step += 1
        new_molecules = {}  # Molecules created this step
        
        # Update molecule positions using Brownian motion
        for molecule in self.molecules:
            if self.molecules[molecule] > 0:  # Only update if we have some of this molecule
                molecule.update_position((self.width, self.height))
        
        # Execute reactions based on their rates and environmental factors
        for reaction in self.reactions:
            # Check if all reactants are available
            reactants_available = True
            for reactant in reaction.reactants:
                if reactant not in self.molecules or self.molecules[reactant] <= 0:
                    reactants_available = False
                    break
            
            if not reactants_available:
                continue
                
            # Calculate probability of reaction occurring
            env_factor = environment.affect_reaction(reaction)
            probability = reaction.effective_rate * env_factor
            
            # Determine how many reaction events occur
            # (Based on rate and minimum available reactant count)
            min_reactant_count = min(self.molecules[r] for r in reaction.reactants)
            max_events = min(min_reactant_count, 10)  # Cap at 10 events per step for performance
            events = 0
            
            for _ in range(max_events):
                if random.random() < probability:
                    events += 1
            
            if events > 0:
                # Consume reactants
                for reactant in reaction.reactants:
                    self.molecules[reactant] -= events
                
                # Create products
                for product in reaction.products:
                    if product in new_molecules:
                        new_molecules[product] += events
                    else:
                        new_molecules[product] = events
        
        # Add new molecules to system
        for molecule, count in new_molecules.items():
            if molecule in self.molecules:
                self.molecules[molecule] += count
            else:
                self.molecules[molecule] = count
        
        # Identify new potential catalysts
        self.identify_catalysts()
        
        # Update compartments
        self._update_compartments(environment)
        
        # Check for potential new compartment formation
        self._check_compartment_formation()
        
        # Update metrics
        self._update_metrics()
        
        return len(new_molecules) > 0  # Return whether any new molecules were created
        
    def _update_compartments(self, environment):
        """Update existing compartments and handle division events."""
        new_compartments = []
        compartments_to_remove = []
        
        for compartment in self.compartments:
            # Update the compartment state
            compartment.update()
            
            # Check stability - remove if too unstable
            if compartment.stability <= 0.1:
                compartments_to_remove.append(compartment)
                continue
                
            # Check for division
            if compartment.can_divide():
                daughter1, daughter2 = compartment.divide()
                new_compartments.append(daughter1)
                new_compartments.append(daughter2)
                compartments_to_remove.append(compartment)
                
            # Environmental effects on compartments
            # Wet-dry cycles affect compartment stability
            if hasattr(environment, 'wet_phase'):
                if environment.wet_phase < 0.2:  # Very dry
                    compartment.stability -= 0.05  # Compartments dehydrate and may collapse
                elif environment.wet_phase > 0.8:  # Very wet
                    if compartment.stability < 0.7:  # Weak compartments
                        compartment.stability -= 0.02  # May dissolve
                        
            # Temperature effects
            if hasattr(environment, 'temperature'):
                # Extreme temperatures are bad for compartments
                if environment.temperature < 10 or environment.temperature > 80:
                    compartment.stability -= 0.03
        
        # Remove unstable or divided compartments
        for compartment in compartments_to_remove:
            if compartment in self.compartments:
                self.compartments.remove(compartment)
                
        # Add new compartments
        self.compartments.extend(new_compartments)
        
    def _check_compartment_formation(self):
        """Check if conditions are right for spontaneous compartment formation."""
        # Basic rule: if enough amphiphilic molecules are in the system, 
        # there's a chance for a new compartment to form
        
        # Count amphiphilic molecules
        amphiphilic_count = sum(
            count for molecule, count in self.molecules.items() 
            if molecule.is_amphiphilic
        )
        
        # Threshold for potential compartment formation
        threshold = 20
        
        if amphiphilic_count >= threshold:
            # Probability increases with more amphiphilic molecules
            p_formation = 0.01 * (amphiphilic_count / threshold)
            
            if random.random() < p_formation:
                # Create a new compartment at a random position
                pos = (random.random() * self.width, random.random() * self.height)
                new_compartment = Compartment(pos)
                
                # Add some amphiphilic molecules to the boundary
                amphiphilic_molecules = [
                    m for m in self.molecules 
                    if m.is_amphiphilic and self.molecules[m] > 0
                ]
                
                # Use up to 10 amphiphilic molecules for the new compartment
                for _ in range(min(10, amphiphilic_count)):
                    if amphiphilic_molecules:
                        molecule = random.choice(amphiphilic_molecules)
                        if self.molecules[molecule] > 0:
                            new_compartment.add_to_boundary(molecule)
                            self.molecules[molecule] -= 1
                
                # Add the compartment to the system
                self.compartments.append(new_compartment)
                
                # Add some random molecules inside
                for molecule, count in self.molecules.items():
                    if count > 10:  # Only use abundant molecules
                        inside_count = random.randint(1, 5)
                        self.molecules[molecule] -= inside_count
                        new_compartment.add_molecule(molecule, inside_count)
        
    def _update_metrics(self):
        """Update time series metrics for analysis."""
        # Calculate total entropy reduction from all reactions
        total_entropy_reduction = sum(
            reaction.entropy_reduction for reaction in self.reactions 
            if all(reactant in self.molecules and self.molecules[reactant] > 0 
                  for reactant in reaction.reactants)
        )
        
        # Calculate catalytic activity (proportion of reactions that are catalyzed)
        active_reactions = [r for r in self.reactions 
                           if all(reactant in self.molecules and self.molecules[reactant] > 0 
                                 for reactant in r.reactants)]
        
        if active_reactions:
            catalyzed_reactions = sum(1 for r in active_reactions if r.is_catalyzed)
            catalytic_activity = catalyzed_reactions / len(active_reactions)
        else:
            catalytic_activity = 0
        
        # Calculate average molecular complexity
        if sum(self.molecules.values()) > 0:
            avg_complexity = sum(
                molecule.complexity * count for molecule, count in self.molecules.items()
            ) / sum(self.molecules.values())
        else:
            avg_complexity = 0
            
        # Calculate compartment metrics
        compartment_count = len(self.compartments)
        if compartment_count > 0:
            avg_stability = sum(c.stability for c in self.compartments) / compartment_count
        else:
            avg_stability = 0
            
        # Calculate entropy ratio (current system entropy / initial entropy)
        # For simplicity, we use a proxy: initial avg complexity / current avg complexity
        if avg_complexity > 0 and len(self.metrics['molecular_complexity']) > 0:
            initial_complexity = self.metrics['molecular_complexity'][0] or 1
            entropy_ratio = initial_complexity / avg_complexity
        else:
            entropy_ratio = 1.0
            
        # Calculate catalytic ratio (proportion of molecules that are catalysts)
        catalyst_count = sum(
            1 for molecule in self.molecules 
            if any(molecule in reaction.catalysts for reaction in self.reactions)
        )
        if sum(self.molecules.values()) > 0:
            catalytic_ratio = catalyst_count / len(self.molecules)
        else:
            catalytic_ratio = 0
        
        # Store metrics
        self.metrics['entropy_reduction'].append(total_entropy_reduction)
        self.metrics['catalytic_activity'].append(catalytic_activity)
        self.metrics['molecular_complexity'].append(avg_complexity)
        self.metrics['compartment_count'].append(compartment_count)
        self.metrics['avg_stability'].append(avg_stability)
        self.metrics['entropy_ratio'].append(entropy_ratio)
        self.metrics['catalytic_ratio'].append(catalytic_ratio)
        
    def calculate_feedback_coefficient(self):
        """
        Calculate the entropy-catalysis feedback coefficient.
        
        This measures how strongly entropy reduction and catalytic activity are coupled.
        A value close to 1 indicates strong positive feedback between the two.
        """
        # Need at least a few data points for correlation
        if len(self.metrics['entropy_reduction']) < 10:
            return 0
            
        # Use a window for calculating correlation to detect more recent patterns
        window_size = min(50, len(self.metrics['entropy_reduction']) // 4)
        
        if window_size < 10:  # Not enough data for a meaningful window
            window_size = len(self.metrics['entropy_reduction'])
            
        # Calculate correlation between entropy reduction and catalytic activity
        # with a small offset to detect causal relationships
        offset = 1  # Offset by 1 time step to detect causality
        
        # Get the most recent data within our window
        er = np.array(self.metrics['entropy_reduction'][-window_size:-offset])
        ca = np.array(self.metrics['catalytic_activity'][-(window_size-offset):])
        
        # Check for data variation to avoid division by zero in correlation
        if len(er) < 5 or np.std(er) < 0.0001 or np.std(ca) < 0.0001:
            # Not enough variation in the data for meaningful correlation
            return 0
            
        try:
            correlation = np.corrcoef(er, ca)[0, 1]
            
            # Handle NaN values and bound the result
            if np.isnan(correlation):
                return 0
                
            return max(-1.0, min(1.0, correlation))  # Bound between -1 and 1
        except Exception:
            # Handle any numerical errors safely
            return 0
        
    def get_molecule_counts(self):
        """Get current molecule counts for visualization."""
        return dict(self.molecules)
        
    def get_compartment_data(self):
        """Get data about compartments for visualization."""
        return [
            {
                'position': c.position,
                'radius': c.radius,
                'stability': c.stability,
                'age': c.age,
                'molecule_count': sum(c.molecules.values()),
                'metabolic_activity': c.metabolic_activity
            } for c in self.compartments
        ]
        
    def get_summary(self):
        """Get a summary of the current system state."""
        total_molecules = sum(self.molecules.values())
        species_count = len([m for m in self.molecules if self.molecules[m] > 0])
        
        amphiphilic_count = sum(
            count for molecule, count in self.molecules.items() 
            if molecule.is_amphiphilic
        )
        
        avg_complexity = 0
        if total_molecules > 0:
            avg_complexity = sum(
                molecule.complexity * count for molecule, count in self.molecules.items()
            ) / total_molecules
        
        feedback_coef = self.calculate_feedback_coefficient()
        
        return {
            'time_step': self.time_step,
            'total_molecules': total_molecules,
            'species_count': species_count,
            'compartment_count': len(self.compartments),
            'reaction_count': len(self.reactions),
            'amphiphilic_count': amphiphilic_count,
            'avg_complexity': avg_complexity,
            'feedback_coefficient': feedback_coef,
            'metrics': self.metrics
        }