from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Game(models.Model):
    GENRE_CHOICES = (
        ('adventure', 'Adventure'),
        ('strategy', 'Strategy'),
        ('role_playing', 'Role Playing'),
        ('puzzle', 'Puzzle'),
        ('card', 'Card'),
        ('word', 'Word'),
        ('not_selected', 'Not selected')
    )
    title = models.CharField(max_length=200)
    description = models.TextField(**NULLABLE)
    preview = models.ImageField(upload_to='games/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publisher = models.CharField(max_length=100, **NULLABLE)
    age_rating = models.CharField(max_length=5, **NULLABLE)
    quantity = models.PositiveIntegerField(default=1)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='not_selected')


    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Cart for {self.user.username}'


class CartItem(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.quantity} x {self.game.title}'


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Wishlist for {self.user.username}'


class WishlistItem(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.game.title} in {self.wishlist.user.username}\'s wishlist'
