from django.urls import path

from store.apps import StoreConfig
from store.views import game_list, view_game, about

app_name = StoreConfig.name

urlpatterns = [
    path("", game_list, name="list"),
    path("<int:pk>/", view_game, name="game"),
    path("about", about, name="about"),
]