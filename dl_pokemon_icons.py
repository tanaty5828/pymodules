import requests
import json
import os
from logging import getLogger


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
        pokemon_names_dic[i] = str(name_i).lower()
    return pokemon_names_dic


def download_file(url, pokemon_id, file_name):
    headers = create_dummy_header(pokemon_id)

    response = requests.get(url, headers=headers)
    if response.status_code is 200:
        with open(dst_path, 'wb') as f:
            f.write(response.content)
    else:
        logger.warning(f'{dst_path} is not eble to download')
        return

def create_dummy_header(pokemon_id):
    return {
        'Referer': f'http://hikochans.com/pixelart/pokemon/{pokemon_id}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Cookie': '_ga=GA1.2.1271940294.1634311876; _gid=GA1.2.1494761810.1634311876; _gat_gtag_UA_67400407_1=1; _gat_gtag_UA_67400407_4=1; __gads=ID=223f8746377373aa-220a532b9ecc00a8:T=1634311874:RT=1634311874:S=ALNI_MbGyRI0uDSbCxTsClu_HhJunoomKQ'
    }

if __name__ == '__main__':
    logger = getLogger(__name__)
    text = get_pokemon_names()
    pokemon_names_dic = text_to_dic(text)

    for pokemon_id, pokemon_name in pokemon_names_dic.items():
        url = f'http://hikochans.com/material/icon/{pokemon_id}.gif'
        dst_path = f'./pokemons/{pokemon_name}.gif'
        if os.path.exists(dst_path):
            logger.warning(f'{dst_path} is already exists.')
            continue
        else:
            logger.info(f'Downloading {pokemon_name}')
            download_file(url, pokemon_id, dst_path)
