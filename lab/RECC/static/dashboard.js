/**
 * RECC Visualization Dashboard
 * JavaScript for interactive visualization and real-time monitoring
 */

// Initialize connection to WebSocket server
const socket = io();

// Dashboard state
let simulationActive = false;
let networkSimulation = null;
let networkNodes = [];
let networkLinks = [];
let learningMode = false;
let learningPaused = false;

// Connect to server
socket.on('connect', () => {
    updateStatus('Connected to server');
});

socket.on('disconnect', () => {
    updateStatus('Disconnected from server', 'danger');
});

// Update status messages
function updateStatus(message, type = 'info') {
    const statusEl = document.getElementById('statusMessage');
    statusEl.textContent = message;
    statusEl.className = 'status-message';
    
    if (type === 'danger') {
        statusEl.style.backgroundColor = '#f8d7da';
        statusEl.style.color = '#842029';
    } else if (type === 'success') {
        statusEl.style.backgroundColor = '#d1e7dd';
        statusEl.style.color = '#0f5132';
    } else if (type === 'warning') {
        statusEl.style.backgroundColor = '#fff3cd';
        statusEl.style.color = '#856404';
    } else {
        statusEl.style.backgroundColor = '#e3f2fd';
        statusEl.style.color = '#0a58ca';
    }
}

// Update mode indicator
function updateModeIndicator() {
    const indicator = document.getElementById('currentModeIndicator');
    
    if (learningMode) {
        if (learningPaused) {
            indicator.className = 'mode-indicator mode-paused';
            indicator.textContent = 'Learning Paused';
        } else {
            indicator.className = 'mode-indicator mode-learning';
            indicator.textContent = 'Learning Mode';
        }
    } else {
        indicator.className = 'mode-indicator mode-interactive';
        indicator.textContent = 'Interactive Mode';
    }
}

// Update button states based on current mode
function updateButtonStates() {
    const toggleLearningBtn = document.getElementById('toggleLearningModeBtn');
    const pauseLearningBtn = document.getElementById('pauseLearningBtn');
    const sendPromptBtn = document.getElementById('sendPromptBtn');
    const promptInput = document.getElementById('promptInput');
    
    if (learningMode) {
        toggleLearningBtn.textContent = 'Stop Learning';
        toggleLearningBtn.className = 'btn btn-danger control-btn';
        pauseLearningBtn.disabled = false;
        
        // Update pause button text based on paused state
        if (learningPaused) {
            pauseLearningBtn.textContent = 'Resume';
            pauseLearningBtn.className = 'btn btn-success control-btn';
            // Enable prompt input when paused
            promptInput.disabled = false;
            sendPromptBtn.disabled = false;
        } else {
            pauseLearningBtn.textContent = 'Pause';
            pauseLearningBtn.className = 'btn btn-warning control-btn';
            // Disable prompt input during active learning
            promptInput.disabled = true;
            sendPromptBtn.disabled = true;
            promptInput.placeholder = "Pause learning to interact...";
        }
    } else {
        // Interactive mode
        toggleLearningBtn.textContent = 'Start Learning';
        toggleLearningBtn.className = 'btn btn-success control-btn';
        pauseLearningBtn.disabled = true;
        pauseLearningBtn.textContent = 'Pause';
        pauseLearningBtn.className = 'btn btn-warning control-btn';
        // Enable prompt input in interactive mode
        promptInput.disabled = false;
        sendPromptBtn.disabled = false;
        promptInput.placeholder = "Enter your prompt...";
    }
}

// Initialize the concept network visualization
function initConceptNetwork() {
    const container = document.getElementById('conceptNetworkViz');
    const width = container.clientWidth;
    const height = 450;
    
    // Clear previous SVG if exists
    d3.select('#conceptNetworkViz svg').remove();
    
    // Create SVG
    const svg = d3.select('#conceptNetworkViz')
        .append('svg')
        .attr('width', width)
        .attr('height', height)
        .attr('viewBox', [0, 0, width, height])
        .attr('style', 'max-width: 100%; height: auto;');
        
    return svg;
}

