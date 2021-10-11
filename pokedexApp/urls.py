from django.urls import path
from .views import *

urlpatterns = [
  path('', HomeView.as_view(), name='pg_inicial'),
  path('pokemon/', PokemonView.as_view() , name='pg_pokemon'),
  path('busca/', SearchView.as_view() , name='pg_busca'),
]