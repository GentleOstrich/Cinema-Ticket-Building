from django.db import models

# Create your models here.
class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 订票用户
    broadcast = models.ForeignKey(Broadcast, on_delete=models.CASCADE) # 放映信息
    time = models.DateTimeField() # 订票时间
    seat = models.IntegerField() # 座位号