// Update concept network visualization
function updateConceptNetwork(data) {
    // Store the data
    // Only update if we have new data to prevent unnecessary redraws
    if (data.nodes && data.edges) {
        // Limit the number of nodes we visualize to prevent browser slowdown
        const maxNodesToShow = 75; // Match the backend limit
        
        // Sort by importance (use reuse_count or activation as a proxy for importance)
        const sortedNodes = [...data.nodes].sort((a, b) => (b.reuse_count || 0) - (a.reuse_count || 0));
        
        // Only take the top nodes
        const limitedNodes = sortedNodes.slice(0, maxNodesToShow);
        
        // Create a set of node IDs that we're keeping
        const nodeIdSet = new Set(limitedNodes.map(n => n.id));
        
        // Only keep edges that connect nodes we're showing
        const limitedEdges = data.edges.filter(e => 
            nodeIdSet.has(e.source) || typeof e.source === 'object' && nodeIdSet.has(e.source.id) &&
            nodeIdSet.has(e.target) || typeof e.target === 'object' && nodeIdSet.has(e.target.id)
        );
        
        // Store the reduced data for later use
        networkNodes = limitedNodes;
        networkLinks = limitedEdges;
    }
    
    // Don't proceed if we don't have any nodes
    if (!networkNodes.length) {
        return;
    }
    
    const container = document.getElementById('conceptNetworkViz');
    const width = container.clientWidth;
    const height = 450;
    
    // Clear previous SVG and initialize
    const svg = initConceptNetwork();
    
    // Create a force simulation with optimized settings
    networkSimulation = d3.forceSimulation(networkNodes)
        // Use logarithmic scale for distance based on network size
        .force('link', d3.forceLink(networkLinks).id(d => d.id)
               .distance(() => Math.min(100, 50 + 50 * Math.log10(networkNodes.length))))
        // Adjust repulsion force based on network size
        .force('charge', d3.forceManyBody()
               .strength(() => -300 / Math.log10(Math.max(10, networkNodes.length))))
        .force('center', d3.forceCenter(width / 2, height / 2))
        // Add collision detection to prevent node overlap
        .force('collision', d3.forceCollide().radius(d => 8 + (d.reuse_count || 0)));
    
    // Create arrow markers for directed edges
    svg.append('defs').selectAll('marker')
        .data(['end'])
        .join('marker')
        .attr('id', d => `arrow-${d}`)
        .attr('viewBox', '0 -5 10 10')
        .attr('refX', 15)
        .attr('refY', 0)
        .attr('markerWidth', 6)
        .attr('markerHeight', 6)
        .attr('orient', 'auto')
        .append('path')
        .attr('fill', '#999')
        .attr('d', 'M0,-5L10,0L0,5');
    
    // Create container for links
    const linkGroup = svg.append('g')
        .attr('class', 'links');
        
    // Create container for nodes    
    const nodeGroup = svg.append('g')
        .attr('class', 'nodes');
    
    // Create links with optimized rendering
    const link = linkGroup.selectAll('line')
        .data(networkLinks)
        .join('line')
        .attr('stroke', '#999')
        .attr('stroke-opacity', 0.6)
        .attr('stroke-width', d => Math.min(Math.sqrt(d.weight) * 2, 3)) // Cap line width
        .attr('marker-end', 'url(#arrow-end)');
    
    // Create a group for each node
    const node = nodeGroup.selectAll('g')
        .data(networkNodes)
        .join('g')
        .call(drag(networkSimulation));
    
    // Add circles to each node group with optimized size
    node.append('circle')
        .attr('r', d => Math.min(5 + (d.reuse_count || 0), 12)) // Cap node size
        .attr('fill', d => colorScale(d.activation || 0.5));
    
    // Add hover tooltip
    node.append('title')
        .text(d => `${d.name}\nActivation: ${d.activation?.toFixed(2) || 0}\nReuse Count: ${d.reuse_count || 0}`);
    
    // Only add labels for important nodes to reduce rendering overhead
    const importantNodes = networkNodes.filter(d => (d.reuse_count || 0) > 2 || (d.activation || 0) > 0.7);
    
    nodeGroup.selectAll('text')
        .data(importantNodes)
        .join('text')
        .attr('x', 8)
        .attr('y', '0.31em')
        .attr('font-size', '9px')
        .text(d => d.name);
    
    // Status info about visualization
    const totalNodes = data.nodes?.length || networkNodes.length;
    const displayedNodes = networkNodes.length;
    d3.select('#conceptNetworkViz')
        .append('div')
        .attr('class', 'network-stats')
        .html(`<small>Showing ${displayedNodes}/${totalNodes} concepts</small>`)
        .style('position', 'absolute')
        .style('bottom', '5px')
        .style('left', '5px')
        .style('background-color', 'rgba(255,255,255,0.7)')
        .style('padding', '2px 5px')
        .style('border-radius', '3px');
    
    // Use requestAnimationFrame for more efficient simulation
    let animationFrameId;
    
    // Update the position on simulation tick with throttling
    networkSimulation.on('tick', () => {
        // Cancel any existing animation frame
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
        }
        
        // Schedule the next update
        animationFrameId = requestAnimationFrame(() => {
            link
                .attr('x1', d => d.source.x)
                .attr('y1', d => d.source.y)
                .attr('x2', d => d.target.x)
                .attr('y2', d => d.target.y);
            
            node
                .attr('transform', d => `translate(${d.x},${d.y})`);
                
            // Update text positions separately
            nodeGroup.selectAll('text')
                .attr('x', d => d.x + 8)
                .attr('y', d => d.y + 3);
        });
    });
    
    // Stop simulation after 300 iterations to save CPU
    networkSimulation.alphaDecay(0.03);
    
    // Add zoom capability
    const zoom = d3.zoom()
        .scaleExtent([0.25, 3])
        .on('zoom', (event) => {
            nodeGroup.attr('transform', event.transform);
            linkGroup.attr('transform', event.transform);
        });
        
    svg.call(zoom);
    
    // Add zoom controls
    const zoomControls = d3.select('#conceptNetworkViz')
        .append('div')
        .attr('class', 'zoom-controls')
        .style('position', 'absolute')
        .style('top', '10px')
        .style('right', '10px');
        
    zoomControls.append('button')
        .attr('class', 'btn btn-sm btn-outline-secondary')
        .text('+')
        .on('click', () => {
            svg.transition().duration(300).call(zoom.scaleBy, 1.3);
        });
        
    zoomControls.append('button')
        .attr('class', 'btn btn-sm btn-outline-secondary mx-1')
        .text('Reset')
        .on('click', () => {
            svg.transition().duration(500).call(zoom.transform, d3.zoomIdentity);
        });
        
    zoomControls.append('button')
        .attr('class', 'btn btn-sm btn-outline-secondary')
        .text('-')
        .on('click', () => {
            svg.transition().duration(300).call(zoom.scaleBy, 0.7);
        });
}

