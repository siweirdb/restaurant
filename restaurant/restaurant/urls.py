from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(('menu.urls','menu'), namespace='menu')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
