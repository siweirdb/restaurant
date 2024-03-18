from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import IndexView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)