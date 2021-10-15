from os import kill, name
import requests
import json
import os
import pprint
import urllib.error
import urllib.request
from bs4 import BeautifulSoup

from requests.models import Response


def get_pokemon_names():
    pokemon_en_name_json_path = 'https://raw.githubusercontent.com/sindresorhus/pokemon/main/data/en.json'
    url = requests.get(pokemon_en_name_json_path)
    text = url.text
    return text


def text_to_dic(text):
    pokemon_names = json.loads(text)
    pokemon_names_dic = {}
    for i, name_i in enumerate(pokemon_names, start=1):
        i = str(i).zfill(3)
        pokemon_names_dic[i] = name_i
    return pokemon_names_dic


def download_file(url, file_name):
    headers = {
        'Referer': 'http://hikochans.com/pixelart/pokemon/001',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Cookie': '_ga=GA1.2.1271940294.1634311876; _gid=GA1.2.1494761810.1634311876; _gat_gtag_UA_67400407_1=1; _gat_gtag_UA_67400407_4=1; __gads=ID=223f8746377373aa-220a532b9ecc00a8:T=1634311874:RT=1634311874:S=ALNI_MbGyRI0uDSbCxTsClu_HhJunoomKQ'
        }

    r2 = requests.get(url, headers=headers)
    print(r2.status_code)
    with open(dst_path, 'wb') as f:
        f.write(r2.content)

text = get_pokemon_names()
pokemon_names_dic = text_to_dic(text)

for pokemon_id, pokemon_name in pokemon_names_dic.items():
    url = f'http://hikochans.com/material/icon/{pokemon_id}.gif'
    dst_path = f'{pokemon_name}.gif'
    print(url, dst_path)
    download_file(url, dst_path)
    break
