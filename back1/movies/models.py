from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

class Movie(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    popularity = models.FloatField(blank=True, null=True)
    vote_count = models.IntegerField(blank=True, null=True)
    vote_average = models.FloatField(blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    genres = models.ManyToManyField(Genre, related_name="genre")
