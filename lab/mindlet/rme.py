import math
from collections import Counter, defaultdict, deque
import random # Added random for motif_resonates placeholder

class RecursiveMemoryEngine:
    """
    Stores motifs, compresses via reuse, and scores based on entropy.
    Corresponds to the original EmergentSet focused on memory.
    """
    def __init__(self, name, elements=None, depth=0, max_depth=3, mode="set"):
        self.name = name
        self.mode = mode  # "set" or "count" - Note: REmindlet primarily used 'set' for memory
        if self.mode == "count":
            # Count mode might be useful for tracking motif frequency directly
            self.elements = dict(elements or {})
        else:
            self.elements = set(elements or [])
        # self.process_fn = process_fn # Removed, evolution logic might be internal or triggered differently
        self.subsets = [] # To track derived sets if using evolve logic
        self.depth = depth
        self.max_depth = max_depth
        self.last_entropy = self.compute_entropy()

    def compute_entropy(self, element_set=None):
        """Computes the Shannon entropy of the token distribution in the memory set."""
        target_set = element_set if element_set is not None else self.elements
        # Flatten the set of tuples into a list of tokens, handling non-tuple elements if any
        tokens = []
        for element in target_set:
            if isinstance(element, tuple):
                tokens.extend(token for token in element if isinstance(token, str)) # Only count string tokens
            elif isinstance(element, str): # Handle potential string elements directly
                 tokens.append(element)
                 
        total_tokens = len(tokens)
        if total_tokens == 0:
            return 0.0 # Entropy is 0 for an empty set or set with no string tokens

        token_counts = Counter(tokens)
        entropy = -sum((count / total_tokens) * math.log2(count / total_tokens) 
                       for count in token_counts.values())
        return entropy

    def update(self, memory_chunk):
        """
        Adds a new chunk of memory (e.g., processed input).
        Placeholder: Simple addition for now. Merge logic handles conditional acceptance.
        Returns the motifs added (or could return change in state).
        """
        # In the new architecture, the decision to add might be external (in the main loop via merge)
        # This update could just prepare the chunk or track frequency if needed.
        # For now, let's assume direct addition for simplicity, mirroring old behavior partly.
        added_motifs = set()
        if isinstance(memory_chunk, (set, list, tuple)):
             for item in memory_chunk:
                 if isinstance(item, tuple): # Ensure motifs are tuples
                     if item not in self.elements:
                         self.elements.add(item)
                         added_motifs.add(item)
        elif isinstance(memory_chunk, tuple): # Single motif
             if memory_chunk not in self.elements:
                 self.elements.add(memory_chunk)
                 added_motifs.add(memory_chunk)
        
        # We might recalculate entropy here or let the main loop do it after updates.
        # self.last_entropy = self.compute_entropy()
        return added_motifs # Return what was actually added

    def merge(self, candidate_set, entropy_reduction, echo_score, threshold, known_motifs):
        """
        Decides whether to integrate a candidate set based on entropy reduction, echo, or resonance.
        Logic migrated and adapted from the original ThoughtThread.
        Returns True if merged, False otherwise.
        """
        # Calculate potential entropy *if* merged
        potential_set = self.elements.union(candidate_set)
        entropy_after_potential_merge = self.compute_entropy(potential_set)
        actual_entropy_reduction = self.last_entropy - entropy_after_potential_merge

        # Check resonance for each candidate motif
        resonates = any(motif_resonates(motif, known_motifs) for motif in candidate_set if isinstance(motif, tuple))

        # --- Merge Decision Logic ---
        # Core condition: Significant entropy reduction OR high echo score
        merge_condition_met = (actual_entropy_reduction > threshold) or (echo_score > 0.7) 
        
        # Resonance Boost: If core condition is borderline, resonance can push it over
        if not merge_condition_met and resonates and (actual_entropy_reduction > (threshold * 0.5) or echo_score > 0.5):
             merge_condition_met = True
             # print("[RME Debug] Resonance boost triggered merge.") # Optional debug

        if merge_condition_met:
            self.elements = potential_set
            self.last_entropy = entropy_after_potential_merge
            # print(f"[RME Debug] Merged. New Entropy: {self.last_entropy:.3f}") # Optional debug
            return True
        else:
            # print(f"[RME Debug] Blocked. ΔH: {actual_entropy_reduction:.3f}, Echo: {echo_score:.3f}, Thr: {threshold:.3f}, Res: {resonates}") # Optional debug
            return False

    def trace_origin(self, motif):
        """
        Placeholder: Trace the lineage of a motif (how it was formed/compressed).
        """
        # TODO: Implement lineage tracking if needed.
        return f"Origin tracking for {motif} not implemented."

    def get_motifs(self):
        """Returns the current set of motifs."""
        return self.elements

    # Optional: Keep evolve logic if needed for internal derivation/compression steps
    # def evolve(self):
    #     """
    #     Internal evolution/derivation based on a process function.
    #     This might be less relevant if derivation is handled by other modules (e.g., IPL).
    #     """
    #     if self.depth >= self.max_depth:
    #         return None
    #     # Requires a process_fn to be defined or passed
    #     # new_elements = self.process_fn(self.elements) if self.process_fn else set()
    #     new_elements = set() # Placeholder
    #     if not new_elements:
    #         return None
    #     # ... (rest of the original evolve logic for creating subsets) ...
    #     return None

