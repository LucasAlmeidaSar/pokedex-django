from django.urls import path
from .views import *

urlpatterns = [
  path('', HomeView.as_view(), name='pg_home'),
  path('pokemon/', PokemonView.as_view() , name='pg_pokemon'),
  path('search/', SearchView.as_view() , name='pg_search'),
  path('type/', TypeView.as_view() , name='pg_type'),
]