import json
import constants as c

class JsonObjectCollection:
    def __init__(self):
        self.collection = []

    def toJSON(self):
        return json.dumps(self.collection, default=lambda o: o.__dict__, ensure_ascii=False, indent=1)

class SentenceFullData:
    def __init__(self, text="", tokens=None, audio_id="", translation="", id=0):
        self.id = id
        self.type = "sentence"
        self.text = text
        self.audio_id = audio_id
        self.translation = translation
        self.tokens = tokens


    def add_token(self, token):
        if self.tokens is None:
            self.tokens = []
        self.tokens.append(token)

class TokenFullData:
    def __init__(self, text = "", words=None, audio_id="", id=0):
        self.id = id
        self.type = "token"
        self.text = text
        self.audio_id = audio_id    
        self.words = words

    def add_word(self, word):
        if self.words is None:
            self.words = []
        self.words.append(word)

class WordFullData:
    def __init__(self, text="", lemma="", upos="", audio_id="", definition_id="", id=0):
        self.id = id        
        self.type = "word"
        self.text = text
        self.lemma = lemma
        self.upos = upos
        self.audio_id = audio_id
        self.definition_id = definition_id



    