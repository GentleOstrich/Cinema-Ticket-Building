from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.utils import timezone
import base64
import json
from . import models

# Create your views here.
@csrf_exempt  # 跨域设置
def index(request):
    if request.method == 'GET':
        favorites = models.Favorite.objects.all()
        json_data = []
        for favorite in favorites:
            # 构造字典
            if favorite.user.username == request.user.username:
                favorite_dict = {
                    'name': favorite.movie.name,
                    'genre': favorite.movie.genre,
                    'region': favorite.movie.region,
                    'lasting': favorite.movie.lasting,
                }

                # 添加经过Base64编码的图片
                if favorite.movie.image:
                    favorite_dict['image'] = base64.b64encode(favorite.movie.image).decode()
                else:
                    favorite_dict['image'] = None

                json_data.append(favorite_dict)
        return JsonResponse({'errno': 0, 'data': json_data})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})


@csrf_exempt  # 跨域设置
def create(request,movie_name):
    if request.method == 'POST':
        user = request.user
        movie = models.Movie.objects.get(name=movie_name)
        time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        favorite = models.Favorite.objects.create(user=user, movie=movie, time=time) 
        favorite.save()
        return JsonResponse({'errno': 0, 'msg': "Create Success"})
    else:
        return JsonResponse({'errno': 3, 'msg': "Wrong Request"})

@csrf_exempt  # 跨域设置
def delete(request,id):
    if request.method == 'POST':
        favorite = models.Favorite.objects.get(id=id)
        if favorite is not None:
            favorite.delete()     
            return JsonResponse({'errno': 0, 'msg': "Delete Success"})
        else:           
            return JsonResponse({'errno': 1, 'msg': 'Favorite not exist'})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})
