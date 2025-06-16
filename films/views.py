from http.client import HTTPResponse

from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.hashers import make_password
from .models import Member, Actor
from .models import Film, FilmMoreInfo, FilmComment
from django.http import HttpResponse


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
            password=hashed_password  # düz password değil!
        )
        member.save()


def home(request):
    return render(request, 'films/anasayfa.html')


def filmler_view(request):
    encokizlenenfilmler = Film.objects.order_by('-average_rating')
    context = {
        'encokizlenenfilmler': encokizlenenfilmler
    }

    return render(request, 'films/filmler.html', context)


def oyuncular_home(request):
    oyuncular = Actor.objects.all()
    context = {
        'oyuncular': oyuncular
    }

    return render(request, 'films/oyuncular.html', context)


def film_more_info(request, pk):
    film = get_object_or_404(Film, pk=pk)
    more_info = FilmMoreInfo.objects.filter(film=film).first()
    comments = FilmComment.objects.filter(film=film).order_by('-created_at')

    if (request.method == "POST"):
        name = request.POST['name']
        comment = request.POST['comment']
        if name and comment:  # eğer her ıkısı de doluysa anlamında ıkısı de tru donuyorsa
            FilmComment.objects.create(film=film, user_name=name, comment_text=comment)
            return redirect('film_more_info', pk=pk)

    return render(request, 'films/film_more_info.html', {
        'film': film,
        'more_info': more_info,
        'comments': comments,
    })
