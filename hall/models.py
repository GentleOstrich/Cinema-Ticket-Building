from django.db import models

# Create your models here.
class Hall(models.Model):
    name = models.CharField(max_length=50)
    seats_num = models.IntegerField(default=0)