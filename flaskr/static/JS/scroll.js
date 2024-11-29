const scrollContainer = document.getElementById('scrollContainer');
let index = 0;
const images = scrollContainer.querySelectorAll('img');

function scrollNext() {
    index++;
    if (index >= images.length) {
        index = 0;
    }
    const scrollWidth = images[0].clientWidth;
    scrollContainer.scrollLeft = index * scrollWidth;
}

setInterval(scrollNext, 5000); // Scrolls every 3 seconds