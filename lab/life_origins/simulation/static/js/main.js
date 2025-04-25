// Main JavaScript for the chemical evolution simulation visualization

// Initialize Socket.IO connection
const socket = io();

// Chart instances
let complexityChart = null;
let moleculesChart = null;
let constraintChart = null;

// Data storage
const simulationData = {
    steps: [],
    complexity: [],
    molecules: [],
    energy: [],
    negentropyValues: [],
    feedbackValues: [],
    resilienceValues: [],
    functionalPhases: [],
    thresholdDetections: []
};

// Constants for threshold detection
const THRESHOLDS = {
    negentropy: 0.15,
    feedback: 0.10,
    resilience: 0.75,
    compartment: 0.50
};

// Maximum number of data points to show in charts (sliding window)
const MAX_VISIBLE_DATA_POINTS = 50;

// Initialize the UI when the document is ready
document.addEventListener('DOMContentLoaded', function() {
    // Set up event listeners
    document.getElementById('start-btn').addEventListener('click', startSimulation);
    document.getElementById('stop-btn').addEventListener('click', stopSimulation);
    
    // Initialize charts
    initializeCharts();
    
    // Set up Socket.IO event listeners
    setupSocketListeners();
});

// Set up all Socket.IO event listeners
function setupSocketListeners() {
    // Connection status
    socket.on('connect', () => {
        updateStatus('Connected to server', 'secondary');
    });
    
    socket.on('disconnect', () => {
        updateStatus('Disconnected from server', 'danger');
        setSimulationRunning(false);
    });
    
    // Status messages
    socket.on('status', (data) => {
        updateStatus(data.status, 'info');
    });
    
    // Handle errors
    socket.on('error', (data) => {
        updateStatus(`Error: ${data.message}`, 'danger');
        setSimulationRunning(false);
    });
    
    // Simulation updates
    socket.on('simulation_update', (data) => {
        updateSimulationData(data);
        updateProgressBar(data.step, data.total_steps);
        updateCharts();
        checkForEmergenceThresholds(data);
        
        // Process molecular network data if available
        if (data.molecular_network) {
            // Store the molecular network data for visualization
            simulationData.moleculeData = data.molecular_network.molecules || {};
            simulationData.reactionData = data.molecular_network.reactions || [];
            
            // Update network visualization if we're in network view
            if (document.getElementById('network-view-panel').style.display !== 'none' && typeof updateNetworkData === 'function') {
                updateNetworkData(simulationData.moleculeData, simulationData.reactionData);
            }
        }
    });
    
    // Threshold detection
    socket.on('threshold_detection', (data) => {
        handleThresholdDetection(data);
    });
    
    // Constraint hypothesis results
    socket.on('constraint_results', (data) => {
        updateConstraintResults(data);
    });
    
    // Final results
    socket.on('simulation_complete', (data) => {
        updateFinalResults(data);
        setSimulationRunning(false);
    });
}

// Check for emergence thresholds in simulation data
function checkForEmergenceThresholds(data) {
    // Update negentropy indicator
    if (data.negentropy !== undefined) {
        document.getElementById('negentropy-indicator').textContent = data.negentropy.toFixed(2);
        if (data.negentropy >= THRESHOLDS.negentropy) {
            document.getElementById('negentropy-indicator').classList.add('threshold-reached');
        }
    }
    
    // Update feedback indicator
    if (data.feedback !== undefined) {
        document.getElementById('feedback-indicator').textContent = data.feedback.toFixed(2);
        if (data.feedback >= THRESHOLDS.feedback) {
            document.getElementById('feedback-indicator').classList.add('threshold-reached');
        }
    }
    
    // Update resilience indicator
    if (data.resilience !== undefined) {
        document.getElementById('resilience-indicator').textContent = data.resilience.toFixed(2);
        if (data.resilience >= THRESHOLDS.resilience) {
            document.getElementById('resilience-indicator').classList.add('threshold-reached');
        }
    }
    
    // Update functional phase indicator
    if (data.functional_phase !== undefined) {
        const phaseElement = document.getElementById('functional-indicator');
        const previousPhase = phaseElement.textContent;
        phaseElement.textContent = data.functional_phase;
        
        // Highlight if this is a new phase transition
        if (data.functional_phase !== previousPhase && data.functional_phase !== "None") {
            phaseElement.classList.add('threshold-reached');
            
            // Add marker to the chart
            addThresholdMarker(complexityChart, data.step, `Phase: ${data.functional_phase}`);
        }
    }
    
    // Update compartmentalization probability
    if (data.compartment_probability) {
        document.getElementById('p-amphiphilic').textContent = 
            data.compartment_probability.p_amphiphilic.toFixed(2);
        document.getElementById('p-assembly').textContent = 
            data.compartment_probability.p_self_assembly.toFixed(2);
        document.getElementById('p-compartment').textContent = 
            data.compartment_probability.p_compartment.toFixed(2);
        
        // Check compartmentalization threshold
        if (data.compartment_probability.p_compartment >= THRESHOLDS.compartment) {
            document.getElementById('p-compartment').classList.add('threshold-reached');
        }
    }
}

