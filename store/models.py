from django.db import models

from users.models import User

NULLABLE = {'blank':True, 'null':True}


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
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='not_selected')
    is_in_the_cart = models.BooleanField(default=False)

    def __str__(self):
        return self.title
