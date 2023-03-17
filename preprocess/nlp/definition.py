import ijson
from preprocess.database.json import Json_Object as jo

def request_definitions(word="", cache=None):
    if word[0].lower() not in spanish_characters:
        return
    with open(f"/home/vincent/Documents/dictionaries/spanish/{spanish_characters[word[0].lower()]}.json",mode="r") as d:
        dictionary = ijson.items(d,"item")
        definitions_list = []
        cache_list = set()
        if item["word"].lower() in cache:
            return


        for item in dictionary:
            if((item["word"].lower()==word.lower()) and (item["word"].lower() not in cache_list) ):
                senses = SensesObject(item)
                word_definition = jo.DefinitionFullData(word=item["word"], pos=item["pos"], senses=senses)
                print(word_definition.word)
                definitions_list.append(word_definition)
        return definitions_list
        
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
