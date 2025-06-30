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
document.addEventListener('DOMContentLoaded', function() {
      const savedEmail = localStorage.getItem('rememberedEmail');
      if (savedEmail) {
          document.getElementById('email').value = savedEmail;
          document.querySelector('input[name="remember_me"]').checked = true;
      }
  });

 document.getElementById('form').addEventListener('submit', function() {
      const remember = document.querySelector('input[name="remember_me"]').checked;
      const email = document.getElementById('email').value;

      if (remember) {
          localStorage.setItem('rememberedEmail', email);
      } else {
          localStorage.removeItem('rememberedEmail');
      }
  });


