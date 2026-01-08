function submitFeedback() {
    fetch("http://127.0.0.1:5000/submit", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            student_name: document.getElementById("name").value,
            class: document.getElementById("class").value,
            subject: document.getElementById("subject").value,
            rating: document.getElementById("rating").value,
            comments: document.getElementById("comments").value
        })
    })
    .then(response => response.json())
    .then(data => alert(data.message));
}
