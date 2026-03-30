import argparse
import os
from pathlib import Path

import sorter


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
        "organisation_parameters",
        nargs="?",
        default="config.json",  # don't know if this will remain a txt file, might change
        help="File containing the parameters for sorting, where files go and how it's determined (defaults to config.json)",
    )

    parser.add_argument(
        "LLM",
        nargs="?",
        choices=[0, "gemini", "ollama"],
        default=0,  # no LLM will be used by default
        help="Should LLMs be allowed (default no). gemini or ollama may be used",
    )

    args = parser.parse_args()

    source = Path(args.source_directory)
    target = Path(args.target_directory)
    config = Path(args.organisation_parameters)
    llm = args.LLM

    sorter.sort(source, target, config, llm)


if __name__ == "__main__":
    main()
