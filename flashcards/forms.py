from django import forms
from .models import Flashcards, Deck


class FlashcardsForm(forms.ModelForm):
    class Meta:
        model = Flashcards
        fields = ('title', 'question', 'answer')

class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ('category',)