import json

def generate_diff(file_path1, file_path2):
    dict_minus = {}
    dict_plus = {}
    dict_ = {}
    dictionary = {}
    file1 = json.load(open(f"{file_path1}"))
    file2 = json.load(open(f"{file_path2}"))
    for key in file1.keys():
        if key not in file2.keys():
            dict_minus[key+'-'] = file1[key]
        else:
            if file1[key] == file2[key]:
                dict_[key] = file1[key]
            else:
                dict_minus[key + '-'] = file1[key]
                dict_plus[key+'+'] = file2[key]
    for key in file2.keys():
        if key not in file1.keys():
            dict_plus[key+'+'] = file2[key]
    dictionary = {**dict_minus, **dict_plus, **dict_}
    line = '{\n'
    sort_dict = sorted(dictionary)
    for i in range(len(sort_dict) - 1):
        if sort_dict[i][:-1] == sort_dict[i-1][:-1]:
            sort_dict[i], sort_dict[i-1] = sort_dict[i-1], sort_dict[i]
    for i in sort_dict:
        if i[-1] != '-' and i[-1] != '+':
            line += f" {i}: {dictionary[i]}\n"
        else:
            line += f"{i[-1]}{i[:-1]}: {dictionary[i]}\n"
    print(line+'}')
    return line+'}'
