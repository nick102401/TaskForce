#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TF_SR_01_01_01.py
@time:2021/08/23
*/

管理员账号查看用户查询模块
"""

import allure

from FastApi.aws.system_function import User
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger
from FastApi.conf import env

log = Logger().logger

# 生成随机字符串
randomStr = get_random_str(6)

user = User()


def setup():
    log.info('-----测试用例预制-----')
    '''
    预置条件
    1.使用管理员账号登录项目考核系统
    '''


@allure.feature('系统功能')
@allure.story('用户查询')
@allure.title('管理员账号查看用户查询模块')
def test_step():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.点击用户查询模块

    预期结果
    1.仅管理员账号可以正常使用用户查询模块
    2.列表展示系统内所有的用户姓名等用户基本信息
    '''

    resp = user.get_user_info(username=env.USERNAME, password=env.PASSWORD)
    assert resp['retCode'] == 200
    assert resp['content']['data']['list'] != []


def teardown():
    log.info('-----环境操作-----')
