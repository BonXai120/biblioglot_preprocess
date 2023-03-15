from preprocess.utils import file_handler as fr
from preprocess.nlp import parse_text as Parser
from preprocess.database.json import construct_json_file as cjf

def text_processing(language, text_path):
    raw_text = fr.read_file(text_path)
    clean_text = clean_raw_text(raw_text)
    parsed_text = Parser.ParsedText(language, clean_text)
    json_document = cjf.construct_json_document(parsed_text)

def clean_raw_text(raw_text):
    stripped_text = raw_text.replace("\n\n", " (PARAGRAPH_END). ")
    stripped_text = stripped_text.replace("\n", " ")
    return stripped_text
    