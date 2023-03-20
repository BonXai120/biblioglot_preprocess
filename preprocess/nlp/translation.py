import requests
import config
from preprocess.utils.to_dict import to_dict
from preprocess.database.json import Json_Object as j
class TranslationFullData:
    def __init__(self, sentence="", index=0, translation=""):
        self.sentence = sentence
        self.index = index
        self.translation = translation



def request_translation(sentence, language=""):
    c = config.get_configs()
    try:
        url = c["TRANSLATION"]["URL"]
        headers = {"Host": c["TRANSLATION"]["HOST"], "Authorization": c["TRANSLATION"]["AUTH_TOKEN"]}
        data = {"source_lang":language.upper(), "target_lang":"EN-US", "text":[sentence]}
        result = requests.post(url, headers=headers, json=data)
        translated_text = result.json()["translations"][0]["text"]
        return translated_text
    except () as error:
        print(error)

def create_translation_json(json_data, language):
    translation_list = []
    for sentence in json_data:
        # translation = request_translation(sentence.text, language)
        translation = "placeholder"
        t_object = TranslationFullData(sentence=sentence["text"], index=sentence["index"], translation=translation)
        translation_list.append(t_object)
    return translation_list

def get_translations(json_data, language):
    translation_objects = j.JsonObjectCollection()
    translation_objects.collection.append(create_translation_json(json_data, language)) 
    return translation_objects.toJSON()