// Utility function for node dragging
function drag(simulation) {
    function dragstarted(event) {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        event.subject.fx = event.subject.x;
        event.subject.fy = event.subject.y;
    }
    
    function dragged(event) {
        event.subject.fx = event.x;
        event.subject.fy = event.y;
    }
    
    function dragended(event) {
        if (!event.active) simulation.alphaTarget(0);
        event.subject.fx = null;
        event.subject.fy = null;
    }
    
    return d3.drag()
        .on('start', dragstarted)
        .on('drag', dragged)
        .on('end', dragended);
}

// Color scale for nodes based on activation
function colorScale(value) {
    // From inactive (blue) to highly active (red)
    return d3.interpolateRgb('#4575b4', '#d73027')(value);
}

// Update emotion gauges
function updateEmotionGauges(emotionalState) {
    const container = document.getElementById('emotionGauges');
    container.innerHTML = '';
    
    Object.entries(emotionalState).forEach(([emotion, value]) => {
        // Create gauge wrapper
        const gaugeDiv = document.createElement('div');
        gaugeDiv.className = 'emotion-gauge';
        
        // Create gauge visualization (simple for now)
        const gaugeValue = document.createElement('div');
        gaugeValue.className = 'progress';
        gaugeValue.style.height = '20px';
        
        const progressBar = document.createElement('div');
        progressBar.className = 'progress-bar';
        progressBar.style.width = `${value * 100}%`;
        progressBar.setAttribute('role', 'progressbar');
        progressBar.setAttribute('aria-valuenow', value * 100);
        progressBar.setAttribute('aria-valuemin', '0');
        progressBar.setAttribute('aria-valuemax', '100');
        
        // Set color based on emotion
        if (emotion === 'curiosity') {
            progressBar.classList.add('bg-info');
        } else if (emotion === 'frustration') {
            progressBar.classList.add('bg-danger');
        } else if (emotion === 'satisfaction') {
            progressBar.classList.add('bg-success');
        } else if (emotion === 'uncertainty') {
            progressBar.classList.add('bg-warning');
        }
        
        gaugeValue.appendChild(progressBar);
        
        // Create label
        const label = document.createElement('div');
        label.textContent = `${emotion}: ${(value * 100).toFixed(0)}%`;
        label.style.marginTop = '5px';
        label.style.fontSize = '0.9rem';
        
        // Add to container
        gaugeDiv.appendChild(gaugeValue);
        gaugeDiv.appendChild(label);
        container.appendChild(gaugeDiv);
    });
}

