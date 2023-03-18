import requests
import config


def request_translation(sentence, language=""):
    c = config.get_configs()
    try:
        url = c["TRANSLATION"]["URL"]
        headers = {"Host": c["TRANSLATION"]["HOST"], "Authorization": c["TRANSLATION"]["AUTH_TOKEN"]}
        data = {"source_lang":language, "target_lang":"EN-US", "text":[sentence]}
        result = requests.post(url, headers=headers, json=data)
        translated_text = result.json()["translations"][0]["text"]
        return translated_text
    except () as error:
        print(error)