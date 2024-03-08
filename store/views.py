from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from .models import Game, CartItem, Cart, WishlistItem, Wishlist
from django.shortcuts import get_object_or_404


def get_game_list_data(request):
    cart = CartItem.objects.filter(cart__user=request.user, cart__is_active=True)
    wishlist = WishlistItem.objects.filter(wishlist__user=request.user, wishlist__is_active=True)

    # Get the list of games in cart and wishlist
    cart_game_ids = set(item.game.id for item in cart)
    wishlist_game_ids = set(item.game.id for item in wishlist)

    return cart_game_ids, wishlist_game_ids

@login_required
def game_list(request):
    query = request.GET.get('q')
    genre_filter = request.GET.getlist('genre')

    games = Game.objects.all()
    cart_game_ids, wishlist_game_ids = get_game_list_data(request)

    # Add 'in_cart' and 'in_wishlist' attributes to each game
    for game in games:
        game.in_cart = game.id in cart_game_ids
        game.in_wishlist = game.id in wishlist_game_ids

    if query:
        games = games.filter(title__icontains=query)

    if genre_filter:
        if genre_filter[0] == '':
            # If the 'all genres' option is selected, show all games
            pass
        else:
            games = games.filter(genre__in=genre_filter)

    title = 'Table & Board'
    context = {'games': games, 'title': title}
    return render(request, 'store/index.html', context)


def view_game(request, pk):
    game = get_object_or_404(Game, pk=pk)

    title = game.title
    cart_game_ids, wishlist_game_ids = get_game_list_data(request)

    # Add 'in_cart' and 'in_wishlist' attributes to each game
    game.in_cart = game.id in cart_game_ids
    game.in_wishlist = game.id in wishlist_game_ids

    context = {'game': game, 'title': title}
    return render(request, 'store/game.html', context)


def about(request):
    title = 'About'
    context = {'title': title}
    return render(request, 'store/about.html', context)


def cart_list(request):
    cart_items = CartItem.objects.filter(cart__user=request.user, cart__is_active=True)
    context = {'object_list': cart_items}
    return render(request, 'store/cart.html', context)


def manage_cart(request):
    if request.method == 'POST':
        game_id = request.POST.get('game_id')

        cart, created = Cart.objects.get_or_create(user=request.user, is_active=True)
        game, _ = Game.objects.get_or_create(id=game_id)

        if CartItem.objects.filter(cart=cart, game=game).exists():
            CartItem.objects.filter(cart=cart, game=game).delete()
            value = 'Add'
        else:
            CartItem.objects.create(cart=cart, game=game)
            value = 'Remove'

        data = {
            "value": value,
            "count": CartItem.objects.filter(cart=cart).count(),
            "game_price": game.price
        }

        return JsonResponse(data, safe=False)


def wishlist_list(request):
    wishlist_items = WishlistItem.objects.filter(wishlist__user=request.user, wishlist__is_active=True)
    context = {'object_list': wishlist_items}
    return render(request, 'store/wishlist.html', context)


def manage_wishlist(request):
    if request.method == 'POST':
        game_id = request.POST.get('game_id')

        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        game = Game.objects.get(id=game_id)

        if not WishlistItem.objects.filter(wishlist=wishlist, game=game).exists():
            WishlistItem.objects.create(wishlist=wishlist, game=game)
            value = 'Unlike'
        else:
            WishlistItem.objects.filter(wishlist=wishlist, game=game).delete()
            value = 'Like'

        data = {
            "value": value,
            "count": WishlistItem.objects.filter(wishlist=wishlist).count()
        }

        return JsonResponse(data, safe=False)
