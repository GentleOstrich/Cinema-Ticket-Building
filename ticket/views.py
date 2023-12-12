from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from . import models


# Create your views here.
@csrf_exempt
def create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        region = data.get('region')
        lasting = data.get('lasting')
        year = data.get('year')
        language = data.get('language')
        description = data.get('description')
        movie = models.Movie.objects.filter(name=name)
        if movie.exists():
            return JsonResponse({'errno': 1, 'msg': 'Repeated name'})
        else:
            ticket = models.Ticket.objects.create(name=name, region=region, lasting=lasting, year=year,
                                                language=language, description=description)
            ticket.save()
            json_data = movie.__dict__
            json_data.pop('_state', None)  # 删除内部状态字段
            return JsonResponse({'errno': 0, 'data': json_data, 'msg': "Create Success"})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})
