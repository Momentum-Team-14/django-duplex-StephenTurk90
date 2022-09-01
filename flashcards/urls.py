from django.urls import path
from . import views

urlpatterns = [
    path('', views.flashcards, name = 'flashcards'),
    path('decks/new', views.new_deck, name='new_deck'),
    path('decks/<int:pk>/', views.deck_detail, name='deck_detail'),
    path('decks/<int:pk>/edit/', views.edit_deck, name='edit_deck'),
    path('decks/<int:pk>/delete/', views.delete_deck, name='delete_deck'),
    path('flashcards/<int:pk>', views.results, name = 'results'),
    path('flashcards/new', views.create_card, name='create_card'),
    path('flashcards/<int:pk>/edit', views.edit_card, name='edit_card'),
    path('flashcard/<int:pk>/delete', views.delete_flashcard, name='delete'),
]