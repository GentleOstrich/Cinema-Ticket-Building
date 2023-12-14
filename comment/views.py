from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.utils import timezone
import json
from . import models


# Create your views here.
@csrf_exempt  # 跨域设置
def index(request, movie_name):
    if request.method == 'GET':
        comments = models.Comment.objects.all()
        json_data = []
        for comment in comments:
            # 构造字典
            if comment.movie.name == movie_name:
                comment_dict = {
                    'id': comment.id,
                    'username': comment.user.username,
                    'time': comment.time,
                    'content': comment.content
                }

                json_data.append(comment_dict)
        return JsonResponse({'errno': 0, 'data': json_data})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})


@csrf_exempt  # 跨域设置
def create(request, movie_name):
    if request.method == 'POST':
        movie = models.Movie.objects.get(name=movie_name)
        user = request.user
        content = request.POST.get('content')
        time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        comment = models.Comment.objects.create(user=user, movie=movie, time=time, content=content)
        comment.save()
        json_data = {
            'id': comment.id,
            'username': comment.user.username,
            'time': comment.time,
            'content': comment.content
        }
        return JsonResponse({'errno': 0, 'data': json_data, 'msg': "Create Comment Success"})
    else:
        return JsonResponse({'errno': 3, 'msg': "Wrong Request"})


@csrf_exempt  # 跨域设置
def delete(request, id):
    if request.method == 'POST':
        comment = models.Comment.objects.get(id=id)
        if comment is not None:
            comment.delete()
            return JsonResponse({'errno': 0, 'msg': "Delete Comment Success"})
        else:
            return JsonResponse({'errno': 1, 'msg': 'Comment not exist'})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})