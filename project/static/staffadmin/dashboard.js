function renderAttendanceChart() {
  const raw = document.getElementById("diagram-data").textContent;
  const diagram = JSON.parse(raw);

  const labels = diagram.labels || [];
  const reason = diagram.reason || [];
  const noReason = diagram.no_reason || [];

  if (!labels.length || (!reason.length && !noReason.length)) {
    return;
  }

  const ctx = document.getElementById("attendanceLineChart").getContext("2d");

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

function classesRoundedChart() {
  const ctx = document.getElementById("classesRoundedChart");

  const kelmagan = Number(
    JSON.parse(document.getElementById("rounded_diagram_kelmagan").textContent),
  );

  const kelgan = Number(
    JSON.parse(document.getElementById("rounded_diagram_kelgan").textContent),
  );

  new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: ["Kelganlar", "Kelmaganlar"],
      datasets: [
        {
          data: [kelgan, kelmagan],
          backgroundColor: ["#00ff99", "#f30008"],
          borderWidth: 2,
          borderRadius: 8,
          borderColor: "#D3D3D3",
          spacing: 3,
        },
      ],
    },
    options: {
      cutout: "65%",
      plugins: {
        legend: { position: "bottom" },

        tooltip: {
          callbacks: {
            label: function (context) {
              const data = context.dataset.data;
              const total = data.reduce((a, b) => a + b, 0);
              const value = context.raw;

              const percent = ((value / total) * 100).toFixed(1);

              return `${context.label}: ${percent}%`;
            },
          },
        },
      },
    },
  });
}

function classesRoundedChart1() {
  const ctx = document.getElementById("classesRoundedChart1");
  const updated_classes = Number(
    JSON.parse(document.getElementById("updated_classes").textContent),
  );

  const unupdated_classes = Number(
    JSON.parse(document.getElementById("unupdated_classes").textContent),
  );
  new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: ["Yangilangan", "Yangilanmagan"],
      datasets: [
        {
          data: [updated_classes, unupdated_classes],
          backgroundColor: ["#00ff99", "#f30008"],
          borderWidth: 2,
          borderRadius: 8,
          borderColor: "#D3D3D3",
          spacing: 3,
        },
      ],
    },
    options: {
      cutout: "65%",
      plugins: {
        legend: { position: "bottom" },
      },
    },
  });
}

classesRoundedChart1();
classesRoundedChart();
renderAttendanceChart();
