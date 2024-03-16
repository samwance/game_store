from django.db import models
from django.utils.text import slugify

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Genre(models.Model):
    preview = models.ImageField(upload_to='genres/')
    name = models.CharField(max_length=100)
    description = models.TextField(**NULLABLE)
    slug = models.SlugField(unique=True, default='noslug')

    def save(self, *args, **kwargs):
        if self.slug == 'noslug':  # Проверка на наличие слага
            self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(**NULLABLE)
    preview = models.ImageField(upload_to='games/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publisher = models.CharField(max_length=100, **NULLABLE)
    age_rating = models.CharField(max_length=5, **NULLABLE)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Cart for {self.user.username}'


class CartItem(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return self.game.title


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
