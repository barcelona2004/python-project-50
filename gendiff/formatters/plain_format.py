from gendiff.formatters.normalize import normalize_values


def string(data):
    if isinstance(data, (tuple, dict, list, set)):
        return '[complex value]'
    elif data in ('null', 'true', 'false'):
        return data
    else:
        return f"'{data}'"


STRING = {
    'unchanged': '',
    'removed': "Property '{path}' was removed",
    'added': "Property '{path}' was added with value: '{v}'",
    'changed': "Property '{path}' was updated. From '{old_v}' to '{new_v}'"
}


def plain_diff(diff: dict, parent='') -> list:
    lst = []
    if parent == '':
        parent = []
    for key, val in diff.items():
        status = val['status']
        parent.append(str(key))
        path = '.'.join(parent)
        if status == 'nested':
            lst.extend(plain_diff(val['value'], parent))
            parent = parent[:-1]
        else:
            v = string(val.get('value'))
            old_v = string(val.get('old'))
            new_v = string(val.get('new'))
            lst.append(STRING.get(status).format(
                path=path,
                v=v,
                old_v=old_v,
                new_v=new_v))
        parent = parent[:-1]
    return lst


def format(diff: dict) -> str:
    diff = normalize_values(diff)
    diff = plain_diff(diff)
    return '\n'.join(filter(lambda x: x != '', diff))
