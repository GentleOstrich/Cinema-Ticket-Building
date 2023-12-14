from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/user/', include(('user.urls', 'user'))),
    path('api/movie/', include(('movie.urls', 'movie'))),
    path('api/broadcast/', include(('broadcast.urls', 'broadcast'))),
    path('api/ticket/', include(('ticket.urls', 'ticket'))),
    path('api/hall/', include(('hall.urls', 'hall'))),
    path('api/favorite/', include(('favorite.urls', 'favorite'))),
    path('api/comment/', include(('comment.urls', 'comment'))),
    path(r'', TemplateView.as_view(template_name='index.html'))
]
