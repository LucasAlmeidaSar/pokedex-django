from pokedexApp.utils import *

url_pokemon = 'https://pokeapi.co/api/v2/pokemon/pikachu'
url_specie = 'https://pokeapi.co/api/v2/pokemon-species/25/'
url_type = 'https://pokeapi.co/api/v2/type/13/'
weakness_list = [{ "name": "ice","url": "https://pokeapi.co/api/v2/type/3/"}]
fake_specie = {'habitat' : '', 'shape' : '','growth_rate' : ''}


def test_get_pokemon_returns_dict():
  pokemon = get_pokemon(url_pokemon)
  assert type(pokemon) == dict

def test_get_pokemon_contains_22_items():
  pokemon = get_pokemon(url_pokemon)
  assert len(pokemon) == 22

def test_get_all_pokemons_returns_list():
  all_pokemons = get_all_pokemons(100)
  assert type(all_pokemons) == list

def test_get_all_pokemons_return_correct_amount():
  amount = 400
  all_pokemons = get_all_pokemons(amount)
  assert amount == len(all_pokemons)

def test_get_all_pokemons_returns_max_898_pokemons():
  all_pokemons = get_all_pokemons(1000)
  assert len(all_pokemons) == 898

def test_get_pokemon_specie_returns_dict():
  specie = get_pokemon_specie(url_specie)
  assert type(specie) == dict

def test_get_pokemon_description_returns_string():
  specie = get_pokemon_specie(url_specie)
  list_of_descriptions = specie['flavor_text_entries']
  description = get_pokemon_description(list_of_descriptions)
  assert type(description) == str

def test_get_pokemon_habitat_returns_string():
  specie = get_pokemon_specie(url_specie)
  habitat = get_pokemon_habitat(specie)
  assert type(habitat) == str

def test_get_pokemon_habitat_returns_uninformed_if_not_habitat():
  habitat = get_pokemon_habitat(fake_specie)
  assert habitat == 'Uninformed'

def test_get_pokemon_growth_rate_returns_string():
  specie = get_pokemon_specie(url_specie)
  growth_rate = get_pokemon_growth_rate(specie)
  assert type(growth_rate) == str

def test_get_pokemon_growth_rate_returns_uninformed_if_not_informed():
  growth_rate = get_pokemon_growth_rate(fake_specie)
  assert growth_rate == 'Uninformed'

def test_get_pokemon_shape_returns_string():
  specie = get_pokemon_specie(url_specie)
  shape = get_pokemon_shape(specie)
  assert type(shape) == str

def test_get_pokemon_shape_returns_uninformed_if_not_informed():
  shape = get_pokemon_shape(fake_specie)
  assert shape == 'Uninformed'


def test_get_pokemon_type_returns_dict():
  pokemon_type = get_pokemon_type(url_type)
  assert type(pokemon_type) == dict

def test_get_pokemon_weakness_or_strenghts_returns_list():
  weakness = get_pokemon_weakness_or_strenghts(weakness_list)
  assert type(weakness) == list

def test_split_lists_in_list_return_list():
  fake_list = [[1,2,3,4],[10,20,30]]
  new_list = split_lists_in_list(fake_list)
  assert type(new_list) == list

def test_split_lists_in_list_returns_unique_list():
  fake_list = [[1,2,3,4],[10,20,30]]
  new_list = split_lists_in_list(fake_list)
  unique_list = []
  for array in fake_list:
    for item in array:
      unique_list.append(item)

  assert new_list == unique_list

def test_remove_duplicates_return_list():
  list_duplicates = [1,10,10,20,30,30,40,50]
  list_uniques = remove_duplicates(list_duplicates)
  assert type(list_uniques) == list

def test_remove_duplicates_return_unique():
  list_duplicates = [10, 10, 10, 20,30,40,50]
  list_uniques = list(dict.fromkeys(list_duplicates))
  list_final = remove_duplicates(list_duplicates)
  assert list_final == list_uniques

def test_get_pokemon_evolutions_return_dict():
  specie = get_pokemon_specie(url_specie)
  assert type(get_pokemon_evolutions(specie)) == dict