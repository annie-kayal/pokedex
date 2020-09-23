from django.db import models
from django.contrib.auth.models import AbstractUser
from pokemon.models import InputtedPokemon

# Create your models here.
class User(AbstractUser):
  email: models.EmailField(blank=False, unique=True)
  first_name: models.CharField(blank=False, max_length=100)
  last_name: models.CharField(blank=True, max_length=100)
  image: models.ImageField(blank=True, upload_to='Images')
  current_pokemon: models.ManyToManyField(InputtedPokemon, related_name='pokemon')
