from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from project.urls import api

urlpatterns = [
    path('api/', include((api.urlpatterns, 'api')), name='api'),  # NOQA
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')), )
