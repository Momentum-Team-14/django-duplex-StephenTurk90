from django.shortcuts import render
from django.utils import timezone
from .models import Card


def card_list(request):
    cards = Card.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'flashcards/card_list.html', {'cards':cards})