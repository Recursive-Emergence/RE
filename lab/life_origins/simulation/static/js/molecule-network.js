// Molecule Network Visualization using D3.js
// This module handles the interactive visualization of molecules and their reaction network

// Network visualization variables
let networkSvg = null;
let simulation = null;
let zoom = null;
let networkData = {
    nodes: [],
    links: []
};
let nodeElements = null;
let linkElements = null;

// Configuration settings
const networkConfig = {
    showReactions: true,
    highlightCatalysts: true,
    zoomLevel: 1.0
};

// Initialize the network visualization
document.addEventListener('DOMContentLoaded', function() {
    // Set up view toggle buttons
    document.getElementById('chart-view-btn').addEventListener('click', function() {
        showView('chart');
    });
    
    document.getElementById('network-view-btn').addEventListener('click', function() {
        showView('network');
        
        // Initialize the network if it hasn't been yet
        if (networkSvg === null) {
            initializeNetwork();
        }
    });
    
    // Network control buttons
    document.getElementById('zoom-in-btn').addEventListener('click', function() {
        zoomNetwork(1.2);
    });
    
    document.getElementById('zoom-out-btn').addEventListener('click', function() {
        zoomNetwork(0.8);
    });
    
    document.getElementById('reset-view-btn').addEventListener('click', function() {
        resetNetworkView();
    });
    
    // Network display options
    document.getElementById('show-reactions').addEventListener('change', function() {
        networkConfig.showReactions = this.checked;
        updateNetworkDisplay();
    });
    
    document.getElementById('highlight-catalysts').addEventListener('change', function() {
        networkConfig.highlightCatalysts = this.checked;
        updateNetworkDisplay();
    });
});

// Switch between chart view and network view
function showView(viewType) {
    const chartPanel = document.getElementById('chart-view-panel');
    const networkPanel = document.getElementById('network-view-panel');
    const chartBtn = document.getElementById('chart-view-btn');
    const networkBtn = document.getElementById('network-view-btn');
    
    if (viewType === 'chart') {
        chartPanel.style.display = 'block';
        networkPanel.style.display = 'none';
        chartBtn.classList.add('active');
        networkBtn.classList.remove('active');
    } else {
        chartPanel.style.display = 'none';
        networkPanel.style.display = 'block';
        chartBtn.classList.remove('active');
        networkBtn.classList.add('active');
    }
}

// Initialize the network visualization
function initializeNetwork() {
    const container = document.getElementById('molecule-network');
    const width = container.clientWidth;
    const height = container.clientHeight;
    
    // Create SVG element
    networkSvg = d3.select('#molecule-network')
        .append('svg')
        .attr('width', '100%')
        .attr('height', '100%')
        .attr('viewBox', `0 0 ${width} ${height}`)
        .attr('preserveAspectRatio', 'xMidYMid meet');
        
    // Add zoom and pan behavior
    zoom = d3.zoom()
        .scaleExtent([0.1, 10])
        .on('zoom', (event) => {
            networkConfig.zoomLevel = event.transform.k;
            networkSvg.select('g').attr('transform', event.transform);
        });
        
    networkSvg.call(zoom);
    
    // Add a group for all network elements
    const g = networkSvg.append('g');
    
    // Create force simulation
    simulation = d3.forceSimulation()
        .force('link', d3.forceLink().id(d => d.id).distance(50))
        .force('charge', d3.forceManyBody().strength(-100))
        .force('center', d3.forceCenter(width / 2, height / 2))
        .force('collision', d3.forceCollide().radius(d => d.radius))
        .on('tick', ticked);
        
    // Add markers for reaction arrows
    networkSvg.append('defs').append('marker')
        .attr('id', 'reaction-arrow')
        .attr('viewBox', '0 -5 10 10')
        .attr('refX', 15)
        .attr('refY', 0)
        .attr('markerWidth', 6)
        .attr('markerHeight', 6)
        .attr('orient', 'auto')
        .append('path')
        .attr('d', 'M0,-5L10,0L0,5')
        .attr('fill', '#999');
        
    // Create link and node groups
    g.append('g').attr('class', 'links');
    g.append('g').attr('class', 'nodes');
}

