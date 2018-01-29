var slides = $('#macbook-slideshow .slide');
var currentSlide = 0;
var slideInterval = setInterval(nextSlide,8000);

function nextSlide() {
    $(slides[currentSlide]).hide();
    currentSlide = (currentSlide+1)%slides.length;
    $(slides[currentSlide]).fadeIn();
}