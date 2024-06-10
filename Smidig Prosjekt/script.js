document.getElementById("loginButton").addEventListener("click", function () {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username && password) {
        if (password === "123") {
            window.location.href = "dashboard.html";
        } else {
            alert("Feil passord")
        }
    } else {
        alert("Skriv inn både passord og brukernavn")
    }
});