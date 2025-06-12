# films/urls.py

from django.urls import path , include
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('filmler.html/', views.filmler_view , name='filmler'),
]

