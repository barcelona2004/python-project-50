from gendiff.generate_diff import generate_diff

def test_generate_diff():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == '{\n-host: 1\n+host: 2\n}'
