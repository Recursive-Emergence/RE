from openai import OpenAI

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
        self.system_message = "You are a caring teacher speaking to a curious young learner who wants to grow. Keep your responses short and concise, but ensure they're complete and thoughtful. Aim for clarity and depth rather than length."

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

# Example usage:
# ai = AI()
# print(ai.answer("What's the capital of Canada?"))
# print(ai.answer("Why is it important?")) # Will have context from previous question
# print(ai.reset_conversation()) # Reset history
# print(ai.answer("Tell me about recursion")) # Start new conversation


