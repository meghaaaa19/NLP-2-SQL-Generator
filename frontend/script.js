async function generateSQL() {
    const query = document.getElementById("queryInput").value;

    const response = await fetch("http://127.0.0.1:5000/generate_sql", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: query })
    });

    const data = await response.json();
    console.log("🔍 Raw API Response:", data);  // Debugging

    displayResults(data);
}

function displayResults(data) {
    const resultDiv = document.getElementById("resultSection");
    const queryResults = document.getElementById("queryResults");
    const sqlQuery = document.getElementById("sqlQuery");

    if (data.error) {
        queryResults.innerHTML = `<p class="text-danger">${data.error}</p>`;
        resultDiv.classList.remove("d-none");
        return;
    }

    sqlQuery.innerText = data.sql; // Show generated SQL

    // Check if results exist
    if (!data.results || !data.results.rows || data.results.rows.length === 0) {
        queryResults.innerHTML = "<p class='text-muted'>No matching records found.</p>";
        resultDiv.classList.remove("d-none");
        return;
    }

    // Create Bootstrap Table
    let tableHTML = `<div class="table-responsive" style="max-height: 400px; overflow-y: auto;">
                    <table class="table table-bordered table-striped">`;
    tableHTML += "<thead class='table-dark position-sticky top-0'><tr>";

    // Column Headers
    data.results.columns.forEach(col => {
        tableHTML += `<th>${col}</th>`;
    });
    tableHTML += "</tr></thead><tbody>";

    // Table Rows
    data.results.rows.forEach(row => {
        tableHTML += "<tr>";
        data.results.columns.forEach(col => {
            tableHTML += `<td>${row[col]}</td>`;
        });
        tableHTML += "</tr>";
    });

    tableHTML += "</tbody></table></div>";
    queryResults.innerHTML = tableHTML;

    resultDiv.classList.remove("d-none");
}

function goBack() {
    document.getElementById("resultSection").classList.add("d-none");
}
