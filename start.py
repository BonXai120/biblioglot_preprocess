from preprocess.__main__ import main as m
import sys
import argparse


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", type=str, required=True)
    parser.add_argument("--language", type=str, required=True)
    parser.add_argument("--text", type=str, required=True)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = create_arg_parser()
    m(args.task, args.language, args.text)