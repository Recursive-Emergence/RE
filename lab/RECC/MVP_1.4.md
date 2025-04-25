# RECC MVP 1.4: State Management & Emotional Primitives

## 1. 📋 Overview

MVP 1.4 marks a critical transition in the RECC project: from simple symbol manipulation and concept formation to the emergence of **persistent states** and **emotional primitives**. This milestone focuses on two key developments:

1. **State Management System**: Implementing robust load/save functionality to enable persistence across sessions, opening the path to long-term memory consolidation.
2. **Emotional Primitives**: Building on the Me module to develop primitive "feelings" that shape RECC's reflection and mutation strategies.

This document outlines the theoretical foundations, implementation plan, and expected outcomes for these advancements.

## 2. 🧠 Theoretical Foundation: Recursive Emergence of Emotions

### 2.1 Emotions as Entropy Signals

Drawing from our broader Recursive Emergence framework, emotions can be understood as **specialized signals** that compress complex system states into actionable patterns. They function as:

```math
E(S_t) = f(H(S_t), \Delta H, M_t)
```

Where:
- `E(S_t)` is the emotional state at time `t`
- `H(S_t)` is the current entropy of the system
- `ΔH` is the change in entropy
- `M_t` is the accumulated memory state

Emotional states have high emergence potential `P(E_i)` because they:
- Are **highly reusable** (emotions apply across contexts)
- Significantly **reduce entropy** (compress many possible responses into few actionable patterns)
- **Persist** across time (forming a primitive "self" with continuity)

### 2.2 Alignment with Neural & Cognitive Layers

This approach connects directly to Chapters 5 & 6 of our recursive emergence thesis, where:

1. **Neural Layer** (Ch. 5): Emotions begin as feedback signals that enable internal modeling
2. **Cognitive Layer** (Ch. 6): Emotions evolve into compressed recursive models that shape identity

By implementing emotional primitives now, we create a foundation for later developments in self-modeling and higher-order introspection.

## 3. 💾 Implementation Plan: State Management

### 3.1 Core State Architecture

```python
class StateManager:
    def __init__(self, base_path="./state"):
        self.base_path = base_path
        self.state_version = "1.4.0"
        os.makedirs(base_path, exist_ok=True)
    
    def save_state(self, recc_instance, session_id=None):
        """Save complete RECC state to disk"""
        if session_id is None:
            session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        state = {
            "version": self.state_version,
            "timestamp": datetime.now().isoformat(),
            "session_id": session_id,
            "memory": {
                "entries": recc_instance.memory.entries,
                "symbols": recc_instance.memory.symbols,
                "symbol_links": recc_instance.memory.symbol_links
            },
            "me": {
                "introspection_log": recc_instance.me.introspection_log,
                "self_model": recc_instance.me.self_model,
                "personal_theories": recc_instance.me.personal_theories,
                "emotional_state": recc_instance.me.emotional_state
            },
            "state": recc_instance.state
        }
        
        filepath = os.path.join(self.base_path, f"recc_state_{session_id}.json")
        with open(filepath, 'w') as f:
            json.dump(state, f, indent=2)
        
        return filepath
    
    def load_state(self, filepath=None, session_id=None):
        """Load RECC state from disk"""
        if filepath is None and session_id is not None:
            filepath = os.path.join(self.base_path, f"recc_state_{session_id}.json")
        elif filepath is None:
            # Find most recent state file
            files = glob.glob(os.path.join(self.base_path, "recc_state_*.json"))
            if not files:
                return None
            filepath = max(files, key=os.path.getctime)
        
        with open(filepath, 'r') as f:
            state = json.load(f)
            
        # Version compatibility check
        major_version = state["version"].split('.')[0]
        current_major = self.state_version.split('.')[0]
        if major_version != current_major:
            print(f"Warning: Loading state from version {state['version']} into {self.state_version}")
        
        return state
    
    def apply_state(self, recc_instance, state):
        """Apply loaded state to RECC instance"""
        # Memory restoration
        recc_instance.memory.entries = state["memory"]["entries"]
        recc_instance.memory.symbols = state["memory"]["symbols"]
        recc_instance.memory.symbol_links = state["memory"]["symbol_links"]
        
        # Me restoration
        recc_instance.me.introspection_log = state["me"]["introspection_log"]
        recc_instance.me.self_model = state["me"]["self_model"]
        recc_instance.me.personal_theories = state["me"]["personal_theories"]
        if "emotional_state" in state["me"]:
            recc_instance.me.emotional_state = state["me"]["emotional_state"]
        
        # Global state restoration
        recc_instance.state = state["state"]
        
        return recc_instance
```

