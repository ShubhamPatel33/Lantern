from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.songsuggestion, name='index'),
    path('diary', views.diary, name='diary'),
    path('color_game', views.color_game, name='color_game'),
    path('meditation', views.meditation, name='mditation'),
    path('songsuggestion', views.songsuggestion, name='songsuggestion'),
   
]