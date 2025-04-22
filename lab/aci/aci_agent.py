"""
ACI Agent Orchestrator: integrates LanguageIO, MemoryGraph, FeedbackLoop, and PersistenceFilter into a CLI loop.
"""
from memory_graph import MemoryGraph
from language_io import LanguageIO, LLMMentor
from feedback_loop import FeedbackLoop
from persistence_filter import PersistenceFilter
from self_model import SelfModel
import argparse
import os
import time

class ACIAgent:
    def __init__(self, graph_file=None, use_llm=False, llm_api=None, prune_interval=10, 
                 quiet_reflection_interval=3600):  # Default: reflect once per hour during quiet times
        self.graph_file = graph_file
        # Core components
        if graph_file and os.path.exists(graph_file):
            self.memory_graph = MemoryGraph.load(graph_file)
        else:
            self.memory_graph = MemoryGraph()
        self.lang_io = LanguageIO()
        # Optional LLM mentor
        self.mentor = LLMMentor(llm_api) if use_llm and llm_api else None
        self.feedback = FeedbackLoop(self.memory_graph)
        self.pruner = PersistenceFilter(self.memory_graph)
        # Self Model for introspection
        self.self_model = SelfModel(self.memory_graph)
        # Autonomous learning settings
        self.last_user_interaction = time.time()
        self.last_reflection = time.time()
        self.quiet_reflection_interval = quiet_reflection_interval
        self.user_inactive_threshold = 300  # Consider user inactive after 5 minutes
        # Loop control
        self.interaction_count = 0
        self.prune_interval = prune_interval

    def choose_response(self, tokens):
        # Retrieve or create node IDs for tokens
        node_ids = []
        for token in tokens:
            matches = self.memory_graph.find_nodes_by_keyword(token)
            if matches:
                nid = matches[0]
            else:
                nid = self.memory_graph.add_node(token)
            node_ids.append(nid)
        # Generate response
        if self.mentor:
            prompt = " ".join(tokens)
            response = self.mentor.generate(prompt)
            # Record mentor interaction for pattern extraction
            self.self_model.record_mentor_interaction(tokens, response)
        else:
            response = self.lang_io.generate_response(tokens)
        return response, node_ids

    def check_for_autonomous_learning(self):
        """
        During quiet periods (no user interaction), initiate autonomous learning
        by having internal reflection dialogues with the LLM mentor.
        """
        current_time = time.time()
        
        # Only proceed if we have an LLM mentor and enough time has passed
        if not self.mentor:
            return
            
        # Check if the user has been inactive and it's time for reflection
        user_inactive = (current_time - self.last_user_interaction) > self.user_inactive_threshold
        reflection_due = (current_time - self.last_reflection) > self.quiet_reflection_interval
        
        if user_inactive and reflection_due:
            # Generate a reflection prompt based on current knowledge
            reflection_prompt = self.self_model.generate_reflection_prompt()
            tokens = self.lang_io.parse(reflection_prompt)
            
            print(f"\n[Internal reflection: {reflection_prompt}]")
            
            # Get mentor response to this reflection
            response, node_ids = self.choose_response(tokens)
            
            print(f"[Mentor response: {response}]")
            
            # Process this as a normal interaction (update persistence, etc.)
            self.feedback.update(node_ids, feedback=True)
            introspection_tokens = self.self_model.simulate(tokens)
            self.feedback.update(introspection_tokens, feedback=True)
            
            # Update reflection timestamp
            self.last_reflection = current_time
            
            # Save after autonomous learning
            if self.graph_file:
                self.memory_graph.save(self.graph_file)
                print(f"[Memory graph saved after reflection]")

    def run(self):
        print("ACI Agent started. Type 'exit' to quit.")
        while True:
            # Check for autonomous learning first
            self.check_for_autonomous_learning()
            
            user_input = self.lang_io.read()
            self.last_user_interaction = time.time()  # Update last interaction time
            
            if not user_input or user_input.strip().lower() == 'exit':
                print("Goodbye!")
                break
                
            tokens = self.lang_io.parse(user_input)
            response, node_ids = self.choose_response(tokens)
            self.lang_io.write(response)
            # Implicit positive feedback for every interaction
            self.feedback.update(node_ids, feedback=True)
            # Internal introspection and self-reinforcement
            introspection_tokens = self.self_model.simulate(tokens)
            self.feedback.update(introspection_tokens, feedback=True)
            self.interaction_count += 1
            # Periodic pruning
            if self.interaction_count % self.prune_interval == 0:
                pruned = self.pruner.prune()
                print(f"[Pruned {pruned} low-persistence nodes]")
                # Auto-save after pruning
                if self.graph_file:
                    self.memory_graph.save(self.graph_file)
                    print(f"[Memory graph saved to {self.graph_file}]")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ACI Agent')
    parser.add_argument('--graph-file', type=str, help='Path to load/save memory graph JSON')
    parser.add_argument('--use-llm', action='store_true', help='Enable LLM mentor for bootstrapped training')
    args = parser.parse_args()
    agent = ACIAgent(graph_file=args.graph_file, use_llm=args.use_llm)
    try:
        agent.run()
    finally:
        if agent.graph_file:
            agent.memory_graph.save(agent.graph_file)
            print(f"Memory graph saved to {agent.graph_file}")