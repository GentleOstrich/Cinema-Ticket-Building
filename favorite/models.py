from django.db import models
from django.contrib.auth.models import User
from movie.models import Movie

# Create your models here.
class Favorite(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) # 放映信息
    time = models.CharField(max_length=20) 