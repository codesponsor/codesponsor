var slides = $('#macbook-slideshow .slide');
var currentSlide = 0;
var slideInterval = setInterval(nextSlide,3500);

function nextSlide() {
    $(slides[currentSlide]).hide();
    $(slides[currentSlide]).removeClass('showing');
    currentSlide = (currentSlide+1)%slides.length;
    $(slides[currentSlide]).fadeIn();
    $(slides[currentSlide]).addClass('showing');
}