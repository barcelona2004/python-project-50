from gendiff.tree import get_diff
from gendiff.parser import get_data
from gendiff.formatters.formatt import formatt
import os


def kost(path: str) -> str:
    new_path = path.split('/')
    new_string = ''
    count = 0
    for i in new_path:
        if i != "scripts":
            if i == "gendiff":
                if count < 1:
                    new_string += f"{i}/"
                    count += 1
            else:
                new_string += f"{i}/"
    return new_string[:-1]


def generate_diff(file_path1: str, file_path2: str, format_name="stylish"):
    file_path1_abs = kost(os.path.abspath(file_path1))
    file_path2_abs = kost(os.path.abspath(file_path2))
    file1 = get_data(file_path1_abs)
    file2 = get_data(file_path2_abs)
    result = get_diff(file1, file2)
    return formatt(result, format_name)
