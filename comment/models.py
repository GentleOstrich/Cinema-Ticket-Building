from django.contrib.auth.models import User
from django.db import models

from movie.models import Movie


# Create your models here.
class Comment(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 订票用户
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    time = models.CharField(max_length=20)  # 订票时间
    content = models.TextField(max_length=1000)
    rating = models.IntegerField()
