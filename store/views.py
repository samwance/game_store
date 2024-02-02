from django.shortcuts import render, redirect, get_object_or_404
from .models import Game


def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_list.html', {'games': games})


def view_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'view_game.html', {'game': game})
