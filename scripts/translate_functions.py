import requests
import json
import os

config_file_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'config.json').replace("\\", "/")

config_file_path = os.path.normpath(config_file_path)

with open(config_file_path, 'r') as file:
    loaded_dictionary = json.load(file)


def translate_text_api(text):
    url = loaded_dictionary["translate_api_url"].lower()

    payload = {
        "q": text,
        "source": loaded_dictionary["translate_language"],
        "target": "en",
        "format": "text",
        "api_key": ""
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    aux = response.json()
    return aux["translatedText"]
