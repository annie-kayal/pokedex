from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny 
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED, HTTP_422_UNPROCESSABLE_ENTITY, HTTP_204_NO_CONTENT

from .models import InputtedPokemon
from .serializers import PokemonSerializer

# Create your views here.


class AllPokemonView(ListCreateAPIView):
    queryset = InputtedPokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [AllowAny]

    def get(self, request):
      all_pokemon = InputtedPokemon.objects.filter(approved=True)
      serializer = PokemonSerializer(all_pokemon, many=True)
      return Response(serializer.data)

    def post(self, request):
      serializer = PokemonSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
      
      return Response(serializer.data, status=HTTP_422_UNPROCESSABLE_ENTITY)


class PokemonDetailView(RetrieveUpdateDestroyAPIView):
    queryset = InputtedPokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [AllowAny]

    def get(self, request, name):
        pokemon = InputtedPokemon.objects.get(name=name)
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)

    def delete(self, request, name):
        pokemon = InputtedPokemon.objects.get(name=name)
        pokemon.delete()
        return  Response(status=HTTP_204_NO_CONTENT)

    def put(self, request, name):
        pokemon = InputtedPokemon.objects.get(name=name)
        serializer = PokemonSerializer(pokemon, data=request.data)
        if serializer.is_valid(raise_exception=True):
          serializer.save(approved=False)
          return Response(serializer.data)

        return Response(serializer.data)     
