"""
RECC Agent Module
Main module that ties together all components of the RECC system
"""
import random
import time
import json
import copy
from datetime import datetime

from event_bus import global_event_bus, EventTypes
from components.memory import Memory
from components.reflective_core import Me
from components.state_manager import StateManager
from components.concept_network import ConceptNetwork

class RECC:
    def __init__(self, llm_function, event_bus=None):
        # Use provided event bus or global instance
        self.event_bus = event_bus or global_event_bus
        
        # Initialize components with event bus
        self.memory = Memory(self.event_bus)
        self.me = Me(self.memory, self.event_bus)
        
        self.llm = llm_function
        self.state = {'age_stage': 'infant', 'version': '1.5.0'}  # Updated version
        self.state_manager = StateManager()
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.prompts = [
            "?",
            "...",
            "What?",
            "Why?",
            "How?"
        ]
        # Start each session with a reset conversation history
        self.reset_conversation_history = True
        # Add tracking for recently used concepts
        self.recent_concepts_used = []
        # Add simulated developmental age
        self.dev_age = 2.0  # Start at basic language stage
        
        # Register for events
        self.setup_event_handlers()
        
        # Add observable metrics
        self.metrics = {
            'cycle_times': [],            # Time per cycle
            'prompt_complexity': [],      # Complexity trend of prompts
            'response_novelty': [],       # Novelty scores of responses
            'concept_creation_rate': []   # Concepts created per cycle
        }
    
    def setup_event_handlers(self):
        """Set up handlers for various events"""
        # Example event handlers
        self.event_bus.subscribe(EventTypes.THRESHOLD_CROSSED, self.handle_threshold_crossed)
        self.event_bus.subscribe(EventTypes.REPETITION_DETECTED, self.handle_repetition_detected)
    
    def handle_threshold_crossed(self, data):
        """Handle threshold crossing events"""
        if data.get('type') == 'stagnation':
            print(f"🚨 Stagnation threshold crossed at cycle {data.get('cycle')}")
            self.reset_dialogue_context()
            self.state['explore_axis'] = 'radical_mutation'
    
    def handle_repetition_detected(self, data):
        """Handle repetition detection events"""
        print(f"🔁 Repetition detected: {data.get('type')} at cycle {data.get('cycle', len(self.memory.entries))}")
    
    def generate_prompt(self):
        """Generate a prompt based on emotional state and memory content"""
        # Generate the prompt
        prompt = self._generate_prompt_internal()
        
        # Emit event when prompt is generated
        self.event_bus.publish(EventTypes.PROMPT_GENERATED, {
            'prompt': prompt,
            'cycle': len(self.memory.entries),
            'emotional_state': copy.deepcopy(self.me.emotional_state),
            'dev_age': self.dev_age
        })
        
        return prompt
    
    def _generate_prompt_internal(self):
        """Internal implementation of prompt generation"""
        # First, try the more natural infant-like prompt generation
        # Higher chance of infant-like prompts when fewer memories exist
        if len(self.memory.entries) < 20 or random.random() < 0.7:
            infant_prompt = self.generate_infant_prompt()
            if infant_prompt:
                return infant_prompt
        
        # If frustration is very high, do a complete reset of conversation and force a new direction
        if self.me.emotional_state['frustration'] > 0.9:
            print("😡 Maximum frustration reached! Forcing complete conversation reset...")
            self.reset_dialogue_context()
            self.state['explore_axis'] = 'radical_mutation'
            
            # Use very simple radical questions - still childlike in structure
            radical_prompts = [
                "Why everything?",
                "What not there?",
                "How feel color?",
                "Where thoughts go?",
                "Why me?",
                "What before beginning?"
            ]
            return random.choice(radical_prompts)
            
        # Try to use the concept network (with simplified structures)
        concept_based_prompt = self.generate_prompt_from_concept_network()
        if (concept_based_prompt and random.random() < 0.6):  # 60% chance to use concept-based prompt
            # Simplify the language to feel more childlike
            simplified = concept_based_prompt.replace("I'm curious about", "Want know")
            simplified = simplified.replace("understand", "know")
            simplified = simplified.replace("completely different perspective", "new way")
            simplified = simplified.replace("fundamentally reimagined", "made new")
            return simplified
            
        # Check for repetition
        if self.memory.detect_repetition(threshold=0.6, window_size=5):
            self.reset_dialogue_context()
            self.state['explore_axis'] = 'mutation'
            
            # Use simpler breakout prompts
            breakout_prompts = [
                "What different?",
                "New idea?",
                "What if not?",
                "Other way?",
                "Opposite?"
            ]
            return random.choice(breakout_prompts)
        
        # Very simple prompts for other emotional states
        emotions = self.me.emotional_state
        
        # Occasionally pick a completely random prompt
        if random.random() < 0.1:
            return random.choice(self.prompts)
        
        if emotions['frustration'] > 0.7:
            self.state['explore_axis'] = 'mutation'
            return random.choice([
                "Want different.",
                "Not this. What else?",
                "New thing?"
            ])
            
        if emotions['curiosity'] > 0.8 and len(self.memory.symbols) >= 2:
            symbols = random.sample(self.memory.symbols, min(2, len(self.memory.symbols)))
            return f"{symbols[0]} and {symbols[1]}?"
            
        if emotions['satisfaction'] > 0.7:
            return random.choice([
                "Like this. More?",
                "Good. What next?",
                "This nice. Why?"
            ])
        
        if emotions['uncertainty'] > 0.8:
            return random.choice([
                "Not sure. Help?",
                "Confused. Simple?",
                "Need clear."
            ])
        
        # Original prompt generation logic - simplified
        if not self.memory.entries or len(self.memory.entries) < 5:
            return random.choice(self.prompts)

        return random.choice([
            "What think?",
            "Tell more?",
            "Why happen?",
            "How work?"
        ])
    
    def generate_infant_prompt(self):
        """Generate a prompt that simulates an infant or very young child's speech pattern"""
        if len(self.memory.entries) < 5:
            # Very basic one-word questions
            return random.choice(["What?", "Why?", "How?", "Where?"])
        
        # Get concepts that are active in memory
        concepts = []
        if hasattr(self.memory, 'concept_network'):
            active_concepts = self.memory.concept_network.get_active_concepts(threshold=0.6)
            concepts = [self.memory.concept_network.concepts[c]['name'] 
                      for c in active_concepts if c in self.memory.concept_network.concepts]
        
        # If no concepts from network, use symbols
        if not concepts and self.memory.symbols:
            concepts = self.memory.symbols
        
        # If still no concepts, use very basic questions
        if not concepts:
            return random.choice(["What this?", "Why that?", "How work?"])
            
        # Select a random concept and form a simple question
        concept = random.choice(concepts)
        templates = [
            f"{concept}?",
            f"{concept} what?",
            f"Why {concept}?",
            f"How {concept}?",
            f"{concept} and what?",
            f"More {concept}?"
        ]
        
        # Occasionally combine two concepts
        if len(concepts) > 1 and random.random() > 0.5:
            concept2 = random.choice([c for c in concepts if c != concept])
            templates.extend([
                f"{concept} and {concept2}?",
                f"{concept} or {concept2}?",
                f"Why {concept} not {concept2}?"
            ])
            
        return random.choice(templates)
        
    def generate_prompt_from_concept_network(self):
        """Generate a prompt based on the concept network"""
        if not hasattr(self.memory, 'concept_network') or not self.memory.concept_network.concepts:
            return None
            
        # Get important concepts from network
        central_concepts = self.memory.concept_network.get_central_concepts(n=3)
        active_concepts = self.memory.concept_network.get_active_concepts(threshold=0.5)
        
        # Combine and get unique concepts
        important_concepts = list(set(central_concepts + active_concepts))
        
        if not important_concepts:
            return None
            
        # Select 1-2 concepts to focus on
        selected = random.sample(important_concepts, min(2, len(important_concepts)))
        concept_names = [self.memory.concept_network.concepts[c]['name'] for c in selected]
        
        # Get the relation type if focusing on two concepts
        relation_type = None
        if len(selected) == 2:
            # Check if there's a relationship between these concepts
            for relation in self.memory.concept_network.relations:
                if (relation['source'] == selected[0] and relation['target'] == selected[1]) or \
                   (relation['source'] == selected[1] and relation['target'] == selected[0]):
                    relation_type = relation['type']
                    break
        
        # Generate prompt based on concepts and their relations
        if len(concept_names) == 1:
            templates = [
                f"Tell more about {concept_names[0]}?",
                f"What is {concept_names[0]}?",
                f"Why is {concept_names[0]} important?",
                f"How does {concept_names[0]} work?",
                f"What happens with {concept_names[0]}?"
            ]
            return random.choice(templates)
        else:
            if relation_type:
                # Use relation-specific template
                if relation_type == 'causes':
                    return f"How does {concept_names[0]} cause {concept_names[1]}?"
                elif relation_type == 'part_of':
                    return f"How is {concept_names[0]} part of {concept_names[1]}?"
                elif relation_type == 'contrasts_with':
                    return f"What's the difference between {concept_names[0]} and {concept_names[1]}?"
                else:
                    return f"How do {concept_names[0]} and {concept_names[1]} connect?"
            else:
                # General template for multiple concepts
                templates = [
                    f"How do {concept_names[0]} and {concept_names[1]} relate?",
                    f"Tell me about {concept_names[0]} and {concept_names[1]}?",
                    f"What connects {concept_names[0]} with {concept_names[1]}?",
                    f"Compare {concept_names[0]} and {concept_names[1]}?"
                ]
                return random.choice(templates)
        
    def reset_dialogue_context(self):
        """Reset the dialogue context to avoid getting stuck"""
        self.reset_conversation_history = True
        print("🔄 Resetting dialogue context for fresh conversation")
        
        # Clear recently used concepts to encourage diversity
        self.recent_concepts_used = []
        
        # Emit event for UI/monitoring
        self.event_bus.publish(EventTypes.DIALOGUE_CONTEXT_RESET, {
            'timestamp': datetime.now().isoformat(),
            'reason': 'break_repetition',
            'cycle': len(self.memory.entries)
        })
    
    def autonomous_loop(self, steps=5, delay=3, save_interval=10):
        """Enhanced autonomous loop with observability events"""
        for step in range(steps):
            cycle_start_time = time.time()
            
            # Generate prompt
            prompt = self.generate_prompt()
            
            # Use the LLM to get a response
            if step == 0 and self.reset_conversation_history:
                response = self.llm(prompt, reset_history=True)
                self.reset_conversation_history = False
            else:
                response = self.llm(prompt, reset_history=False)
            
            # Process the interaction and get metrics
            entry = self.memory.add(prompt, response, self.state.copy())
            decision = self.me.reflect()
            
            # Calculate cycle metrics
            cycle_time = time.time() - cycle_start_time
            
            # Track metrics
            self.metrics['cycle_times'].append(cycle_time)
            
            # Count new concepts
            new_concepts = entry.get('concept_data', {}).get('new_concepts', 0)
            self.metrics['concept_creation_rate'].append(new_concepts)
            
            # Track prompt complexity
            prompt_complexity = len(prompt.split())
            self.metrics['prompt_complexity'].append(prompt_complexity)
            
            # Track novelty
            self.metrics['response_novelty'].append(entry.get('novelty', 0))

            # Emit the cycle complete event
            self.event_bus.publish(EventTypes.CYCLE_COMPLETE, {
                'step': step,
                'total_steps': steps,
                'prompt': prompt,
                'response': response,
                'cycle_time': cycle_time,
                'decision': decision,
                'entry': entry,
                'metrics': {
                    'new_concepts': new_concepts,
                    'prompt_complexity': prompt_complexity,
                    'novelty': entry.get('novelty', 0),
                    'emotional_state': self.me.emotional_state
                }
            })
            
            # Emit threshold events for significant changes
            self._check_and_emit_thresholds()
            
            # Log current cycle status
            print(f"\n--- Cycle {step+1}/{steps} ---")
            print(f"Prompt: {prompt}")
            print(f"Response: {response}")
            
            # Log concept network statistics
            network_stats = self.memory.concept_network.get_network_stats()
            print(f"Concept Network: {network_stats['concept_count']} concepts, {network_stats['relation_count']} relations")
            
            # Get central concepts
            central_concepts = self.memory.get_core_concepts(3)
            central_names = [self.memory.concept_network.concepts[c]['name'] 
                            for c in central_concepts if c in self.memory.concept_network.concepts]
            if central_names:
                print(f"Central concepts: {', '.join(central_names)}")
            
            print(f"Emotions: {json.dumps(self.me.emotional_state, indent=2)}")
            print(f"Reflection: {json.dumps(decision, indent=2)}")

            # Periodic state saving - but less frequently
            if (step + 1) % save_interval == 0:
                self.state_manager.save_state(self, self.session_id)
                # Clean up excessive state files
                self.state_manager.cleanup_old_states()
                
            # Potential memory consolidation after significant accumulation
            if len(self.memory.entries) > 20 and step % 10 == 0:
                print("💾 Consolidating memory...")
                result = self.memory.consolidate_memory(threshold=0.25)
                print(f"Memory consolidated: {result['original']} → {result['consolidated']} entries")
                
            time.sleep(delay)

        # Final state save
        self.state_manager.save_state(self, self.session_id)
        
        # Generate and save visualizations
        self._generate_visualizations()
        
        return self.memory.symbols, self.memory.symbol_links
    
    def _generate_visualizations(self):
        """Generate and save visualizations for the current state"""
        try:
            from lab.RECC.visualization_utils import draw_concept_map, visualize_emotions
            
            visualization_data = {}
            
            # Generate concept network visualization
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            concept_map_path = f"./visualization/static/concept_network_{timestamp}.png"
            draw_concept_map(concept_network=self.memory.concept_network, save_path=concept_map_path)
            visualization_data['concept_map'] = concept_map_path
            
            # Generate emotional development visualization
            if len(self.me.emotion_history) > 2:
                emotions_path = f"./visualization/static/emotional_development_{timestamp}.png"
                visualize_emotions(self.me, save_path=emotions_path)
                visualization_data['emotions'] = emotions_path
            
            # Emit visualization save event
            self.event_bus.publish(EventTypes.VISUALIZATION_SAVE, visualization_data)
            
            return visualization_data
            
        except Exception as e:
            print(f"Error generating visualizations: {e}")
            return None
        
    def _check_and_emit_thresholds(self):
        """Check for threshold crossings and emit events"""
        # Check for repetition
        if self.memory.detect_repetition():
            self.event_bus.publish(EventTypes.THRESHOLD_CROSSED, {
                'type': 'repetition',
                'description': 'Repetition pattern detected',
                'cycle': len(self.memory.entries),
                'severity': 'high'
            })
            
        # Check for emotional threshold crossings
        emotions = self.me.emotional_state
        prev_emotions = self.me.emotion_history[-2]['state'] if len(self.me.emotion_history) > 1 else emotions
        
        for emotion, value in emotions.items():
            prev_value = prev_emotions.get(emotion, 0.5)
            
            # Detect significant emotional changes
            if abs(value - prev_value) > 0.25:  # Major shift
                self.event_bus.publish(EventTypes.EMOTIONAL_CHANGE, {
                    'emotion': emotion,
                    'previous': prev_value,
                    'current': value,
                    'delta': value - prev_value,
                    'cycle': len(self.memory.entries)
                })
    
    def register_handler(self, event_type, handler_function):
        """Register external event handlers for observability"""
        self.event_bus.subscribe(event_type, handler_function)