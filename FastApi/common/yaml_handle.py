import os

import yaml


def read_data_from_file(file_name):
    """
    读取yaml文件的内容
    :param file_name
    """
    dataPath = os.path.abspath(__file__).split('FastApi')[0]
    f = open(dataPath + 'FastApi/conf/' + file_name, encoding='utf-8')
    res_json = yaml.load(f, Loader=yaml.FullLoader)  # 添加loader参数是为了去掉load warning
    return res_json


if __name__ == '__main__':
    pass
    print(read_data_from_file('interface'))
