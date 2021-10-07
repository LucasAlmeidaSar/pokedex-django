from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from .utils import *
import requests

class HomeView(TemplateView):
    template_name = "pokedexApp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pokemonsList = getAllPokemons(898)
        paginate_by = 12

        paginator = Paginator(pokemonsList, paginate_by)
        page = self.request.GET.get('page')
        pokemonsList = paginator.get_page(page)

        pokemons = [getPokemon(pokemon['url']) for pokemon in pokemonsList]

        context['pokemonsList'] = pokemonsList
        context['pokemons'] = pokemons
        return context




class PokemonView(TemplateView):
    template_name = 'pokedexApp/pokemon.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pokemonID = self.request.GET.get('pokemonID')  
        pokemon = getPokemon(f"https://pokeapi.co/api/v2/pokemon/{pokemonID}")
        specie = getPokemonSpecie(pokemon['species']['url'])
        weakness_list = []
        strenghts_list = []

        for types in pokemon['types']:
          url = types['type']['url']
          weakness = getPokemonType(url, 'double_damage_from')          
          weakness_list.append(weakness['list'])
          strenghts = getPokemonType(url, 'double_damage_to')    
          strenghts_list.append(strenghts['list'])



        description_list = specie['flavor_text_entries']
        description_formated = getPokemonDescription(description_list)
        pokemon['description'] = description_formated
        pokemon['habitat'] = getPokemonHabitat(specie)
        pokemon['growth_rate'] = getPokemonGrowthRate(specie)
        pokemon['shape'] = getPokemonShape(specie)
        pokemon['weakness_list'] = weakness_list
        pokemon['strenghts_list'] = strenghts_list

        context['pokemonID'] = pokemonID      
        context['pokemon'] = pokemon
        context['specie'] = specie
        return context



class BuscaView(TemplateView):
    template_name = 'pokedexApp/pokemon_busca.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        termo = self.request.GET.get('termo')
        paginated_by = 12

        allPokemons = getAllPokemons(898)
        pokemonsList = []
        for pokemon in allPokemons:
          termo_verify(pokemon, termo, pokemonsList)


        paginator = Paginator(pokemonsList, paginated_by)
        page = self.request.GET.get('page')
        pokemonsList = paginator.get_page(page)

        pokemons = [getPokemon(pokemon['url']) for pokemon in pokemonsList]

        context['pokemons'] = pokemons
        context['pokemonsList'] = pokemonsList

        return context
