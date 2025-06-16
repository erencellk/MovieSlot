from django.contrib import admin
from .models import Genre, Member, Film, Actor, Rating, Review, Director, Watchlist, MovieImage, FilmMoreInfo, \
    FilmComment

# modellerimizin admin panelinde gözükmesi için Django' ya kaydettim.
admin.site.register(Genre)
admin.site.register(Member)
admin.site.register(Film)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(Review)
admin.site.register(Director)
admin.site.register(Watchlist)
admin.site.register(MovieImage)
admin.site.register(FilmMoreInfo)
admin.site.register(FilmComment)
