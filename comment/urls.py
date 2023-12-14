from django.urls import path
from .views import *

urlpatterns = [
    path('index/<str:movie_name>/', index),
    path('create/<str:movie_name>/', create),
    path('delete/<int:id>/', delete),
    path('score/<str:movie_name>/',score),
]
