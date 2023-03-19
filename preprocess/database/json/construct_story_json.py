from preprocess.database.json import Json_Object as j
import json
from preprocess.nlp import translation as t
from preprocess.nlp import definition as d
from uuid import uuid4

def construct_json_document(parsedText, language=""):
    json_object = construct_json_collection(parsedText, language)
    json_document = json_object.toJSON()
    return json_document

def construct_json_sentence(sentence, language="", place_id=0):
    token_list = []
    for token in sentence.tokens:
        token_list.append(construct_json_token(token, language)) 
    sentence_json_object = j.SentenceFullData(text=sentence.text, tokens=token_list, uuid=str(uuid4()), index=place_id)
    return sentence_json_object

def construct_json_token(token, language=""):
    word_list = []
    for word in token.words:
        word_list.append(construct_json_word(word, language))

    token_json_object = j.TokenFullData(text=token.text, words=word_list)
    return token_json_object

def construct_json_word(word, language=""):
    word_json_object = j.WordFullData(text=word.text, lemma=word.lemma, upos=word.upos)
    return word_json_object

def construct_json_collection(parsedText, language=""):
    place_id = 0
    text_collection = j.JsonObjectCollection()
    for sentence in parsedText.sentences_objects:
        text_collection.collection.append(construct_json_sentence(sentence, language, place_id))
        place_id += 1
    
    return text_collection
