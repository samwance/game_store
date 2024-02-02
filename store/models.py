from django.db import models

NULLABLE = {'blank':True, 'null':True}


class Game(models.Model):
    GENRE_CHOICES = (
        ('adventure', 'Adventure'),
        ('strategy', 'Strategy'),
        ('role_playing', 'Role Playing'),
        ('puzzle', 'Puzzle'),
        ('card', 'Card'),
        ('not_selected', 'Not selected')
    )
    title = models.CharField(max_length=200)
    description = models.TextField(**NULLABLE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publisher = models.CharField(max_length=100)
    release_date = models.DateField(auto_now=True)
    age_rating = models.CharField(max_length=5, **NULLABLE)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='not_selected')

    def __str__(self):
        return self.title
