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
        movies = models.Movie.objects.all()
        json_data = []
        for movie in movies:
            # 构造字典
            movie_dict = {
                'name': movie.name,
                'description': movie.description,
                'year': movie.year,
                'region': movie.region,
                'language': movie.language,
                'genre': movie.genre,
                'lasting': movie.lasting,
                # 其他需要的字段
            }

            # 添加经过Base64编码的图片
            if movie.image:
                movie_dict['image'] = base64.b64encode(movie.image).decode()
            else:
                movie_dict['image'] = None

            json_data.append(movie_dict)
        return JsonResponse({'errno': 0, 'data': json_data})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})

@csrf_exempt
def create(request):
    if request.method == 'POST':
        data = {key: request.POST[key] for key in request.POST}
        image = request.FILES.get('image')
        name = data.get('name')
        region = data.get('region')
        genre = data.get('genre')
        lasting = data.get('lasting')
        year = data.get('year')
        language = data.get('language')
        description = data.get('description')
        movie = models.Movie.objects.filter(name=name)
        if name == '' or name is None :
            return JsonResponse({'errno': 1, 'msg': 'Null name'})
        if movie.exists():
            return JsonResponse({'errno': 2, 'msg': 'Repeated name'})
        else:
            if image is None: 
                movie = models.Movie.objects.create(name=name, region=region,
            lasting=lasting, year=year, language=language, description=description)
            else: 
                movie = models.Movie.objects.create(name=name, region=region,image=image.read(),
            lasting=lasting, year=year, language=language, description=description) 
            movie.save()
            json_data = {
                'name': movie.name,
                'description': movie.description,
                'year': movie.year,
                'region': movie.region,
                'language': movie.language,
                'genre': movie.genre,
                'lasting': movie.lasting,
                # 其他需要的字段
            }
            return JsonResponse({'errno': 0, 'data':json_data, 'msg': "Create Success"})
    else:
        return JsonResponse({'errno': 3, 'msg': "Wrong Request"})

@csrf_exempt  # 跨域设置
def delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        movie = models.Movie.objects.filter(name=name)
        if movie.exists():
            movie.delete()     
            return JsonResponse({'errno': 0, 'msg': "Delete Success"})
        else:           
            return JsonResponse({'errno': 1, 'msg': 'Username not exist'})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})



@csrf_exempt  # 跨域设置
def update(request,old_name):
    if request.method == 'POST':
        data = {key: request.POST[key] for key in request.POST}
        movie = models.Movie.objects.get(name=old_name)
        if data.get('name') is None or data.get('name') == '':
            return JsonResponse({'errno': 1, 'msg': 'Null name'})
        elif models.Movie.objects.filter(name=data.get('name')).exists:
            return JsonResponse({'errno': 2, 'msg': 'Repeated name'})
        elif movie is not None:
            image = request.FILES.get('image')
            if image is not None:
                movie.image = image.read()
            name = data.get('name')
            if name != '':
                movie.name = name
            region = data.get('region')
            if region != '':
                movie.region = region
            genre = data.get('genre')
            if genre != '':
                movie.genre = genre
            lasting = data.get('lasting')
            if lasting != '':
                movie.lasting = lasting
            year = data.get('year')
            if year != '':
                movie.year = year
            language = data.get('language')
            if language != '':
                movie.language = language
            description = data.get('description')
            if description != '':
                movie.description = description
            movie.save()
            json_data = {
                'name': movie.name,
                'description': movie.description,
                'year': movie.year,
                'region': movie.region,
                'language': movie.language,
                'genre': movie.genre,
                'lasting': movie.lasting,
                # 其他需要的字段
            }
            return JsonResponse({'errno': 0, 'data':json_data, 'msg': "Update Success"})
    else:
        return JsonResponse({'errno': 3, 'msg': "Wrong Request"})



