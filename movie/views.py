from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from . import models


# Create your views here.
@csrf_exempt    # 跨域设置
def index(request):
    if request.method == 'GET':
        movies = models.Movie.objects.all()
        str_data = serializers.serialize('json', movies)
        json_data = json.loads(str_data)
        return JsonResponse({'errno': 0, 'data': json_data})