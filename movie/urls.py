from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index),
    path('create/', create),
    path('delete/', delete),
]
