from gendiff.tree import get_diff
from gendiff.parser import get_data


def generate_diff(file_path1: str, file_path2: str) -> dict:
    file1 = get_data(file_path1)
    file2 = get_data(file_path2)
    result = get_diff(file1, file2)
    print(result)
    return result
