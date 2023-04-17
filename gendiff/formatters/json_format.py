import json
from gendiff.formatters.normalize import normalize_values


def format(diff: dict) -> str:
    diff = normalize_values(diff)
    return json.dumps(diff, indent=4)
