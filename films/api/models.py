
from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)
    live = models.CharField(max_length=200)


class Genre(models.Model):
    genrename = models.CharField(max_length=100)

# Create your models here.
class Films(models.Model):
    name = models.CharField(max_length=200)
    release = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Afisha(models.Model):
    date = models.DateField()
    films = models.ManyToManyField(Films)