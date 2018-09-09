let header = document.getElementById('header')

window.addEventListener("scroll", function() {
    (window.scrollY === 0) ? header.classList.remove("header-bg") : header.classList.add("header-bg");
});

// Slick Corousell
$(document).ready(function(){
    $('.items-aliados').slick({
        autoplay: true,
        autoplaySpeed: 5000,
        variableWidth: true
    });
});