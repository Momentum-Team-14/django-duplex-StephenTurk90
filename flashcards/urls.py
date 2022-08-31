from django.urls import path
from . import views

urlpatterns = [
    path('', views.flashcards, name = 'flashcards'),
    path('flashcards/<int:pk>', views.results, name = 'results'),
]