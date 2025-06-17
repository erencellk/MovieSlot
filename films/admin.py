from django.contrib import admin
from .models import Genre, Member, Film, Actor, Rating, Review, Director, Watchlist, MovieImage, FilmMoreInfo, FilmComment

# FilmComment için özel admin
class FilmCommentAdmin(admin.ModelAdmin):
    list_display = ('film', 'user_name', 'comment_text', 'created_at')  # admin tablosunda gösterilecek alanlar
    list_filter = ('created_at', 'film')  # filtreleme imkanı
    search_fields = ('user_name', 'comment_text')  # arama çubuğunda aranabilir alanlar

# Modelleri admin paneline kaydet
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
admin.site.register(FilmComment, FilmCommentAdmin)  # özel admin sınıfıyla kaydettik
