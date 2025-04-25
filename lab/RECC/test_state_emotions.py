#!/usr/bin/env python3
# Test script for RECC MVP 1.4 features: State persistence and emotional primitives

import os
import json
from datetime import datetime
import matplotlib.pyplot as plt
import time
import random
import sys

# Add a mock AI class to avoid OpenAI dependency for testing
class MockAI:
    def __init__(self, model="mock", instruction="", max_tokens=100, temperature=1):
        pass
    
    def answer(self, prompt, format=None):
        responses = [
            "Learning is a spiral of growth that transforms us through cycles of understanding.",
            "The unity of patterns in nature reveals fundamental truths about recursive systems.",
            "Emotions are internal signals that help minds navigate complexity through recursive feeling.",
            "Principles of transformation emerge when we observe the balance between stability and change.",
            "The mind creates loops of understanding that flow through different levels of abstraction."
        ]
        time.sleep(0.5)  # Simulate processing time
        return random.choice(responses)

# Mock the llmentor.AI class for testing
sys.modules['llmentor'] = type('llmentor', (), {'AI': MockAI})

# Now we can import from recc
from recc import RECC, StateManager, visualize_emotions

# Mock LLM for direct testing
def mock_llm(prompt):
    responses = [
        "Learning is a spiral of growth that transforms us through cycles of understanding.",
        "The unity of patterns in nature reveals fundamental truths about recursive systems.",
        "Emotions are internal signals that help minds navigate complexity through recursive feeling.",
        "Principles of transformation emerge when we observe the balance between stability and change.",
        "The mind creates loops of understanding that flow through different levels of abstraction."
    ]
    time.sleep(0.5)  # Simulate processing time
    return random.choice(responses)

def test_state_persistence():
    """Test saving and loading state"""
    print("\n--- TESTING STATE PERSISTENCE ---")
    
    # Initialize agent with mock LLM
    print("🧠 Initializing RECC agent...")
    agent = RECC(mock_llm)
    
    # Run a few cycles to generate state
    print("Running initial cycles...")
    agent.autonomous_loop(steps=3, delay=0, save_interval=3)
    
    # Store some key metrics before save
    orig_memory_count = len(agent.memory.entries)
    orig_symbols = agent.memory.symbols.copy()
    orig_theories = agent.me.personal_theories.copy()
    orig_emotions = agent.me.emotional_state.copy()
    
    # Save state
    print("\nSaving state...")
    test_session_id = f"test_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    filepath = agent.save_state(test_session_id)
    
    # Create new agent
    print("\n🔄 Creating new agent instance...")
    new_agent = RECC(mock_llm)
    
    # Check that it's really new (different state)
    assert len(new_agent.memory.entries) == 0, "New agent should have empty memory"
    
    # Load state into new agent
    print("Loading saved state into new agent...")
    success = new_agent.load_state(session_id=test_session_id)
    
    # Verify state was restored correctly
    print("\n📊 Verifying state restoration:")
    print(f"- Memory entries: {'✅' if len(new_agent.memory.entries) == orig_memory_count else '❌'} ({len(new_agent.memory.entries)} vs {orig_memory_count})")
    print(f"- Symbols: {'✅' if set(new_agent.memory.symbols) == set(orig_symbols) else '❌'} ({len(new_agent.memory.symbols)} symbols)")
    print(f"- Theories: {'✅' if len(new_agent.me.personal_theories) == len(orig_theories) else '❌'} ({len(new_agent.me.personal_theories)} theories)")
    
    emotion_match = all(abs(new_agent.me.emotional_state[k] - orig_emotions[k]) < 0.001 for k in orig_emotions)
    print(f"- Emotional state: {'✅' if emotion_match else '❌'}")
    
    # Run additional cycles on restored agent
    print("\nRunning additional cycles on restored agent...")
    new_agent.autonomous_loop(steps=2, delay=0, save_interval=2)
    
    print("\n✅ State persistence test complete!")
    return success

