#!/usr/bin/env python3
"""
RECC MVP 1.6 Test Script
This script tests the MVP 1.6 implementation against the key metrics
defined in the requirements document.
"""

import time
import json
import sys
import os
from datetime import datetime
from pprint import pprint

# Make sure the components directory is in the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import required modules
from event_bus import global_event_bus, EventTypes
from components.recc_integration import RECC_MVP16

class TestReporter:
    """Simple reporter for test results"""
    
    def __init__(self):
        self.results = []
        self.start_time = datetime.now()
        
    def section(self, title):
        """Print a section header"""
        print(f"\n{'=' * 50}")
        print(f"  {title}")
        print(f"{'=' * 50}")
        
    def test(self, name, value, target, passed=None):
        """Record a test result"""
        if passed is None:
            # Default pass condition: value >= target
            passed = value >= target
            
        result = {
            'name': name,
            'value': value,
            'target': target,
            'passed': passed,
            'timestamp': datetime.now().isoformat()
        }
        
        self.results.append(result)
        
        # Print the result
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] {name}: {value} (Target: {target})")
        
        return passed
    
    def summary(self):
        """Print a summary of test results"""
        passed = sum(1 for r in self.results if r['passed'])
        total = len(self.results)
        duration = (datetime.now() - self.start_time).total_seconds()
        
        self.section("TEST SUMMARY")
        print(f"Tests Passed: {passed}/{total} ({passed/total*100:.1f}%)")
        print(f"Duration: {duration:.2f} seconds")
        print(f"Timestamp: {datetime.now().isoformat()}")
        
        # Return if all tests passed
        return passed == total
    
    def save_report(self, filename="mvp16_test_results.json"):
        """Save the test results to a JSON file"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'passed': sum(1 for r in self.results if r['passed']),
            'total': len(self.results),
            'duration_seconds': (datetime.now() - self.start_time).total_seconds(),
            'results': self.results
        }
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
            
        print(f"\nReport saved to: {filename}")

class EventCollector:
    """Collects events from the event bus for inspection"""
    
    def __init__(self, event_bus=None):
        self.events = []
        self.event_bus = event_bus or global_event_bus
        
        # Subscribe to specific event types we care about rather than using a wildcard
        self.event_bus.subscribe(EventTypes.SYSTEM_INITIALIZED, self._collect_event)
        self.event_bus.subscribe(EventTypes.SYSTEM_INITIALIZING, self._collect_event)
        self.event_bus.subscribe(EventTypes.PROCESSING_CYCLE_COMPLETE, self._collect_event)
        self.event_bus.subscribe(EventTypes.RECURSIVE_MODIFICATION, self._collect_event)
        self.event_bus.subscribe(EventTypes.RECURSIVE_LEVEL_ACTIVATED, self._collect_event)
        self.event_bus.subscribe(EventTypes.EMERGENT_PROPERTIES_UPDATED, self._collect_event)
        self.event_bus.subscribe(EventTypes.MEMORY_PROCESSED, self._collect_event)
        self.event_bus.subscribe(EventTypes.MEMORY_RETRIEVED, self._collect_event)
        self.event_bus.subscribe(EventTypes.REFLECTION_COMPLETE, self._collect_event)
        
    def _collect_event(self, data):
        """Collect an event"""
        # Determine event type from caller info (since it's not passed to the callback)
        import inspect
        frame = inspect.currentframe()
        try:
            # Get the event type from the call stack
            event_type = frame.f_back.f_locals.get('event_type')
            if not event_type:
                event_type = "unknown"
        finally:
            del frame  # Avoid reference cycles
            
        self.events.append({
            'type': event_type,
            'data': data,
            'timestamp': datetime.now().isoformat()
        })
        
    def get_events_by_type(self, event_type):
        """Get all events of a specific type"""
        return [e for e in self.events if e['type'] == event_type]
    
    def count_events_by_type(self):
        """Count events by type"""
        counts = {}
        for event in self.events:
            event_type = event['type']
            counts[event_type] = counts.get(event_type, 0) + 1
        return counts
    
    def report(self):
        """Print a report of collected events"""
        counts = self.count_events_by_type()
        print("\nEvent Summary:")
        print("-------------")
        for event_type, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
            print(f"{event_type}: {count}")
        print(f"Total Events: {len(self.events)}")

def run_tests():
    """Run the MVP 1.6 evaluation tests"""
    reporter = TestReporter()
    event_collector = EventCollector()
    
    reporter.section("INITIALIZING MVP 1.6")
    print("Creating RECC_MVP16 instance...")
    
    # Create an instance of the RECC_MVP16 system
    recc = RECC_MVP16()
    
    # Check initialization
    reporter.test(
        "System Initialization", 
        len(event_collector.get_events_by_type(EventTypes.SYSTEM_INITIALIZED)),
        1
    )
    
    # Run initial cycle to set baseline
    reporter.section("RUNNING BASELINE CYCLE")
    initial_input = {
        'prompt': "What patterns do you notice in how you process information?",
        'response': "I observe that I process information through layers of abstraction. First, I detect basic patterns in the input. Then, I analyze how these patterns relate to each other. Finally, I reflect on my own pattern detection process to improve it over time.",
        'context': "Initial baseline test"
    }
    
    print("Processing initial input...")
    result = recc.process_input(initial_input)
    
    # Run multiple autonomous cycles to build up recursive reflection
    reporter.section("RUNNING AUTONOMOUS CYCLES")
    print("Running 20 autonomous cycles to build recursive depth...")
    autonomous_result = recc.autonomous_cycle(steps=20)
    
    # Get performance metrics after cycles
    metrics = recc.get_performance_metrics()
    
    # Print current metrics
    reporter.section("CURRENT SYSTEM METRICS")
    pprint(metrics)
    
    # Evaluate against MVP 1.6 success criteria
    reporter.section("EVALUATING SUCCESS CRITERIA")
    
    # 1. Effective Recursive Depth (Target: ≥ 3.0)
    reporter.test(
        "Effective Recursive Depth",
        metrics['effective_recursive_depth'],
        3.0
    )
    
    # 2. Self-Model Stability (Target: > 80%)
    reporter.test(
        "Self-Model Stability",
        metrics['self_model_stability'],
        0.8
    )
    
    # 3. Cross-Level Modifications (Target: ≥ 10 per 100 cycles)
    reporter.test(
        "Cross-Level Modifications Rate",
        metrics['modification_rate_per_100_cycles'],
        10
    )
    
    # 4. Hierarchical Concepts (Target: ≥ 3 levels)
    reporter.test(
        "Concept Hierarchy Depth",
        metrics['concept_hierarchy_depth'],
        3
    )
    
    # 5. Meta-Strategy Evolution (Target: Measurable change)
    reporter.test(
        "Meta-Strategy Evolution",
        metrics['meta_strategy_evolution'] > 0,
        True,
        metrics['meta_strategy_evolution'] > 0.05
    )
    
    # Check event distribution to verify system activity
    reporter.section("EVENT DISTRIBUTION")
    event_collector.report()
    
    # Visualize recursive depth
    viz_data = recc.visualize_recursive_depth()
    reporter.section("RECURSIVE DEPTH VISUALIZATION DATA")
    print(f"Effective Depth: {viz_data['effective_depth']}")
    print(f"Cross-Level Modifications: {viz_data['cross_level_modifications']}")
    print("Level details:")
    for level in viz_data['levels']:
        state_marker = "✓" if level['state'] == 'active' else " "
        print(f"  [{state_marker}] Level {level['depth']}: {level['history_entries']} entries")
    
    # Generate and save test report
    reporter.summary()
    reporter.save_report()

if __name__ == "__main__":
    run_tests()