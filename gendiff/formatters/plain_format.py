from gendiff.formatters.normalize import normalize_values

STRING = {
    'unchanged': '',
    'removed': "Property '{path}' was removed",
    'added': "Property '{path}' was added with value: {value}",
    'changed': "Property '{path}' was updated. From {old_val} to {new_val}"
}


def string(data):
    if isinstance(data, (tuple, dict, list, set)):
        return '[complex value]'
    elif data in ('null', 'true', 'false', 0):
        return data
    else:
        return f"'{data}'"


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
            value = string(val.get('value'))
            old_val = string(val.get('old'))
            new_val = string(val.get('new'))
            lst.append(STRING.get(status).format(
                path=path,
                value=value,
                old_val=old_val,
                new_val=new_val))
        parent = parent[:-1]
    return lst


def format(diff: dict) -> str:
    diff = normalize_values(diff)
    diff = plain_diff(diff)
    return '\n'.join(filter(lambda x: x != '', diff))
