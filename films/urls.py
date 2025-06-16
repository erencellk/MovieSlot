# films/urls.py

from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('filmler.html/', views.filmler_view, name='filmler'),

    path('oyuncular.html/', views.oyuncular_home, name='oyuncular'),

    path('film/info/<int:pk>/', views.film_more_info, name='film_more_info')

]
