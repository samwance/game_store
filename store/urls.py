from django.urls import path

from store.apps import StoreConfig
from store.views import game_list, view_game, about, manage_cart, cart_list, \
    wishlist_list, manage_wishlist

app_name = StoreConfig.name

urlpatterns = [
    path("", game_list, name="list"),
    path("<int:pk>/", view_game, name="game"),
    path("about", about, name="about"),
    path('manage_cart/', manage_cart, name='manage_cart'),
    path('manage_wishlist/', manage_wishlist, name='manage_wishlist'),
    path('cart/', cart_list, name='cart'),
    path('wishlist/', wishlist_list, name='wishlist'),
]
