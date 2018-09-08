let header = document.getElementById('header')

window.addEventListener("scroll", function() {
    (window.scrollY === 0) ? header.classList.remove("header-bg") : header.classList.add("header-bg");
});

// Mapas de Google


function initMap() {
    var myLatLng = {lat: 2.458462, lng: -76.593013};

    var map = new google.maps.Map(document.getElementById('map'), {
        center: myLatLng,
        zoom: 16
    });

    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        title: 'Cooincoffee'
    });
}

// Slick Corousell
$(document).ready(function(){
    $('.items-aliados').slick({
        autoplay: true,
        autoplaySpeed: 5000,
        variableWidth: true
    });
});