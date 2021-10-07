import requests

def getPokemon(url_pokemon):
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



def getAllPokemons(amount_pokemons):
    contador = 0
    limit = amount_pokemons
    url = f"https://pokeapi.co/api/v2/pokemon/?limit={limit}"
    response = requests.get(url)
    jsonObject = response.json()
    pokemonsList = jsonObject['results']
    for pokemon in pokemonsList:
        contador += 1
        img = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{contador}.png"
        pokemon['id'] = f"{contador}"
        pokemon['img'] = img

    return pokemonsList



def termo_verify(pokemon, term, array):
    if pokemon['name'].find(term) != -1 or pokemon['id'].find(term) != -1:
      array.append(pokemon)


def getPokemonSpecie(url):
  response = requests.get(url)
  specie = response.json()
  return specie

def getPokemonDescription(array):
  for item in array:
    if item['language']['name'] == 'en':
      string = item['flavor_text']
      break

  string = string.replace('\n', ' ')
  string = string.replace('\f', ' ')
  string = string.replace('POKéMON', 'pokemon') 
  return string

def getPokemonHabitat(specie):
  habitat = 'Uninformed' if not specie['habitat'] else specie['habitat']['name'].capitalize()
  return habitat

def getPokemonGrowthRate(specie):
  growth_rate = 'Uninformed' if not specie['growth_rate'] else specie['growth_rate']['name'].capitalize()
  return growth_rate

def getPokemonShape(specie):
  shape = 'Uninformed' if not specie['shape'] else specie['shape']['name'].capitalize()
  return shape


def getPokemonType(url, item):
  # Fazendo o get da url
  response = requests.get(url)

  # Transoformando a resposta em JSON e armazenando na variável type
  type = response.json()

  # Criando a variável que receberá o array com os objetos para varrer.
  array_weakness = type['damage_relations'][item]

  # Criando a variável final que terá a lista somente com os nomes das fraquezas 
  list = getPokemonWeakness(array_weakness)

  # Adicionando um item na variável Type com a lista das fraquezas
  type['list'] = list
 
  # Retorno o type para ser usado na minha página.
  return type



def getPokemonWeakness(array):
  # Criando um array vazio para preencher com os nomes das fraquezas
  all_weakness = []

  # Passando por cada item do array, recolhendo os nomes e adicionando a lista vazia
  for item in array:
    all_weakness.append(item['name'])
   
  # retorno a lista com os nomes após preenchê-la
  return all_weakness
  
