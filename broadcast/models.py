from django.db import models

# Create your models here.
class Broadcast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    beginTime = models.DateTimeField
    endTime = models.DateTimeField
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    seats = models.CharField(max_length=1000)