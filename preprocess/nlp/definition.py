import ijson
from preprocess.database.json import Json_Object as jo
import constants as c
import config
import preprocess.database.mongo.operations as mongo
import re
from uuid import uuid4
from preprocess.utils.to_dict import to_dict

class DefinitionCollection:
    def __init__(self):
        self.collection = []
    
    def toJSON():
        return json.dumps(self.collection, default=lambda o: o.__dict__, ensure_ascii=False, indent=1)

class DefinitionFullData:
    def __init__(self, word="", pos="", audio_id="", senses=None):
        self.word = word
        self.pos = pos
        self.audio_id = audio_id
        self.senses = senses

class SensesObject:
    def __init__(self, item, current, unfound, word_set):
        self.senses_list = []
        self.populate_senses(item, current, unfound, word_set)
    def populate_senses(self, item, current, unfound, word_set):
        for sense in item["senses"]:
            sense_dict = {"definition":[], "links": [], "tags": []}
            if "raw_glosses" in sense:
                sense_dict["definition"] = sense["raw_glosses"]
            if "links" in sense:
                for link in sense["links"]:
                    for string in link:
                        if "#Spanish" in string:
                            sense_dict["links"].append(string)
                            link_word = string.split("#Spanish", 1)[0]
                            split_words = link_word.split(" ")
                            for w in split_words:
                                if(w not in current or w not in unfound or w not in c.CURRENT_DB_KEYS):
                                    word_set.add(w)
                                    

            if "tags" in sense:
                sense_dict["tags"] = sense["tags"]
            self.senses_list.append(sense_dict)

class WordLoad:
    def __init__(self, found_words=None, unfound_words=None):
        self.found_words = found_words
        self.unfound_words = unfound_words


def request_definition(word="", current_words=None, unfound_words=None, word_set=None, found_list=None):
    co = config.get_configs()
    
    if word in current_words:
        return
    if word in unfound_words:
        return    
    if word in c.CURRENT_DB_KEYS:
        return

    definition_list = []
    for item in c.DICTIONARY[word]:
        senses = SensesObject(item, current_words, unfound_words, word_set)
        word_definition = DefinitionFullData(word=item["word"], pos=item["pos"], senses=senses.senses_list)
        definition_dict = to_dict(word_definition)
        definition_list.append(definition_dict)
        found_list.append(definition_dict)

    if len(definition_list) == 0:
        unfound_words.append({"word": word})
        return

    current_words[word] = definition_list
        
def extract_words(json_data):
    word_set = set()
    for sentence in json_data:
        for token in sentence["tokens"]:
            word_set.add(token["text"])
            for word in token["words"]:
                word_set.add(word["text"])
                word_set.add(word["lemma"])
    return word_set

def get_definitions(json_data):
    word_set = extract_words(json_data)
    found_list = jo.JsonObjectCollection()
    word_dict = {}
    unfound_list = jo.JsonObjectCollection()
    while len(word_set) != 0:
        word = word_set.pop()
        request_definition(word=word.lower(), current_words=word_dict, unfound_words=unfound_list.collection, word_set=word_set, found_list=found_list.collection)
    load = WordLoad(found_words=found_list, unfound_words=unfound_list)
    return load

