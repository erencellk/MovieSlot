from django.db import models
from django.contrib.auth.models import User


# Genre Class Baslangıcı
class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name  # herhangi bir print yazısında bana class'ın içine ne yazdıysam onu döndürür.

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
    # Genre Class Bitiş


# Class Actor Baslangıcı
class Actor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    biography = models.TextField()
    birthday = models.DateField()
    films = models.ManyToManyField("Film")  # ard arda oldukları ıcın bır tanesını boyle declare ettım.

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
    release_date = models.DateField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    director = models.ForeignKey('Director', on_delete=models.CASCADE)
    duration = models.IntegerField()
    language = models.CharField(max_length=50)
    rating = models.FloatField()
    actors = models.ManyToManyField(Actor)  # many-to-many ilişkisi

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'
    # Film Class Bitiş


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

class Member(models.Model):
    username = models.CharField(max_length=50)
    usersurname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=128)  # hashed parolayı burada tutacagım
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    profile_pic = models.ImageField(upload_to="images/", null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return (self.username + " - " + self.usersurname + " - " +
                self.email + " - " + self.password)  # kayıt olan tüm bilgiler dönsün istiyorum.

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'
    # Class Member Bitis


# Review Class Baslangıcı
class Review(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
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


# Class Rating Baslangıcı
class Rating(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    score = models.IntegerField()  # 1-5 arası
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.score)

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
    # Class Rating Bitis


# Class WatchList Baslangıcı
class Watchlist(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    added_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.film.title + " - " + self.member.username

    class Meta:
        verbose_name = 'Watchlist'
        verbose_name_plural = 'Watchlists'
    # Class WatchList Bitis
