# ACI Sandbox Design: Text-Based "Baby"

A concise plan to build a minimal text-based sandbox agent ("baby") that learns through language interactions, testing the recursive emergence theory via pattern reuse and entropy reduction.

## 1. Objectives
- Validate recursive emergence: observe whether language patterns emerge, persist, and seed new structures.
- Minimize compute: use lightweight components to emphasize memory reuse over heavy models.
- Measure and prune: implement metrics and thresholds to manage graph complexity.

## 2. Core Architecture

```
+---------------------+      +-----------------+      +--------------------+
| User / Env         |<---->| Language I/O    |<---->| Agent Orchestrator |
+---------------------+      | (Processor)     |      | (Workflow Glue)    |
                             +-----------------+      +--------------------+
                                                            |
                                                            V
+---------------------+      +-----------------+      +--------------------+
| Persistence Filter  |<---->| Memory Graph    |<---->| Feedback Loop      |
| (Pruning)          |      | (Pattern Store) |      | (Reinforcement)    |
+---------------------+      +-----------------+      +--------------------+
```

## 3. Components

### 3.1 Agent Orchestrator
- Coordinates I/O, graph queries, updates, and pruning triggers.
- Implements the main loop: receive → retrieve → decide → respond → update.

### 3.2 Language I/O (Processor)
- Parses input text into tokens/intents (simple regex or keyword-based).
- Generates replies via templates or small n‑gram lookup.
- **LLM Mentor (Tool)**: an optional plugin that wraps a pre-trained language model API. When active, it provides bootstrapped responses and training signals, especially useful at cold start or sparse interaction.

### 3.3 Memory Graph (Pattern Store)
- Uses an in‑RAM graph (e.g., Python dict or NetworkX).
- **Nodes**: patterns (words/phrases), each with `persistence_score`, timestamps.
- **Edges**: relationships (`follows`, `associated_with`), each with weight.
- Supports CRUD: add, update scores, query by similarity or keyword.

### 3.4 Feedback Loop (Reinforcement)
- On each interaction, adjust `persistence_score` and edge weights:
  - Success → +Δ
  - Failure → –Δ
- Optionally synthesize new nodes for novel successful combinations.

### 3.5 Persistence Filter (Pruning)
- Runs every N interactions.
- Defines dynamic threshold: `θ = α × mean(P)`, where `α ∈ (0,1)`.
- Removes nodes/edges with `P < θ` to cap graph size.

### 3.6 Self-Model ("Me" Module)
- **Responsibility:** Maintain and update an explicit self-model, enabling internal recursive simulations of the agent’s own state and future actions.
- **Data Structures:** A lightweight representation (e.g., subset of MemoryGraph) focused on self-related patterns and state variables.
- **Functionality:**
  - Generate internal prompts (`introspection_tokens`) reflecting current self-state.
  - Simulate responses or predictions about self (future intents, goals).
  - Feed simulation outputs back into the Feedback Loop for self-reinforcement and refining of subjectivity.

## 4. Interaction Workflow (Pseudocode)
```
loop:
  input = LanguageIO.read()
  tokens = LanguageIO.parse(input)
  candidates = MemoryGraph.find(tokens)
  response = Agent.choose(candidates)
  LanguageIO.write(response)
  feedback = getFeedback()
  FeedbackLoop.update(response, feedback)
  introspection_tokens = SelfModel.simulate(tokens)
  FeedbackLoop.update(introspection_tokens, feedback=True)
  if interactionCount % pruneInterval == 0:
    PersistenceFilter.prune()
```  

## 5. Metrics & Validation
- **Graph size**: nodes/edges count over time
- **Mean persistence**: average `P` across nodes
- **Response relevance**: simple user rating or overlap score
- **Emergent patterns**: track multi-step sequences forming new nodes
- **Compute cost**: average CPU and memory per cycle

## 6. Next Steps (Implementation)
1. Create `memory_graph.py`: graph data structures and API.  
2. Build `language_io.py`: parsing and templating, design LLMMentor as a pluggable tool interface.  
3. Implement `feedback_loop.py`: reinforcement logic.  
4. Develop `persistence_filter.py`: dynamic pruning.  
5. Implement `self_model.py`: Me Module for internal self-simulation and introspection.  
6. Extend `aci_agent.py`: support plugging/unplugging the LLM Mentor tool, handle cold start.  
7. Simple CLI for interaction and logging.  
8. Seed initial patterns and templates for core concepts.

## 7. Minimal System Configuration
- **CPU:** Quad‑core CPU  
- **RAM:** 8–16 GB (graph in memory)  
- **Storage:** SSD 100 GB+  
- **GPU:** Optional (not required initially)

This setup emphasizes memory-driven emergence with low compute overhead.
