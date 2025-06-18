from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('filmler.html/', views.filmler_view, name='filmler'),
    path('film/info/<int:pk>/', views.film_more_info, name='film_more_info'),
    path('actor/info/<int:pk>/', views.actor_detail, name='actor_detail'),
    path('oyuncular.html/', views.oscar_winners, name='oyuncular'),
]
