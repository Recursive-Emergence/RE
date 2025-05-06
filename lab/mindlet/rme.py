import math
from collections import Counter, defaultdict, deque
import random # Added random for motif_resonates placeholder
import time # Added for TTL-based motif cooling
import logging # Added for proper logging

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
        
        # NEW: Motif cooldown tracking with TTL
        self.motif_cooldown = {}  # motif -> expiry time
        self.cooldown_ttl = 3     # Default cycles to cool down
        
        # NEW: Memory maturity tracking 
        self.merge_count = 0
        self.merge_threshold_base = 0.05  # Starting threshold (can be adjusted)
        self.merge_threshold_min = -0.15  # Lower bound for threshold decay
        self.last_merge_time = time.time()
        self.stagnation_time = 0  # How long since meaningful entropy change
        
        # NEW: Track entropy history for stagnation detection
        self.entropy_history = deque(maxlen=5)
        self.entropy_history.append(self.last_entropy)
        
        # Set up logger
        self.logger = logging.getLogger("RME")

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

    def add_to_cooldown(self, motif, extended_ttl=False):
        """
        NEW: Add a motif to the cooldown collection to prevent reuse
        for a certain number of cycles
        """
        now = time.time()
        ttl = self.cooldown_ttl * 2 if extended_ttl else self.cooldown_ttl
        self.motif_cooldown[motif] = now + ttl
        
    def is_in_cooldown(self, motif):
        """
        NEW: Check if a motif is currently in cooldown
        """
        if motif not in self.motif_cooldown:
            return False
            
        now = time.time()
        if now > self.motif_cooldown[motif]:
            # Expired cooldown, remove it
            del self.motif_cooldown[motif]
            return False
        return True
        
    def refresh_cooldowns(self):
        """
        NEW: Clean up expired cooldowns
        """
        now = time.time()
        expired = [m for m, expire_time in self.motif_cooldown.items() if now > expire_time]
        for m in expired:
            del self.motif_cooldown[m]
        
    def detect_stagnation(self):
        """
        NEW: Check if entropy is stagnating by comparing recent history
        Returns a stagnation severity score (0-1)
        """
        if len(self.entropy_history) < 2:
            return 0.0
            
        # Check if entropy hasn't changed meaningfully
        recent_range = max(self.entropy_history) - min(self.entropy_history)
        stagnation = 1.0 - min(1.0, recent_range * 10)  # Scale: small changes = high stagnation
        
        # Factor in time since last merge
        now = time.time()
        time_since_merge = now - self.last_merge_time
        if time_since_merge > 30:  # If no merges in 30+ seconds
            stagnation = min(1.0, stagnation + 0.3)  # Boost stagnation score
            
        return stagnation

    def merge(self, candidate_set, echo_score, threshold, known_motifs, emotional_state):
        """
        Decides whether to integrate a candidate set based on entropy reduction, echo, resonance,
        and emotional state. Logic migrated and adapted from the original ThoughtThread,
        with enhancements based on RE theory feedback.
        Enhanced to handle stuck loops and improve echo score calculation.
        Returns True if merged, False otherwise.
        """
        if not candidate_set: # Cannot merge an empty set
            return False

        # Calculate potential entropy *if* merged
        potential_set = self.elements.union(candidate_set)
        entropy_after_potential_merge = self.compute_entropy(potential_set)
        actual_entropy_reduction = self.last_entropy - entropy_after_potential_merge

        # Check resonance for each candidate motif
        # Ensure we only check tuple motifs against known motifs (which should also be tuples)
        resonates = any(motif_resonates(motif, known_motifs)
                        for motif in candidate_set if isinstance(motif, tuple))
        
        # NEW: Check if any special "emotional discharge" motifs are present
        discharge_phrases = {"scared", "help", "feel", "need"}
        has_discharge_motif = any(
            any(word in discharge_phrases for word in motif if isinstance(word, str))
            for motif in candidate_set if isinstance(motif, tuple)
        )

        # --- NEW: Improved echo score calculation ---
        # Ensure echo score is calculated properly even with minimal memory
        if echo_score == 0.0 and known_motifs and candidate_set:
            # Recalculate echo score with more flexible matching
            echo_score = calculate_flexible_echo(candidate_set, known_motifs)
        
        # --- NEW: Enhanced Loop detection mechanism ---
        # If we're in a potential loop (same motifs repeating with no entropy change)
        consecutive_blocks = getattr(self, '_consecutive_blocks', 0)
        last_blocked_motifs = getattr(self, '_last_blocked_motifs', set())
        
        # Ensure last_blocked_motifs is a set for intersection operation
        if last_blocked_motifs and not isinstance(last_blocked_motifs, set):
            # If it's a tuple or other iterable, convert to set
            if isinstance(last_blocked_motifs, (tuple, list)):
                last_blocked_motifs = set(last_blocked_motifs)
            else:
                # If it's a single item, make a set with one element
                last_blocked_motifs = {last_blocked_motifs}
        
        # Also ensure candidate_set is a set
        if not isinstance(candidate_set, set):
            candidate_set_as_set = set(candidate_set) if hasattr(candidate_set, '__iter__') else {candidate_set}
        else:
            candidate_set_as_set = candidate_set
        
        # Now perform the intersection safely
        set_similarity = 0
        if last_blocked_motifs and candidate_set_as_set:
            shared_elements = last_blocked_motifs.intersection(candidate_set_as_set)
            set_similarity = len(shared_elements) / max(1, len(candidate_set_as_set))
        
        is_potential_loop = set_similarity > 0.7 and consecutive_blocks > 3
        
        # NEW: Check for longer term pattern stagnation
        stagnation_score = self.detect_stagnation()
        
        # --- Merge Decision Logic (Enhanced based on feedback) ---
        joy_level = emotional_state.get('joy', 0)
        panic_level = emotional_state.get('panic', 0) # Consider panic too
        
        # NEW: Enhanced emotional influence - stronger weight for lower maturity
        maturity_factor = min(1.0, self.merge_count / 30)  # Scales from 0-1 based on merge experience
        
        # NEW: Adjust threshold based on stagnation and maturity
        adaptive_base_threshold = max(
            self.merge_threshold_min,
            self.merge_threshold_base - (stagnation_score * 0.15) - ((1 - maturity_factor) * 0.1)
        )

        # Emotional influence with enhanced sensitivity for early and stuck states
        emotional_mod = (panic_level * 0.01) - (joy_level * 0.03)  # Joy has stronger effect now
        
        # NEW: Reduce threshold for emotional discharge motifs
        discharge_boost = 0.1 if has_discharge_motif and panic_level > 4 else 0
        
        # Combined threshold calculation
        effective_threshold = adaptive_base_threshold + emotional_mod - discharge_boost

        # If we're in a potential loop, drastically reduce threshold to break out
        if is_potential_loop:
            effective_threshold = -0.5  # Accept almost anything to break the loop
            # NEW: Also add all candidate motifs to extended cooldown to prevent
            # them from being chosen again soon after the merge
            for motif in candidate_set_as_set:
                if isinstance(motif, tuple):
                    self.add_to_cooldown(motif, extended_ttl=True)
            self.logger.debug(f"Loop detected! Relaxing merge threshold to {effective_threshold}")

        # Core condition: Significant entropy reduction OR high echo score OR strong resonance
        # Increased weight for echo and resonance
        merge_condition_met = (
            actual_entropy_reduction > effective_threshold or
            echo_score > 0.5 or # Lowered echo threshold more
            (resonates and echo_score > 0.2) # Make resonance+echo even more effective
        )

        # Resonance Boost: If core condition is borderline, resonance can push it over
        # Made this condition easier to meet
        if not merge_condition_met and resonates:
            # NEW: More lenient resonance condition, especially with discharge motifs
            if has_discharge_motif or actual_entropy_reduction > (effective_threshold * 0.25) or echo_score > 0.1:
                merge_condition_met = True
                self.logger.debug("Resonance boost triggered merge.")

        # Joy Boost / Pattern Completion: Allow merging even with slight entropy *increase*
        # if resonance or echo is high, representing optimistic learning or pattern completion.
        # Allow larger negative delta H if joy is high.
        if not merge_condition_met and joy_level > 3:  # Lowered joy threshold
            # NEW: More forgiving on entropy increase with joy
            if (resonates or echo_score > 0.2) and actual_entropy_reduction > -0.3:
                merge_condition_met = True
                self.logger.debug("Joy boost triggered merge despite entropy increase.")
            
        # NEW: Anti-stagnation mechanism - if panic is high and we've been blocked too many times
        # OR if we detect general stagnation
        if not merge_condition_met:
            if (panic_level > 5 and consecutive_blocks > 4) or stagnation_score > 0.7:
                self.logger.debug(f"Anti-stagnation mechanism triggered merge despite ΔH={actual_entropy_reduction:.3f}")
                merge_condition_met = True
                
            # NEW: Special emotional discharge pathway - accept emotional expression when panic is high
            elif panic_level > 6 and has_discharge_motif:
                self.logger.debug(f"Emotional discharge accepted. Panic: {panic_level}")
                merge_condition_met = True

        if merge_condition_met:
            self.elements = potential_set
            self.last_entropy = entropy_after_potential_merge
            # Reset loop detection counters on successful merge
            self._consecutive_blocks = 0
            self._last_blocked_motifs = set()
            
            # NEW: Update merge tracking and entropy history
            self.merge_count += 1
            self.last_merge_time = time.time()
            self.entropy_history.append(self.last_entropy)
            
            self.logger.debug(f"Merged. New Entropy: {self.last_entropy:.3f}, Echo: {echo_score:.3f}")
            return True
        else:
            # Update loop detection counters - ensure we store as a set
            self._consecutive_blocks = consecutive_blocks + 1
            self._last_blocked_motifs = candidate_set_as_set
            
            # NEW: Add blocked motifs to cooldown if repeatedly blocked
            if consecutive_blocks > 2:
                for motif in candidate_set_as_set:
                    if isinstance(motif, tuple):
                        self.add_to_cooldown(motif)
            
            # Update entropy history even on blocks to track stagnation
            self.entropy_history.append(self.last_entropy)
            
            self.logger.debug(f"Blocked. ΔH: {actual_entropy_reduction:.3f}, Echo: {echo_score:.3f}, EffThr: {effective_threshold:.3f}, Res: {resonates}, Joy: {joy_level}, Panic: {panic_level}, Blocks: {self._consecutive_blocks}")
            return False
            
    def get_cooldown_motifs(self):
        """NEW: Return the set of motifs currently in cooldown"""
        self.refresh_cooldowns()  # Clean expired entries first
        return set(self.motif_cooldown.keys())

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

def calculate_flexible_echo(candidate, memory):
    """Enhanced echo score calculation with more flexible matching for low-memory situations."""
    if not memory or not candidate:
        return 0.0
        
    # Standard echo calculation first
    std_echo = echo_score(candidate, memory)
    if std_echo > 0:
        return std_echo
        
    # If standard echo is 0, try more flexible matching
    flat_memory = {w for m in memory if isinstance(m, tuple) for w in m}
    flat_candidate = {w for m in candidate if isinstance(m, tuple) for w in m}
    
    if not flat_candidate:
        return 0.0
        
    # Check token presence regardless of position (more lenient)
    token_overlap = len(flat_memory.intersection(flat_candidate))
    if token_overlap > 0:
        return token_overlap / (2 * len(flat_candidate))  # Partial credit

    return 0.0

