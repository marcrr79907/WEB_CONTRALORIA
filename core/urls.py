from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('', include('gestion_contraloria.urls')),
    path('', include('plantilla.urls')),
]
