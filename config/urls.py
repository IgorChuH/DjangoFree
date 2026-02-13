from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
    path('', include('blog.urls', namespace='blog'))# Подключаем URL приложения catalog
]

