from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
# from models import User  # 引入数据库 User 对象

@csrf_exempt    # 跨域设置
def login(request):  # 继承请求类
    if request.method == 'POST':  # 判断请求方式是否为 POST
        user_id = request.POST.get('user_id')  # 获取请求体中的请求数据
        user_password = request.POST.get('user_password')
        user = authenticate(request, user_id=user_id, user_password=user_password)
        if user is not None:
            return JsonResponse({'errno': 0, 'msg': "Login Success"})
        else:
            return JsonResponse({'errno': 1, 'msg': "wrong Id or Password"})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})

