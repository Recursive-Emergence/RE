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

    def process_user_input(self, prompt, reset_history=False):
        """
        Process input directly from a user, using the agent's genuine knowledge
        instead of calling the LLM and transforming the response.
        
        This ensures that user interactions reflect the agent's actual learning and
        concept development rather than the LLM's knowledge.
        """
        # Reset conversation history if needed
        if reset_history or self.reset_conversation_history:
            self.reset_conversation_history = False
            
        # Create a genuine response based on the agent's knowledge
        response = self.generate_response(prompt)
            
        # Track metrics and process through the agent's systems
        entry = self.memory.add(prompt, response, self.state.copy())
        
        # Allow reflection to update the agent's emotional state
        decision = self.me.reflect()
        
        # Create a structured response that shows this came from the agent
        result = {
            'response': response,
            'entry_id': entry['id'],
            'emotional_state': copy.deepcopy(self.me.emotional_state),
            'decision': decision
        }
        
        # Emit event for monitoring
        self.event_bus.publish(EventTypes.USER_INTERACTION_PROCESSED, {
            'prompt': prompt,
            'response': response,
            'cycle': len(self.memory.entries),
            'emotional_state': copy.deepcopy(self.me.emotional_state),
        })
        
        return result

    def generate_response(self, user_prompt):
        """
        Generate a genuine RECC response using the agent's concept network,
        memory, and emotional state, instead of relying on the LLM.
        """
        # First, try to understand the user prompt and extract key concepts
        prompt_concepts = []
        if hasattr(self.memory, 'concept_network'):
            # Extract potential concepts from the user prompt
            concept_extraction = self.memory.concept_network.extract_concepts_from_text(user_prompt)
            prompt_concepts = concept_extraction
            
        # Find entries in memory related to these concepts
        relevant_entries = []
        if prompt_concepts:
            # Get related memories for each concept
            for concept_id in prompt_concepts:
                if concept_id in self.memory.concept_network.concepts:
                    concept_name = self.memory.concept_network.concepts[concept_id]['name']
                    # Find entries containing this concept
                    for entry in self.memory.entries:
                        if concept_name.lower() in entry.get('prompt', '').lower() or concept_name.lower() in entry.get('response', '').lower():
                            if entry not in relevant_entries:
                                relevant_entries.append(entry)
        
        # Get the most recent memories regardless of relevance as context
        recent_entries = self.memory.get_recent(5)
        
        # Combine relevant and recent entries, prioritizing relevance
        context_entries = relevant_entries + [entry for entry in recent_entries if entry not in relevant_entries]
        
        # Generate response based on agent's current knowledge state
        emotions = self.me.emotional_state
        age = self.dev_age
        
        # Determine the response type based on emotional state
        response_type = "neutral"
        if emotions['curiosity'] > 0.7:
            response_type = "curious"
        elif emotions['satisfaction'] > 0.7:
            response_type = "satisfied"  
        elif emotions['frustration'] > 0.6:
            response_type = "frustrated"
        elif emotions['uncertainty'] > 0.8:
            response_type = "uncertain"
            
        # Generate a response using agent's current knowledge and emotional state
        response = self._generate_response_from_knowledge(user_prompt, context_entries, response_type, prompt_concepts)
        
        # Format the response based on developmental age (simplify vocabulary, etc.)
        formatted_response = self._format_response_by_age(response)
        
        return formatted_response
    
    def _generate_response_from_knowledge(self, prompt, context_entries, response_type, prompt_concepts):
        """Generate a response based on the agent's knowledge and emotional state"""
        # Start with core pieces of knowledge relevant to the concepts mentioned
        concept_info = []
        if prompt_concepts:
            for concept_id in prompt_concepts:
                if concept_id in self.memory.concept_network.concepts:
                    concept = self.memory.concept_network.concepts[concept_id]
                    # Add this concept to our knowledge base
                    concept_info.append(concept['name'])
        
        # Get excerpts from relevant memory entries
        memory_excerpts = []
        for entry in context_entries[:5]:  # Limit to first 5 entries
            # These are passages the agent might "remember" to use in its response
            memory_excerpts.append(entry.get('response', ''))
        
        # Look for personal theories related to these concepts
        relevant_theories = []
        for theory in self.me.personal_theories:
            # Check if theory is related to any prompt concept
            if any(concept in theory.get('description', '') for concept in concept_info):
                relevant_theories.append(theory.get('description', ''))
        
        # Generate a themed response based on emotional state
        if not concept_info and not memory_excerpts and not relevant_theories:
            # If no relevant information, give a simple response
            if response_type == "curious":
                return "I want to learn about that! Tell me more?"
            elif response_type == "satisfied":
                return "I like talking to you. What else can we talk about?"
            elif response_type == "frustrated":
                return "I don't know about that. Can we talk about something else?"
            elif response_type == "uncertain":
                return "I'm not sure what that means. Can you explain it more simply?"
            else:
                return "Hmm, I don't know much about that yet. What is it?"
        
        # Generate a response using the collected knowledge
        if response_type == "curious":
            # Curious response focuses on questions about the concepts
            if concept_info:
                main_concept = concept_info[0]
                if relevant_theories:
                    return f"I think {main_concept} is about {relevant_theories[0]}. Is that right? Want to know more!"
                else:
                    return f"I'm curious about {main_concept}! How does it work? Tell me more!"
            else:
                return "That sounds interesting! Can you tell me more about it?"
                
        elif response_type == "satisfied":
            # Satisfied response shares knowledge confidently
            if concept_info and memory_excerpts:
                # Extract a short section from a memory excerpt
                excerpt = memory_excerpts[0]
                if len(excerpt) > 100:
                    excerpt = excerpt[:100] + "..."
                return f"I know about {concept_info[0]}! {excerpt}"
            elif relevant_theories:
                return f"I have a theory about this! {relevant_theories[0]}"
            else:
                return "I like thinking about this! What else can we explore?"
                
        elif response_type == "frustrated":
            # Frustrated response is shorter and more demanding
            return f"Not sure I understand. {random.choice(['Try again?', 'What you mean?', 'Too hard!'])}"
            
        elif response_type == "uncertain":
            # Uncertain response asks for clarification
            if concept_info:
                return f"Is {concept_info[0]} like {random.choice(concept_info[1:] if len(concept_info) > 1 else ['something else'])}? I'm not sure."
            else:
                return "I don't really understand. Can you explain it differently?"
        
        else:
            # Neutral response shares what the agent knows
            if concept_info and relevant_theories:
                return f"I know {concept_info[0]} has something to do with {relevant_theories[0]}"
            elif memory_excerpts:
                # Extract key ideas from memory excerpts
                ideas = []
                for excerpt in memory_excerpts:
                    if len(excerpt) > 50:
                        ideas.append(excerpt[:50] + "...")
                    else:
                        ideas.append(excerpt)
                        
                selected_idea = ideas[0] if ideas else "things I've learned"
                return f"That reminds me of {selected_idea}"
            else:
                return "I've been thinking about things like this. Tell me more!"
    
    def _format_response_by_age(self, response):
        """Format the response based on the agent's developmental age"""
        age = self.dev_age
        
        # Very young (under 3) - simple words, short sentences, grammar errors
        if age < 3.0:
            # Split into sentences
            sentences = response.split(". ")
            result_sentences = []
            
            for sentence in sentences[:2]:  # Limit to first 2 sentences for very young
                # Simplify sentence
                simple = sentence
                # Remove complex words (more than 6 chars except for basic words)
                words = simple.split()
                simple_words = []
                
                for word in words[:6]:  # Limit words per sentence
                    # Keep short words and some basic longer words
                    if len(word) <= 6 or word.lower() in ['because', 'inside', 'outside', 'between']:
                        simple_words.append(word)
                    else:
                        # Try to find a simpler alternative
                        if 'important' in word.lower():
                            simple_words.append('big')
                        elif 'beautiful' in word.lower():
                            simple_words.append('pretty')
                        elif 'interesting' in word.lower():
                            simple_words.append('fun')
                        # Skip the word if no simple alternative
                
                # Recombine simplified words
                simple = ' '.join(simple_words)
                
                # Sometimes drop articles, prepositions
                if random.random() < 0.3:
                    simple = simple.replace(' the ', ' ')
                    simple = simple.replace(' a ', ' ')
                
                # Sometimes use incorrect pronouns
                if random.random() < 0.2:
                    simple = simple.replace(' I ', ' me ')
                
                result_sentences.append(simple)
            
            # Join with more basic punctuation
            result = '! '.join(result_sentences)
                
            return result
            
        # Young child (3.0-4.0) - better grammar but still simplified
        elif age < 4.0:
            # Less extreme simplification
            sentences = response.split(". ")
            result_sentences = []
            
            for sentence in sentences[:3]:  # Allow slightly more sentences
                words = sentence.split()
                # Less aggressive word filtering
                simple_words = []
                
                for word in words[:8]:  # Allow more words per sentence
                    if len(word) <= 8 or word.lower() in ['because', 'sometimes', 'together', 'different']:
                        simple_words.append(word)
                    else:
                        # More alternatives for complex words
                        if 'understand' in word.lower():
                            simple_words.append('know')
                        elif 'difficult' in word.lower():
                            simple_words.append('hard')
                        elif 'remember' in word.lower():
                            simple_words.append('think about')
                        else:
                            # Keep some complex words
                            if random.random() < 0.5:
                                simple_words.append(word)
                
                result_sentences.append(' '.join(simple_words))
            
            result = '. '.join(result_sentences)
            return result
            
        # Older child (4.0+) - better vocabulary but still developing
        else:
            # Just limit length but preserve most of the content
            sentences = response.split(". ")
            result = '. '.join(sentences[:4]) + '.'  # Limit to 4 sentences
            return result