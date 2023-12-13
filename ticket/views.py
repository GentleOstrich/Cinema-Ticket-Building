from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from . import models

# Create your views here.
@csrf_exempt  # 跨域设置
def index(request):
    if request.method == 'GET':
        tickets = models.Ticket.objects.all()
        json_data = []
        for ticket in tickets:
            # 构造字典
            if ticket.user.username == request.user.username:
                ticket_dict = {
                    'id': ticket.id,
                    'movie_name': ticket.broadcast.movie.name,
                    'beginTime': ticket.broadcast.beginTime,
                    'endTime': ticket.broadcast.endTime,
                    'time': ticket.time,
                    'seat': ticket.seat,
                }

                json_data.append(ticket_dict)
        return JsonResponse({'errno': 0, 'data': json_data})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})
