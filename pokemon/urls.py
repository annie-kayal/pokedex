from django.urls import path
from .views import AllPokemonView, PokemonDetailView

urlpatterns = [
  path('', AllPokemonView.as_view()),
  path('<str:name>/', PokemonDetailView.as_view())
]