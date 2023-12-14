from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import base64,json
from . import models




# Create your views here.
@csrf_exempt  # 跨域设置
def index(request,movie_name):
    if request.method == 'GET':
        broadcasts = models.Broadcast.objects.all()
        json_data = []
        for broadcast in broadcasts:
            # 构造字典
            print(broadcast.movie.name)
            if broadcast.movie.name == movie_name:
                broadcast_dict = {
                    'id': broadcast.id,
                    'hall': broadcast.hall.name,
                    'beginTime': broadcast.beginTime,
                    'endTime': broadcast.endTime,
                    'seats': broadcast.seats,
                }

                json_data.append(broadcast_dict)
        return JsonResponse({'errno': 0, 'data': json_data})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})

@csrf_exempt
def create(request,movie_name):
    if request.method == 'POST':
        movie = models.Movie.objects.get(name=movie_name)
        hall_name = request.POST.get('hall_name')
        hall = models.Hall.objects.get(name=hall_name)
        beginTime = request.POST.get('beginTime')
        endTime = request.POST.get('endTime')
        seats = "0"*hall.seats_num
        broadcast = models.Broadcast.objects.create(movie=movie,hall=hall,beginTime=beginTime,
        endTime=endTime,seats=seats) 
        broadcast.save()
        json_data = {
            'id': broadcast.id,
            'hall': broadcast.hall.name,
            'beginTime': broadcast.beginTime,
            'endTime': broadcast.endTime,
            'seats': broadcast.seats,
        }
        return JsonResponse({'errno': 0, 'data':json_data, 'msg': "Create Success"})
    else:
        return JsonResponse({'errno': 3, 'msg': "Wrong Request"})

@csrf_exempt  # 跨域设置
def delete(request,id):
    if request.method == 'POST':
        broadcast = models.Broadcast.objects.filter(id=id)
        if broadcast.exists():
            broadcast.delete()     
            return JsonResponse({'errno': 0, 'msg': "Delete Success"})
        else:           
            return JsonResponse({'errno': 1, 'msg': 'Broadcastq not exist'})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})



@csrf_exempt  # 跨域设置
def update(request,id):
    if request.method == 'POST':
        broadcast = models.Broadcast.objects.get(id=id)
        hall_name = request.POST.get('hall_name')
        if hall_name != '':
            hall = models.Hall.objects.get(name=hall_name)
            broadcast.hall = hall
            broadcast.seats = "0"*hall.seats_num
        beginTime = request.POST.get('beginTime')
        if beginTime != '':
            broadcast.beginTime = beginTime
        endTime = request.POST.get('endTime')
        if endTime != '':
            broadcast.endTime = endTime
        seats = request.POST.get('seats')
        broadcast.save()
        json_data = {
            'id': broadcast.id,
            'hall': broadcast.hall.name,
            'beginTime': broadcast.beginTime,
            'endTime': broadcast.endTime,
            'seats': broadcast.seats,
        }
        return JsonResponse({'errno': 0, 'data':json_data, 'msg': "Update Success"})
    else:
        return JsonResponse({'errno': 3, 'msg': "Wrong Request"})





# Create your views here.
