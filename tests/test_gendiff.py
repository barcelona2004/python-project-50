from gendiff import generate_diff


def test_generate_diff():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == '{\n  - host: 1\n  + host: 2\n}'


def test_generate_diff_is_string():
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert type(result) == str


def test_gendiff_order():
    result = generate_diff('tests/fixtures/file3.json', 'tests/fixtures/file4.json')
    assert result == '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n ' \
                     ' + timeout: 20\n  + verbose: true\n}'


def test_gendiff_for_yaml():
    result = generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml')
    assert result == '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n' \
                     '  + timeout: 20\n  + verbose: true\n}'


def test_gendiff_for_yamlstr():
    result = generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml')
    assert type(result) == str


def test_recursion():
    result = generate_diff('tests/fixtures/file5.json', 'tests/fixtures/file6.json')
    assert result == "{\n    follow: {\n      - count: 6\n      + count: 5\n    }\n" \
                     "host: hexlet.io\n  - proxy: 123.234.53.22\n" \
                     "  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}"


def test_plain():
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', "plain")
    assert result == "Property 'host' was updated. From '1' to '2'"
