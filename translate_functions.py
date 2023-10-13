from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import requests
import json


def translate_text_api(text):

    url = "https://translator.athosnetwork.es/translate"

    payload = {
        "q": text,
        "source": "es",
        "target": "en",
        "format": "text",
        "api_key": ""
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    aux = response.json()
    return aux["translatedText"]
