from django.urls import path
from . import views

urlpatterns = [
    path('', views.flashcards, name = 'flashcards'),
    path('flashcards/<int:pk>', views.results, name = 'results'),
    path('flashcards/new', views.create_card, name='create_card'),
    path('flashcards/<int:pk>/edit', views.edit_card, name='edit_card'),
    path('flashcard/<int:pk>/delete', views.delete_card, name='delete'),
]