# import llm_clients
import argparse
import os
from configparser import ConfigParser

import processor


def main():

    parser = argparse.ArgumentParser(description="Automatically organise your files")

    parser.add_argument(
        "source_directory",
        nargs="?",
        default=os.getcwd(),
        help="The directory containing the files to be organised (defaults to current directory)",
    )

    parser.add_argument(
        "target_directory",
        help="The target parent directory where organised files should be placed",
    )

    parser.add_argument(
        "organisation parameters",
        nargs="?",
        default="config.txt",  # don't know if this will remain a txt file, might change
        help="File containing the parameters for how sorting should be handled, where files go and how it's determined",
    )

    parser.add_argument(
        "LLM use",
        nargs="?",
        choices=[0, "gemini", "ollama"],
        default=0,  # no LLM will be used by default
        help="Should LLMs be allowed (default no). gemini or ollama may be used",
    )

    args = parser.parse_args()

    source = args.source_directory
    target = args.target_directory


if __name__ == "__main__":
    main()
