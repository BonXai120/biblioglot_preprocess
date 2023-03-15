import json

class SentenceCollection:
    def __init__(self):
        self.collection = []
    def toJSON(self):
        return json.dumps(self.collection, default=lambda o: o.__dict__, ensure_ascii=False, indent=1)

class SentenceFullData:
    def __init__(self, text="", tokens=None, audio_id="", translation="", paragraph_end=False):
        self.text = text
        self.tokens = tokens
        self.audio_id = audio_id
        self.translation = translation
        self.paragraph_end = paragraph_end

    def set_text(self, text):
        self.text = text

    def add_token(self, token):
        if self.tokens is None:
            self.tokens = []
        self.tokens.append(token)

    def set_audio_id(self, audio_id):
        self.audio_id = audio_id

    def set_translation(self, translation):
        self.translation = translation
    
    def set_paragraph_end(self, paragraph_end):
        self.paragraph_end = paragraph_end

class TokenFullData:
    def __init__(self, text = "", words=None):
        self.text = text    
        self.words = words

    def set_text(self, text):
        self.text = text

    def set_words(self, words):
        self.words = words

    def add_word(self, word):
        if self.words is None:
            self.words = []
        self.words.append(word)

class WordFullData:
    def __init__(self, text="", lemma="", upos="", audio_id="", definition=""):
        self.text = text
        self.lemma = lemma
        self.upos = upos
        self.audio_id = audio_id
        self.definition = definition

    def set_text(self, text):
        self.text = text

    def set_lemma(self, lemma):
        self.lemma = lemma

    def set_upos(self, upos):
        self.upos = upos

    def set_audio_id(self, audio_id):
        self.audio_id = audio_id

    def set_definition(self, definition):
        self.definition = definition
        