from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('words/', include('words.urls')),
    path('games/', include('games.urls')),
]
