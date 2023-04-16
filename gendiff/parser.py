import json
import yaml
import os


def get_data(path: str) -> dict:
    _, extension = os.path.splitext(path)
    if extension == '.json':
        return json.load(open(f'{path}'))
    elif extension == '.yaml' or extension == '.yml':
        return yaml.safe_load(open(f'{path}'))[0]
    else:
        raise ValueError(f"Wrong extension {extension}")
