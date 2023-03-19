import stanza
import preprocess.utils.file_handler as f

class ParsedText:
    def __init__(self, language, text):
        self.language = language
        self.text = text
        self.words = []
        self.tokens = []
        self.sentences_objects = []
        self.sentences_text = []
        self.doc = self.parse_text(language, text)
        self.populate_annotations(self.doc.sentences)

    def parse_text(self, language, text):
        process_options = "tokenize,mwt,pos,lemma,ner"
        stanza.download(lang=language, processors=process_options)
        nlp = stanza.Pipeline(lang=language, processors=process_options, download_method=None)
        doc = nlp(text)
        return doc
    
    def populate_annotations(self, doc_sentences):
        for sentence in doc_sentences:
            tokens = []
            for token in sentence.tokens:
                if token.words[0].upos == "PUNCT" or token.words[0].upos == "SYM":
                    continue
                self.add_token(token)
                tokens.append(token)
                for word in token.words:
                    self.add_word(word)
            self.add_sentence_text(sentence.text)
            parsed_sentence = ParsedSentence(sentence.text, tokens)
            self.add_sentence_object(parsed_sentence)

    def add_sentence_object(self, parsed_sentence):
        self.sentences_objects.append(parsed_sentence)

    def add_sentence_text(self, sentence_text):
        self.sentences_text.append(sentence_text)

    def add_token(self, token):
        self.tokens.append(token)

    def add_word(self, word):
        self.words.append(word)

class ParsedSentence:
    def __init__(self, sentence_text, tokens):
        self.text = sentence_text
        self.tokens = tokens
