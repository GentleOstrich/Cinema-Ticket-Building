from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index),
    path('create/<str:movie_name>/',create),
    path('delete/<int:id>/',delete),
    path('isFavorite/<str:movie_name>',isFavorite),
]