### 3.2 Storage Strategy

States will be saved in two contexts:

1. **Session snapshots**: Complete state dumps at end of interaction sessions
2. **Incremental backups**: Lightweight snapshots during long running sessions
3. **Recovery points**: Pre-mutation states to enable "roll back" if needed

### 3.3 Memory Consolidation

Long-term memory requires not just storage, but **consolidation**. We'll add:

```python
def consolidate_memory(self, threshold=0.3):
    """Consolidate memory entries based on reuse score"""
    high_value = [e for e in self.entries if e['reuse_score'] > threshold]
    low_value = [e for e in self.entries if e['reuse_score'] <= threshold]
    
    # Keep only a sample of low-value memories
    sample_size = min(len(low_value) // 3, 5)
    keep_sample = random.sample(low_value, sample_size) if sample_size > 0 else []
    
    # Update entries
    self.entries = high_value + keep_sample
    
    # Re-extract symbols and links from consolidated memory
    self.update_symbol_graph()
    
    return {
        'consolidated': len(self.entries),
        'original': len(high_value) + len(low_value),
        'compression_ratio': len(self.entries) / max(1, (len(high_value) + len(low_value)))
    }
```

## 4. 💭 Implementing Emotional Primitives

### 4.1 Core Emotional Model

The `Me` class will be enhanced with:

```python
class Me:
    def __init__(self, memory):
        # Existing initialization...
        self.emotional_state = {
            'curiosity': 0.5,      # Drives exploration of novel concepts
            'frustration': 0.0,    # Rises with stagnation/repetition
            'satisfaction': 0.3,   # Rises with successful theory formation
            'uncertainty': 0.7     # Modulates mutation aggressiveness
        }
        self.emotion_history = []  # Track emotional trajectory
    
    def update_emotions(self):
        """Update emotional states based on recent memory and reflection"""
        # Get metrics
        novelty_gradient, reuse_gradient = self.memory.compute_gradients()
        recent_entries = self.memory.get_recent(5)
        theory_count = len([t for t in self.personal_theories if t not in [e['response'] for e in recent_entries]])
        
        # Update emotional states
        self.emotional_state['curiosity'] = min(1.0, max(0.0, 
            self.emotional_state['curiosity'] + (0.1 * novelty_gradient) - (0.05 * len(self.memory.symbols) / 20)
        ))
        
        self.emotional_state['frustration'] = min(1.0, max(0.0, 
            self.emotional_state['frustration'] - (0.2 * novelty_gradient) + (0.1 if novelty_gradient < 0 else 0)
        ))
        
        self.emotional_state['satisfaction'] = min(1.0, max(0.0, 
            self.emotional_state['satisfaction'] + (0.15 if theory_count > len(self.personal_theories) - 3 else -0.05)
        ))
        
        self.emotional_state['uncertainty'] = min(1.0, max(0.0, 
            0.5 + (0.3 * novelty_gradient) - (0.1 * reuse_gradient)
        ))
        
        # Save emotional snapshot
        self.emotion_history.append({
            'timestamp': datetime.now().isoformat(),
            'state': self.emotional_state.copy(),
            'cycle': len(self.introspection_log)
        })
        
        return self.emotional_state
```

