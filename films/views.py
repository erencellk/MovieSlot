from doctest import script_from_examples

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import Member, Actor, Film, FilmMoreInfo, FilmComment, OscarAward, Login,oneCıkanFilmler
from django.shortcuts import render, redirect
from .models import Register
from django.http import JsonResponse
from django.contrib import messages
import random


def create_member(info):
    if info.method == "POST":
        username = info.POST['username']
        usersurname = info.POST['usersurname']
        email = info.POST['email']
        password = info.POST['password']

        hashed_password = make_password(password)

        member = Member.objects.create(
            username=username,
            usersurname=usersurname,
            email=email,
            password=hashed_password
        )
        member.save()





def filmler_view(request):
    encokizlenenfilmler = Film.objects.order_by('-average_rating')
    context = {
        'encokizlenenfilmler': encokizlenenfilmler
    }
    return render(request, 'films/filmler.html', context)


def film_more_info(request, pk):
    film = get_object_or_404(Film, pk=pk)
    more_info = FilmMoreInfo.objects.filter(film=film).first()
    comments = FilmComment.objects.filter(film=film).order_by('-created_at')

    if request.method == "POST":

        ad = request.POST.get('kullanici_adi')
        soyad = request.POST.get('kullanici_soyadi')
        yorum = request.POST.get('yorum')
        puan = request.POST.get('puan')

        if ad and soyad and yorum and puan:
            tam_ad = ad + " " + soyad
            FilmComment.objects.create(film=film, user_name=tam_ad, comment_text=yorum, rating=int(puan))
            return redirect('film_more_info', pk=pk)


    return render(request, 'films/film_more_info.html', {
        'film': film,
        'more_info': more_info,
        'comments': comments,

    })


def actor_detail(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    awards = OscarAward.objects.filter(actor=f"{actor.name} {actor.surname}")
    return render(request, 'films/oyuncular.html', {
        'actor': actor,
        'awards': awards,
    })


def oscar_winners(request):
    actors = Actor.objects.all()
    awards = OscarAward.objects.all()

    actor_awards = []
    for actor in actors:
        related_awards = [award for award in awards if
                          award.actor and actor.name in award.actor or actor.surname in award.actor]
        if related_awards:
            actor_awards.append({
                'actor': actor,
                'awards': related_awards
            })

    return render(request, 'films/oyuncular.html', {
        'actor_awards': actor_awards
    })


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        # Register modelinde bu kullanıcı var mı kontrol et
        if Register.objects.filter(email=email, sifre=password).exists():
            kullanici = Register.objects.get(email=email)

            request.session['kullanici_id'] = kullanici.id
            if not remember:
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(60 * 60 * 24 * 7)
            messages.success(request, f'👋 {kullanici.ad}!')
            return redirect('home')  # home.html'e yönlendir
        else:
            messages.error(request, 'Email veya şifre hatalı!')
            return redirect('login')

    return render(request, 'films/giris.html')

def register_view(request):
    if request.method == "POST":
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        email = request.POST.get('email')
        sifre = request.POST.get('sifre')

        if Register.objects.filter(email=email).exists():
            messages.error(request, "Bu email zaten kayıtlı ❌")
            return redirect('register')

        if ad and soyad and email:
            Register.objects.create(ad=ad, soyad=soyad, email=email,sifre=sifre)
            messages.success(request, "Kaydınız başarıyla oluşturuldu ✅")
            return redirect('register')
        else:
            messages.error(request, "Lütfen tüm alanları doldurun ❌")

    return render(request, 'films/kayıtol.html')






def yorumlar(request):
    return render(request, 'films/yorumlar.html')

def puanlama(request):
    return render(request, 'films/puanlama.html')

def film_gorselleri(request):
    return render(request , 'films/filmgörselleri.html')

def logout_views(request):
    request.session.flush()
    messages.success(request, 'Başarıyla çıkış yaptınız!')
    return redirect('home')

def uyeler(request):
    return render(request , 'films/üyeler.html')


def onecıkanfilmler(request):
    film_listesi = oneCıkanFilmler.objects.all()
    rastgele_film=random.choice(film_listesi) if film_listesi else None

    return render(request,'films/anasayfa.html',{
        'rastgele_film': rastgele_film
    })


def home(request):
    kullanici = None
    if 'kullanici_id' in request.session:
        from .models import Register
        try:
            kullanici = Register.objects.get(id=request.session['kullanici_id'])
        except Register.DoesNotExist:
            pass

    film = oneCıkanFilmler.objects.order_by('?').first()
    return render(request, 'films/anasayfa.html', {
        'kullanici': kullanici,
        'film': film
    })


def rastgele_film(request):
    film = oneCıkanFilmler.objects.order_by('?').first()
    return JsonResponse(
        {
            'isim': film.isim,
            'youtube_url':film.youtube_url

         })