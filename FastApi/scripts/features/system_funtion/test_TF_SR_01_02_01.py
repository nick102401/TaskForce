#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TF_SR_01_02_01.py
@time:2021/08/23
*/

管理员设置用户角色
"""
import json

import allure

from FastApi.aws.user import User
from FastApi.base.base_api import ApiDriver
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger
from FastApi.conf import env

log = Logger().logger

# 生成随机字符串
randomStr = get_random_str(6)

# 临时用户
USER_TEMP = '13200000001'

# 初始化
driver = ApiDriver(USER_TEMP, env.USER_PWD)
user = User()


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    1.使用管理员账号登录项目考核系统
    '''

    # 注册临时用户
    global userId
    driver.register()
    # 获取用户ID
    resp = driver.login()
    userId = json.loads(resp['content'])['data']['item']['userId']


@allure.feature('系统功能')
@allure.story('用户查询')
@allure.title('管理员设置用户角色')
def test_step():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.点击用户查询模块
    2.点击要修改用户后修改角色按钮
    3.选择要修改的角色，点击保存

    预期结果
    1.用户角色可选范围：开发人员、项目经理、职能人员、PMO、EPG、QA、部门主任
    2.该用户角色修改成功
    '''
    global pre_role
    resp = user.get_personal_info(userName=USER_TEMP)
    pre_role = resp['content']['data']['item']['role']

    # 修改用户角色
    user.modify_user_role(userId=userId, role='1,2,3,4,5,6,8')


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        # 恢复用户原角色
        user.modify_user_role(userId=userId, role=pre_role)
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