// Render network with current data
function renderNetwork() {
    if (!networkSvg) return;
    
    const g = networkSvg.select('g');
    const links = g.select('.links').selectAll('line')
        .data(networkData.links, d => `${d.source.id || d.source}-${d.target.id || d.target}`);
        
    // Remove old links
    links.exit().remove();
    
    // Add new links
    const newLinks = links.enter().append('line')
        .attr('class', 'reaction')
        .attr('stroke', d => d.type === 'catalysis' ? '#9c27b0' : '#999')
        .attr('stroke-dasharray', d => d.type === 'catalysis' ? '5,5' : null)
        .attr('marker-end', d => d.type === 'reaction' ? 'url(#reaction-arrow)' : null);
        
    linkElements = newLinks.merge(links);
    
    // Update nodes
    const nodes = g.select('.nodes').selectAll('.node-group')
        .data(networkData.nodes, d => d.id);
        
    // Remove old nodes
    nodes.exit().remove();
    
    // Add new nodes
    const nodeGroups = nodes.enter().append('g')
        .attr('class', 'node-group')
        .call(d3.drag()
            .on('start', dragstarted)
            .on('drag', dragged)
            .on('end', dragended));
    
    // Add circle for each molecule
    nodeGroups.append('circle')
        .attr('class', 'molecule')
        .attr('r', d => getNodeRadius(d))
        .attr('fill', d => getMoleculeColor(d))
        .attr('stroke', d => {
            if (d.is_amphiphilic) return '#ff9800';
            return '#666';
        });
    
    // Add text label for each molecule
    nodeGroups.append('text')
        .attr('text-anchor', 'middle')
        .attr('dy', '.3em')
        .attr('font-size', '10px')
        .text(d => d.name);
    
    // Add events for tooltips
    nodeGroups.on('mouseover', showTooltip)
        .on('mouseout', hideTooltip)
        .on('click', showMoleculeDetail);
    
    nodeElements = nodeGroups.merge(nodes);
    
    // Update the simulation
    simulation.nodes(networkData.nodes);
    simulation.force('link').links(networkData.links);
    simulation.alpha(0.3).restart();
}

// Update the network when data changes
function updateNetworkData(molecules, reactions) {
    // Process molecules into nodes
    const nodes = Object.entries(molecules).map(([name, data]) => {
        return {
            id: name,
            name: name,
            count: data.count || 0,
            complexity: data.complexity || 1,
            is_amphiphilic: data.is_amphiphilic || false,
            is_catalyst: data.is_catalyst || false,
            position: data.position || null
        };
    });
    
    // Process reactions into links
    const links = [];
    if (reactions && networkConfig.showReactions) {
        reactions.forEach(reaction => {
            // For each reactant to product, create a link
            reaction.reactants.forEach(reactant => {
                reaction.products.forEach(product => {
                    links.push({
                        source: reactant,
                        target: product,
                        type: 'reaction'
                    });
                });
            });
            
            // Add catalysis links
            if (networkConfig.highlightCatalysts && reaction.catalysts) {
                reaction.catalysts.forEach(catalyst => {
                    // Mark the catalyst node
                    const catalystNode = nodes.find(n => n.id === catalyst);
                    if (catalystNode) {
                        catalystNode.is_catalyst = true;
                    }
                    
                    // Create catalysis links to products
                    reaction.products.forEach(product => {
                        links.push({
                            source: catalyst,
                            target: product,
                            type: 'catalysis'
                        });
                    });
                });
            }
        });
    }
    
    // Filter out molecules with count 0
    networkData.nodes = nodes.filter(n => n.count > 0);
    networkData.links = links.filter(link => {
        const sourceExists = networkData.nodes.some(n => n.id === link.source);
        const targetExists = networkData.nodes.some(n => n.id === link.target);
        return sourceExists && targetExists;
    });
    
    renderNetwork();
}

