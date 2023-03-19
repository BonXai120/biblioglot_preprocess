import constants as c
import ijson
from collections import defaultdict
from preprocess.core.processor import processing as p

def main(task, language, text_path):
    if task == "story":
        p.story_processing(language, text_path)
    elif task == "definition":
        c.init_dictionary(language)

    