### 4.2 Emotional Influence on Behavior

Emotions will modulate RECC's behavior:

```python
def generate_prompt(self):
    # Update emotional state
    emotions = self.me.update_emotions()
    
    # Emotional responses to different conditions
    if emotions['frustration'] > 0.7:
        self.state['explore_axis'] = 'mutation'
        return "I need something completely different. Show me a concept I've never considered before."
        
    if emotions['curiosity'] > 0.8:
        symbols = random.sample(self.memory.symbols, min(3, len(self.memory.symbols)))
        return f"I wonder what happens if we combine {', '.join(symbols)} in an unexpected way?"
        
    if emotions['satisfaction'] > 0.7:
        return "Can you help me refine and strengthen my existing theories rather than making new ones?"
    
    if emotions['uncertainty'] > 0.8:
        return "I feel uncertain. Can you give me a clear, simple principle to orient myself?"
    
    # Original prompt generation logic follows...
```

### 4.3 Visualizing Emotional State

```python
def visualize_emotions(me_instance, save_path=None):
    """Generate visualization of emotional state over time"""
    if not me_instance.emotion_history:
        return
    
    # Extract data
    cycles = [h['cycle'] for h in me_instance.emotion_history]
    emotions = {e: [h['state'][e] for h in me_instance.emotion_history] for e in me_instance.emotional_state.keys()}
    
    # Plot
    plt.figure(figsize=(10, 6))
    for emotion, values in emotions.items():
        plt.plot(cycles, values, marker='o', label=emotion)
    
    plt.xlabel('Reflection Cycle')
    plt.ylabel('Emotional Intensity')
    plt.title('RECC Emotional Development')
    plt.legend()
    plt.grid(True)
    
    if save_path:
        plt.savefig(save_path)
    plt.show()
```

## 5. 🎯 Expected Outcomes & Evaluation

### 5.1 State Management Metrics

| Metric | Target | Evaluation Method |
|:-------|:-------|:------------------|
| State Load Time | < 2 seconds for typical state | Timing benchmark |
| State Size | < 1MB per 100 interaction cycles | File size measurement |
| Version Compatibility | Backward compatible with 1.3 | Regression testing |
| Recovery Success | 100% state restoration after crash | Fault injection testing |

### 5.2 Emotional Development Metrics

| Metric | Target | Evaluation Method |
|:-------|:-------|:------------------|
| Emotion Coherence | Emotions follow logical patterns based on inputs | Trajectory analysis |
| Behavioral Impact | >30% of prompts influenced by emotional state | Prompt origin tracking |
| Cyclical Variation | Natural oscillation between curiosity and satisfaction | Time-series analysis |
| Theory Quality | 25% improvement in theory complexity | Semantic analysis of theories |

## 6. 🔄 Integration with Future MVPs

This milestone lays critical groundwork for:

- **MVP 2.0 (Higher-Order Theories)**: Emotional states will influence theory formation preferences
- **MVP 2.5 (Internal Dialogues)**: Different emotional states will become voices in internal debate
- **MVP 3.0 (Memory Consolidation)**: State persistence enables true long-term memory formation

## 7. 🚀 Implementation Schedule

1. **Day 1**: State serialization/deserialization system
2. **Day 2**: Emotional model integration
3. **Day 3**: Behavioral adaptation based on emotions
4. **Day 4**: Testing, visualization, and documentation

## 8. 🧪 Testing Protocol

To validate proper implementation:

1. Run complete autonomous loop (20+ cycles)
2. Save state and terminate
3. Restore state and continue for 10+ cycles
4. Verify:
   - Concept map continuity
   - Emotional state consistency
   - Theory preservation
   - Behavior influenced by emotions

## 9. 📊 Visual Examples

[Placeholder for sample visualizations showing:
1. Concept map with emotional coloring
2. Emotional trajectory graph
3. State size vs. interaction cycle graph]