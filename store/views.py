from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView

from .models import Game, CartItem, Cart, WishlistItem, Wishlist


def game_list(request):
    games = Game.objects.all()
    cart = CartItem.objects.filter(cart__user=request.user, cart__is_active=True)
    wishlist = WishlistItem.objects.filter(wishlist__user=request.user, wishlist__is_active=True)

    # Get the list of games in cart and wishlist
    cart_game_ids = set(item.game.id for item in cart)
    wishlist_game_ids = set(item.game.id for item in wishlist)

    # Add 'in_cart' and 'in_wishlist' attributes to each game
    for game in games:
        game.in_cart = game.id in cart_game_ids
        game.in_wishlist = game.id in wishlist_game_ids

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


def cart_list(request):
    cart_items = CartItem.objects.filter(cart__user=request.user, cart__is_active=True)
    total_price = sum(item.get_total_price() for item in cart_items)
    context = {'object_list': cart_items, 'total_price': total_price}
    return render(request, 'cart.html', context)


def add_to_cart(request):
    game_id = request.POST.get('game_id')
    cart, created = Cart.objects.get_or_create(user=request.user, is_active=True)
    game, _ = Game.objects.get_or_create(id=game_id)
    CartItem.objects.update_or_create(cart=cart, game=game, defaults={'quantity': 1})
    return JsonResponse({'success': True})


def update_cart_item(request, cart_item_id):
    quantity = request.POST.get('quantity')
    try:
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.quantity = int(quantity)
        cart_item.save()
        return JsonResponse({'success': True})
    except CartItem.DoesNotExist:
        return JsonResponse({'success': False})


def remove_from_cart(request):
    game_id = request.POST.get('game_id')
    game = Game.objects.get(id=game_id)
    cart = Cart.objects.get(user=request.user)
    if CartItem.objects.filter(cart=cart, game=game).exists():
        CartItem.objects.filter(cart=cart, game=game).delete()
    return JsonResponse({'removed_from_cart': True})


def wishlist_list(request):
    wishlist_items = WishlistItem.objects.filter(wishlist__user=request.user, wishlist__is_active=True)
    context = {'object_list': wishlist_items}
    return render(request, 'wishlist.html', context)


def add_to_wishlist(request):
    game_id = request.POST.get('game_id')
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    game = Game.objects.get(id=game_id)

    # Проверяем, есть ли игра уже в списке желаемого
    if not WishlistItem.objects.filter(wishlist=wishlist, game=game).exists():
        WishlistItem.objects.create(wishlist=wishlist, game=game)

    return JsonResponse({'in_wishlist': WishlistItem.objects.filter(wishlist=wishlist, game=game).exists()})


def remove_from_wishlist(request):
    game_id = request.POST.get('game_id')
    game = Game.objects.get(id=game_id)
    wishlist = Wishlist.objects.get(user=request.user)
    if WishlistItem.objects.filter(wishlist=wishlist, game=game).exists():
        WishlistItem.objects.filter(wishlist=wishlist, game=game).delete()
    return JsonResponse({'removed_from_wishlist': True})
