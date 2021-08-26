import os

import yaml

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_data_from_file(file_path):
    """
    读取yaml文件的内容
    :param file_path
    """

    if '/' in file_path:
        f = open(os.path.join(project_path, file_path), encoding='utf-8')
    else:
        f = open(os.path.join(project_path, 'data/' + file_path), encoding='utf-8')
    res_json = yaml.load(f, Loader=yaml.FullLoader)  # 添加loader参数是为了去掉load warning
    return res_json


def read_data_from_file_to_params(file_path, case_name=None, index=None):
    res_json = read_data_from_file(file_path)
    if isinstance(res_json, dict) and case_name:
        res_json = res_json[case_name]
    res_list = []
    if index is not None:
        if isinstance(index, str) and '-' in index:
            startIdx, endIdx = index.split('-')
            startIdx = int(startIdx)
            endIdx = int(endIdx) + 1
            for one in res_json[startIdx:endIdx]:
                data = []
                for k, v in one.items():
                    data.append(v)
                res_list.append(data)
        else:
            if isinstance(index, str):
                index = int(index)
            data = []
            for k, v in res_json[index].items():
                data.append(v)
            res_list.append(data)
    else:
        for i in range(len(res_json)):
            data = []
            for k, v in res_json[i].items():
                data.append(v)
            res_list.append(data)
    return res_list


def get_field_name(file_path, case_name, filed_name):
    res_json = read_data_from_file(file_path)
    if isinstance(res_json, dict) and case_name:
        res_json = res_json[case_name]
    res_list = []
    for one in res_json:
        res_list.append(one[filed_name])
    return res_list


if __name__ == '__main__':
    pass
    print(read_data_from_file_to_params("recruitment_data.yaml", case_name='recruitment_data', index=1))
