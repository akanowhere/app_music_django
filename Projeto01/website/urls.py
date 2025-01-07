#from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    #url(r'^music/', include('music.urls')),
    re_path(r'^', include('music.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
