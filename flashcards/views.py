from django.shortcuts import render, get_object_or_404, redirect
from .models import Flashcards, Deck
from .forms import FlashcardsForm, DeckForm
from django.shortcuts import redirect


def deck(request):
    deck = Deck.objects.all()
    return render(request, 'flashcards/list_decks.html'), {'decks': decks}


def new_deck(request):
    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid():
            deck = form.save()
            return redirect('results', pk=deck.pk)
    else:
        form = DeckForm()
    return render(request, 'flashcards/new_deck.html', {'form': form})


def deck_detail(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    cards = deck.cards.all()
    return render(request, 'flashcards/deck_detail.html', {'deck': deck})


def edit_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == 'POST':
        deck_form = DeckForm(request.POST, instance=deck)
        if deck_form.is_valid():
            deck = deck_form.save()
            return redirect('deck_detail', pk=deck.pk)
    else:
        deck_form = DeckForm(instance=deck)
    return render(request, 'flashcards/edit_deck.html', {'form': form})


def delete_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    deck.delete()
    return redirect('flashcards')


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


def delete_flashcard(request, pk):
    flashcard = get_object_or_404(Flashcards, pk=pk)
    flashcard.delete()
    return redirect('flashcards')
