from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/user/', include(('user.urls', 'user'))),
    # re_path(r'^$', TemplateView.as_view(template_name='index.html')),
]
