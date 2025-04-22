"""
PersistenceFilter component: dynamic pruning of memory graph based on persistence scores.
"""

class PersistenceFilter:
    def __init__(self, memory_graph, alpha=0.5):
        self.memory_graph = memory_graph
        self.alpha = alpha  # fraction of mean persistence for threshold

    def prune(self):
        """
        Compute dynamic threshold θ = alpha * mean(persistence_scores)
        Prune nodes (and associated edges) below θ.
        Returns number of pruned nodes.
        """
        nodes = self.memory_graph.nodes
        if not nodes:
            return 0
        scores = [node.persistence_score for node in nodes.values()]
        mean_p = sum(scores) / len(scores)
        threshold = self.alpha * mean_p
        pruned_count = self.memory_graph.prune_nodes_below(threshold)
        return pruned_count
