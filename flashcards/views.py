from django.shortcuts import render
from .models import Flashcards

def flashcards(request):
    flashcards = Flashcards.objects.all()
    return render(request, 'flashcards/flashcards.html', {'flashcards': flashcards})
