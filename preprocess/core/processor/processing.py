from preprocess.utils import file_handler as fr
from preprocess.nlp import parse_text as Parser
from preprocess.database.json import construct_story_json as csj
import json

def story_processing(language, text_path):
    raw_text = fr.read_file(text_path)
    clean_text = clean_raw_text(raw_text)
    parsed_text = Parser.ParsedText(language, clean_text)
    json_document = csj.construct_json_document(parsed_text, language)
    fr.write_file("tests/test.json", json_document)

def definition_processing(language, text_path):
    raw_text = fr.read_file(text_path)
    clean_text = clean_raw_text(raw_text)
    parsed_text = Parser.ParsedText(language, text_path)

def clean_raw_text(raw_text):
    stripped_text = raw_text.replace("\n", " ")
    stripped_text = stripped_text.replace("--", " ")
    return stripped_text
