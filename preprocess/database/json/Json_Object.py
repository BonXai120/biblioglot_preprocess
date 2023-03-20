import json
import constants as c

class JsonObjectCollection:
    def __init__(self):
        self.collection = []

    def toJSON(self):
        return json.dumps(self.collection, default=lambda o: o.__dict__, ensure_ascii=False, indent=1)

class SentenceFullData:
    def __init__(self, text="", tokens=None, audio_id="", index=0):
        self.index = index
        self.type = "sentence"
        self.text = text
        self.audio_id = index
        self.tokens = tokens


    def add_token(self, token):
        if self.tokens is None:
            self.tokens = []
        self.tokens.append(token)

class TokenFullData:
    def __init__(self, text = "", words=None):

        self.type = "token"
        self.text = text
        self.words = words

    def add_word(self, word):
        if self.words is None:
            self.words = []
        self.words.append(word)

class WordFullData:
    def __init__(self, text="", lemma="", upos=""):    
        self.type = "word"
        self.text = text
        self.lemma = lemma
        self.upos = upos



    