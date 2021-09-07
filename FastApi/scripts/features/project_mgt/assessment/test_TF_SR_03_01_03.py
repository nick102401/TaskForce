#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TF_SR_03_01_03.py
@time:2021/09/03
*/

测试某项目赠送小红花数量达到限制后，对其他项目赠送小红花能够成功赠送
"""

import allure
import pytest

from FastApi.aws.project import Personnel, Project
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger
from FastApi.conf import env

log = Logger().logger

# 生成随机字符串
randomStr = get_random_str(6)

# 项目初始化
project = Project()


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    1、项目经理登录账号
    2、该项目经理同时为多个项目的项目经理
    3、该项目经理A项目赠送小红花数量达到指定数量
    4、该项目经理B项目赠送小红花数量小于指定数量
    '''


@pytest.mark.usefixtures('init_project_and_member_1')
@pytest.mark.usefixtures('init_project_and_member')
@allure.feature('我的项目')
@allure.story('综评')
@allure.title('赠送小红花数量达到限制后，对其他项目赠送小红花能够成功赠送')
def test_step(init_project_and_member, init_project_and_member_1):
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.对B项目赠送小红花，赠送数量小于剩余可赠送小红花数量

    预期结果
    1.赠送成功
    '''

    global projectName, projectName1
    projectName = init_project_and_member
    projectName1 = init_project_and_member_1
    global person, person1
    person = Personnel(projectName)
    person1 = Personnel(projectName1)

    # A项目赠送小红花已达上限
    for i in range(50):
        resp = person.give_red_flower(memberName=env.USERNAME_PG)
        assert resp['retCode'] == 200
        assert resp['content']['msg'] == 'success'

    # 对B项目赠送小红花，赠送数量小于剩余可赠送小红花数量
    resp = person1.give_red_flower(memberName=env.USERNAME_PG)
    assert resp['content']['code'] == 0
    assert resp['content']['msg'] == 'success'


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        # 完结项目
        person1.delete_member(del_userName=env.USERNAME_RD)
        person1.delete_member(del_userName=env.USERNAME_PG)
        project.disable_or_archive_project(projectName1, operationType='archive', userName=env.USERNAME_PM)
    except Exception as ex:
        log.info('环境清理失败')
        log.info(ex)
    try:
        # 完结项目
        person.delete_member(del_userName=env.USERNAME_RD)
        person.delete_member(del_userName=env.USERNAME_PG)
        project.disable_or_archive_project(projectName, operationType='archive', userName=env.USERNAME_PM)
    except Exception as ex:
        log.info('环境清理失败')
        log.info(ex)
