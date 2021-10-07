from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from .utils import *

class HomeView(TemplateView):
  template_name = "pokedexApp/index.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pokemonsList = get_all_pokemons(898)
    paginate_by = 12

    paginator = Paginator(pokemonsList, paginate_by)
    page = self.request.GET.get('page')
    pokemonsList = paginator.get_page(page)

    pokemons = [get_pokemon(pokemon['url']) for pokemon in pokemonsList]

    context['pokemonsList'] = pokemonsList
    context['pokemons'] = pokemons
    return context




class PokemonView(TemplateView):
  template_name = 'pokedexApp/pokemon.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pokemonID = self.request.GET.get('pokemonID')  
    pokemon = get_pokemon(f"https://pokeapi.co/api/v2/pokemon/{pokemonID}")
    specie = get_pokemon_specie(pokemon['species']['url'])
    weakness_list = []
    strenghts_list = []

    for types in pokemon['types']:
      url = types['type']['url']
      type = get_pokemon_type(url)          
      weakness_list.append(type['list_weakness'])
      strenghts_list.append(type['list_strenghts'])

    pokemon_evolutions = get_pokemon_evolutions(specie)
    evolution_one = pokemon_evolutions['evolution_one']

    if pokemon_evolutions['evolves']:
      context['pokemon_evolution_two'] = pokemon_evolutions['evolution_two']      
      if pokemon_evolutions['more_than_two_evolutions']:
        context['pokemon_evolution_three'] = pokemon_evolutions['evolution_three']



    description_list = specie['flavor_text_entries']
    description_formated = get_pokemon_description(description_list)
    pokemon['description'] = description_formated
    pokemon['habitat'] = get_pokemon_habitat(specie)
    pokemon['growth_rate'] = get_pokemon_growth_rate(specie)
    pokemon['shape'] = get_pokemon_shape(specie)
    pokemon['weakness_list'] = weakness_list
    pokemon['strenghts_list'] = strenghts_list
    context['pokemon_evolution_one'] = evolution_one
    context['pokemon_evolves'] = pokemon_evolutions['evolves']
    context['evolves_three_times'] = pokemon_evolutions['more_than_two_evolutions']

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

        allPokemons = get_all_pokemons(898)
        pokemonsList = []
        for pokemon in allPokemons:
          term_verifyer(pokemon, termo, pokemonsList)


        paginator = Paginator(pokemonsList, paginated_by)
        page = self.request.GET.get('page')
        pokemonsList = paginator.get_page(page)

        pokemons = [get_pokemon(pokemon['url']) for pokemon in pokemonsList]

        context['pokemons'] = pokemons
        context['pokemonsList'] = pokemonsList

        return context
