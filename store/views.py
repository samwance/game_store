
from django.shortcuts import render, get_object_or_404, redirect

from .models import Game


common_context = {}

common_context['cart_items'] = Game.objects.filter(is_in_the_cart=True)
common_context['totalQuantity'] = common_context['cart_items'].count()
common_context['totalPrice'] = sum(item.price for item in common_context['cart_items'])


def game_list(request):
    games = Game.objects.all()
    title = 'Table & Board'
    context = {'games': games, 'title': title, **common_context}
    return render(request, 'store/index.html', context)


def add_to_cart(request, game_id):
    game = Game.objects.get(id=game_id)
    if game.is_in_the_cart:
        game.is_in_the_cart = False
    else:
        game.is_in_the_cart = True
    game.save()
    return redirect('store:list')


def about(request):
    title = 'About'
    context = {'title': title, **common_context}
    return render(request, 'store/about.html', context)


def view_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    title = game.title
    context = {'game': game, 'title': title, **common_context}
    return render(request, 'store/game.html', context)
