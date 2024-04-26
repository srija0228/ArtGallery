# art_gallery/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import PasswordResetDoneView,LoginView, LogoutView, PasswordResetView 
from django.conf import settings
from django.conf.urls.static import static
from gallery.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gallery.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)