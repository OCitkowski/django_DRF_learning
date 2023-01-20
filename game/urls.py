from django.urls import path
from .views import game_view

app_name = 'game'
urlpatterns = [

    path('', game_view, name='game')
]