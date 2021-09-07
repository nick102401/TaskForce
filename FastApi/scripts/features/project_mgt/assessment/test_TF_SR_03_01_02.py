#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TF_SR_03_01_02.py
@time:2021/09/03
*/

测试对不同成员赠送小红花累计数量大于指定数量，系统能够正确处理
"""

import allure
import pytest

from FastApi.aws.project import Personnel, Project
from FastApi.common.logs_handle import Logger
from FastApi.conf import env

log = Logger().logger

# 项目初始化
project = Project()


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    '''


@pytest.mark.xfail()
@pytest.mark.usefixtures('init_project_and_member')
@allure.feature('我的项目')
@allure.story('综评')
@allure.title('对不同成员赠送小红花累计数量大于指定数量')
def test_step(init_project_and_member):
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1、对一项目成员赠送20个小红花
    2、对另一项目成员赠送31个小红花

    预期结果
    1、赠送成功
    2、前30个小红花赠送成功，最后一个小红花赠送失败，提示小红花数量超限制
    '''

    global projectName
    projectName = init_project_and_member
    global person
    person = Personnel(projectName)

    # 对一项目成员赠送20个小红花
    for i in range(20):
        resp = person.give_red_flower(memberName=env.USERNAME_PG)
        assert resp['retCode'] == 200
        assert resp['content']['msg'] == 'success'

    # 对另一项目成员先赠送30个小红花
    for i in range(30):
        resp = person.give_red_flower(memberName=env.USERNAME_RD)
        assert resp['retCode'] == 200
        assert resp['content']['msg'] == 'success'

    # 再赠送1个小红花
    resp = person.give_red_flower(memberName=env.USERNAME_RD)
    assert resp['content']['code'] == -1


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        # 完结项目
        person.delete_member(del_userName=env.USERNAME_RD)
        person.delete_member(del_userName=env.USERNAME_PG)
        project.disable_or_archive_project(projectName, operationType='archive', userName=env.USERNAME_PM)
    except Exception as ex:
        log.info('环境清理失败')
        log.info(ex)