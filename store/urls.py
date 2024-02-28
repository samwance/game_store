from django.urls import path

from store.apps import StoreConfig
from store.views import game_list, view_game, about, add_to_cart, add_to_wishlist, remove_from_wishlist, \
    remove_from_cart, update_cart_item, cart_list, wishlist_list

app_name = StoreConfig.name

urlpatterns = [
    path("", game_list, name="list"),
    path("<int:pk>/", view_game, name="game"),
    path("about", about, name="about"),
    path('add/', add_to_cart, name='add_to_cart'),
    path('remove/', remove_from_cart, name='remove_from_cart'),
    path('update/', update_cart_item, name='update_cart'),
    path('cart/', cart_list, name='cart_view'),
    path('like/', add_to_wishlist, name='add_to_wishlist'),
    path('unlike/', remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist/', wishlist_list, name='wishlist_view'),
]