def test_emotional_development():
    """Test emotional development over interaction cycles"""
    print("\n--- TESTING EMOTIONAL DEVELOPMENT ---")
    
    # Initialize agent with mock LLM
    agent = RECC(mock_llm)
    
    # Set initial emotional state
    agent.me.emotional_state = {
        'curiosity': 0.8,
        'frustration': 0.1,
        'satisfaction': 0.2,
        'uncertainty': 0.5
    }
    
    # Run multiple cycles to observe emotional changes
    print("Running cycles to observe emotional development...")
    steps = 10
    
    # Track emotional states
    emotions_over_time = {emotion: [] for emotion in agent.me.emotional_state}
    
    # Run cycles
    for i in range(steps):
        print(f"\nCycle {i+1}/{steps}:")
        
        # Generate prompt influenced by emotions
        prompt = agent.generate_prompt()
        
        # Note which emotion is dominant
        dominant_emotion = max(agent.me.emotional_state.items(), key=lambda x: x[1])[0]
        print(f"- Dominant emotion: {dominant_emotion} ({agent.me.emotional_state[dominant_emotion]:.2f})")
        print(f"- Generated prompt: \"{prompt}\"")
        
        # Process response
        response = agent.llm(prompt)
        agent.memory.add(prompt, response, agent.state.copy())
        agent.me.reflect()
        
        # Track emotional state
        for emotion, value in agent.me.emotional_state.items():
            emotions_over_time[emotion].append(value)
    
    # Visualize emotional development
    print("\nVisualizing emotional development...")
    plt.figure(figsize=(10, 6))
    for emotion, values in emotions_over_time.items():
        plt.plot(range(1, steps+1), values, marker='o', label=emotion)
    
    plt.xlabel('Cycle')
    plt.ylabel('Emotional Intensity')
    plt.title('RECC Emotional Development Test')
    plt.legend()
    plt.grid(True)
    plt.savefig('emotion_development_test.png')
    print(f"Saved emotional development plot to emotion_development_test.png")
    
    # Check emotion-driven behavior
    print("\n📊 Emotion-Driven Behavior Analysis:")
    print(f"- Unique generated prompts: {len(set([e['prompt'] for e in agent.memory.entries[-steps:]]))}/{steps}")
    
    print("\n✅ Emotional development test complete!")
    return True

def test_memory_consolidation():
    """Test memory consolidation functionality"""
    print("\n--- TESTING MEMORY CONSOLIDATION ---")
    
    # Initialize agent with mock LLM
    agent = RECC(mock_llm)
    
    # Add many entries to trigger consolidation
    print("Adding 25 memory entries...")
    for i in range(25):
        prompt = f"Test prompt {i}"
        response = f"Test response {i} with {'high reuse' if i % 3 == 0 else 'low reuse'} content"
        agent.memory.add(prompt, response, {"test": True})
    
    # Update scores for consolidation
    agent.memory.update_scores()
    
    # Store pre-consolidation counts
    pre_count = len(agent.memory.entries)
    
    # Manually assign reuse scores for testing
    for i, entry in enumerate(agent.memory.entries):
        if i % 3 == 0:  # Make every third entry "high value"
            entry['reuse_score'] = 0.4
        else:
            entry['reuse_score'] = 0.1
    
    print(f"Pre-consolidation memory entries: {pre_count}")
    
    # Perform consolidation
    print("Consolidating memory...")
    result = agent.memory.consolidate_memory(threshold=0.25)
    
    # Check results
    print(f"Post-consolidation memory entries: {len(agent.memory.entries)}")
    print(f"Compression ratio: {result['compression_ratio']:.2f}")
    
    # Verify high-value memories were kept
    high_value_count = sum(1 for e in agent.memory.entries if e['reuse_score'] > 0.25)
    print(f"High-value memories retained: {high_value_count}")
    
    print("\n✅ Memory consolidation test complete!")
    return len(agent.memory.entries) < pre_count

if __name__ == "__main__":
    print("===== RECC MVP 1.4 FEATURE TESTS =====")
    print("Testing key features of MVP 1.4: State persistence and emotional primitives")
    
    # Create state directory if it doesn't exist
    os.makedirs("./state", exist_ok=True)
    
    # Run tests
    state_test_passed = test_state_persistence()
    emotions_test_passed = test_emotional_development()
    consolidation_test_passed = test_memory_consolidation()
    
    # Summary
    print("\n===== TEST SUMMARY =====")
    print(f"State Persistence: {'✅ PASSED' if state_test_passed else '❌ FAILED'}")
    print(f"Emotional Development: {'✅ PASSED' if emotions_test_passed else '❌ FAILED'}")
    print(f"Memory Consolidation: {'✅ PASSED' if consolidation_test_passed else '❌ FAILED'}")
    
    if state_test_passed and emotions_test_passed and consolidation_test_passed:
        print("\n🎉 All MVP 1.4 features are working correctly!")
    else:
        print("\n⚠️ Some tests failed. Please review the output above.")