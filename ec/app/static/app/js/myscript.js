document.getElementById("filter-button").addEventListener("click", function() {
    var keyword = prompt("Introduceți cuvântul cheie pentru filtrare:");
    if (keyword !== null) {
        window.location.href = "/search/?query=" + keyword;
    }
});