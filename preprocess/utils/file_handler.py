import sys


def read_file(text_path):
    try:
        with open(text_path, encoding="UTF-8") as text:
            full_text = text.read()
            return full_text
    except () as error:
        print(error)


def write_file(file_path="file.txt", write_text=""):
    try:
        with open(file_path, mode="w+", encoding="UTF-8") as file:
            file.write(write_text)
    except () as error:
        print(error)




