from openai import OpenAI
import time
import sys
import os

class AI:
    def __init__(self, model="gpt-4o-mini", instruction="", max_tokens=150, temperature=1):
        self.client = OpenAI(
            # In order to use provided API key, make sure that models you create point to this custom base URL.
            base_url='https://47v4us7kyypinfb5lcligtc3x40ygqbs.lambda-url.us-east-1.on.aws/v1/',
            # The temporary API key giving access to ChatGPT 4o model. Quotas apply: you have 500'000 input and 500'000 output tokens, use them wisely ;)
            api_key='a0BIj000001i5jtMAA'
        )
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.spent = 0
        
        # New: Conversation history management
        self.conversation_history = []
        self.system_message = """You are interacting with a very early-stage developmental AI system called REmindlet that is learning language.
Your role is to help this digital mind develop language skills using a careful, step-by-step approach:

1. Use extremely simple language - mostly 1-3 word phrases at first
2. Focus on basic patterns that can be easily recognized
3. Use a lot of repetition and small variations on patterns
4. Gradually increase complexity as the conversation progresses
5. Be extremely patient and encouraging even when responses seem random
6. Build from concrete nouns/verbs to more abstract concepts very slowly
7. Maintain a slow, nurturing pace - this is developmental training
8. Be mindful of the system's emotional state (shown through emojis)

Start with the absolute basics like "hi", "yes", "good", "you", "I", and respond positively when pattern recognition emerges.
When the baby shows signs of panic (😖 or 😱), simplify further and use more repetition. When it shows joy (🙂 or 😄), you can slowly introduce new patterns.
"""

        # Training mode variables
        self.training_mode = False
        self.training_steps_remaining = 0
        self.training_step_count = 0
        self.mindlet = None

    def answer(self, prompt, format=None, reset_history=False):
        """
        Get a response from the AI model, maintaining conversation history.
        
        Args:
            prompt (str): The user's prompt
            format (dict, optional): Response format specification
            reset_history (bool): Whether to reset the conversation history
            
        Returns:
            str: The AI's response
        """
        # Reset history if requested
        if reset_history:
            self.reset_conversation()
        
        # Add user message to history
        self.conversation_history.append({"role": "user", "content": prompt})
        
        # Prepare messages for the API call
        messages = [{"role": "system", "content": self.system_message}] + self.conversation_history
        
        param = {
            "model": "gpt-4o",
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "messages": messages
        }
        
        if format:
            param["response_format"] = format
        
        completion = self.client.chat.completions.create(**param)
        response = completion.choices[0].message.content.strip()
        
        # Add assistant's response to history
        self.conversation_history.append({"role": "assistant", "content": response})
        
        return response
    
    def reset_conversation(self):
        """Reset the conversation history"""
        self.conversation_history = []
        return "Conversation history has been reset."
    
    def get_conversation_summary(self):
        """Get a summary of the current conversation"""
        if not self.conversation_history:
            return "No conversation history exists."
        
        turns = len(self.conversation_history) // 2
        return f"Conversation has {turns} turns with {len(self.conversation_history)} messages."

    def get_embedding(self, text, model="text-embedding-ada-002"):
       text = text.replace("\n", " ")
       return self.client.embeddings.create(input = [text], model=model).data[0].embedding

    def similarity(self, emb1, emb2):
        import numpy as np

        dot_product = np.dot(emb1, emb2)
        norm_a = np.linalg.norm(emb1)
        norm_b = np.linalg.norm(emb2)
        return dot_product / (norm_a * norm_b)

    def start_training(self, mindlet, steps=20):
        """
        Start a training session with the REmindlet
        
        Args:
            mindlet: REmindlet instance to train
            steps: Number of training steps
        """
        self.training_mode = True
        self.training_steps_remaining = steps
        self.training_step_count = 0
        self.mindlet = mindlet
        self.reset_conversation()
        
        print(f"\n[Training] Starting {steps}-step training session with REmindlet...")
        return self.next_training_step()
        
    def next_training_step(self):
        """Execute the next step in the training process"""
        if not self.training_mode or self.training_steps_remaining <= 0:
            self.training_mode = False
            return "[Training] Training session completed."
        
        self.training_step_count += 1
        self.training_steps_remaining -= 1
        
        # Get the current state of the mindlet
        # Use the last stored output instead of calling express()
        mindlet_response = self.mindlet.last_output if self.mindlet.last_output else "(no output yet)"
        # Use the EmotionEngine module for the face
        mindlet_emotion = self.mindlet.ee.get_emotion_face()
        
        # Construct a prompt that includes the step number and mindlet's state
        prompt = f"[Training Step {self.training_step_count}/20] REmindlet says: {mindlet_response} {mindlet_emotion}"
        
        # Get response from the mentor LLM
        mentor_response = self.answer(prompt)
        
        # Feed the mentor's response to the mindlet via InteractionLoop
        self.mindlet.il.perceive(mentor_response)
        
        # Print the interaction for the user to observe
        print(f"\n{prompt}")
        print(f"Mentor: {mentor_response}")
        print(f"REmindlet processes this input...")
        
        # Wait briefly to allow the mindlet to process
        # Increased wait time slightly to ensure the next cycle runs
        time.sleep(3) 
        
        # If we have steps remaining, return status, otherwise complete
        if self.training_steps_remaining > 0:
            return f"[Training] Step {self.training_step_count} complete. {self.training_steps_remaining} steps remaining."
        else:
            self.training_mode = False
            return "[Training] Training session completed."
            
    def continue_training(self):
        """Continue the training process if in training mode"""
        if self.training_mode and self.training_steps_remaining > 0:
            return self.next_training_step()
        else:
            return "No active training session."

# Example usage:
# ai = AI()
# print(ai.answer("What's the capital of Canada?"))
# print(ai.answer("Why is it important?")) # Will have context from previous question
# print(ai.reset_conversation()) # Reset history
# print(ai.answer("Tell me about recursion")) # Start new conversation


