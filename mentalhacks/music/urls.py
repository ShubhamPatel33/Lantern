from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.songsuggestion, name='index'),
    path('diary', views.diary, name='diary'),
   
]