"""
Language I/O component: parse user input, generate responses via templates or optional LLM integration.
"""
import re
import random

class LanguageIO:
    def __init__(self, templates=None):
        # Simple response templates keyed by keyword
        self.templates = templates or {
            'hello': ['Hello!', 'Hi there!', 'Greetings!'],
            'hi': ['Hello!', 'Hi!', 'Hey there!'],
            'how': ['I am learning, can you tell me more?', 'Could you rephrase that?'],
            'default': ["Hmm..."]
        }

    def parse(self, text):
        """Tokenize input text into lowercase word tokens."""
        tokens = re.findall(r"\b\w+\b", text.lower())
        return tokens

    def generate_response(self, tokens):
        """Generate a response based on templates matching tokens."""
        for token in tokens:
            if token in self.templates:
                return random.choice(self.templates[token])
        return random.choice(self.templates['default'])

    def read(self, prompt='> '):
        """Read raw input from user."""
        try:
            return input(prompt)
        except EOFError:
            return ''

    def write(self, response):
        """Output response to user."""
        print(response)

class LLMMentor:
    """
    Optional wrapper for a pre-trained LLM to provide mentoring feedback.
    Replace `generate` with actual API call as needed.
    """
    def __init__(self, llm_api):
        self.llm_api = llm_api

    def generate(self, prompt):
        """Generate a response using the LLM API."""
        # Example stub; replace with real API call
        return self.llm_api.generate(prompt)
