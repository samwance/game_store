from functools import reduce

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from .models import Game, CartItem, Cart, WishlistItem, Wishlist, Genre
from django.shortcuts import get_object_or_404
from django.db.models import Q


def get_game_list_data(request):
    cart = CartItem.objects.filter(cart__user=request.user, cart__is_active=True)
    wishlist = WishlistItem.objects.filter(wishlist__user=request.user, wishlist__is_active=True)

    # Get the list of games in cart and wishlist
    cart_game_ids = set(item.game.id for item in cart)
    wishlist_game_ids = set(item.game.id for item in wishlist)

    return cart_game_ids, wishlist_game_ids


def home(request):
    genres = Genre.objects.all()
    featured_games = Game.objects.all()[:5]
    context = {
        'title': 'Table & Board',
        'genres': genres,
        'featured_games': featured_games
    }
    return render(request, 'store/home.html', context)


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
            # Filter games by all selected genres
            genre_filter = [' '.join(genre.split('+')) for genre in genre_filter]
            genre_set = set(genre_filter)
            games = games.filter(genre__name__in=genre_set)
    title = 'Table & Board'
    context = {'games': games, 'title': title, 'query': query, 'genre_filter': genre_filter}
    return render(request, 'store/index.html', context)


def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'store/genre_list.html', {'genres': genres, 'title': 'Genres'})


def view_game(request, pk):
    game = get_object_or_404(Game, pk=pk)

    title = game.title
    cart_game_ids, wishlist_game_ids = get_game_list_data(request)

    # Add 'in_cart' and 'in_wishlist' attributes to each game
    game.in_cart = game.id in cart_game_ids
    game.in_wishlist = game.id in wishlist_game_ids

    context = {'game': game, 'title': title}
    return render(request, 'store/game.html', context)


def view_genre(request, slug):
    genre = Genre.objects.get(slug=slug)
    return render(request, 'store/genre.html', {'genre': genre, 'title': genre.name})


def about(request):
    title = 'About'
    context = {'title': title}
    return render(request, 'store/about.html', context)


def cart_list(request):
    cart_items = CartItem.objects.filter(cart__user=request.user, cart__is_active=True)
    context = {'object_list': cart_items, 'title': 'Cart'}
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
    context = {'object_list': wishlist_items, 'title': 'Wishlist'}
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
