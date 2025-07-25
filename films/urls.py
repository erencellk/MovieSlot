from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('filmler.html/', views.filmler_view, name='filmler'),
    path('film/info/<int:pk>/', views.film_more_info, name='film_more_info'),
    path('actor/info/<int:pk>/', views.actor_detail, name='actor_detail'),
    path('oyuncular.html/', views.oscar_winners, name='oyuncular'),
    path('login/', views.login, name='login'),

    path('register/',views.register_view ,  name='register'),

    path('uyeler/',views.profil_listesi , name='uyeler'),

    path('yorumlar/' , views.yorumlar , name='yorumlar'),

    path('puanlama/' , views.puanlama, name='puanlama'),

    path('filmgorselleri/' ,views.film_gorselleri , name='film_gorselleri'),

    path('logout/' , views.logout_views , name='logout'),

    path('rastgele-film/', views.rastgele_film, name='rastgele_film'),



]
