import json


def create_dicts(file1, file2):
    dict_minus = {}
    dict_plus = {}
    dict_ = {}
    for key in file1.keys():
        if key not in file2.keys():
            dict_minus[key + '-'] = file1[key]
        else:
            if file1[key] == file2[key]:
                dict_[key] = file1[key]
            else:
                dict_minus[key + '-'] = file1[key]
                dict_plus[key + '+'] = file2[key]
    for key in file2.keys():
        if key not in file1.keys():
            dict_plus[key + '+'] = file2[key]
    return {**dict_minus, **dict_plus, **dict_}


def sort_dicts(dictionary):
    line = '{\n'
    sort_dict = sorted(dictionary)
    for i in range(len(sort_dict) - 1):
        if sort_dict[i][:-1] == sort_dict[i - 1][:-1]:
            sort_dict[i], sort_dict[i - 1] = sort_dict[i - 1], sort_dict[i]
    for i in sort_dict:
        if i[-1] != '-' and i[-1] != '+':
            line += f" {i}: {dictionary[i]}\n"
        else:
            line += f"{i[-1]}{i[:-1]}: {dictionary[i]}\n"
    return line


def generate_diff(file_path1, file_path2):
    dictionary = {}
    file1 = json.load(open(f"{file_path1}"))
    file2 = json.load(open(f"{file_path2}"))
    dictionary = create_dicts(file1, file2)
    line = sort_dicts(dictionary)
    print(line + '}')
    return line + '}'
