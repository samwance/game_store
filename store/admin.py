from django.contrib import admin

from store.models import Game, Cart, CartItem, Wishlist, WishlistItem


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'publisher', 'age_rating', 'genre')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_active')


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'quantity', 'cart')


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_active')



@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'wishlist')
