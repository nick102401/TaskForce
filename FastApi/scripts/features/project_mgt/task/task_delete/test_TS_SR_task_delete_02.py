#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TS_SR_task_delete_02.py
@time:2021/08/23
*/

删除已分配执行中的任务/子任务:
01:删除已分配执行中的任务
02:删除已分配执行中的子任务
"""
import json

import allure

from FastApi.aws.project import Task
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName

log = Logger().logger

# 自定义参数
taskName = 'TS_SR_task_delete_02_1' + get_random_str(2)
subtaskName = 'TS_SR_task_delete_02_2' + get_random_str(2)

# 初始化
task = Task(projectName, userName=env.USERNAME_PM)


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    1.存在已分配执行中的任务和子任务
    '''

    # 创建任务
    resp = task.create_task(taskName=taskName,
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 创建子任务
    resp = task.create_task(taskName=subtaskName,
                            broTaskName=taskName,
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('删除已分配执行中的任务')
def test_step_01():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.PM用户登录
    2.删除已分配执行中的任务,有预期结果1

    预期结果
    1.任务删除成功
    '''

    # 领取任务
    resp = task.get_task(taskName=taskName, userName=env.USERNAME_PM)
    assert resp['retCode'] == 200

    resp = task.query_tasks(assign=1)
    assert taskName in json.dumps(resp['content'])

    # 删除任务
    resp = task.delete_task(taskName=taskName, assign=1)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    resp = task.query_tasks(assign=1)
    assert taskName not in json.dumps(resp['content'])


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('删除已分配执行中的子任务')
def test_step_02():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.PM用户登录
    2.删除已分配执行中的子任务,有预期结果1

    预期结果
    1.子任务删除成功
    '''

    # 领取任务
    resp = task.get_task(taskName=subtaskName, userName=env.USERNAME_PM)
    assert resp['retCode'] == 200

    resp = task.query_tasks(assign=1)
    assert subtaskName in json.dumps(resp['content'])

    # 删除任务
    resp = task.delete_task(taskName=subtaskName, assign=1)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    resp = task.query_tasks(assign=1)
    assert subtaskName not in json.dumps(resp['content'])


def teardown_module(module):
    log.info('-----环境操作-----')
