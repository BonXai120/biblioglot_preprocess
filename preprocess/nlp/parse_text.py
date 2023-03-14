import stanza
import preprocess.utils.file_handler as f

class ParsedText:
    def __init__(self, language, text):
        self.language = language
        self.text = text
        self.tokens = []
        self.sentences = []
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
                self.add_token(token)
                tokens.append(token)
            parsed_sentence = ParsedSentence(sentence.text, tokens)
            self.add_sentence(parsed_sentence)

    def add_sentence(self, parsed_sentence):
        self.sentences.append(parsed_sentence)

    def add_token(self, token):
        self.tokens.append(token)

class ParsedSentence:
    def __init__(self, sentence_text, tokens):
        self.text = sentence_text
        self.tokens = tokens
