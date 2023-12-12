from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create),
    path('login/', login),
    path('is_login/', is_login),
    path('signout/', signout),
    path('adminCheck/', adminCheck),
    path('index/', index),
    path('delete/', delete),
    path('askName/', askName)
]
