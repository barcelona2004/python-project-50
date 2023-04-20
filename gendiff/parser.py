import json
import yaml
import os
from yaml.loader import SafeLoader


def get_data(path: str) -> dict:
    _, extension = os.path.splitext(path)
    if extension == '.json':
        with open(path) as f:
            data = json.load(f)
            return data
    elif extension == '.yaml' or extension == '.yml':
        with open(path) as f:
            data = yaml.load(f, Loader=SafeLoader)
            return data[0]
    else:
        raise ValueError(f"Wrong extenssion {extension}")
