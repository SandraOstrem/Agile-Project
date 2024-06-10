document.getElementById("loginButton").addEventListener("click", function () {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username && password) {
        if (password === "123" && username === "admin") { // Dette kan man vel se ved å bare inspisere elementet?
            window.location.href = "dashboard.html";
        } else {
            alert("Feil passord eller brukernavn")
        }
    } else {
        alert("Skriv inn både passord og brukernavn")
    }
});