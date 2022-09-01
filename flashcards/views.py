from django.shortcuts import render, get_object_or_404, redirect
from .models import Flashcards
from .forms import FlashcardsForm
from django.shortcuts import redirect


def flashcards(request):
    flashcards = Flashcards.objects.all()
    return render(request, 'flashcards/flashcards.html', {'flashcards': flashcards})


def results(request, pk):
    flashcard = get_object_or_404(Flashcards, pk=pk)
    return render(request, 'flashcards/results.html', {'flashcard': flashcard})


def create_card(request):
    if request.method == 'POST':
        form = FlashcardsForm(request.POST)
        if form.is_valid():
            flashcard = form.save()
            return redirect('results', pk=flashcard.pk)
    else:
        form = FlashcardsForm()
    return render(request, 'flashcards/create_card.html', {'form': form})


def edit_card(request, pk):
    flashcard = get_object_or_404(Flashcards, pk=pk)
    if request.method == 'POST':
        form = FlashcardsForm(request.POST, instance=flashcard)
        if form.is_valid():
            flashcard = form.save(commit=False)
            flashcard.save()
            return redirect('results', pk=flashcard.pk)
    else:
        form = FlashcardsForm(instance=flashcard)
    return render(request, 'flashcards/edit_card.html', {'form': form})


def delete_card(request, pk):
    flashcard = get_object_or_404(Flashcards, pk=pk)
    flashcard.delete()
    return redirect('flashcards')