// Update metrics display
function updateMetrics(metrics) {
    const container = document.getElementById('metricsContainer');
    container.innerHTML = '';
    
    const createMetric = (label, value, colSize = 6) => {
        const metricCol = document.createElement('div');
        metricCol.className = `col-${colSize} mb-2`;
        
        const metricCard = document.createElement('div');
        metricCard.className = 'metric-card';
        
        const metricLabel = document.createElement('div');
        metricLabel.className = 'metric-label';
        metricLabel.textContent = label;
        
        const metricValue = document.createElement('div');
        metricValue.className = 'metric-value';
        metricValue.textContent = value;
        
        metricCard.appendChild(metricLabel);
        metricCard.appendChild(metricValue);
        metricCol.appendChild(metricCard);
        
        container.appendChild(metricCol);
    };
    
    // Display key metrics
    createMetric('Memory Size', metrics.memory_size);
    createMetric('Concept Count', metrics.concept_count);
    createMetric('Relation Count', metrics.relation_count);
    createMetric('Avg. Connections', metrics.avg_connections?.toFixed(2) || '0');
    createMetric('Theory Count', metrics.theory_count);
    createMetric('Avg. Novelty', metrics.avg_novelty?.toFixed(2) || '0');
}

// Append interaction to history
function appendInteraction(prompt, response, userGenerated = false) {
    const container = document.getElementById('interactionHistory');
    
    // Create interaction box
    const box = document.createElement('div');
    box.className = 'interaction-box';
    if (userGenerated) {
        box.style.borderLeft = '3px solid #28a745'; // Green for user-initiated
    }
    
    // Prompt
    const promptEl = document.createElement('div');
    promptEl.className = 'interaction-prompt';
    promptEl.textContent = userGenerated ? `👤 ${prompt}` : `🧠 ${prompt}`;
    
    // Response
    const responseEl = document.createElement('div');
    responseEl.className = 'interaction-response';
    responseEl.textContent = `🧠 ${response}`; // Changed from 🤖 to 🧠 to represent the baby agent's brain
    
    // Append to box
    box.appendChild(promptEl);
    box.appendChild(responseEl);
    
    // Prepend to container (newest at top)
    container.prepend(box);
}

