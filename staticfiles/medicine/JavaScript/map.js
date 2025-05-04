const script = document.createElement('script');
script.src = 'http://sehirharitasi.ibb.gov.tr/api/map2.js';
script.async = true;
document.head.appendChild(script);

// Harita oluşturma fonksiyonu
function initializeMap() {
    // Harita seçenekleri
    const mapOptions = {
        center: new google.maps.LatLng(41.0082, 28.9784), // İstanbul koordinatları
        zoom: 12, // Yakınlaştırma seviyesi
        mapTypeId: google.maps.MapTypeId.ROADMAP // Harita tipi
    };

    // Harita öğesini oluşturma
    const map = new google.maps.Map(document.getElementById('map'), mapOptions);

    // İstanbul Haritası API'sinden alınan harita, 'map' ID'sine sahip div içine yerleştirilir
}

// Harita yüklendiğinde initializeMap fonksiyonunu çağırma
window.onload = initializeMap;
