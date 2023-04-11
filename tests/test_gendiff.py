from gendiff import generate_diff

def test_generate_diff():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == '{\n-host: 1\n+host: 2\n}'


def test_generate_diff_is_string():
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert type(result) == str

def test_gendiff_order():
    result = generate_diff('tests/fixtures/file3.json', 'tests/fixtures/file4.json')
    assert result == '{\n-follow: False\n host: hexlet.io\n-proxy: 123.234.53.22\n-timeout: 50\n'\
                     '+timeout: 20\n+verbose: True\n}'