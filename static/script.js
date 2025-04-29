// Function to handle URL scan
function scanUrl() {
    const url = document.getElementById('url_input').value;
    if (url === "") {
        alert("Please enter a URL to scan.");
        return;
    }

    fetch('http://127.0.0.1:5000/url_scan', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "url": url })
    })
    .then(response => response.json())
    .then(data => {
        const result = data.result;
        const resultElement = document.getElementById('url_result');
        resultElement.textContent = `The URL is ${result}.`;
        resultElement.className = result === "benign" ? "result-text success" : "result-text error";
    })
    .catch(error => {
        console.error('Error:', error);
        alert("An error occurred. Please try again later.");
    });
}
