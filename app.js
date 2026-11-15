let energyChart = null;

document.addEventListener("DOMContentLoaded", () => {
    initChart();
    setupListeners();
});

function initChart() {
    const ctx = document.getElementById("energyChart").getContext("2d");
    energyChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Array.from({length: 24}, (_, i) => `${i.toString().padStart(2, '0')}:00`),
            datasets: [
                {
                    label: 'Washing Machine',
                    data: [0,0,0,0,0,0, 0,0,0,0,0, 2.1, 2.1,0,0,0,0,0, 0,0,0,0,0,0],
                    backgroundColor: '#10b981',
                },
                {
                    label: 'Water Heater',
                    data: [0,0,0,0,0,3.5, 3.5,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0],
                    backgroundColor: '#6366f1',
                },
                {
                    label: 'EV Charger',
                    data: [7.2,7.2,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,7.2,7.2],
                    backgroundColor: '#f59e0b',
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: { stacked: true, grid: { color: '#1e293b' }, ticks: { color: '#94a3b8' } },
                y: { stacked: true, grid: { color: '#1e293b' }, ticks: { color: '#94a3b8' }, title: { display: true, text: 'Power (kW)', color: '#94a3b8' } }
            },
            plugins: {
                legend: { labels: { color: '#f8fafc' } }
            }
        }
    });
}

function setupListeners() {
    const costInput = document.getElementById("weight-cost");
    const comfortInput = document.getElementById("weight-comfort");
    const convInput = document.getElementById("weight-conv");

    [costInput, comfortInput, convInput].forEach(input => {
        input.addEventListener("input", updateWeights);
    });
}

function updateWeights() {
    const cost = parseFloat(document.getElementById("weight-cost").value);
    const comfort = parseFloat(document.getElementById("weight-comfort").value);
    const conv = parseFloat(document.getElementById("weight-conv").value);

    document.getElementById("val-cost").innerText = cost.toFixed(2);
    document.getElementById("val-comfort").innerText = comfort.toFixed(2);
    document.getElementById("val-conv").innerText = conv.toFixed(2);

    const costKpi = (3.20 - cost * 1.5).toFixed(2);
    const peakKpi = (7.2 - cost * 2.0).toFixed(1);
    
    document.getElementById("kpi-cost").innerText = `$${costKpi}`;
    document.getElementById("kpi-peak").innerText = `${peakKpi} kW`;
}

function setWeights(c, f, v) {
    document.getElementById("weight-cost").value = c;
    document.getElementById("weight-comfort").value = f;
    document.getElementById("weight-conv").value = v;
    updateWeights();
}
