from django.db import models


# Create your models here.
POKEMON_TYPES = (
  ('NORMAL', 'normal'),
  ('FIRE', 'fire'),
  ('WATER', 'water'),
  ('GRASS', 'grass'),
  ('ELECTRIC', 'electric'),
  ('ICE', 'ice'),
  ('FIGHTING', 'fighting'),
  ('POSION', 'posion'),
  ('GROUND', 'ground'),
  ('FLYING', 'flying'),
  ('PSYHIC', 'psyhic'),
  ('BUG', 'bug'),
  ('ROCK', 'rock'),
  ('GHOST', 'ghost'),
  ('DARK', 'dark'),
  ('DRAGON', 'dragon'),
  ('STEEL', 'steel'),
  ('FAIRY', 'fairy'),
)


class InputtedPokemon(models.Model):
  name = models.CharField(blank=False, max_length=100, unique=True)
  image = models.ImageField(blank=True, upload_to='Images')
  attacks = models.CharField(blank=False, max_length=100, default='none')
  evolution = models.CharField(blank=True, max_length=100) 
  primary_type = models.CharField(blank=False, choices=POKEMON_TYPES, default='normal', max_length=100)
  secondary_type = models.CharField(blank=True, choices=POKEMON_TYPES, default='normal', max_length=100)
  approved = models.BooleanField(default=False)

  def __str__(self):
    return f'{self.name}'

    