// Show threshold alerts
function showThresholdAlerts(thresholds) {
    const container = document.getElementById('thresholdAlerts');
    
    thresholds.forEach(threshold => {
        const alert = document.createElement('div');
        alert.className = `threshold-alert ${threshold.type}`;
        
        // Create title
        const title = document.createElement('div');
        title.style.fontWeight = 'bold';
        
        if (threshold.type === 'repetition') {
            title.textContent = 'Repetition Detected';
        } else if (threshold.type === 'emotional') {
            title.textContent = `High ${threshold.emotion}`;
        } else {
            title.textContent = threshold.type;
        }
        
        // Create description
        const desc = document.createElement('div');
        desc.textContent = threshold.description;
        
        // Add severity indicator
        if (threshold.severity === 'high') {
            alert.style.borderLeftColor = '#cc0000';
        } else if (threshold.severity === 'medium') {
            alert.style.borderLeftColor = '#ff9900';
        } else {
            alert.style.borderLeftColor = '#cccc00';
        }
        
        // Append to alert
        alert.appendChild(title);
        alert.appendChild(desc);
        
        // Add to container
        container.prepend(alert);
        
        // Auto-remove after 10 seconds
        setTimeout(() => {
            alert.style.opacity = '0';
            alert.style.transition = 'opacity 1s ease-out';
            setTimeout(() => {
                container.removeChild(alert);
            }, 1000);
        }, 10000);
    });
}

// Handle RECC state updates
socket.on('recc_state_update', (data) => {
    // Update all visualizations and displays
    if (data.concept_network) {
        updateConceptNetwork(data.concept_network);
    }
    
    if (data.emotional_state) {
        updateEmotionGauges(data.emotional_state);
        
        // Synchronize UI controls with RECC state
        document.getElementById('curiositySlider').value = data.emotional_state.curiosity || 0.5;
        document.getElementById('frustrationSlider').value = data.emotional_state.frustration || 0;
        document.getElementById('satisfactionSlider').value = data.emotional_state.satisfaction || 0.3;
        document.getElementById('uncertaintySlider').value = data.emotional_state.uncertainty || 0.7;
    }
    
    if (data.metrics) {
        updateMetrics(data.metrics);
    }
    
    // Update mode controls
    learningMode = data.learning_mode || false;
    learningPaused = data.learning_paused || false;
    updateModeIndicator();
    updateButtonStates();
    
    updateStatus(`Updated state at ${new Date(data.timestamp).toLocaleTimeString()}`);
});

// Handle RECC responses
socket.on('recc_response', (data) => {
    appendInteraction(data.prompt, data.response, data.user_generated);
    updateStatus(`Response received for cycle ${data.cycle}`, 'success');
});

// Handle learning mode toggle
socket.on('learning_mode_update', (data) => {
    learningMode = data.active;
    learningPaused = data.paused;
    
    // Update UI to reflect the changes
    updateModeIndicator();
    updateButtonStates();
    
    if (learningMode) {
        if (learningPaused) {
            updateStatus('Learning mode paused', 'warning');
        } else {
            updateStatus('Learning mode active', 'success');
        }
    } else {
        updateStatus('Interactive mode active', 'info');
    }
});

// Handle cycle completion events
socket.on('cycle_complete', (data) => {
    updateStatus(`Learning cycle ${data.step+1}/${data.total_steps} complete`, 'success');
});

// Handle threshold crossing events
socket.on('threshold_crossed', (data) => {
    showThresholdAlerts([{
        type: data.type,
        description: data.description,
        severity: data.severity
    }]);
});

// Handle emotional change events
socket.on('emotional_change', (data) => {
    showThresholdAlerts([{
        type: 'emotional',
        emotion: data.emotion,
        description: `${data.emotion} changed from ${data.previous.toFixed(2)} to ${data.current.toFixed(2)}`,
        severity: Math.abs(data.delta) > 0.5 ? 'high' : (Math.abs(data.delta) > 0.3 ? 'medium' : 'low')
    }]);
});

// Handle prompt generation events
socket.on('prompt_generated', (data) => {
    updateStatus(`Generated prompt: ${data.prompt}`);
});

// Handle errors
socket.on('error', (data) => {
    updateStatus(`Error: ${data.message}`, 'danger');
});

