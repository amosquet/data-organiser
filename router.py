import json
import re
from pathlib import Path


# Load the regex mapping from the JSON configuration file.
def load_config(config_path: Path) -> dict:

    if not config_path.exists():
        print(f"Error: Configuration file not found at {config_path}")
        return {}

    try:
        raw_json_string = config_path.read_text(encoding="utf-8")

        rules_dictionary = json.loads(raw_json_string)
        return rules_dictionary

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON configuration: {e}")
        return {}


# Evaluate any string (filename or extracted text) against the rules.
def regex_categorise(target_string: str, rules: dict) -> str | None:
    if not target_string:
        return None

    for folder, patterns in rules.items():
        for pattern in patterns:
            if re.search(pattern, target_string, re.IGNORECASE):
                return folder
    return None
