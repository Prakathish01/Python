# How to connect an API using python

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_data(name):
    url = f"{base_url}/pokemon/{name}"
    responses = requests.get(url)
    if responses.status_code == 200:
        pokemon_data = responses.json()
        return pokemon_data
    else:
        print(f"The data is not retrieved {responses.status_code}")

pokemon_names = ["Pikachu", "Charmander", "Bulbasaur", "Squirtle", "Eevee"]
for pokemon_name in pokemon_names:
    pokemon_info= get_data(pokemon_name)

    if pokemon_info:
        print(f"Name : {pokemon_info["name"]:<5}")
        print(f"Id : {pokemon_info["id"]:<5}")
        print(f"Weight : {pokemon_info["weight"]:<5}")
        print(f"Height :{pokemon_info["height"]:<5}")
        print("----------------------------------")
