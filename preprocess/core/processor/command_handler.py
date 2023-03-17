import sys
import argparse
from preprocess.core.processor import processing


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", type=str, required=True)
    parser.add_argument("--language", type=str, required=True)
    parser.add_argument("--text", type=str, required=True)
    args = parser.parse_args()
    return args


def process_command():
    args = create_arg_parser()
    processing.full_processing(args.language, args.text)
