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
    appendProcessingLog('Connected to RECC server', 'success');
});

socket.on('disconnect', () => {
    updateStatus('Disconnected from server', 'danger');
});

// Overwrite updateStatus to only log to Processing Log
function updateStatus(message, type = 'info') {
    appendProcessingLog(message, type);
}

// --------- Processing Log ---------
function appendProcessingLog(message, type = 'info') {
    const logContainer = document.getElementById('processingLog');
    if (!logContainer) return;
    const entry = document.createElement('div');
    entry.textContent = `[${new Date().toLocaleTimeString()}] ${message}`;
    if (type === 'danger') {
        entry.style.color = '#842029';
    } else if (type === 'success') {
        entry.style.color = '#0f5132';
    } else if (type === 'warning') {
        entry.style.color = '#856404';
    } else {
        entry.style.color = '#0a58ca';
    }
    logContainer.appendChild(entry);
    logContainer.scrollTop = logContainer.scrollHeight;
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
        // Use the already filtered data from the server
        networkNodes = data.nodes;
        networkLinks = data.edges;
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
        // Use force link with moderate distance to avoid crowding
        .force('link', d3.forceLink(networkLinks).id(d => d.id)
               .distance(() => 80))
        // Use moderate charge strength to prevent overlapping
        .force('charge', d3.forceManyBody()
               .strength(-150))
        .force('center', d3.forceCenter(width / 2, height / 2))
        // Add collision detection to prevent node overlap
        .force('collision', d3.forceCollide().radius(d => 10 + (d.reuse_count || 0)));
    
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
    
    // Add circles to each node group with optimized size and highlight recent concepts
    node.append('circle')
        .attr('r', d => {
            // Base size on reuse count, but larger for recent concepts
            const baseSize = Math.min(5 + (d.reuse_count || 0), 12);
            return d.isRecent ? baseSize + 3 : baseSize;
        })
        .attr('fill', d => d.isRecent ? highlightColorScale(d.activation || 0.5) : colorScale(d.activation || 0.5))
        .attr('stroke', d => d.isRecent ? '#ff3333' : 'none')  // Add red stroke for recent concepts
        .attr('stroke-width', d => d.isRecent ? 2 : 0);
    
    // Add hover tooltip with more detailed information
    node.append('title')
        .text(d => {
            let tooltipText = `${d.name}\n`;
            tooltipText += `Activation: ${d.activation?.toFixed(2) || 0}\n`;
            tooltipText += `Reuse Count: ${d.reuse_count || 0}\n`;
            if (d.isRecent) tooltipText += '(Used in recent conversation)';
            return tooltipText;
        });
    
    // Show labels for all nodes since we're now dealing with a smaller, more focused set
    nodeGroup.selectAll('text')
        .data(networkNodes)
        .join('text')
        .attr('x', 8)
        .attr('y', '0.31em')
        .attr('font-size', d => d.isRecent ? '10px' : '9px')  // Slightly larger for recent concepts
        .attr('font-weight', d => d.isRecent ? 'bold' : 'normal')  // Bold for recent concepts
        .text(d => d.name);
    
    // Status info about visualization
    const totalNodes = data.metadata?.total_concepts || networkNodes.length;
    const displayedNodes = networkNodes.length;
    const focusType = data.metadata?.focus_type || 'general';
    
    d3.select('#conceptNetworkViz')
        .append('div')
        .attr('class', 'network-stats')
        .html(`<small>Showing ${displayedNodes}/${totalNodes} concepts - Focus: ${focusType === 'conversation_relevant' ? 'Recent Conversation' : 'General'}</small>`)
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

// Highlight color scale for recent concepts
function highlightColorScale(value) {
    // From inactive (light blue) to highly active (orange)
    return d3.interpolateRgb('#91bfdb', '#fc8d59')(value);
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
    responseEl.textContent = `🧠 ${response}`; // Use brain emoji for baby agent's responses
    
    // Append to box
    box.appendChild(promptEl);
    box.appendChild(responseEl);
    
    // Prepend to container (newest at top)
    container.prepend(box);
}

// Handle RECC state updates
socket.on('recc_state_update', (data) => {
    // Update all visualizations and displays
    if (data.concept_network) {
        updateConceptNetwork(data.concept_network);
    }
    
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

// Initialize when document is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Initialize concept network with empty data
    initConceptNetwork();
    
    // Update status
    updateStatus('Dashboard ready. Connect to start visualization.');
});