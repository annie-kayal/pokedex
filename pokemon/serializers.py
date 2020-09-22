from rest_framework import serializers
from .models import InputtedPokemon, POKEMON_TYPES

class PokemonSerializer(serializers.ModelSerializer ):
  class Meta:
    model = InputtedPokemon
    fields = ('id', 'name', 'image', 'attacks', 'evolution', 'primary_type', 'secondary_type')



