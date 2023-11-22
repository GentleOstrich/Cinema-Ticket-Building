from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create),
    path('login/', login),
    path('is_login/', is_login),
]
