from django.db import models
from django.contrib.auth.models import User
from broadcast.models import Broadcast

# Create your models here.
class Ticket(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 订票用户
    broadcast = models.ForeignKey(Broadcast, on_delete=models.CASCADE) # 放映信息
    time = models.CharField(max_length=20) # 订票时间
    seat = models.IntegerField() # 座位号