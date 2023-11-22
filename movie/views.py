from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models


# Create your views here.
@csrf_exempt    # 跨域设置
def index(request):
    if request.method == 'GET':
        movies = models.Movie.objects.all()
        print(list(movies))
        return JsonResponse({'errno': 0, 'data': {'movies': list(movies)}})