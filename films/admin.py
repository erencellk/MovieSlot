from django.contrib import admin
from .models import Members, Film, Actor, Review, Director, MovieImage, FilmMoreInfo, FilmComment, OscarAward, Login, \
    Register, oneCıkanFilmler


# FilmComment için özel admin
class FilmCommentAdmin(admin.ModelAdmin):
    list_display = ('film', 'user_name', 'comment_text', 'created_at')  # admin tablosunda gösterilecek alanlar
    list_filter = ('created_at', 'film')  # filtreleme imkanı
    search_fields = ('user_name', 'comment_text')  # arama çubuğunda aranabilir alanlar


class UyelerAdmin(admin.ModelAdmin):
    list_display = ('register', 'cinsiyet', 'kayit_tarihi', 'profile_picture')
    search_fields = ('register__ad', 'register__soyad', 'register__email')
    list_filter = ('cinsiyet',)
    ordering = ('-kayit_tarihi',)



admin.site.register(Members, UyelerAdmin)
admin.site.register(Film)
admin.site.register(Actor)
admin.site.register(Review)
admin.site.register(Director)
admin.site.register(MovieImage)
admin.site.register(FilmMoreInfo)
admin.site.register(OscarAward)
admin.site.register(Login)
admin.site.register(Register)
admin.site.register(oneCıkanFilmler)
admin.site.register(FilmComment, FilmCommentAdmin)
