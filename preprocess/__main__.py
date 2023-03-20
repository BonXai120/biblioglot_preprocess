import constants as c
import ijson
from collections import defaultdict
from preprocess.core.processor import processing as p
import preprocess.utils.dir_handler as dh

def main(task, language, text_path):
    if task in {"story", "definition", "translation", "audio"}:
        if not dh.package_dir_exists():
            dh.create_package_dir()
    if task in {"story", "definition", "translation"}:
        if not dh.json_dir_exists():
            dh.create_json_dir()

    if task == "story":
        p.story_processing(language, text_path)
    elif task == "definition":
        c.init_dictionary(language)
        p.definition_processing(language, text_path)
    elif task == "translation":
        p.translation_processing(language, text_path)

    
