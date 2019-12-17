import os
from dotenv import load_dotenv
import requests
import json
from urllib.parse import quote, unquote

load_dotenv()


def translate(text='Hello, world!', target='ru'):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    q = quote(text)
    payload = f"q={q}&target={target}"
    headers = {
        'x-rapidapi-host': "google-translate1.p.rapidapi.com",
        'x-rapidapi-key': os.getenv("RAPIDAPI_KEY"),
        'content-type': "application/x-www-form-urlencoded"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    res = json.loads(response.text)
    return res['data']['translations'][0]['translatedText'].replace('&#39;', '\'')
