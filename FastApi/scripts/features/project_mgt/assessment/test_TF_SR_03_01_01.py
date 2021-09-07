#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TF_SR_03_01_01.py
@time:2021/09/03
*/

01:测试小红花赠送累计数量小于指定数量，能够成功赠送
02:测试小红花赠送累计数量等于指定数量，能够成功赠送
03:测试对同一成员赠送小红花数量大于指定数量，系统能够正确处理
"""

import allure
import pytest

from FastApi.aws.project import Personnel, Project, ComprehensiveEvaluation
from FastApi.common.logs_handle import Logger
from FastApi.conf import env

log = Logger().logger

# 项目初始化
project = Project()


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    1.项目经理登录账号
    '''


@pytest.mark.usefixtures('init_project_and_member')
@allure.feature('我的项目')
@allure.story('综评')
@allure.title('小红花赠送累计数量小于指定数量')
def test_step_01(init_project_and_member):
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.对项目成员赠送小红花，赠送数量小于剩余可赠送小红花数量

    预期结果
    1.赠送成功
    '''
    global projectName
    projectName = init_project_and_member
    global person
    person = Personnel(projectName)

    resp = person.give_red_flower(memberName=env.USERNAME_PG)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('我的项目')
@allure.story('综评')
@allure.title('小红花赠送累计数量等于指定数量')
def test_step_02():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.对项目成员赠送小红花，赠送数量等于剩余可赠送小红花数量

    预期结果
    1.赠送成功
    '''

    comprehensiveEvaluation = ComprehensiveEvaluation(projectName)
    resp = comprehensiveEvaluation.query_added_value_report()
    currentTotal = resp['content']['data']['meta']['total']

    for i in range(50 - int(currentTotal)):
        resp = person.give_red_flower(memberName=env.USERNAME_PG)
        assert resp['retCode'] == 200
        assert resp['content']['msg'] == 'success'


@pytest.mark.xfail()
@allure.feature('我的项目')
@allure.story('综评')
@allure.title('小红花赠送累计数量大于指定数量')
def test_step_03():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.对同一项目成员赠送小红花，赠送数量超过50

    预期结果
    1.赠送失败，提示小红花数量超限制
    '''

    # 已对同一项目成员赠送50个
    resp = person.give_red_flower(memberName=env.USERNAME_PG)
    assert resp['content']['code'] == -1
    assert resp['content']['msg'] == 'success'


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
