from django.shortcuts import render, get_object_or_404
from .models import Game


def game_list(request):
    games = Game.objects.all()
    title = 'Table & Board'
    context = {'games': games, 'title': title}
    return render(request, 'store/index.html', context)


def about(request):
    title = 'About'
    context = {'title': title}
    return render(request, 'store/about.html', context)


def view_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    title = game.title
    context = {'game': game, 'title': title}
    return render(request, 'store/game.html', context)

