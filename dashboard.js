document.getElementById("modeToggle").addEventListener("click", function() {
    const body = document.getElementById("body");
    body.classList.toggle("light-mode");


    if (document.body.classList.contains('light-mode')) {
        this.textContent = '🌙'; // Change text to 'Light Mode' when in dark mode
    } else {
        this.textContent = '🌞'; // Change text to 'Dark Mode' when not in dark mode
    }
});
