from preprocess.database.json import Json_Object as j
import json


def construct_json_document(parsedText):
    json_object = construct_json_collection(parsedText)
    json_document = json_object.toJSON()
    return json_document

def construct_json_sentence(sentence):
    token_list = []
    for token in sentence.tokens:
        token_list.append(construct_json_token(token)) 
    sentence_json_object = j.SentenceFullData(text=sentence.text, tokens=token_list)
    return sentence_json_object

def construct_json_token(token):
    word_list = []
    for word in token.words:
        word_list.append(construct_json_word(word))
    
    token_json_object = j.TokenFullData(text=token.text, words=word_list)
    return token_json_object

def construct_json_word(word):
    word_json_object = j.WordFullData(text=word.text, lemma=word.lemma, upos=word.upos)
    return word_json_object

def construct_json_collection(parsedText):
    text_collection = j.SentenceCollection()
    for sentence in parsedText.sentences:
        text_collection.collection.append((construct_json_sentence(sentence)))
    
    return text_collection