// Handle threshold detection events from server
function handleThresholdDetection(data) {
    // Add visual indicator for threshold detection
    data.thresholds.forEach(threshold => {
        let message = '';
        
        switch(threshold) {
            case 'negentropy':
                message = 'Negentropy Leap Detected';
                break;
            case 'feedback':
                message = 'Feedback Cycle Established';
                break;
            case 'resilience':
                message = 'System Resilience Achieved';
                break;
            case 'compartmentalization':
                message = 'Compartmentalization Threshold';
                break;
        }
        
        // Add marker to chart
        if (message && complexityChart) {
            addThresholdMarker(complexityChart, data.step, message);
        }
    });
}

// Initialize all charts
function initializeCharts() {
    // Complexity chart
    complexityChart = new Chart(
        document.getElementById('complexity-chart').getContext('2d'), 
        {
            type: 'line',
            data: {
                labels: [],
                datasets: [{
                    label: 'Complexity Score',
                    backgroundColor: 'rgba(0, 123, 255, 0.1)',
                    borderColor: 'rgba(0, 123, 255, 1)',
                    data: []
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                aspectRatio: 2,
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Complexity Score'
                        },
                        // Fix y-axis scaling
                        min: 0,
                        suggestedMax: 10
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Simulation Step'
                        }
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: 'System Complexity Over Time'
                    }
                }
            }
        }
    );
    
    // Molecules chart
    moleculesChart = new Chart(
        document.getElementById('molecules-chart').getContext('2d'), 
        {
            type: 'line',
            data: {
                labels: [],
                datasets: [{
                    label: 'Molecule Count',
                    backgroundColor: 'rgba(40, 167, 69, 0.1)',
                    borderColor: 'rgba(40, 167, 69, 1)',
                    data: []
                }, {
                    label: 'Energy Currency',
                    backgroundColor: 'rgba(255, 193, 7, 0.1)',
                    borderColor: 'rgba(255, 193, 7, 1)',
                    data: []
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                aspectRatio: 2,
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Count'
                        },
                        // Fix y-axis scaling
                        min: 0,
                        suggestedMax: 100
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Simulation Step'
                        }
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: 'Molecules and Energy Over Time'
                    }
                }
            }
        }
    );
}

// Start the simulation
function startSimulation() {
    // Get input values
    const simulationType = document.getElementById('simulation-type').value;
    const steps = parseInt(document.getElementById('steps').value);
    
    // Validate inputs
    if (steps < 100 || steps > 10000) {
        updateStatus('Steps must be between 100 and 10000', 'danger');
        return;
    }
    
    // Clear previous data
    resetSimulationData();
    resetCharts();
    resetThresholdIndicators();
    
    // Show/hide constraint results section based on simulation type
    document.getElementById('constraint-results').style.display = 
        (simulationType === 'constraint_hypothesis') ? 'block' : 'none';
    
    // Start simulation on server
    socket.emit('start_simulation', {
        type: simulationType,
        steps: steps
    });
    
    // Update UI
    setSimulationRunning(true);
    updateStatus('Starting simulation...', 'info');
}

// Stop the simulation
function stopSimulation() {
    socket.emit('stop_simulation');
    updateStatus('Stopping simulation...', 'warning');
    // Clean up markers
    document.querySelectorAll('.feature-marker, .feature-marker-label').forEach(marker => marker.remove());
}

// Update the status message
function updateStatus(message, type) {
    const statusElement = document.getElementById('status-message');
    statusElement.textContent = message;
    
    // Remove all alert classes
    statusElement.classList.remove('alert-primary', 'alert-secondary', 'alert-success', 
        'alert-danger', 'alert-warning', 'alert-info');
    
    // Add the appropriate alert class
    statusElement.classList.add(`alert-${type}`);
}

// Update progress bar
function updateProgressBar(current, total) {
    const progressBar = document.getElementById('simulation-progress');
    const percentage = (current / total) * 100;
    
    progressBar.style.width = `${percentage}%`;
    progressBar.setAttribute('aria-valuenow', percentage);
}

