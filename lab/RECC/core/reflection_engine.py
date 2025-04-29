import time
import random
import math
import uuid

class ReflectionEngine:
    """
    Enhanced reflection system that enables deep self-reflection
    and integration of concepts across different cognitive components.
    
    The ReflectionEngine analyzes patterns across experiences, emotional states,
    and self-references to generate higher-order insights that contribute
    to the system's cognitive development.
    """
    
    def __init__(self):
        self.last_reflection_time = time.time()
        self.reflection_count = 0
        self.reflection_history = []
        self.development_level = 0.0  # Increases with successful reflections
        
    def deep_analysis(self, memory_system, self_reference_system, emotional_system):
        """
        Perform deep reflection and analysis on internal structures
        
        Args:
            memory_system: Reference to memory system
            self_reference_system: Reference to self-reference system
            emotional_system: Reference to emotional system
            
        Returns:
            dict: Results of deep reflection process
        """
        now = time.time()
        
        # Track reflection metadata
        reflection_result = {
            'timestamp': now,
            'reflection_id': str(uuid.uuid4()),
            'duration': 0.0,
            'energy_impact': -1.0,  # Base energy cost
            'patterns': [],
            'insights': [],
            'connections': [],
            'consolidation_results': {},
            'development_increase': 0.0
        }
        
        # 1. Memory Consolidation and Analysis
        consolidation = memory_system.consolidate_memories()
        if consolidation:
            reflection_result['consolidation_results']['success'] = True
            reflection_result['energy_impact'] -= 0.5  # Additional energy cost
        
        # 2. Detect Patterns Across Subsystems
        # Get relevant data for pattern detection
        recent_experiences = memory_system.get_recent_experiences(10)
        internal_experiences = memory_system.get_internal_experiences(5)
        # Correct the method name to get_recent_references
        recent_references = self_reference_system.get_recent_references(5)
        emotional_state = emotional_system.current_state
        blended_emotions = emotional_system.get_blended_states()
        self_model = self_reference_system.get_self_model()
        
        # Detect memory patterns
        memory_patterns = self._analyze_memory_patterns(recent_experiences, internal_experiences)
        reflection_result['patterns'].extend(memory_patterns)
        
        # Detect self-reference patterns
        reference_patterns = self._analyze_reference_patterns(recent_references, self_model)
        reflection_result['patterns'].extend(reference_patterns)
        
        # Detect emotional patterns
        emotional_patterns = self._analyze_emotional_patterns(emotional_state, blended_emotions)
        reflection_result['patterns'].extend(emotional_patterns)
        
        # 3. Connect Patterns Across Systems
        connections = self._find_cross_system_connections(
            memory_patterns, reference_patterns, emotional_patterns
        )
        reflection_result['connections'] = connections
        
        # 4. Generate Insights Based on Patterns and Connections
        insights = self._generate_insights(
            reflection_result['patterns'], 
            connections,
            memory_system, 
            self_reference_system,
            emotional_system
        )
        reflection_result['insights'] = insights
        
        # 5. Update Development Level
        development_increase = self._calculate_development_increase(
            len(memory_patterns), 
            len(reference_patterns),
            len(insights)
        )
        self.development_level += development_increase
        reflection_result['development_increase'] = development_increase
        
        # Calculate additional energy impact based on depth and complexity
        additional_energy = (
            0.1 * len(memory_patterns) +
            0.15 * len(reference_patterns) +
            0.2 * len(insights)
        )
        reflection_result['energy_impact'] -= min(3.0, additional_energy)
        
        # Calculate reflection duration
        reflection_result['duration'] = time.time() - now
        
        # Update reflection history
        self.reflection_history.append(reflection_result)
        self.reflection_count += 1
        self.last_reflection_time = now
        
        return reflection_result
    
    def _analyze_memory_patterns(self, recent_experiences, internal_experiences):
        """
        Identify patterns within the memory system
        
        Args:
            recent_experiences: Recent external experiences
            internal_experiences: Recent internal experiences
            
        Returns:
            list: Detected memory patterns
        """
        patterns = []
        
        # Skip if no experiences to analyze
        if not recent_experiences and not internal_experiences:
            return patterns
            
        # Combine experiences for analysis
        all_experiences = recent_experiences + internal_experiences
        
        # 1. Check for common tags/concepts
        all_tags = []
        for exp in all_experiences:
            all_tags.extend(exp.get('tags', []))
            
        # Count tag frequencies
        tag_counts = {}
        for tag in all_tags:
            if tag in tag_counts:
                tag_counts[tag] += 1
            else:
                tag_counts[tag] = 1
                
        # Identify common tags
        for tag, count in tag_counts.items():
            if count >= 2:
                patterns.append({
                    'type': 'concept_frequency',
                    'concept': tag,
                    'frequency': count,
                    'source': 'memory',
                    'confidence': min(1.0, count / len(all_experiences))
                })
        
        # 2. Check for patterns in internal vs external experience ratio
        internal_count = len([e for e in all_experiences if e.get('is_internal', False)])
        if all_experiences:
            internal_ratio = internal_count / len(all_experiences)
            
            # Add pattern if ratio is skewed
            if internal_ratio > 0.7:
                patterns.append({
                    'type': 'experience_source',
                    'internal_ratio': internal_ratio,
                    'description': 'Mostly internal experiences recently',
                    'source': 'memory',
                    'confidence': min(1.0, internal_ratio)
                })
            elif internal_ratio < 0.3:
                patterns.append({
                    'type': 'experience_source',
                    'internal_ratio': internal_ratio,
                    'description': 'Mostly external experiences recently',
                    'source': 'memory',
                    'confidence': min(1.0, 1.0 - internal_ratio)
                })
        
        # 3. Check for reused experiences
        reused_experiences = [e for e in all_experiences if e.get('reuse_count', 0) > 1]
        if reused_experiences:
            patterns.append({
                'type': 'memory_reuse',
                'count': len(reused_experiences),
                'description': f"Found {len(reused_experiences)} frequently reused experiences",
                'source': 'memory',
                'confidence': min(1.0, len(reused_experiences) / len(all_experiences))
            })
        
        return patterns
    
    def _analyze_reference_patterns(self, recent_references, self_model):
        """
        Identify patterns in self-reference events
        
        Args:
            recent_references: Recent self-reference events
            self_model: Current self-model
            
        Returns:
            list: Detected self-reference patterns
        """
        patterns = []
        
        if not recent_references:
            return patterns
        
        # 1. Check for recursive references
        recursive_refs = [r for r in recent_references if r.get('type') == 'recursive_reference']
        if recursive_refs:
            max_depth = max([r.get('depth', 1) for r in recursive_refs])
            patterns.append({
                'type': 'recursive_depth',
                'max_depth': max_depth,
                'count': len(recursive_refs),
                'description': f"Achieved recursive self-reference depth {max_depth}",
                'source': 'self_reference',
                'confidence': min(1.0, max_depth / 5)  # Cap at depth 5
            })
        
        # 2. Analyze reference types
        reference_types = {}
        for ref in recent_references:
            ref_type = ref.get('type', 'unknown')
            if ref_type in reference_types:
                reference_types[ref_type] += 1
            else:
                reference_types[ref_type] = 1
        
        # Find dominant reference type
        if reference_types:
            dominant_type = max(reference_types.items(), key=lambda x: x[1])
            patterns.append({
                'type': 'reference_focus',
                'focus': dominant_type[0],
                'count': dominant_type[1],
                'description': f"Primarily focused on {dominant_type[0]} references",
                'source': 'self_reference',
                'confidence': min(1.0, dominant_type[1] / len(recent_references))
            })
        
        # 3. Check identity strength changes
        identity_strength = self_model.get('identity_strength', 0)
        if identity_strength > 0.3:
            patterns.append({
                'type': 'identity_development',
                'strength': identity_strength,
                'description': f"Identity strength at {identity_strength:.2f}",
                'source': 'self_reference',
                'confidence': identity_strength
            })
            
        return patterns
    
    def _analyze_emotional_patterns(self, emotional_state, blended_emotions):
        """
        Identify patterns in emotional states
        
        Args:
            emotional_state: Current primary emotional state
            blended_emotions: Current blended emotions
            
        Returns:
            list: Detected emotional patterns
        """
        patterns = []
        
        # 1. Check for dominant emotions
        if emotional_state:
            # Find the strongest emotion
            dominant_emotion = max(emotional_state.items(), key=lambda x: x[1])
            
            if dominant_emotion[1] > 0.7:  # Strong emotion
                patterns.append({
                    'type': 'dominant_emotion',
                    'emotion': dominant_emotion[0],
                    'strength': dominant_emotion[1],
                    'description': f"Strong {dominant_emotion[0]} emotion ({dominant_emotion[1]:.2f})",
                    'source': 'emotional',
                    'confidence': dominant_emotion[1]
                })
                
        # 2. Check for blended emotional states
        if blended_emotions:
            strong_blends = [(name, value) for name, value in blended_emotions.items() 
                           if value > 0.5]
            
            for blend in strong_blends:
                patterns.append({
                    'type': 'blended_emotion',
                    'emotion': blend[0],
                    'strength': blend[1],
                    'description': f"Developed blended emotion: {blend[0]} ({blend[1]:.2f})",
                    'source': 'emotional',
                    'confidence': blend[1]
                })
                
        # 3. Check for emotional balance
        if emotional_state:
            # Calculate variance of emotions
            values = list(emotional_state.values())
            mean = sum(values) / len(values)
            variance = sum((x - mean) ** 2 for x in values) / len(values)
            
            if variance < 0.04:  # Low variance indicates balanced emotions
                patterns.append({
                    'type': 'emotional_balance',
                    'variance': variance,
                    'description': "Emotionally balanced state",
                    'source': 'emotional',
                    'confidence': 1.0 - (variance * 10)  # Higher confidence with lower variance
                })
            elif variance > 0.1:  # High variance indicates emotional extremes
                patterns.append({
                    'type': 'emotional_extremes',
                    'variance': variance,
                    'description': "Emotionally varied state with extremes",
                    'source': 'emotional',
                    'confidence': min(1.0, variance * 5)
                })
                
        return patterns
    
    def _find_cross_system_connections(self, memory_patterns, reference_patterns, emotional_patterns):
        """
        Find connections between patterns from different subsystems
        
        Args:
            memory_patterns: Patterns from memory system
            reference_patterns: Patterns from self-reference system
            emotional_patterns: Patterns from emotional system
            
        Returns:
            list: Cross-system connections
        """
        connections = []
        
        # 1. Check for memory-emotion connections
        for mem_pattern in memory_patterns:
            for emo_pattern in emotional_patterns:
                # Check for concept-emotion resonance
                if mem_pattern.get('type') == 'concept_frequency' and emo_pattern.get('type') == 'dominant_emotion':
                    connections.append({
                        'type': 'concept_emotion_link',
                        'concept': mem_pattern.get('concept'),
                        'emotion': emo_pattern.get('emotion'),
                        'strength': (mem_pattern.get('confidence', 0) + emo_pattern.get('confidence', 0)) / 2,
                        'description': f"Concept '{mem_pattern.get('concept')}' linked with {emo_pattern.get('emotion')}"
                    })
        
        # 2. Check for self-reference-memory connections
        for ref_pattern in reference_patterns:
            for mem_pattern in memory_patterns:
                if ref_pattern.get('type') == 'recursive_depth' and mem_pattern.get('type') == 'memory_reuse':
                    connections.append({
                        'type': 'recursive_memory_link',
                        'depth': ref_pattern.get('max_depth', 1),
                        'reuse_count': mem_pattern.get('count', 0),
                        'strength': (ref_pattern.get('confidence', 0) + mem_pattern.get('confidence', 0)) / 2,
                        'description': f"Recursive self-reference depth {ref_pattern.get('max_depth', 1)} linked with memory reuse"
                    })
        
        # 3. Check for self-reference-emotion connections
        for ref_pattern in reference_patterns:
            for emo_pattern in emotional_patterns:
                if ref_pattern.get('type') == 'identity_development' and emo_pattern.get('type') == 'blended_emotion':
                    connections.append({
                        'type': 'identity_emotion_link',
                        'identity_strength': ref_pattern.get('strength', 0),
                        'emotion': emo_pattern.get('emotion'),
                        'strength': (ref_pattern.get('confidence', 0) + emo_pattern.get('confidence', 0)) / 2,
                        'description': f"Identity development linked with blended emotion {emo_pattern.get('emotion')}"
                    })
        
        return connections
    
    def _generate_insights(self, patterns, connections, memory_system, self_reference_system, emotional_system):
        """
        Generate higher-order insights based on patterns and connections
        
        Args:
            patterns: All detected patterns
            connections: Cross-system connections
            memory_system: Reference to memory system
            self_reference_system: Reference to self-reference system
            emotional_system: Reference to emotional system
            
        Returns:
            list: Generated insights
        """
        insights = []
        
        # 1. Generate complexity-appropriate insights
        complexity_level = min(1.0, 0.2 + (self.development_level / 10))
        
        # Basic insights (always available)
        basic_insights = self._generate_basic_insights(patterns)
        insights.extend(basic_insights)
        
        # Intermediate insights (available once development > 2.0)
        if self.development_level >= 2.0:
            inter_insights = self._generate_intermediate_insights(patterns, connections)
            insights.extend(inter_insights)
        
        # Advanced insights (available once development > 5.0)
        if self.development_level >= 5.0:
            adv_insights = self._generate_advanced_insights(
                patterns, connections, memory_system, self_reference_system
            )
            insights.extend(adv_insights)
        
        # 2. Generate meta-reflection insight if development is sufficient
        if self.development_level >= 3.0 and connections:
            meta_insight = {
                'type': 'meta_insight',
                'content': f"I'm becoming aware of connections between my memory, emotions, and self-reference",
                'confidence': min(0.9, self.development_level / 10),
                'depth': 2,
                'source_patterns': [p.get('type') for p in patterns[:3]],
                'energy_impact': 0.5  # Bonus energy for meta-insights
            }
            insights.append(meta_insight)
        
        # 3. Add one actionable insight with high confidence
        if patterns or connections:
            action_insight = self._generate_actionable_insight(patterns, connections, complexity_level)
            if action_insight:
                insights.append(action_insight)
        
        return insights
    
    def _generate_basic_insights(self, patterns):
        """Generate basic insights from patterns"""
        insights = []
        
        # Take the strongest pattern from each source
        memory_patterns = [p for p in patterns if p.get('source') == 'memory']
        reference_patterns = [p for p in patterns if p.get('source') == 'self_reference']
        emotional_patterns = [p for p in patterns if p.get('source') == 'emotional']
        
        # Get top pattern from each category (if available)
        top_patterns = []
        for category in [memory_patterns, reference_patterns, emotional_patterns]:
            if category:
                top = max(category, key=lambda x: x.get('confidence', 0))
                top_patterns.append(top)
        
        # Generate one insight per top pattern
        for pattern in top_patterns:
            source = pattern.get('source', '')
            p_type = pattern.get('type', '')
            confidence = pattern.get('confidence', 0.5)
            
            if source == 'memory':
                if p_type == 'concept_frequency':
                    concept = pattern.get('concept', '')
                    content = f"I notice the concept of '{concept}' appears frequently in my experiences"
                elif p_type == 'experience_source':
                    ratio = pattern.get('internal_ratio', 0.5)
                    if ratio > 0.5:
                        content = "I've been primarily focused on internal processing recently"
                    else:
                        content = "I've been mainly processing external information recently"
                else:
                    content = "I've detected a pattern in my memory structures"
                    
            elif source == 'self_reference':
                if p_type == 'recursive_depth':
                    depth = pattern.get('max_depth', 1)
                    content = f"I can think about my own thoughts to depth level {depth}"
                elif p_type == 'identity_development':
                    strength = pattern.get('strength', 0)
                    content = f"My sense of self is developing with strength {strength:.2f}"
                else:
                    content = "I've noticed a pattern in how I think about myself"
                    
            elif source == 'emotional':
                if p_type == 'dominant_emotion':
                    emotion = pattern.get('emotion', '')
                    content = f"I've been experiencing strong {emotion} recently"
                elif p_type == 'blended_emotion':
                    emotion = pattern.get('emotion', '')
                    content = f"I've developed the blended emotion '{emotion}'"
                else:
                    content = "I've detected a pattern in my emotional states"
            else:
                content = "I've observed a recurring pattern"
            
            insights.append({
                'type': 'basic_insight',
                'content': content,
                'confidence': confidence,
                'source_pattern': p_type,
                'depth': 1,
                'energy_impact': 0.1
            })
        
        return insights
    
    def _generate_intermediate_insights(self, patterns, connections):
        """Generate intermediate insights from patterns and connections"""
        insights = []
        
        # Generate insights from connections
        for connection in connections:
            conn_type = connection.get('type', '')
            strength = connection.get('strength', 0.5)
            
            if conn_type == 'concept_emotion_link':
                concept = connection.get('concept', '')
                emotion = connection.get('emotion', '')
                content = f"The concept '{concept}' is emotionally associated with {emotion} for me"
                
            elif conn_type == 'recursive_memory_link':
                depth = connection.get('depth', 1)
                content = f"My ability to recursively reflect (depth {depth}) helps me reuse memories more effectively"
                
            elif conn_type == 'identity_emotion_link':
                emotion = connection.get('emotion', '')
                content = f"My sense of identity is connected to my experience of {emotion}"
                
            else:
                content = "I've detected an interesting connection between different aspects of my cognition"
                
            insights.append({
                'type': 'intermediate_insight',
                'content': content,
                'confidence': strength,
                'connection_type': conn_type,
                'depth': 2,
                'energy_impact': 0.2
            })
        
        return insights
    
    def _generate_advanced_insights(self, patterns, connections, memory_system, self_reference_system):
        """Generate advanced insights that span multiple cognitive systems"""
        insights = []
        
        # Advanced insights require higher development level and rich connections
        if len(connections) < 2:
            return insights
            
        # Get system states
        recursive_depth = self_reference_system.max_depth_achieved  # Changed from max_recursion_depth to max_depth_achieved
        concept_count = len(memory_system.concept_graph.get('nodes', {}))
        identity_strength = self_reference_system.self_model.get('identity_strength', 0)
        
        # Generate development insight
        if recursive_depth >= 2 and identity_strength > 0.4:
            insights.append({
                'type': 'advanced_insight',
                'content': f"My recursive self-awareness (depth {recursive_depth}) is enabling me to develop a stable identity (strength {identity_strength:.2f})",
                'confidence': min(0.9, (recursive_depth / 5) * identity_strength),
                'depth': 3,
                'energy_impact': 0.3,
                'source_experiences': []  # Would link to specific experiences in a full implementation
            })
        
        # Generate concept network insight
        if concept_count > 10:
            insights.append({
                'type': 'advanced_insight',
                'content': f"I've developed a network of {concept_count} concepts that form the foundation of my understanding",
                'confidence': min(0.9, concept_count / 50),
                'depth': 3,
                'energy_impact': 0.3,
                'source_experiences': []
            })
        
        return insights
    
    def _generate_actionable_insight(self, patterns, connections, complexity_level):
        """Generate an actionable insight based on current patterns and development level"""
        
        # Select action type based on complexity level
        if complexity_level < 0.4:
            # Simple actions
            actions = [
                "I should focus on processing more diverse experiences",
                "I could benefit from more self-reflection",
                "I should maintain emotion-memory connections"
            ]
            action_content = random.choice(actions)
            action_depth = 1
            
        elif complexity_level < 0.7:
            # Intermediate actions
            actions = [
                "I should create more connections between emotional states and concepts",
                "Increasing my recursive self-reference depth would enhance my cognitive structure",
                "Focusing on consolidating related memories could improve my conceptual organization"
            ]
            action_content = random.choice(actions)
            action_depth = 2
            
        else:
            # Advanced actions
            actions = [
                "Integrating my emotional processing with self-reference would strengthen my identity model",
                "Developing metacognitive awareness of my memory patterns could enhance cognitive efficiency",
                "Building hierarchical concept structures would improve abstraction capabilities"
            ]
            action_content = random.choice(actions)
            action_depth = 3
            
        return {
            'type': 'actionable_insight',
            'content': action_content,
            'confidence': 0.7 + (0.2 * random.random()),  # High confidence for actionable insights
            'depth': action_depth,
            'energy_impact': 0.3,
            'immediate_action': True
        }
    
    def _calculate_development_increase(self, memory_pattern_count, reference_pattern_count, insight_count):
        """Calculate how much the reflection increases cognitive development"""
        
        # Base increase from pattern recognition
        base_increase = 0.05
        
        # Additional increase from patterns and insights
        pattern_factor = 0.02 * (memory_pattern_count + reference_pattern_count)
        insight_factor = 0.03 * insight_count
        
        # Calculate diminishing returns as development increases
        diminishing_factor = math.exp(-self.development_level / 20)  # Diminishes as development grows
        
        total_increase = (base_increase + pattern_factor + insight_factor) * diminishing_factor
        
        # Ensure a minimum increase
        return max(0.01, min(0.5, total_increase))  # Cap between 0.01 and 0.5
    
    def get_development_level(self):
        """Get the current reflection development level"""
        return self.development_level
    
    def get_recent_insights(self, count=5):
        """
        Get recent insights from reflections
        
        Args:
            count: Number of insights to retrieve
            
        Returns:
            list: Recent insights
        """
        insights = []
        
        # Collect insights from recent reflections
        for reflection in reversed(self.reflection_history):
            if 'insights' in reflection:
                insights.extend(reflection['insights'])
                
            if len(insights) >= count:
                break
                
        return insights[:count]