import json
import yaml
import os


def get_data(file_path: str) -> dict:
    f = open(file_path)
    _, extension = os.path.splitext(file_path)
    if extension == '.json':
        return json.load(f)
    elif extension == '.yaml' or extension == '.yml':
        return yaml.safe_load(f)[0]
    else:
        raise ValueError(f"Wrong extension {extension}")
