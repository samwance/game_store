from django.contrib import admin

from store.models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
