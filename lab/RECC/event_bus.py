#!/usr/bin/env python3
# RECC MVP 1.5: Event Bus Module
# Implements event-driven communication between RECC components

class EventBus:
    """
    Event bus for pub/sub pattern between RECC components.
    Allows modules to communicate without direct coupling.
    """
    def __init__(self):
        self.subscribers = {}
        
    def subscribe(self, event_type, callback):
        """
        Subscribe a callback function to an event type
        
        Args:
            event_type: String identifier for the event
            callback: Function to be called when event is published
        """
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)
        
    def unsubscribe(self, event_type, callback):
        """
        Unsubscribe a callback from an event type
        
        Args:
            event_type: String identifier for the event
            callback: Function to remove from subscribers
        """
        if event_type in self.subscribers and callback in self.subscribers[event_type]:
            self.subscribers[event_type].remove(callback)
        
    def publish(self, event_type, data=None):
        """
        Publish an event to all subscribers
        
        Args:
            event_type: String identifier for the event
            data: Data to pass to the callback functions
        """
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                callback(data)
                
    def get_subscriber_count(self, event_type=None):
        """
        Get count of subscribers for a specific event type or all types
        
        Args:
            event_type: Optional, specific event to count subscribers for
            
        Returns:
            Integer count of subscribers
        """
        if event_type:
            return len(self.subscribers.get(event_type, []))
        else:
            return sum(len(subscribers) for subscribers in self.subscribers.values())
            
    def get_event_types(self):
        """Return all registered event types"""
        return list(self.subscribers.keys())

# Global event bus instance
global_event_bus = EventBus()

# Event types constants
class EventTypes:
    # Cognitive events
    PROMPT_GENERATED = "prompt_generated"
    RESPONSE_RECEIVED = "response_received"  
    CONCEPT_CREATED = "concept_created"
    RELATION_CREATED = "relation_created"
    THEORY_FORMED = "theory_formed"
    DIALOGUE_CONTEXT_RESET = "dialogue_context_reset"
    
    # Emotional events
    EMOTIONAL_CHANGE = "emotional_change"
    FRUSTRATION_THRESHOLD = "frustration_threshold"
    CURIOSITY_THRESHOLD = "curiosity_threshold"
    
    # System events
    CYCLE_COMPLETE = "cycle_complete"
    THRESHOLD_CROSSED = "threshold_crossed"
    REPETITION_DETECTED = "repetition_detected"
    
    # Visualization events
    VISUALIZATION_SAVE = "visualization_save"
    MEMORY_CONSOLIDATION = "memory_consolidation"
    
    # User interaction events
    USER_PROMPT = "user_prompt"
    USER_INTERACTION_PROCESSED = "user_interaction_processed"
    PARAMETER_ADJUSTED = "parameter_adjusted"
    
    # MVP 1.6 events
    SYSTEM_INITIALIZING = "system_initializing"  # New event for initialization start
    SYSTEM_INITIALIZED = "system_initialized"
    PROCESSING_CYCLE_COMPLETE = "processing_cycle_complete"
    MEMORY_PROCESSED = "memory_processed"
    MEMORY_RETRIEVED = "memory_retrieved"
    MEMORY_STORED = "memory_stored"
    REFLECTION_COMPLETE = "reflection_complete"
    RECURSIVE_MODIFICATION = "recursive_modification"
    RECURSIVE_LEVEL_ACTIVATED = "recursive_level_activated"
    EMERGENT_PROPERTIES_UPDATED = "emergent_properties_updated"
    STATE_SAVED = "state_saved"
    STATE_LOADED = "state_loaded"
    STATE_APPLIED = "state_applied"