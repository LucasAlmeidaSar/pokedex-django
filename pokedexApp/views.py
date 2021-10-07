from django.views.generic.base import TemplateView
from django.core import paginator
import requests

class HomeView(TemplateView):
  pass

class PokemonView(HomeView):
  pass

class BuscaView(HomeView):
  pass
