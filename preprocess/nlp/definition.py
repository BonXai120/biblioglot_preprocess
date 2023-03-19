import ijson
from preprocess.database.json import Json_Object as jo
import constants as c
import config
import preprocess.database.mongo.operations as mongo
import re

insert_load = {}

class DefinitionCollection:
    def __init__(self):
        self.collection = []
    
    def toJSON():
        return json.dumps(self.collection, default=lambda o: o.__dict__, ensure_ascii=False, indent=1)

class DefinitionFullData:
    def __init__(self, word="", pos="", senses=None):
        self.word = word
        self.pos = pos
        self.senses = senses

class SensesObject:
    def __init__(self, item):
        self.senses_list = []
        self.populate_senses(item)
    
    def add_gloss(self, sense, definition):
        sense["glosses"].append(definition)

    def add_link(self, sense, link):
        sense["links"].append(link)

    def populate_senses(self, item):
        for sense in item["senses"]:
            sense_dict = {"glosses":[], "links": []}

            if "glosses" in sense:
                for gloss in sense["glosses"]:
                    self.add_gloss(sense_dict ,gloss)
            if "links" in sense:
                for link in sense["links"]:
                    self.add_link(sense_dict, link)
            self.senses_list.append(sense_dict)


def request_definitions(word="", language=""):
    co = config.get_configs()
    # regex = re.compile(word.lower(), re.IGNORECASE)
    # db = mongo.get_database("dictionary")
    # query = mongo.query_count(key_name="word", value=regex, db=db, collection_name=language)

    if word.lower() in insert_load:
        print(insert_load[word.lower()])
    if word.lower() in c.CURRENT_KEYS:
        return
    if word[0].lower() not in c.SPANISH_CHAR_SET:
        return
    definition_list = []
    for item in c.DICTIONARY[word.lower()]:
        senses = SensesObject(item)
        word_definition = DefinitionFullData(word=item["word"], pos=item["pos"], senses=senses)
        definition_dict = to_dict(word_definition)
        definition_list.append(definition_dict)

    insert_load[word.lower()] = definition_list
        
    if len(definition_list) == 0:
        print(f"{word} not found in dictionary")
        return
    # mongo.insert_many(definition_list, "dictionary", language)
        
def to_dict(obj):
    if isinstance(obj, (list, tuple)):
        return [to_dict(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: to_dict(value) for key, value in obj.items()}
    elif hasattr(obj, '__dict__'):
        return to_dict(obj.__dict__)
    else:
        return obj