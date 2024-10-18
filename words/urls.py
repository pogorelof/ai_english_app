from django.urls import path
from . import views

app_name = 'words'

urlpatterns = [
    path('', views.WordListView.as_view(), name='word_list'),
    path('add_word/', views.add_word, name='add_word'),
    path('video/', views.words_from_video, name='words_from_video'),
    path('video/add_word', views.words_from_video_handler, name='video_add_word'),
    path('delete_word/<int:pk>', views.delete_word, name='delete_word'),
]
