from preprocess.database.json import Json_Object as j
import json
from preprocess.nlp import translation as t
from preprocess.nlp import definition as d

def construct_json_document(parsedText, language=""):
    json_object = construct_json_collection(parsedText, language)
    json_document = json_object.toJSON()
    return json_document

def construct_json_sentence(sentence, language="", id=0):
    token_index = 0
    token_list = []
    for token in sentence.tokens:
        token_list.append(construct_json_token(token, language, token_index)) 
        token_index += 1
    sentence_json_object = j.SentenceFullData(text=sentence.text, tokens=token_list, id=id)
    return sentence_json_object

def construct_json_token(token, language="", id=0):
    word_index = 0
    word_list = []
    for word in token.words:
        word_list.append(construct_json_word(word, language, word_index))
        word_index += 1
    
    token_json_object = j.TokenFullData(text=token.text, words=word_list, id=id)
    return token_json_object

def construct_json_word(word, language="", id=0):
    word_json_object = j.WordFullData(text=word.text, lemma=word.lemma, upos=word.upos, id=id)
    return word_json_object

def construct_json_collection(parsedText, language=""):
    sentence_index = 0
    text_collection = j.JsonObjectCollection()
    for sentence in parsedText.sentences:
        text_collection.collection.append((construct_json_sentence(sentence, language, sentence_index)))
        sentence_index += 1
    
    return text_collection
