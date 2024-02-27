from django.urls import path

from store.apps import StoreConfig
from store.views import game_list, view_game, about, add_to_cart

app_name = StoreConfig.name

urlpatterns = [
    path("", game_list, name="list"),
    path("<int:pk>/", view_game, name="game"),
    path("about", about, name="about"),
    path('add_to_cart/<int:game_id>/', add_to_cart, name='add_to_cart'),
]