from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import requests
import json
from modules import devices, modelloader, script_callbacks, errors
from modules.shared import opts
import os

ruta_al_archivo_dict = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'config.json').replace("\\", "/")

ruta_al_archivo_dict = os.path.normpath(ruta_al_archivo_dict)

with open(ruta_al_archivo_dict, 'r') as archivo:
    diccionario_cargado = json.load(archivo)


def translate_text_api(text):
    url = diccionario_cargado["translate_api_url"].lower()

    payload = {
        "q": text,
        "source": diccionario_cargado["translate_language"],
        "target": "en",
        "format": "text",
        "api_key": ""
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    aux = response.json()
    return aux["translatedText"]
