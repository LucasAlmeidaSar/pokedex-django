import requests

def get_pokemon(url_pokemon : str) -> dict:
  response = requests.get(url_pokemon)
  pokemon = response.json()
  img = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon['id']}.png"
  pokemon['img'] = img
  types = [types['type']['name'].capitalize() for types in pokemon['types']]
  pokemon['types_string'] = ' | '.join(types)
  height = pokemon['height'] / 10
  weight = pokemon['weight'] / 10
  pokemon['height_mts'] = height
  pokemon['weight_kg'] = weight
  return pokemon


def get_all_pokemons(amount_pokemons:int) -> list:
  counter = 0
  limit = amount_pokemons if amount_pokemons <= 898 else 898
  url = f"https://pokeapi.co/api/v2/pokemon/?limit={limit}"
  response = requests.get(url)
  jsonObject = response.json()
  pokemonsList = jsonObject['results']
  for pokemon in pokemonsList:
    counter += 1
    img = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{counter}.png"
    pokemon['id'] = f"{counter}"
    pokemon['img'] = img

  return pokemonsList



def term_verifyer(pokemon:dict, term:str, array:list):
  if pokemon['name'].find(term) != -1 or pokemon['id'].find(term) != -1:
    array.append(pokemon)


def get_pokemon_specie(url_specie:str) -> dict:
  response = requests.get(url_specie)
  specie = response.json()
  return specie

def get_pokemon_description(list_of_descriptions:list) -> str:
  for description in list_of_descriptions:
    if description['language']['name'] == 'en':
      pokemon_description = description['flavor_text']
      break
  pokemon_description = pokemon_description.replace('\n', ' ')
  pokemon_description = pokemon_description.replace('\f', ' ')
  pokemon_description = pokemon_description.replace('POKéMON', 'pokemon') 
  return pokemon_description

def get_pokemon_habitat(specie:dict) -> str:
  habitat = 'Uninformed' if not specie['habitat'] else specie['habitat']['name'].capitalize()
  return habitat

def get_pokemon_growth_rate(specie:dict) -> str:
  growth_rate = 'Uninformed' if not specie['growth_rate'] else specie['growth_rate']['name'].capitalize()
  return growth_rate

def get_pokemon_shape(specie:dict) -> str:
  shape = 'Uninformed' if not specie['shape'] else specie['shape']['name'].capitalize()
  return shape


def get_pokemon_type(url_type:str) -> dict:
  response = requests.get(url_type)
  type = response.json()

  weakness = type['damage_relations']['double_damage_from'] 
  strenghts = type['damage_relations']['double_damage_to'] 

  list_weakness = get_pokemon_weakness_or_strenghts(weakness)
  list_strenghts = get_pokemon_weakness_or_strenghts(strenghts)

  type['list_weakness'] = list_weakness
  type['list_strenghts'] = list_strenghts

  return type
  

def get_pokemon_weakness_or_strenghts(list:list) -> list:
  list_items = [item['name'] for item in list]   
  return list_items
  
