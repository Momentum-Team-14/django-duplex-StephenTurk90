from django.shortcuts import render

def flashcards(request):
    return render(request, 'flashcards/flashcards.html', {'flashcards': flashcards})
