from django.shortcuts import render, get_object_or_404
from .models import Flashcards

def flashcards(request):
    flashcards = Flashcards.objects.all()
    return render(request, 'flashcards/flashcards.html', {'flashcards': flashcards})

def results(request, pk):
    flashcard = get_object_or_404(Flashcards, pk=pk)
    return render(request, 'flashcards/results.html', {'flashcard': flashcard})
