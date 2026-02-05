let attendanceLineChartInstance = null;
let classesRoundedChartInstance = null;
let classesRoundedChart1Instance = null;
let attendanceRowChartInstance = null;

function renderAttendanceChart(diagram) {
  const labels = diagram.labels || [];
  const reason = diagram.reason || [];
  const noReason = diagram.no_reason || [];

  if (!labels.length) return;

  const canvas = document.getElementById("attendanceLineChart");
  if (!canvas) return;

  if (attendanceLineChartInstance) attendanceLineChartInstance.destroy();

  attendanceLineChartInstance = new Chart(canvas, {
    type: "line",
    data: {
      labels,
      datasets: [
        { label: "Sababli kelmaganlar", data: reason, tension: 0.5 },
        { label: "Sababsiz kelmaganlar", data: noReason, tension: 0.5 },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: { legend: { display: true, position: "top" } },
      scales: {
        y: { beginAtZero: true, ticks: { stepSize: 1, precision: 0 } },
      },
    },
  });
}

function classesRoundedChart(stats) {
  const canvas = document.getElementById("classesRoundedChart");
  if (!canvas) return;

  const kelmagan = Number(stats.km_protcent || 0);
  const kelgan = Number(stats.k_protcent || 0);

  if (classesRoundedChartInstance) classesRoundedChartInstance.destroy();

  classesRoundedChartInstance = new Chart(canvas, {
    type: "doughnut",
    data: {
      labels: ["Kelganlar", "Kelmagan"],
      datasets: [
        {
          data: [kelgan, kelmagan],
          borderWidth: 2,
          borderRadius: 8,
          spacing: 3,
        },
      ],
    },
    options: {
      responsive: true,
      cutout: "65%",
      plugins: { legend: { position: "bottom" } },
    },
  });
}

function classesRoundedChart1(classesData) {
  const canvas = document.getElementById("classesRoundedChart1");
  if (!canvas) return;

  const updated = Number(classesData.updated_classes || 0);
  const unupdated = Number(classesData.unupdated_classes || 0);

  if (classesRoundedChart1Instance) classesRoundedChart1Instance.destroy();

  classesRoundedChart1Instance = new Chart(canvas, {
    type: "doughnut",
    data: {
      labels: ["Yangilangan", "Yangilanmagan"],
      datasets: [
        {
          data: [updated, unupdated],
          borderWidth: 2,
          borderRadius: 8,
          spacing: 3,
        },
      ],
    },
    options: {
      responsive: true,
      cutout: "70%",
      plugins: {
        legend: {
          position: "bottom",
          maxHeight: 40, 
          labels: {
            boxWidth: 12,
            padding: 15,
          },
        },
      },
    },
  });
}

function drawClassAbsenceBarChart(classesData) {
  const canvas = document.getElementById("attendanceRowChart");
  if (!canvas) return;

  const rows = classesData.classes || [];
  const labels = rows.map((r) => r.name);
  const totals = rows.map(
    (r) => Number(r.reason_absent || 0) + Number(r.no_reason_absent || 0),
  );

  if (attendanceRowChartInstance) attendanceRowChartInstance.destroy();

  attendanceRowChartInstance = new Chart(canvas, {
    type: "bar",
    data: {
      labels,
      datasets: [
        { label: "Kelmaganlar", data: totals, borderWidth: 1, borderRadius: 8 },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { position: "bottom" },
      },
      scales: {
        x: {
          ticks: {
            autoSkip: false,
            maxRotation: 45,
            minRotation: 45,
          },
          grid: { display: false },
        },
        y: {
          beginAtZero: true,
          ticks: { precision: 0, stepSize: 1 },
        },
      },
    },
  });
}

const btn = document.getElementById("upload-excel-btn");
const fileInput = document.getElementById("excel-file");
const resultDiv = document.getElementById("upload-result");

btn.onclick = () => fileInput.click();

fileInput.onchange = async () => {
  const file = fileInput.files[0];
  if (!file) return;

  const formData = new FormData();
  formData.append("file", file);
  formData.append("school_name", "{{ school_name }}");

  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

  resultDiv.innerHTML = "⏳ Yuklanmoqda...";

  try {
    const res = await fetch("/admin/upload/", {
      method: "POST",
      headers: { "X-CSRFToken": csrftoken },
      body: formData
    });

    const data = await res.json();

    if (data.ok) {
      resultDiv.innerHTML = "✅ Muvaffaqiyatli yuklandi!";
      resultDiv.style.color = "green";
    } else {
      resultDiv.innerHTML = "❌ " + data.error;
      resultDiv.style.color = "red";
    }

  } catch (e) {
    resultDiv.innerHTML = "❌ Server xatosi";
    resultDiv.style.color = "red";
  }
};

document.addEventListener("DOMContentLoaded", () => {
  const classesData = JSON.parse(
    document.getElementById("classes-data").textContent,
  );
  const diagramData = JSON.parse(
    document.getElementById("diagram-data").textContent,
  );
  const schoolStats = JSON.parse(
    document.getElementById("school-stats").textContent,
  );

  classesRoundedChart1(classesData);
  classesRoundedChart(schoolStats);
  renderAttendanceChart(diagramData);
  drawClassAbsenceBarChart(classesData);
});
