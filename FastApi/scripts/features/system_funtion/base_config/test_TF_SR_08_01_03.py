#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:CAT
@file:test_TF_SR_08_01_01.py
@time:2021/08/24
*/

测试新增考核项，能够成功新增
"""

import allure

from FastApi.aws.system_function import BaseConfig
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger

log = Logger().logger

# 生成随机字符串
randomStr = get_random_str(6)

# pro = Project()
# person = Personnel(projectName=projectName, userName=env.USERNAME_PM)
base = BaseConfig()


def setup():
    log.info('-----测试用例预制-----')


@allure.feature('基础配置')
@allure.story('合格项点配置')
@allure.title('查看合格项点')
def test_step():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
        "1.进入添加合格项页面
       

    预期结果
         1.合格项查看成功

    '''
    resp = base.query_pass_item


def teardown():
    log.info('-----环境操作-----')
