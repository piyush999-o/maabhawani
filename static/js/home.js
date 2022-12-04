const toursBtn = document.getElementById('tours-btn');

toursBtn.addEventListener("click", () => {
    scrollFunction()
})

function scrollFunction() {

    window.scroll({
        top: 620,
        behavior: "smooth"
    });
}

// if (document.documentElement.scrollTop <= 50) {
//     toursBtn.href = "#all-tours"
// } else {
//     toursBtn.href = "#"
// }
