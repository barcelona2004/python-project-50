import pytest
from gendiff import generate_diff

def test_generate_diff():
    assert generate_diff('tests/test_file1.json', 'tests/test_file2.json') == '{\n-host: 1\n+host: 2\n}'
