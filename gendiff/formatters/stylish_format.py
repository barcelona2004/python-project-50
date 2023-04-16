# from gendiff.formatters.normalize import normalize_values
#
# STATUS = {"unchanged": " ", "added": "+ ", "removed": "- "}
#
#
# def stringify_value(value, depth: int) -> str:
#     if not isinstance(value, dict):
#         return value
#     hold = ["{"]
#     for key, val in value.items():
#         hold.append(f"\n{'  ' * depth}  {key}: {stringify_value(val, depth + 2)}")
#     hold.append(f"\n{'  ' * (depth - 1)}}}")
#     return ''.join(hold)
#
#
# def stringify_diff(diff: dict, depth=1) -> str:
#     lst = []
#     for key, val in diff.items():
#         status = val['status']
#         if status == "nested":
#             lst.append(f"{' ' * depth} {key}: {{\n")
#             lst.append(f"{stringify_diff(val['value'], depth + 2)}")
#             lst.append(f"{'  ' * (depth + 1)}}}\n")
#         elif status == 'changed':
#             lst.append(f"{'  ' * depth}- {key}: "
#                        f"{stringify_value(val['old_value'], depth + 2)}\n")
#             lst.append(f"{'  ' * depth}+ {key}: "
#                        f"{stringify_value(val['new_value'], depth + 2)}\n")
#         else:
#             lst.append(f"{'  ' * depth}{STATUS[status]}{key}: "
#                        f"{stringify_value(val['value'], depth + 2)}\n")
#         result = ''.join(lst)
#         return result
#
#
# def format(diff: dict) -> str:
#     diff = normalize_values(diff)
#     return stringify_diff(diff)
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


def formatting(diff: dict) -> str:
    diff = normalize_values(diff)
    return f"{{\n{stringify_diff(diff)}}}"
