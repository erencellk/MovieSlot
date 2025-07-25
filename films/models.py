from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models



# Class Actor Baslangıcı
class Actor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    actor_picture = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.name + " - " + self.surname

    class Meta:
        verbose_name = 'Actor'
        verbose_name_plural = 'Actors'
    # Class Actor Bitis


# Film Class Baslangıcı
class Film(models.Model):
    title = models.CharField(max_length=100)  # CharField = kısa metinler için kullanılır.
    description = models.TextField()  # TextField() = uzun metinler için kullanılır.
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    genre = models.TextField(null=True, blank=True)
    duration = models.IntegerField()
    language = models.CharField(max_length=50)
    average_rating = models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'
    # Film Class Bitiş


# Class OscarAward baslangıcı
class OscarAward(models.Model):
    actor = models.TextField(blank=True, null=True)
    film = models.TextField(blank=True, null=True)
    year = models.IntegerField(validators=[MinValueValidator(1800), MaxValueValidator(2027)], blank=False, null=True)

    def __str__(self):
        return f"{self.actor} - {self.year}"

    class Meta:
        verbose_name = 'Oscar Award'
        verbose_name_plural = 'Oscar Awards'


# Class FilmMoreInfo baslangıcı
class FilmMoreInfo(models.Model):
    film = models.OneToOneField(Film, on_delete=models.CASCADE)
    youtube_trailer_url = models.URLField(max_length=500)

    def __str__(self):
        return self.film.title + " - " + self.youtube_trailer_url

    class Meta:
        verbose_name = 'FilmMoreInfo'
        verbose_name_plural = 'FilmMoreInfos'


# Class FılmMoreInfo bitiş


# class FilmComment baslangıcı
class FilmComment(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='comments')
    user_name = models.CharField(max_length=100)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=True, blank=True, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])

    def __str__(self):
        return f" Yorum : {self.user_name} - {self.comment_text}"

    class Meta:
        verbose_name = 'FilmComment'
        verbose_name_plural = 'FilmComments'


# Class FilmComment bitis


# Director Class Baslangıcı
class Director(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    biography = models.TextField()
    birth_date = models.DateField()

    def __str__(self):
        return self.first_name + " - " + self.last_name

    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directors'
    # Director Class Bitişi


# User Member Baslangıcı


# Review Class Baslangıcı
class Review(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    member = models.ForeignKey('Members', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()  # 1-5 arası puanlama
    created_at = models.DateTimeField(auto_now_add=True)  # ilk kayıtta zamanı bir kere yazdırdım.
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.text) > 50:
            return self.text[:50] + "..."  # ilk 50 karakter
        else:
            return self.text

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
    # Class Review Bitis


# Class MovieImage Baslangıcı
class MovieImage(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    text_alt = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.film)

    class Meta:
        verbose_name = 'Movie Image'
        verbose_name_plural = 'Movie Images'
    # Class MovieImage Bitis


class Login(models.Model):
    password = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = 'Login'
        verbose_name_plural = 'Logins'


class Register(models.Model):
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    sifre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ad} {self.soyad}"

    class Meta:
        verbose_name = 'Register'
        verbose_name_plural = 'Registers'


class oneCıkanFilmler(models.Model):
    isim = models.TextField(max_length=100)
    youtube_url = models.URLField()

    def __str__(self):
        return self.isim

    class Meta:
        verbose_name = 'OneCıkanFilm'
        verbose_name_plural = 'OneCıkanFilmler'


class Members(models.Model):
    register = models.ForeignKey('Register', on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="media/", null=True, blank=True)
    cinsiyet = models.CharField(max_length=10, choices=[('Erkek', 'Erkek'), ('Kadın', 'Kadın')], default='Erkek')
    kayit_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.register.ad} {self.register.soyad}"  # Register modelindeki ad ve soyad verilerini çekme

    class Meta:
        verbose_name = 'Üye'
        verbose_name_plural = 'Üyeler'


class KullaniciYorum(models.Model):
    kullanici_adi = models.CharField(max_length=100)
    yorum_metni = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Yorum yapan: {self.kullanici_adi}"
