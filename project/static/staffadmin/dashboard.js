function renderAttendanceChart() {
    const raw = document.getElementById("diagram-data").textContent;
    const diagram = JSON.parse(raw);

    const labels = diagram.labels || [];
    const reason = diagram.reason || [];
    const noReason = diagram.no_reason || [];

    if (!labels.length || (!reason.length && !noReason.length)) {
        return;
    }

    const ctx = document
        .getElementById("attendanceLineChart")
        .getContext("2d");

    new Chart(ctx, {
        type: "line",
        data: {
            labels,
            datasets: [
                {
                    label: "Sababli kelmaganlar",
                    data: reason,
                    tension: 0.5,
                    borderColor: "#11cc00",
                    backgroundColor: "#11cc00",
                },
                {
                    label: "Sababsiz kelmaganlar",
                    data: noReason,
                    tension: 0.5,
                    borderColor: "#f74c3c",
                    backgroundColor: "#f74c3c",
                },
            ],
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true,
                    position: "top", 
                },
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1,
                        precision: 0,
                    },
                },
            },
        },
    });
}

renderAttendanceChart();