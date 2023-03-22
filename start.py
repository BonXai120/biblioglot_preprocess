from preprocess.__main__ import main as m
import sys
import argparse


def create_arg_parser():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="task")
    parser_story = subparsers.add_parser("story")
    parser_story.add_argument("--language", type=str, required=True)
    parser_story.add_argument("--text", type=str, required=True)

    parser_definition = subparsers.add_parser("definition")
    parser_definition.add_argument("--language", type=str, required=True)
    parser_definition.add_argument("--text", type=str, required=False)

    parser_translation = subparsers.add_parser("translation")
    parser_translation.add_argument("--language", type=str, required=True)
    parser_translation.add_argument("--text", type=str, required=False)

    parser_audio = subparsers.add_parser("audio")
    parser_audio.add_argument("--language", type=str, required=True)
    parser_audio.add_argument("--text", type=str, required=True)
    parser_audio.add_argument("--name", type=str, required=True)

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = create_arg_parser()
    if args.task in {"story", "definition", "translation"}:
        m(task=args.task, language=args.language, text_path=args.text)
    elif args.task in {"audio"}:
        m(task=args.task, language=args.language, text_path=args.text, name=args.name)

    