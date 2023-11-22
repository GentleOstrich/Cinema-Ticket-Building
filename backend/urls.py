from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/user/', include(('user.urls', 'user'))),
    path('api/movie/', include(('movie.urls', 'movie'))),
    path(r'', TemplateView.as_view(template_name='index.html'))
]

