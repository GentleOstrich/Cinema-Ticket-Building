from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib.auth.models import User


# from models import User  # 引入数据库 User 对象

@csrf_exempt  # 跨域设置
def login(request):  # 继承请求类
    if request.method == 'POST':
        username = request.POST.get('_value[username]')
        password = request.POST.get('_value[password]')
        remember = None
        user = auth.authenticate(request, username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            # if remember:
            #     # 设置为None，则表示使用全局的过期时间
            #     request.session.set_expiry(None)
            # else:
            #     #否则设为0，关掉浏览器就注销登陆状态了
            #     request.session.set_expiry(0)
            print(request.user)
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
        user = User.objects.filter(username=username)
        if user.exists():
            return JsonResponse({'errno': 1, 'msg': 'Repeated username'})
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return JsonResponse({'errno': 0, 'msg': "Create Success"})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})


@csrf_exempt
def is_login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return JsonResponse({'code': 1})
        else:
            return JsonResponse({'code': 0})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})


@csrf_exempt
def signout(request):  # 只能用signout，不可与内置函数logout重名
    if request.method == 'GET':
        logout(request)
        return JsonResponse({'errno': 0, 'msg': "Logout Success"})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})


admins = ['zyk', 'lyh', 'gzh']


@csrf_exempt  # 跨域设置
def adminCheck(request):
    if request.method == 'POST':
        username = request.user.username
        for admin in admins:
            if admin == username:
                return JsonResponse({'errno': 0, 'username': username, 'msg': "isAdmin"})
        return JsonResponse({'errno': 1, 'msg': "not admin"})

    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})


@csrf_exempt  # 跨域设置
def index(request):
    if request.method == 'GET':
        users = User.objects.all()
        str_data = serializers.serialize('json', users)
        json_data = json.loads(str_data)
        return JsonResponse({'errno': 0, 'data': json_data})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})


@csrf_exempt  # 跨域设置
def delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        user = User.objects.filter(username=username)
        if user.exists():
            user.delete()
            return JsonResponse({'errno': 0, 'msg': "Delete Success"})
        else:
            return JsonResponse({'errno': 1, 'msg': 'Username not exist'})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})

@csrf_exempt  # 跨域设置
def update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        password = data.get('password')
        email = data.get('email')
        user = request.user
        user.password = password
        user.email = email
        user.save()
        return JsonResponse({'errno': 0, 'msg': "Update Success"})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})


@csrf_exempt  # 跨域设置
def askName(request):
    if request.method == 'POST':
        username = request.user.username
        return JsonResponse({'errno': 0, 'username': username, 'msg': "success"})

    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})
