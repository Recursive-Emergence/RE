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
    networkNodes = data.nodes;
    networkLinks = data.edges;
    
    const container = document.getElementById('conceptNetworkViz');
    const width = container.clientWidth;
    const height = 450;
    
    // Clear previous SVG and initialize
    const svg = initConceptNetwork();
    
    // Create a force simulation
    networkSimulation = d3.forceSimulation(networkNodes)
        .force('link', d3.forceLink(networkLinks).id(d => d.id).distance(100))
        .force('charge', d3.forceManyBody().strength(-300))
        .force('center', d3.forceCenter(width / 2, height / 2));
    
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
        
    // Create links
    const link = svg.append('g')
        .selectAll('line')
        .data(networkLinks)
        .join('line')
        .attr('stroke', '#999')
        .attr('stroke-opacity', 0.6)
        .attr('stroke-width', d => Math.sqrt(d.weight) * 2)
        .attr('marker-end', 'url(#arrow-end)');
    
    // Create a group for each node
    const node = svg.append('g')
        .selectAll('g')
        .data(networkNodes)
        .join('g')
        .call(drag(networkSimulation));
    
    // Add circles to each node group
    node.append('circle')
        .attr('r', d => 5 + (d.reuse_count || 0))
        .attr('fill', d => colorScale(d.activation || 0.5));
    
    // Add labels to each node group
    node.append('text')
        .text(d => d.name)
        .attr('x', 8)
        .attr('y', '0.31em')
        .attr('font-size', '10px');
    
    // Create hover tooltip
    node.append('title')
        .text(d => `${d.name}\nActivation: ${d.activation?.toFixed(2)}\nReuse Count: ${d.reuse_count || 0}`);
    
    // Update the position on simulation tick
    networkSimulation.on('tick', () => {
        link
            .attr('x1', d => d.source.x)
            .attr('y1', d => d.source.y)
            .attr('x2', d => d.target.x)
            .attr('y2', d => d.target.y);
        
        node
            .attr('transform', d => `translate(${d.x},${d.y})`);
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
function appendInteraction(prompt, response) {
    const container = document.getElementById('interactionHistory');
    
    // Create interaction box
    const box = document.createElement('div');
    box.className = 'interaction-box';
    
    // Prompt
    const promptEl = document.createElement('div');
    promptEl.className = 'interaction-prompt';
    promptEl.textContent = `👤 ${prompt}`;
    
    // Response
    const responseEl = document.createElement('div');
    responseEl.className = 'interaction-response';
    responseEl.textContent = `🤖 ${response}`;
    
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

// Handle RECC updates
socket.on('recc_update', (data) => {
    // Update all visualizations and displays
    updateConceptNetwork(data.concept_network);
    updateEmotionGauges(data.emotional_state);
    updateMetrics(data.metrics);
    appendInteraction(data.prompt, data.response);
    
    // Synchronize UI controls with RECC state
    document.getElementById('curiositySlider').value = data.emotional_state.curiosity;
    document.getElementById('frustrationSlider').value = data.emotional_state.frustration;
    document.getElementById('satisfactionSlider').value = data.emotional_state.satisfaction;
    document.getElementById('uncertaintySlider').value = data.emotional_state.uncertainty;
    
    // Show any threshold alerts
    if (data.thresholds && data.thresholds.length > 0) {
        showThresholdAlerts(data.thresholds);
    }
    
    updateStatus(`Cycle ${data.cycle} complete`, 'success');
});

// Handle generated prompts in autonomous mode
socket.on('prompt_generated', (data) => {
    updateStatus(`Generated prompt: ${data.prompt}`);
});

// Handle waiting for prompt in interactive mode
socket.on('waiting_for_prompt', (data) => {
    updateStatus('Waiting for your prompt...', 'warning');
});

// Handle errors
socket.on('error', (data) => {
    updateStatus(`Error: ${data.message}`, 'danger');
});

// Handle status updates
socket.on('status', (data) => {
    updateStatus(data.status);
});

// -------- UI Event Handlers --------

// Start simulation button
document.getElementById('startSimulationBtn').addEventListener('click', () => {
    const steps = parseInt(document.getElementById('stepsInput').value) || 20;
    const mode = document.querySelector('input[name="mode"]:checked').value;
    
    socket.emit('start_simulation', {
        steps: steps,
        mode: mode
    });
    
    simulationActive = true;
    updateStatus('Starting simulation...', 'info');
});

// Stop simulation button
document.getElementById('stopSimulationBtn').addEventListener('click', () => {
    socket.emit('stop_simulation');
    simulationActive = false;
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

// Initialize when document is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Initialize concept network with empty data
    initConceptNetwork();
    
    // Initialize controls
    document.getElementById('stopSimulationBtn').disabled = true;
    
    // Update status
    updateStatus('Dashboard ready. Connect to start visualization.');
});