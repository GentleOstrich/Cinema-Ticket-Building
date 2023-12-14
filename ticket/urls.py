from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index),
    path('create/<int:broadcast_id>/<int:seat>/',create),
    path('delete/<int:id>/',delete),
]
