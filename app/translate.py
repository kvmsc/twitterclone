import json
import requests
from flask_babel import _
from flask import current_app

def translate(text, dest_language):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    auth = {'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY']}
    base_url = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to={}".format(dest_language)
    body = [{'text': text}]
    r = requests.post(base_url, headers=auth, json=body)
    if r.status_code != 200:
        return _('Error! The translation service failed.')
    return json.loads(r.content)[0]['translations'][0]['text']