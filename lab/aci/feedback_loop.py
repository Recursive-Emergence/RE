"""
FeedbackLoop component: reinforcement logic to update memory graph based on interaction outcomes.
"""

class FeedbackLoop:
    def __init__(self, memory_graph, delta=0.1):
        self.memory_graph = memory_graph
        self.delta = delta  # base increment/decrement value

    def update(self, node_ids, feedback):
        """
        Adjust persistence scores and edge weights based on feedback.
        node_ids: list of node IDs involved in the last response
        feedback: boolean or numerical; True/positive or False/negative
        """
        # Determine adjustment sign
        adj = self.delta if feedback else -self.delta
        # Update persistence for each node
        for nid in node_ids:
            self.memory_graph.update_persistence(nid, adj)
        # Update edge weights for consecutive node pairs
        for i in range(len(node_ids) - 1):
            src, tgt = node_ids[i], node_ids[i+1]
            self.memory_graph.add_edge(src, tgt, 'follows', weight=adj)
        return True