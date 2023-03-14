import sys


def read_file(text_path):
    try:
        with open(text_path, encoding="UTF-8") as text:
            full_text = text.read()
            return full_text
    except (FileNotFoundError, TypeError) as error:
        if error == FileNotFoundError:
            print("ERROR: File was not found ")
            sys.exit(1)
        elif error == TypeError:
            print("ERROR: Invalid file path type")
            sys.exit(1)

def write_file(file_path, write_text):
    try:
        with open(file_path, mode="a+", encoding="UTF-8") as file:
            file.write(write_text)
    except () as error:
        print(error)




