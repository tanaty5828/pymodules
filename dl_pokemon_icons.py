from os import name
import requests
import json


def get_pokemon_names():
    pokemon_en_name_json_path = 'https://raw.githubusercontent.com/sindresorhus/pokemon/main/data/en.json'
    url = requests.get(pokemon_en_name_json_path)
    text = url.text
    return text

def text_to_dic(text):
    pokemon_names = json.loads(text)
    pokemon_names_dic = {}
    for name_i, i in enumerate(pokemon_names, start=1):
        i = str(i).zfill(3)
        pokemon_names_dic[i] = name_i
    return pokemon_names_dic

text = get_pokemon_names()
pokemon_names_dic = text_to_dic(text)
print(pokemon_names_dic)