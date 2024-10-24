from django.urls import path
from . import views


app_name = 'games'
urlpatterns = [
    path('memorization/', views.memorization, name='memorization'),
    path('get_random_word', views.get_random_word, name='get_random_word'),
    path('check_word', views.check_word, name='check_word'),
]
