from django.contrib import admin

from store.models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'publisher', 'age_rating', 'genre', 'is_in_the_cart')
    list_editable = ('is_in_the_cart',)
