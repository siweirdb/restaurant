from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import IndexView, send_email
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('send/', views.send_email, name='send')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)