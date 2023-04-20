import os.path
from collections import OrderedDict


def append_keys(from_, to, const, status):
    for key in from_:
        to[key] = {'status': status, 'value': const[key]}


def get_diff(old_dict: dict, new_dict: dict) -> OrderedDict:
    gen_dict = {}
    only_old_keys = set(old_dict.keys()) - set(new_dict.keys())
    only_new_keys = set(new_dict.keys()) - set(old_dict.keys())
    both_keys = old_dict.keys() & new_dict.keys()
    append_keys(only_old_keys, gen_dict, old_dict, "removed")
    append_keys(only_new_keys, gen_dict, new_dict, "added")

    for key in both_keys:
        old_value = old_dict[key]
        new_value = new_dict[key]
        if isinstance(old_value, dict) and isinstance(new_value, dict):
            gen_dict[key] = {'status': 'nested',
                             'value': get_diff(old_value, new_value)}
        elif old_value == new_value:
            gen_dict[key] = {'status': 'unchanged', 'value': old_value}
        elif old_value != new_value:
            gen_dict[key] = {'status': 'changed',
                             'old': old_value, 'new': new_value}

    return OrderedDict(sorted(gen_dict.items()))
