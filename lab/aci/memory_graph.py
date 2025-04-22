"""
MemoryGraph component: in-memory graph of language patterns with persistence and relationships.
"""
import time
import uuid
import json

class Node:
    def __init__(self, content):
        self.pattern_id = str(uuid.uuid4())
        self.content = content
        self.persistence_score = 1.0
        self.creation_timestamp = time.time()
        self.last_used_timestamp = self.creation_timestamp

class Edge:
    def __init__(self, source_id, target_id, relationship_type, weight=1.0):
        self.source_id = source_id
        self.target_id = target_id
        self.relationship_type = relationship_type
        self.weight = weight

class MemoryGraph:
    def __init__(self):
        # nodes: id -> Node
        self.nodes = {}
        # edges: (source_id, target_id, relationship_type) -> Edge
        self.edges = {}

    def add_node(self, content):
        """Create and store a new pattern node."""
        node = Node(content)
        self.nodes[node.pattern_id] = node
        return node.pattern_id

    def update_persistence(self, node_id, delta):
        """Adjust a node's persistence score and timestamp."""
        node = self.nodes.get(node_id)
        if not node:
            return False
        node.persistence_score += delta
        node.last_used_timestamp = time.time()
        return True

    def add_edge(self, source_id, target_id, relationship_type, weight=1.0):
        """Create or update an edge between two nodes."""
        key = (source_id, target_id, relationship_type)
        if key in self.edges:
            self.edges[key].weight += weight
        else:
            self.edges[key] = Edge(source_id, target_id, relationship_type, weight)
        return key

    def update_edge_weight(self, source_id, target_id, relationship_type, delta):
        """Adjust weight of an existing edge."""
        key = (source_id, target_id, relationship_type)
        edge = self.edges.get(key)
        if not edge:
            return False
        edge.weight += delta
        return True

    def get_node(self, node_id):
        """Retrieve a node by its ID."""
        return self.nodes.get(node_id)

    def find_nodes_by_keyword(self, keyword):
        """Return node IDs whose content contains the given keyword."""
        return [nid for nid, node in self.nodes.items() if keyword.lower() in node.content.lower()]

    def get_neighbors(self, node_id):
        """Fetch target node IDs for edges originating from the given node."""
        return [edge.target_id for edge in self.edges.values() if edge.source_id == node_id]

    def remove_node(self, node_id):
        """Remove a node and its associated edges."""
        if node_id not in self.nodes:
            return False
        del self.nodes[node_id]
        keys_to_remove = [k for k in self.edges if k[0] == node_id or k[1] == node_id]
        for k in keys_to_remove:
            del self.edges[k]
        return True

    def prune_nodes_below(self, threshold):
        """Prune nodes and edges with persistence_score < threshold."""
        to_remove = [nid for nid, node in self.nodes.items() if node.persistence_score < threshold]
        for nid in to_remove:
            self.remove_node(nid)
        return len(to_remove)

    def save(self, filepath):
        """
        Serialize the memory graph (nodes and edges) to a JSON file.
        """
        data = {
            "nodes": [
                {
                    "pattern_id": nid,
                    "content": node.content,
                    "persistence_score": node.persistence_score,
                    "creation_timestamp": node.creation_timestamp,
                    "last_used_timestamp": node.last_used_timestamp
                }
                for nid, node in self.nodes.items()
            ],
            "edges": [
                {
                    "source_id": edge.source_id,
                    "target_id": edge.target_id,
                    "relationship_type": edge.relationship_type,
                    "weight": edge.weight
                }
                for edge in self.edges.values()
            ]
        }
        with open(filepath, 'w') as f:
            json.dump(data, f)

    @classmethod
    def load(cls, filepath):
        """
        Load a memory graph from a JSON file and return a MemoryGraph instance.
        """
        with open(filepath, 'r') as f:
            data = json.load(f)
        mg = cls()
        # Recreate nodes
        for n in data.get('nodes', []):
            node = Node(n['content'])
            node.pattern_id = n['pattern_id']
            node.persistence_score = n['persistence_score']
            node.creation_timestamp = n['creation_timestamp']
            node.last_used_timestamp = n['last_used_timestamp']
            mg.nodes[node.pattern_id] = node
        # Recreate edges
        for e in data.get('edges', []):
            key = (e['source_id'], e['target_id'], e['relationship_type'])
            mg.edges[key] = Edge(e['source_id'], e['target_id'], e['relationship_type'], e['weight'])
        return mg
