from django.db import models
from django.conf import settings



class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=300)
    pubDate = models.CharField(max_length=100)
    userRating = models.FloatField()
    genres = models.ManyToManyField(Genre, related_name="movie_genres")
    backdrop = models.CharField(max_length=300)
    description = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies", blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comment_user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Score(models.Model):
    star = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Credit(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
    actor1 = models.CharField(max_length=30)
    actor2 = models.CharField(max_length=30)
    actor3 = models.CharField(max_length=30)
    actor4 = models.CharField(max_length=30)
    actor5 = models.CharField(max_length=30)
    actor6 = models.CharField(max_length=30)
    director = models.CharField(max_length=30)

