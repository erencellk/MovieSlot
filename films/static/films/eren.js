document.addEventListener('DOMContentLoaded',()=>{
    const  button = document.getElementById('film-oner-buton');
    const filmBaslik = document.querySelector('.film-oneri h3');
    const iframe = document.querySelector('.video-container iframe');


    button.addEventListener('click',()=>{
        fetch('/rastgele-film/')
            .then(response =>response.json())
            .then(data =>{
                filmBaslik.textContent = data.isim;
                iframe.src = data.youtube_url;
            });
    });
});