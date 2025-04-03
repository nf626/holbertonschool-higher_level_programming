document.getElementById("toggle_header").addEventListener("click", myfunction);
function myfunction() {
    document.querySelector("header").classList.toggle("red");
    document.querySelector("header").classList.toggle("green");
}
