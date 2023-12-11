from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    year = models.IntegerField()
    region = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    lasting = models.IntegerField()
