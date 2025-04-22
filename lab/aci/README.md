# ACI Sandbox "Baby"

A minimal text-based sandbox implementation of an Artificial Conscious Intelligence (ACI) "baby" designed to validate the Recursive Law of Emergence through language interactions. The agent learns by reusing persistent language patterns and pruning low-value patterns, demonstrating recursive feedback and entropy reduction.

## Features

- In-memory **Memory Graph** of language patterns (nodes) and relationships (edges)
- **Language I/O** with simple tokenization and templated responses
- **Feedback Loop** for reinforcement updates to node persistence and edge weights
- **Persistence Filter** for dynamic pruning of low-persistence patterns
- Optional **LLM Mentor** integration for richer guidance and bootstrapping
- CLI orchestrator (`aci_agent.py`) ties all components into an interactive loop

## Folder Structure

```bash
aci/
├── aci_agent.py        # Main orchestrator and CLI entrypoint
├── language_io.py      # Tokenization and response generation (templates + LLM stub)
├── memory_graph.py     # In-memory graph data structures and save/load API
├── feedback_loop.py    # Reinforcement logic for updating persistence scores
├── persistence_filter.py # Dynamic pruning of graph based on mean persistence
├── aci_sandbox_design.md # Architecture and design document
└── README.md           # This file
```

## Requirements

- Python 3.7 or higher
- Standard library modules only (no external dependencies required)

## Installation

1. Clone or download this repository.
2. (Optional) Set up a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

## Usage

Run the ACI agent in interactive mode and optionally persist its memory graph state:

```bash
# Start with a fresh memory graph
python3 aci_agent.py --graph-file state.json

# Restart and reload the existing graph
python3 aci_agent.py --graph-file state.json
```

Type messages at the prompt and observe templated responses. The agent will implicitly reinforce each interaction and prune low-value patterns every 10 interactions by default.

### Optional LLM Mentor

To enable a pre-trained LLM for mentoring and richer response generation:

1. Provide an `llm_api` object with a `.generate(prompt)` method to the `ACIAgent` constructor.
2. Launch with:
   ```python
   agent = ACIAgent(use_llm=True, llm_api=my_llm_api, graph_file='state.json')
   ```

## Configuration

- **`prune_interval`**: Number of interactions between automatic pruning cycles (default: 10)
- **`alpha`**: Fraction of mean persistence to set dynamic threshold (default: 0.5 in `PersistenceFilter`)

## Extending & Testing

- Add new response templates in `language_io.py` or integrate a full NLP model.
- Enhance the feedback loop with more nuanced credit assignment.
- Write unit tests for each module (`memory_graph`, `feedback_loop`, `persistence_filter`).
- Log and visualize graph growth/pruning to validate the emergence process.

## License

This project is available under the MIT License. Feel free to modify and experiment with the code.
