from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('diary', views.diary, name='diary'),
    path('about', views.aboutus, name='about'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('color_game', views.color_game, name='color_game'),
    path('pacman_game', views.pacman, name='pacman'),
    path('meditation', views.meditation, name='mditation'),
    path('diary-list', views.diary_list, name="diary_list"),
    path('diary-list/<int:id>', views.diary_single, name="diary_single"),
    path('songsuggestion', views.songsuggestion, name='songsuggestion'),

]