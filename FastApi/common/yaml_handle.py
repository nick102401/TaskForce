import os

import yaml

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_data_from_file(file_path):
    """
    读取yaml文件的内容
    :param file_path: data目录下文件名称或FastApi目录下相对路径
    :return:
    """
    if '/' in file_path:
        f = open(os.path.join(project_path, file_path), encoding='utf-8')
    else:
        file_name = file_path
        # 遍历data目录下文件获取路径
        for root, dirs, files in os.walk(os.path.join(project_path, 'data')):
            if file_name in files:
                file_path = root + '/' + file_name
                break
        else:
            file_path = os.path.join(project_path, 'data/' + file_name)
        f = open(file_path, encoding='utf-8')
    res_json = yaml.load(f, Loader=yaml.FullLoader)  # 添加loader参数是为了去掉load warning
    return res_json


def read_data_from_file_to_params(file_path, case_name=None, index=None):
    """
    读取yaml文件
    :param file_path: 文件名称或路径
    :param case_name: case_name
    :param index: 索引
    :return: 列表格式
    """
    res_json = read_data_from_file(file_path)
    if isinstance(res_json, dict) and case_name:
        res_json = res_json[case_name]
        res_list = []

        if isinstance(index, str) and '-' in index:
            startIdx, endIdx = index.split('-')
            startIdx = int(startIdx)
            endIdx = int(endIdx) + 1
            for one in res_json[startIdx:endIdx]:
                data = []
                for k, v in one.items():
                    data.append(v)
                res_list.append(data)
        elif isinstance(res_json, list) and index:
            res_json = res_json[index]
            data = []
            for k, v in res_json.items():
                data.append(v)
            res_list.append(data)
        elif isinstance(res_json, list) and not index:
            for ele in res_json:
                data = []
                for k, v in ele.items():
                    data.append(v)
                res_list.append(data)
        elif isinstance(res_json, dict):
            data = []
            for k, v in res_json.items():
                data.append(v)
            res_list.append(data)
        return res_list
    else:
        return res_json


def get_field_name(file_path, case_name, filed_name):
    """
    获取属性名称
    :param file_path: 文件名称或路径
    :param case_name: case_name
    :param filed_name: 属性名称
    :return:
    """
    res_json = read_data_from_file(file_path)
    if isinstance(res_json, dict) and case_name:
        res_json = res_json[case_name]
    res_list = []
    for one in res_json:
        res_list.append(one[filed_name])
    return res_list


if __name__ == '__main__':
    pass
    print(read_data_from_file('preset_project_body.yaml'))
    # print(read_data_from_file_to_params("recruitment_data.yaml", case_name='recruitment_data'))
    # print(read_data_from_file_to_params("preset_project_body.yaml", case_name='PRESET_TASK'))
    # res = read_data_from_file('recruitment_data.yaml')['recruitment_data']
    # for one in res:
    #     print(one['roleName'])
    # print(read_data_from_file_to_params('recruitment_data.yaml','recruitment_data'))
    # print(read_data_from_file_to_params("recruitment_data.yaml", case_name='recruitment_data', index=1))
    # print(params)
    # res = get_field_name('recruitment_data.yaml','recruitment_data','roleType')
    # print(res[0])
    # print(read_data_from_file_to_params("recruitment_data.yaml", case_name='recruitment_data_none'))
