from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import base64,json
from . import models

# Create your views here.
@csrf_exempt  # 跨域设置
def index(request):
    if request.method == 'GET':
        halls = models.Hall.objects.all()
        json_data = []
        for hall in halls:
            # 构造字典
            hall_dict = {
                'name': hall.name,
                'seats_num': hall.seats_num,
            }
            json_data.append(hall_dict)
        return JsonResponse({'errno': 0, 'data': json_data})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})

@csrf_exempt
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        seats_num = request.POST.get('seats_num')
        hall = models.Hall.objects.filter(name=name)
        if name == '' or name is None :
            return JsonResponse({'errno': 1, 'msg': 'Null name'})
        if hall.exists():
            return JsonResponse({'errno': 2, 'msg': 'Repeated name'})
        else:
            hall = models.Hall.objects.create(name=name, seats_num=seats_num) 
            hall.save()
            json_data = {
                'name': hall.name,
                'seats_num': hall.seats_num,
            }
            return JsonResponse({'errno': 0, 'data':json_data, 'msg': "Create Success"})
    else:
        return JsonResponse({'errno': 3, 'msg': "Wrong Request"})

@csrf_exempt  # 跨域设置
def delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        hall = models.Hall.objects.filter(name=name)
        if hall.exists():
            hall.delete()     
            return JsonResponse({'errno': 0, 'msg': "Delete Success"})
        else:           
            return JsonResponse({'errno': 1, 'msg': 'Username not exist'})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})



@csrf_exempt  # 跨域设置
def update(request,old_name):
    if request.method == 'POST':
        data = {key: request.POST[key] for key in request.POST}
        hall = models.Hall.objects.get(name=old_name)
        if data.get('name') != "" and models.Hall.objects.filter(name=data.get('name')).exists:
            return JsonResponse({'errno': 2, 'msg': 'Repeated name'})
        elif hall is not None:
            name = data.get('name')
            if name != '':
                hall.name = name
            seats_num = data.get('seats_num')
            if seats_num != '':
                hall.seats_num = seats_num
            hall.save()
            json_data = {
                'name': hall.name,
                'seats_num': hall.seats_num,
            }
            return JsonResponse({'errno': 0, 'data':json_data, 'msg': "Update Success"})
    else:
        return JsonResponse({'errno': 3, 'msg': "Wrong Request"})




