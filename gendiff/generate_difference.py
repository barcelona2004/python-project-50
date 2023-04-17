from gendiff.tree import get_diff
from gendiff.parser import get_data
from gendiff.formatters.formatt import formatt


def generate_diff(file_path1: str, file_path2: str, format_name="stylish") -> str:
    file1 = get_data(file_path1)
    file2 = get_data(file_path2)
    result = get_diff(file1, file2)
    return formatt(result, format_name)
