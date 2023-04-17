from gendiff.formatters.normalize import normalize_values

STATUS = {
        'unchanged': "  ",
        'added': "+ ",
        'removed': "- "
    }
def stringify_val(value, depth: int) -> str:
    if not isinstance(value, dict):
        return value
    hold = ["{"]
    for k, v in value.items():
        hold.append(f"\n{'  ' * depth}  {k}: {stringify_val(v, depth + 2)}")
    hold.append(f"\n{'  ' * (depth - 1)}}}")
    return ''.join(hold)


def stringify_diff(diff: dict, depth=1) -> str:
    lst = []
    for k, v in diff.items():
        status = v['status']
        if status == 'nested':
            lst.append(f"{'  ' * depth}  {k}: {{\n")
            lst.append(f"{stringify_diff(v['value'], depth + 2)}")
            lst.append(f"{'  ' * (depth + 1)}}}\n")
        elif status == 'changed':
            lst.append(f"{'  ' * depth}- {k}: "
                       f"{stringify_val(v['old'], depth + 2)}\n")
            lst.append(f"{'  ' * depth}+ {k}: "
                       f"{stringify_val(v['new'], depth + 2)}\n")
        else:
            lst.append(f"{'  ' * depth}{STATUS[status]}{k}: "
                       f"{stringify_val(v['value'], depth + 2)}\n")
    res = ''.join(lst)
    return res


def format(diff: dict) -> str:
    diff = normalize_values(diff)
    return f"{{\n{stringify_diff(diff)}}}"
