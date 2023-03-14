class JsonCollection:
    def __init__(self):
        self.collection = []

class SentenceFullData:
    def __init__(self, text="", tokens=None, audio_id="", translation=""):
        self.text = text
        self.tokens = tokens
        self.audio_id = audio_id
        self.translation = translation
        self.paragraph_end = False

    def set_text(self, text):
        self.text = text

    def add_token(self, token):
        self.tokens.append(token)

    def set_audio_id(self, audio_id):
        self.audio_id = audio_id

    def set_translation(self, translation):
        self.translation = translation
    
    def set_paragraph_end(self, paragraph_end):
        self.paragraph_end = paragraph_end

class TokenFullData:
    def __init__(self):
        self.text = ""
        self.words = []

    def set_text(self, text):
        self.text = text

    def set_words(self, words):
        self.words = words

class WordFullData:
    def __init__(self):
        self.text = ""
        self.lemma = ""
        self.upos = ""
        self.audio_id = ""
        self.definition = ""
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
        