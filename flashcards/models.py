from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Flashcards(models.Model):
    deck = models.ForeignKey('Deck', on_delete=models.CASCADE, related_name='cards', blank=True, null=True)
    title = models.CharField(max_length=250)
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)
    
    class Meta:
        verbose_name_plural = "flashcards"

    def __str__(self):
        return self.title


class Deck(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.title