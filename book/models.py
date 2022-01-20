from django.contrib.auth.models import User
from django.db import models

class Book(models.Model):
    GENRE_CHOICE = (
        ('non-fiction', 'non-fiction'),
        ('science-fiction', 'science-fiction'),
        ('fantasy', 'fantasy'),
        ('fairy-tale', 'fairy-tale'),
        ('fiction', 'fiction')
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField()
    genre = models.CharField(choices=GENRE_CHOICE, max_length=100)
    date_filmed = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Rating(models.Model):
    RATE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
