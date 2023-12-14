from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.utils import timezone
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


@csrf_exempt  # 跨域设置
def create(request,broadcast_id,seat):
    if request.method == 'POST':
        user = request.user
        broadcast = models.Broadcast.objects.get(id=broadcast_id)
        time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        seat = seat
        ticket = models.Ticket.objects.create(user=user, broadcast=broadcast, time=time,seat=seat) 
        ticket.save()
        arr = list(broadcast.seats)
        arr[seat] = "1"
        broadcast.seats = "".join(arr)
        broadcast.save()
        return JsonResponse({'errno': 0, 'msg': "Create Success"})
    else:
        return JsonResponse({'errno': 3, 'msg': "Wrong Request"})

@csrf_exempt  # 跨域设置
def delete(request,id):
    if request.method == 'POST':
        ticket = models.Ticket.objects.filter(id=id)
        if ticket.exists():
            ticket.delete()     
            return JsonResponse({'errno': 0, 'msg': "Delete Success"})
        else:           
            return JsonResponse({'errno': 1, 'msg': 'Ticket not exist'})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})