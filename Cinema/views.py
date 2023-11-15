import json

from django.core import serializers
from django.http import JsonResponse
from django.views.generic.base import View
from django.shortcuts import render

from Cinema.models import User

# Create your views here.
class UserListView(View):
    def get(self,request):
        res = {'code':0,'msg':'Success','data':[]}
        try:
            user_list = User.objects.all()
            user_list = json.loads(serializers.serialize('json',user_list))
            res['data'] = user_list
        except Exception as e:
            res['code'] = -1
            res['msg'] = 'Failed'

        return JsonResponse(res)
