function toggleMenu() {
    const menuToggle = document.querySelector('.menu-toggle');
    const listemenu = document.querySelector('.liste-menu');

    menuToggle.classList.toggle('open');
    listemenu.classList.toggle('show');

    if(menuToggle.textContent === '☰'){
        menuToggle.textContent = 'X';
    }
    else{
        menuToggle.textContent = '☰';
    }
}

let enSonKaydirmaYeri = 0;
const menuIkonu = document.querySelector('.menu-toggle');
const listemenu = document.querySelector('.liste-menu');

window.addEventListener('scroll', function () {
    const simdikiKaydirmaYeri = window.pageYOffset;

    // MENÜ AÇIKSA hamburger menüyü sabit göster
    if (listemenu.classList.contains('show')) {
        menuIkonu.classList.remove('hidden');
        return;
    }

    // MENÜ KAPALIYSA scroll yönüne göre gizle/göster
    if (simdikiKaydirmaYeri > enSonKaydirmaYeri) {
        menuIkonu.classList.add('hidden');  // aşağı
    } else {
        menuIkonu.classList.remove('hidden'); // yukarı
    }

    enSonKaydirmaYeri = simdikiKaydirmaYeri <= 0 ? 0 : simdikiKaydirmaYeri;
});