// Handle status updates
socket.on('status', (data) => {
    updateStatus(data.status);
});

// Handle visualization saves
socket.on('visualization_saved', (data) => {
    updateStatus('New visualizations saved', 'info');
});

// Handle state saving/loading
socket.on('state_saved', (data) => {
    updateStatus(`State saved to ${data.filepath}`, 'success');
});

socket.on('state_loaded', (data) => {
    updateStatus(`State loaded successfully`, 'success');
});

// -------- UI Event Handlers --------

// Toggle learning mode button
document.getElementById('toggleLearningModeBtn').addEventListener('click', () => {
    if (learningMode) {
        // Currently active, so turn it off
        socket.emit('toggle_learning_mode', {
            enable: false
        });
    } else {
        // Currently inactive, so turn it on
        const steps = parseInt(document.getElementById('stepsInput').value) || 100;
        const delay = parseInt(document.getElementById('delayInput').value) || 3;
        
        socket.emit('toggle_learning_mode', {
            enable: true,
            steps: steps,
            delay: delay
        });
    }
});

// Pause learning button
document.getElementById('pauseLearningBtn').addEventListener('click', () => {
    // Toggle pause state
    socket.emit('pause_learning', {
        pause: !learningPaused
    });
});

// Send prompt button
document.getElementById('sendPromptBtn').addEventListener('click', () => {
    const promptInput = document.getElementById('promptInput');
    const prompt = promptInput.value.trim();
    
    if (prompt) {
        socket.emit('send_prompt', { prompt });
        promptInput.value = '';
        updateStatus('Sending prompt...', 'info');
    }
});

// Enter key in prompt input
document.getElementById('promptInput').addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        document.getElementById('sendPromptBtn').click();
    }
});

// Clear interactions button
document.getElementById('clearInteractionsBtn').addEventListener('click', () => {
    document.getElementById('interactionHistory').innerHTML = '';
});

// Refresh network button
document.getElementById('refreshNetworkBtn').addEventListener('click', () => {
    if (networkNodes.length > 0) {
        updateConceptNetwork({ nodes: networkNodes, edges: networkLinks });
    }
});

// Parameter adjustment sliders
const emotionSliders = ['curiositySlider', 'frustrationSlider', 'satisfactionSlider', 'uncertaintySlider'];
emotionSliders.forEach(sliderId => {
    document.getElementById(sliderId).addEventListener('change', (e) => {
        const emotionName = sliderId.replace('Slider', '');
        const value = parseFloat(e.target.value);
        
        socket.emit('adjust_parameter', {
            type: 'emotional_state',
            name: emotionName,
            value: value
        });
        
        updateStatus(`Adjusting ${emotionName} to ${value.toFixed(2)}`, 'info');
    });
});

// Development age slider
document.getElementById('devAgeSlider').addEventListener('input', (e) => {
    const value = parseFloat(e.target.value);
    document.getElementById('devAgeValue').textContent = value.toFixed(1);
});

document.getElementById('devAgeSlider').addEventListener('change', (e) => {
    const value = parseFloat(e.target.value);
    
    socket.emit('adjust_parameter', {
        type: 'dev_age',
        name: 'dev_age',
        value: value
    });
    
    updateStatus(`Adjusting developmental age to ${value.toFixed(1)}`, 'info');
});

// State management buttons
document.getElementById('saveStateBtn').addEventListener('click', () => {
    socket.emit('save_state');
    updateStatus('Saving state...', 'info');
});

document.getElementById('loadStateBtn').addEventListener('click', () => {
    // This could be extended to show a modal with available state files
    const sessionId = prompt('Enter session ID to load:');
    if (sessionId) {
        socket.emit('load_state', { session_id: sessionId });
        updateStatus('Loading state...', 'info');
    }
});

// Initialize when document is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Initialize concept network with empty data
    initConceptNetwork();
    
    // Initialize controls
    updateModeIndicator();
    updateButtonStates();
    
    // Update status
    updateStatus('Dashboard ready. Connect to start visualization.');
});