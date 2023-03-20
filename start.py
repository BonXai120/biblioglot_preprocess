from preprocess.__main__ import main as m
import sys
import argparse


def create_arg_parser():
    parser = argparse.ArgumentParser()
    # parser.add_argument("--task", type=str, required=True)
    # parser.add_argument("--language", type=str, required=True)
    # parser.add_argument("--text", type=str, required=True)

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

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = create_arg_parser()
    m(args.task, args.language, args.text)