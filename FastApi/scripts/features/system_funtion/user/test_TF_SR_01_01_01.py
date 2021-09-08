#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TF_SR_01_01_01.py
@time:2021/08/23
*/

01:管理员账号查看用户查询模块
02:非管理员账号查看用户查询模块
03:管理员通过用户姓名查询系统用户
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


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    1.使用管理员账号登录项目考核系统
    2.使用非管理员账号登录项目考核系统
    '''


@allure.feature('系统功能')
@allure.story('用户查询')
@allure.title('管理员账号查看用户查询模块')
def test_step_01():
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


@allure.feature('系统功能')
@allure.story('用户查询')
@allure.title('非管理员账号查看用户查询模块')
def test_step_02():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.点击用户查询模块

    预期结果
    1.仅管理员账号可以正常使用用户查询模块，非管理员账号隐藏该模块
    '''

    # 校验PM角色
    resp = user.get_user_info(username=env.USERNAME_PM, password=env.USER_PWD)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == '非管理员不能查看用户列表'

    # 校验PMO角色
    resp = user.get_user_info(username=env.USERNAME_PMO, password=env.USER_PWD)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == '非管理员不能查看用户列表'


@allure.feature('系统功能')
@allure.story('用户查询')
@allure.title('管理员通过用户姓名查询系统用户')
def test_step_03():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.点击用户查询模块
    2.输入要查询的用户姓名
    
    预期结果
    1.可展示要查询的用户基本信息列表
    '''
    resp = user.get_user_info(searchKey=env.USERNAME_RD, username=env.USERNAME, password=env.PASSWORD)
    assert resp['retCode'] == 200
    assert resp['content']['data']['list'][0]['operatorNo'] == env.USERNAME_RD


def teardown_module(module):
    log.info('-----清理环境操作-----')
