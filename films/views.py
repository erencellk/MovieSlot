from http.client import HTTPResponse

from django.shortcuts import render

from django.contrib.auth.hashers import make_password
from .models import Member
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
    return HttpResponse("""
    <html>
    <body>
    <div style="display:flex; justify-content:center; align-items:center;" >
    
    <h1>Welcome home page!</h1>
    </div>
    
    
    
    </body>
    
    
    
    
    
    </html>
    
    """)







    # herhangi bir giriş kaydı basarılı ise bu mesaj gosterılecek.
