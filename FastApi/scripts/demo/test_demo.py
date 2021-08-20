#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_demo.py
@time:2021/08/19
*/

用例标题/描述
"""

import allure
import yaml

from FastApi.common.excel_handle import Excel
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger

excel = Excel('interface.xlsx', data='Sheet')
log = Logger().logger

# 生成随机字符串
randomStr = get_random_str(6)


def setup():
    log.info('-----这是测试用例预制步骤-----')
    yaml.load()
    global dataList
    dataList = excel.read_date()


@allure.feature('特性名称')
@allure.story('需求名称')
@allure.title('用例名称')
def test_step():
    log.info('-----这是测试用例执行步骤-----')
    for data in dataList:
        print(data)


def teardown():
    log.info('-----这是测试用例清理环境操作-----')
