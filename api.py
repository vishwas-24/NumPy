# How to connect to and API using python

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    responce = requests.get(url)

    if responce.status_code == 200:
        pokemon_data = responce.json()
        return pokemon_data
    else:
        print(f"Failed to retrive data {responce.status_code}")


pokemon_name = "greninja"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name   : {pokemon_info["name"].capitalize()}")
    print(f"Id     : {pokemon_info["id"]}")
    print(f"Height : {pokemon_info["height"]}")
    print(f"Weight : {pokemon_info["weight"]}")