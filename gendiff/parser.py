import json
import yaml
import os


def get_data(path: str) -> dict:
    f = open(path)
    _, extension = os.path.splitext(path)
    if extension == '.json':
        return json.load(f)
    elif extension == '.yaml' or extension == '.yml':
        return yaml.safe_load(f)[0]
    else:
        raise ValueError(f"Wrong extenssion {extension}")
