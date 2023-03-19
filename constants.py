SPANISH_CHAR_SET = {'&': '0', '*': '1', '-': '2', '0': '3', '1': '4', '2': '5', '3': '6', '4': '7', '5': '8', '6': '9', '7': '10', '8': '11', '9': '12', '?': '13', '@': '14', 'a': '15', 'b': '16', 'c': '17', 'd': '18', 'e': '19', 'f': '20', 'g': '21', 'h': '22', 'i': '23', 'j': '24', 'k': '25', 'l': '26', 'm': '27', 'n': '28', 'o': '29', 'p': '30', 'q': '31', 'r': '32', 's': '33', 't': '34', 'u': '35', 'v': '36', 'w': '37', 'x': '38', 'y': '39', 'z': '40', '~': '41', '¡': '42', '¿': '43', 'à': '44', 'á': '45', 'ç': '46', 'é': '47', 'í': '48', 'ñ': '49', 'ò': '50', 'ó': '51', 'ú': '52', 'đ': '53', '℆': '54', '◌': '55', '⸘': '56', 'ꝇ': '57'}

POS_TAGS_SET = {"ADJ":"adjective","ADP":"adposition","ADV":"adverb","AUX":"auxiliary","CCONJ":"coordinationg conjunction","DET":"determiner","INTJ":"interjection","NOUN":"noun","NUM":"numeral","PART":"particle","PRON":"pronoun","PROPN":"proper noun","PUNCT":"punctuation","SCONJ":"subordinating conjunction","SYM":"symbol","VERB":"verb","X":"other"}

import ijson
from collections import defaultdict
import preprocess.database.mongo.operations as mongo
import config as cf
from pymongo import MongoClient

CURRENT_DB_KEYS = set()
DICTIONARY = defaultdict(list)

def init_dictionary(language):
    CURRENT_DB = get_elems(language)
    for i in CURRENT_DB:
        CURRENT_DB_KEYS.add(i["word"].lower())
    dict_path = get_dict_path(language)
    with open(dict_path, "r") as file:
        data = ijson.items(file, "item")
        for item in data:
            DICTIONARY[item["word"].lower()].append(item)

def get_elems(language):
    CONNECTION_STRING = cf.get_configs()["DATABASE"]["CONNECTION"]
    client = MongoClient(CONNECTION_STRING)
    db = client["dictionary"]
    result = db[language].find({}, {"word": 1})
    return result

def get_dict_path(language):
    if(language == "es"):
        path = cf.get_configs()["PATH"]["ES_DICT_PATH"]   
    return path

