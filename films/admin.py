from django.contrib import admin
from .models import Member, Film, Actor,  Review, Director, MovieImage, FilmMoreInfo, FilmComment,OscarAward , Login ,Register

# FilmComment için özel admin
class FilmCommentAdmin(admin.ModelAdmin):
    list_display = ('film', 'user_name', 'comment_text', 'created_at')  # admin tablosunda gösterilecek alanlar
    list_filter = ('created_at', 'film')  # filtreleme imkanı
    search_fields = ('user_name', 'comment_text')  # arama çubuğunda aranabilir alanlar

# Modelleri admin paneline kaydet
admin.site.register(Member)
admin.site.register(Film)
admin.site.register(Actor)
admin.site.register(Review)
admin.site.register(Director)
admin.site.register(MovieImage)
admin.site.register(FilmMoreInfo)
admin.site.register(OscarAward)
admin.site.register(Login)
admin.site.register(Register)
admin.site.register(FilmComment, FilmCommentAdmin)  # özel admin sınıfıyla kaydettik
