from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()

class Song(models.Model):
    title = models.CharField(max_length=40)
    date_relesed = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

class Lyrics(models.Model):
    content = models.CharField(max_length=400)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)