// Update UI for simulation running state
function setSimulationRunning(isRunning) {
    document.getElementById('start-btn').disabled = isRunning;
    document.getElementById('stop-btn').disabled = !isRunning;
    document.getElementById('simulation-type').disabled = isRunning;
    document.getElementById('steps').disabled = isRunning;
    
    if (!isRunning) {
        updateProgressBar(0, 1);
        
        // Clean up all marker elements when simulation stops
        document.querySelectorAll('.feature-marker, .feature-marker-label').forEach(marker => {
            marker.remove();
        });
        
        // Force chart redraw with fixed dimensions
        if (complexityChart) {
            complexityChart.resize();
        }
        if (moleculesChart) {
            moleculesChart.resize();
        }
    }
}

// Update simulation data with new values
function updateSimulationData(data) {
    simulationData.steps.push(data.step);
    simulationData.complexity.push(data.complexity);
    simulationData.molecules.push(data.molecules);
    simulationData.energy.push(data.energy);
    
    // Calculate derived metrics for threshold detection
    calculateNegentropyValue(data);
    calculateFeedbackCoefficient(data);
    calculateResilience(data);
    detectFunctionalPhase(data);
    
    // Apply data windowing to prevent charts from continuously expanding
    if (simulationData.steps.length > MAX_VISIBLE_DATA_POINTS) {
        simulationData.steps.shift();
        simulationData.complexity.shift();
        simulationData.molecules.shift();
        simulationData.energy.shift();
        simulationData.negentropyValues.shift();
        simulationData.feedbackValues.shift();
        simulationData.resilienceValues.shift();
        simulationData.functionalPhases.shift();
    }
}

// Reset all simulation data
function resetSimulationData() {
    simulationData.steps = [];
    simulationData.complexity = [];
    simulationData.molecules = [];
    simulationData.energy = [];
    simulationData.negentropyValues = [];
    simulationData.feedbackValues = [];
    simulationData.resilienceValues = [];
    simulationData.functionalPhases = [];
    simulationData.thresholdDetections = [];
}

// Reset all charts
function resetCharts() {
    if (complexityChart) {
        complexityChart.data.labels = [];
        complexityChart.data.datasets[0].data = [];
        complexityChart.update();
    }
    
    if (moleculesChart) {
        moleculesChart.data.labels = [];
        moleculesChart.data.datasets[0].data = [];
        moleculesChart.data.datasets[1].data = [];
        moleculesChart.update();
    }
    
    if (constraintChart) {
        if (constraintChart) {
            constraintChart.destroy();
            constraintChart = null;
        }
    }
}

// Update charts with current data
function updateCharts() {
    if (complexityChart) {
        // Update data
        complexityChart.data.labels = simulationData.steps;
        complexityChart.data.datasets[0].data = simulationData.complexity;
        
        // Set fixed y-axis limits to prevent vertical expansion
        complexityChart.options.scales.y.min = 0;
        complexityChart.options.scales.y.suggestedMax = Math.max(10, Math.ceil(Math.max(...simulationData.complexity) * 1.1));
        
        complexityChart.update();
    }
    
    if (moleculesChart) {
        // Update data
        moleculesChart.data.labels = simulationData.steps;
        moleculesChart.data.datasets[0].data = simulationData.molecules;
        moleculesChart.data.datasets[1].data = simulationData.energy;
        
        // Set fixed y-axis limits to prevent vertical expansion
        moleculesChart.options.scales.y.min = 0;
        const maxValue = Math.max(
            Math.max(...simulationData.molecules), 
            Math.max(...simulationData.energy)
        );
        moleculesChart.options.scales.y.suggestedMax = Math.max(100, Math.ceil(maxValue * 1.1));
        
        moleculesChart.update();
    }
}

// Initialize constraint results chart
function initializeConstraintChart() {
    if (constraintChart) {
        constraintChart.destroy();
    }
    
    const ctx = document.getElementById('constraint-chart').getContext('2d');
    constraintChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['1', '2', '3', '4', '5'],
            datasets: [
                {
                    label: 'Feedback Coefficient',
                    backgroundColor: 'rgba(0, 123, 255, 0.7)',
                    data: [0, 0, 0, 0, 0]
                },
                {
                    label: 'Complexity Score',
                    backgroundColor: 'rgba(40, 167, 69, 0.7)',
                    data: [0, 0, 0, 0, 0]
                },
                {
                    label: 'Molecule Count',
                    backgroundColor: 'rgba(255, 193, 7, 0.7)',
                    data: [0, 0, 0, 0, 0]
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Constraint Level'
                    }
                },
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Value'
                    }
                }
            },
            plugins: {
                title: {
                    display: true,
                    text: 'Constraint Hypothesis Results'
                }
            }
        }
    });
}

