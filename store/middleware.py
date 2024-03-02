from .models import CartItem


class CartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        cart_items = CartItem.objects.filter(cart__user=request.user, cart__is_active=True)
        total_price = sum(item.game.price for item in cart_items)

        request.cart_count = cart_items.count()
        request.cart_price = total_price

        response = self.get_response(request)
        return response
