import requests

def request_translation(sentence, language=""):
    try:
        url = "https://api-free.deepl.com/v2/translate"
        headers = {"Host":"api-free.deepl.com", "Authorization":"DeepL-Auth-Key 53a6bd0a-04c8-0bec-94fc-757a011486f7:fx"}
        data = {"source_lang":language, "target_lang":"EN-US", "text":[sentence]}
        result = requests.post(url, headers=headers, json=data)
        translated_text = result.json()["translations"][0]["text"]
        return translated_text
    except () as error:
        print(error)