// Tick function for force simulation
function ticked() {
    if (!nodeElements || !linkElements) return;
    
    linkElements
        .attr('x1', d => d.source.x)
        .attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x)
        .attr('y2', d => d.target.y);
        
    nodeElements.attr('transform', d => `translate(${d.x},${d.y})`);
}

// Drag functions for nodes
function dragstarted(event, d) {
    if (!event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragged(event, d) {
    d.fx = event.x;
    d.fy = event.y;
}

function dragended(event, d) {
    if (!event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}

// Helper functions for node visualization
function getNodeRadius(node) {
    return 5 + Math.min(15, Math.sqrt(node.count) + node.complexity);
}

function getMoleculeColor(node) {
    if (node.is_catalyst && networkConfig.highlightCatalysts) {
        return '#e1bee7'; // Light purple for catalysts
    }
    
    if (node.complexity > 8) {
        return '#4caf50'; // Green for complex molecules
    } else if (node.complexity > 4) {
        return '#8bc34a'; // Light green for medium complexity
    } else {
        return '#2196f3'; // Blue for simple molecules
    }
}

// Tooltip functions
function showTooltip(event, d) {
    const tooltip = document.getElementById('molecule-tooltip');
    tooltip.innerHTML = `
        <strong>${d.name}</strong><br>
        Count: ${d.count}<br>
        Complexity: ${d.complexity.toFixed(1)}
        ${d.is_amphiphilic ? '<br><span class="badge bg-warning">Amphiphilic</span>' : ''}
        ${d.is_catalyst ? '<br><span class="badge bg-purple">Catalyst</span>' : ''}
    `;
    
    // Position the tooltip near the mouse but not directly under it
    const rect = document.getElementById('molecule-network').getBoundingClientRect();
    tooltip.style.left = (event.pageX - rect.left + 10) + 'px';
    tooltip.style.top = (event.pageY - rect.top + 10) + 'px';
    tooltip.style.display = 'block';
}

function hideTooltip() {
    document.getElementById('molecule-tooltip').style.display = 'none';
}

function showMoleculeDetail(event, d) {
    // TODO: Show detailed information about the molecule in a modal or info panel
    console.log('Molecule details:', d);
}

// Zoom controls
function zoomNetwork(factor) {
    const newZoom = networkConfig.zoomLevel * factor;
    networkSvg.transition().duration(300).call(
        zoom.transform,
        d3.zoomIdentity.scale(newZoom)
    );
}

function resetNetworkView() {
    networkSvg.transition().duration(500).call(
        zoom.transform,
        d3.zoomIdentity
    );
}

// Update network display based on config
function updateNetworkDisplay() {
    // Re-populate network data to apply new settings
    if (simulation && simulationData.moleculeData) {
        updateNetworkData(simulationData.moleculeData, simulationData.reactionData);
    }
}

// Add network data update to socketio events
// Add these functions to the existing Socket.IO event handling in main.js
function addNetworkDataHandling() {
    // Store molecule and reaction data
    simulationData.moleculeData = {};
    simulationData.reactionData = [];
    
    // Original Socket.IO update handler - we'll extend this in main.js
    const originalUpdateHandler = socket.onUpdateHandlers?.simulation_update;
    
    // Function to process network data from simulation updates
    window.processNetworkData = function(data) {
        // Check if we got molecular network data
        if (data.molecular_network) {
            simulationData.moleculeData = data.molecular_network.molecules || {};
            simulationData.reactionData = data.molecular_network.reactions || [];
            
            // Update the visualization if in network view
            if (document.getElementById('network-view-panel').style.display !== 'none') {
                updateNetworkData(simulationData.moleculeData, simulationData.reactionData);
            }
        }
    };
}

// Initialize network data handling
addNetworkDataHandling();