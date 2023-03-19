from preprocess.utils import file_handler as fr
from preprocess.nlp import parse_text as Parser
from preprocess.database.json import construct_story_json as csj
import json
from preprocess.nlp import definition as d
import preprocess.database.mongo.operations as mongo

def story_processing(language, text_path):
    raw_text = fr.read_file(text_path)
    clean_text = clean_raw_text(raw_text)
    parsed_text = Parser.ParsedText(language, clean_text)
    json_document = csj.construct_json_document(parsed_text, language)
    fr.write_file("tests/test.json", json_document)

def definition_processing(language, file_path):

    with open(file_path, "r") as fp:
        story = json.load(fp)
        word_load = d.get_definitions(story)
        found_words = word_load.found_words
        unfound_words = word_load.unfound_words
        print(unfound_words)
        found_db = mongo.get_database("dictionary")
        for i in found_words:
            mongo.insert_many(found_words[i], found_db, language)
        unfound_db = mongo.get_database("unfound")
        mongo.insert_many(unfound_words, unfound_db, language)

def clean_raw_text(raw_text):
    stripped_text = raw_text.replace("\n", " ")
    stripped_text = stripped_text.replace("--", " ")
    return stripped_text