// Update constraint results
function updateConstraintResults(data) {
    if (!constraintChart) {
        initializeConstraintChart();
    }
    
    const index = data.constraint_level - 1;
    
    // Update the chart with the new results
    constraintChart.data.datasets[0].data[index] = data.feedback_coef;
    constraintChart.data.datasets[1].data[index] = data.complexity_score;
    constraintChart.data.datasets[2].data[index] = data.molecule_count;
    constraintChart.update();
    
    // Check if this is the "Goldilocks zone" (level 2)
    if (data.constraint_level === 2) {
        document.getElementById('feedback-indicator').textContent = data.feedback_coef.toFixed(2);
        if (data.feedback_coef >= THRESHOLDS.feedback) {
            document.getElementById('feedback-indicator').classList.add('threshold-reached');
        }
    }
    
    // Update compartment probability calculation
    updateCompartmentProbability();
}

// Reset threshold indicators
function resetThresholdIndicators() {
    document.getElementById('negentropy-indicator').textContent = "0.00";
    document.getElementById('functional-indicator').textContent = "None";
    document.getElementById('resilience-indicator').textContent = "0.00";
    document.getElementById('feedback-indicator').textContent = "0.00";
    document.getElementById('p-amphiphilic').textContent = "0.00";
    document.getElementById('p-assembly').textContent = "0.00";
    document.getElementById('p-compartment').textContent = "0.00";
    
    document.getElementById('negentropy-indicator').classList.remove('threshold-reached');
    document.getElementById('resilience-indicator').classList.remove('threshold-reached');
    document.getElementById('feedback-indicator').classList.remove('threshold-reached');
    document.getElementById('p-compartment').classList.remove('threshold-reached');
}

// Calculate negentropy value (order increase)
function calculateNegentropyValue(data) {
    if (simulationData.complexity.length < 2) {
        simulationData.negentropyValues.push(0);
        return;
    }
    
    // Get the last two complexity values
    const current = data.complexity;
    const prev = simulationData.complexity[simulationData.complexity.length - 2];
    
    // Calculate the rate of increase in complexity
    const increase = current - prev;
    const normalized = increase / (prev > 0 ? prev : 1);
    
    // Smooth the value (trailing average)
    const negentropyValue = Math.max(0, normalized);
    simulationData.negentropyValues.push(negentropyValue);
    
    // Update UI
    document.getElementById('negentropy-indicator').textContent = negentropyValue.toFixed(2);
    
    // Check if threshold reached
    if (negentropyValue >= THRESHOLDS.negentropy) {
        document.getElementById('negentropy-indicator').classList.add('threshold-reached');
        recordThresholdDetection('negentropy', data.step);
    }
}

// Calculate feedback coefficient
function calculateFeedbackCoefficient(data) {
    // In a real system, this would involve more complex calculations
    // Here we'll use a simplified model based on complexity and energy
    if (simulationData.complexity.length < 3) {
        simulationData.feedbackValues.push(0);
        return;
    }
    
    // Get recent values
    const complexityTrend = data.complexity - simulationData.complexity[simulationData.complexity.length - 3];
    const energyEfficiency = data.energy / simulationData.molecules.length;
    
    // Calculate feedback coefficient (simplified model)
    const feedback = (complexityTrend > 0 ? complexityTrend / 3 : 0) * energyEfficiency / 10;
    simulationData.feedbackValues.push(feedback);
    
    // Update UI
    document.getElementById('feedback-indicator').textContent = feedback.toFixed(2);
    
    // Check if threshold reached
    if (feedback >= THRESHOLDS.feedback) {
        document.getElementById('feedback-indicator').classList.add('threshold-reached');
        recordThresholdDetection('feedback', data.step);
    }
}

