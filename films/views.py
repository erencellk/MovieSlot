from http.client import HTTPResponse

from django.shortcuts import render

from django.contrib.auth.hashers import make_password
from .models import Member
from .models import  Film
from django.http import HttpResponse


def create_member(info):
    if info.method == "POST":
        username = info.POST['username']
        usersurname = info.POST['usersurname']
        email = info.POST['email']
        password = info.POST['password']

    hashed_password = make_password(
        password)  # Bu düz şifre, Django’nun güvenli make_password() fonksiyonu ile hashlenir.

    member = Member.objects.create(
        username=username,
        usersurname=usersurname,
        email=email,
        password=password
    )
    member.save()  # olusturulan nesne veri tabanına eklendi.






def home(request):
    return render(request, 'films/anasayfa.html')

def filmler_view(request):

    encokizlenenfilmler = Film.objects.order_by('average_rating')
    context = {
        'encokizlenenfilmler' : encokizlenenfilmler
    }

    return render(request, 'films/filmler.html' , context)