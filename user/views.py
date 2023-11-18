from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.models import User
# from models import User  # 引入数据库 User 对象

@csrf_exempt    # 跨域设置
def login(request):  # 继承请求类
    if request.method == 'POST':
        username = request.POST.get('_value[username]') 
        password = request.POST.get('_value[password]')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            return JsonResponse({'errno': 0, 'msg': "Login Success"})
        else:
            return JsonResponse({'errno': 1, 'msg': "wrong Name or Password"})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})


@csrf_exempt
def create(request):
    if request.method == 'POST':
        username = request.POST.get('_value[username]')
        password = request.POST.get('_value[password]')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return JsonResponse({'errno': 0, 'msg': "Create Success"})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})