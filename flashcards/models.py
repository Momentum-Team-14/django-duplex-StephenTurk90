from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Flashcards(models.Model):
    title = models.CharField(max_length=100)
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "flashcards"

    def __str__(self):
        return self.title