# === Helper Functions (Potentially moved here from REmindlet.py) ===

def cluster_motifs(memory_elements):
    """Groups motifs by their first element."""
    clusters = defaultdict(set)
    # Ensure memory_elements is iterable and contains tuples
    if not hasattr(memory_elements, '__iter__'):
        return {} # Return empty dict if not iterable
        
    for motif in memory_elements:
        # Ensure motif is a tuple and has at least 2 elements for head/tail split
        if isinstance(motif, tuple) and len(motif) > 1:
            # Exclude motifs containing '?' if desired (as per original logic)
            if "?" not in motif:
                head, *rest = motif
                clusters[head].update(rest)
    return dict(clusters)

def summarize_memory(memory_elements):
    """Provides a short summary of the most recent stable motifs."""
    if not hasattr(memory_elements, '__iter__'):
        return "(no memory elements)"

    # Filter for tuples, exclude '?', ensure length > 1
    stable_motifs = [m for m in memory_elements if isinstance(m, tuple) and "?" not in m and len(m) > 1]
    
    # Sort by converting tuple to string (simple chronological proxy if added sequentially)
    # A more robust approach might need timestamps if order is critical.
    try:
        # Attempt to sort; might fail if elements are not comparable, though strings should be.
        recent = sorted([" ".join(m) for m in stable_motifs])[-5:]
    except TypeError:
        # Fallback if sorting fails
        recent = [" ".join(m) for m in stable_motifs[-5:]]

    if not recent:
        return "(no stable motifs yet)"
    return "Recently learned: " + "; ".join(recent)


def echo_score(candidate, memory):
    """Calculates the overlap score between candidate motifs and existing memory."""
    if not memory: return 0.0
    flat_memory = {w for m in memory if isinstance(m, tuple) for w in m}
    flat_candidate = {w for m in candidate if isinstance(m, tuple) for w in m}
    if not flat_candidate: return 0.0
    return len(flat_memory & flat_candidate) / len(flat_candidate)

def motif_resonates(candidate_motif, known_motifs, resonance_threshold=0.5):
    """
    Checks if a candidate motif 'resonates' with existing known motifs.
    Placeholder: Simple overlap check. Could be replaced with embedding similarity.
    """
    if not known_motifs: return False # Cannot resonate with nothing
    
    # Simple overlap: Check if any token in the candidate exists in any known motif
    candidate_tokens = set(t for t in candidate_motif if isinstance(t, str)) # Ensure we only check string tokens
    if not candidate_tokens: return False # Empty motif cannot resonate

    for known_motif in known_motifs:
        known_tokens = set(t for t in known_motif if isinstance(t, str))
        if candidate_tokens.intersection(known_tokens):
            # Basic resonance found - could add more complex scoring later
            # For now, any overlap counts as resonance for simplicity
            return True 
            # Example of a score-based approach (if needed later):
            # overlap = len(candidate_tokens.intersection(known_tokens))
            # score = overlap / len(candidate_tokens.union(known_tokens)) # Jaccard index
            # if score >= resonance_threshold:
            #     return True
                
    return False

