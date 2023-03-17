import json

class JsonObjectCollection:
    def __init__(self):
        self.collection = []
    def toJSON(self):
        return json.dumps(self.collection, default=lambda o: o.__dict__, ensure_ascii=False, indent=1)

class SentenceFullData:
    def __init__(self, text="", tokens=None, audio_id="", translation="", paragraph_end=False, id=0):
        self.type = "sentence"
        self.id = id
        self.text = text
        self.tokens = tokens
        self.audio_id = audio_id
        self.translation = translation
        self.paragraph_end = paragraph_end

    def add_token(self, token):
        if self.tokens is None:
            self.tokens = []
        self.tokens.append(token)

class TokenFullData:
    def __init__(self, text = "", words=None, id=0):
        self.type = "token"
        self.id = id
        self.text = text    
        self.words = words

    def add_word(self, word):
        if self.words is None:
            self.words = []
        self.words.append(word)

class WordFullData:
    def __init__(self, text="", lemma="", upos="", audio_id="", definition_id="", id=0):
        self.type = "word"
        self.id = id
        self.text = text
        self.lemma = lemma
        self.upos = upos
        self.audio_id = audio_id
        self.definition_id = definition_id

class DefinitionFullData:
    def __init__(self, word="", pos="", senses=None):
        self.word = word
        self.pos = pos
        self.senses = senses



    