// Calculate system resilience
function calculateResilience(data) {
    // In a real system, this would involve perturbation testing
    // Here we'll use a simplified model based on complexity stability
    if (simulationData.complexity.length < 5) {
        simulationData.resilienceValues.push(0);
        return;
    }
    
    // Get recent complexity values
    const recentComplexity = simulationData.complexity.slice(-5);
    
    // Calculate standard deviation (volatility)
    const mean = recentComplexity.reduce((sum, val) => sum + val, 0) / recentComplexity.length;
    const squaredDiffs = recentComplexity.map(val => Math.pow(val - mean, 2));
    const variance = squaredDiffs.reduce((sum, val) => sum + val, 0) / squaredDiffs.length;
    const stdDev = Math.sqrt(variance);
    
    // Higher complexity with lower volatility = higher resilience
    const complexity = recentComplexity[recentComplexity.length - 1];
    const volatility = stdDev / (mean > 0 ? mean : 1);
    const resilience = Math.min(1, Math.max(0, 1 - volatility) * (complexity / 10));
    
    simulationData.resilienceValues.push(resilience);
    
    // Update UI
    document.getElementById('resilience-indicator').textContent = resilience.toFixed(2);
    
    // Check if threshold reached
    if (resilience >= THRESHOLDS.resilience) {
        document.getElementById('resilience-indicator').classList.add('threshold-reached');
        recordThresholdDetection('resilience', data.step);
    }
}

// Detect functional phase transitions
function detectFunctionalPhase(data) {
    let phase = "None";
    
    // Simplified detection based on complexity and molecular count thresholds
    if (data.molecules > 15 && data.complexity > 5) {
        phase = "Catalytic Networks";
    } else if (data.complexity > 3) {
        phase = "Reaction Cycles";
    } else if (data.molecules > 8) {
        phase = "Molecular Diversity";
    }
    
    simulationData.functionalPhases.push(phase);
    
    // Update UI
    const phaseElement = document.getElementById('functional-indicator');
    phaseElement.textContent = phase;
    
    // Mark as transition if this is a new phase
    const previousPhase = simulationData.functionalPhases.length > 1 ? 
        simulationData.functionalPhases[simulationData.functionalPhases.length - 2] : "None";
    
    if (phase !== previousPhase && phase !== "None") {
        phaseElement.classList.add('threshold-reached');
        recordThresholdDetection('functional-phase', data.step, phase);
        
        // Add visual marker to complexity chart
        addThresholdMarker(complexityChart, data.step, `Phase: ${phase}`);
    }
}

// Update compartment probability calculation
function updateCompartmentProbability() {
    // In a real system, these would be calculated from actual molecular properties
    // Here we'll use a simplified model based on the simulation state
    
    // Calculate probability of amphiphilic molecules
    const pAmphiphilic = simulationData.molecules.length > 0 ? 
        Math.min(0.8, simulationData.molecules[simulationData.molecules.length - 1] / 20) : 0;
    
    // Calculate probability of self-assembly given amphiphilic molecules
    const pAssembly = simulationData.complexity.length > 0 ? 
        Math.min(0.9, simulationData.complexity[simulationData.complexity.length - 1] / 10) : 0;
    
    // Calculate overall compartmentalization probability
    const pCompartment = pAmphiphilic * pAssembly;
    
    // Update UI
    document.getElementById('p-amphiphilic').textContent = pAmphiphilic.toFixed(2);
    document.getElementById('p-assembly').textContent = pAssembly.toFixed(2);
    document.getElementById('p-compartment').textContent = pCompartment.toFixed(2);
    
    // Check if threshold reached
    if (pCompartment >= THRESHOLDS.compartment) {
        document.getElementById('p-compartment').classList.add('threshold-reached');
        recordThresholdDetection('compartmentalization', simulationData.steps[simulationData.steps.length - 1]);
    }
}

// Record a threshold detection event
function recordThresholdDetection(type, step, value = null) {
    const detection = {
        type: type,
        step: step,
        value: value
    };
    
    // Only add if this is a new detection of this type
    if (!simulationData.thresholdDetections.some(d => d.type === type)) {
        simulationData.thresholdDetections.push(detection);
    }
}

// Add a threshold marker to a chart
function addThresholdMarker(chart, step, label) {
    // Find the x position in the chart
    const chartElement = chart.canvas;
    const stepIndex = simulationData.steps.indexOf(step);
    if (stepIndex === -1) return;
    
    const chartPosition = chart.scales.x.getPixelForValue(stepIndex);
    
    // Create marker elements
    const marker = document.createElement('div');
    marker.className = 'feature-marker';
    marker.style.left = `${chartPosition}px`;
    chartElement.parentNode.appendChild(marker);
    
    // Create label
    const markerLabel = document.createElement('div');
    markerLabel.className = 'feature-marker-label';
    markerLabel.textContent = label;
    markerLabel.style.left = `${chartPosition}px`;
    markerLabel.style.bottom = '20px';
    chartElement.parentNode.appendChild(markerLabel);
}

// Process final results
function updateFinalResults(data) {
    updateStatus(`Simulation complete with ${data.final_molecules} molecules and complexity score ${data.complexity_score.toFixed(2)}`, 'success');
}