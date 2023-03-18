import ijson
from preprocess.database.json import Json_Object as jo
import constants as c
import config

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


def request_definitions(word=""):
    co = config.get_configs()
    if word[0].lower() not in c.SPANISH_CHAR_SET:
        return
    with open(f"{co['PATH']['ES_DICT_PATH']}{c.SPANISH_CHAR_SET[word[0].lower()]}.json",mode="r") as d:
        dictionary = ijson.items(d,"item")
        definitions_list = []

        for item in dictionary:
            if((item["word"].lower()==word.lower())):
                senses = SensesObject(item)
                word_definition = DefinitionFullData(word=item["word"], pos=item["pos"], senses=senses)
                definitions_list.append(word_definition)
        return definitions_list
        
