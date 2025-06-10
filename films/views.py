from django.shortcuts import render

from django.contrib.auth.hashers import make_password
from .models import Member


def create_member(info):
    if info.method == "POST":
        username = info.POST['username']
        usersurname = info.POST['usersurname']
        email = info.POST['email']
        password = info.POST['password']

    hashed_password = make_password(password)  # Bu düz şifre, Django’nun güvenli make_password() fonksiyonu ile hashlenir.

    member = Member.objects.create(
        username=username,
        usersurname=usersurname,
        email=email,
        password=password
    )
    member.save() # olusturulan nesne veri tabanına eklendi.
