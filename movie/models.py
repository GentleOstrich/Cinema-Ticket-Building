from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.BinaryField(null=True, blank=True)
    year = models.CharField(max_length=5)
    region = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    lasting = models.CharField(max_length=10)
