#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TS_SR_task_delete_03.py
@time:2021/09/02
*/

删除我执行的任务
01:项目管理角色删除我执行的任务
02:非项目管理角色删除我执行的任务
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
taskName1 = 'TS_SR_task_delete_03_1' + get_random_str(2)
taskName2 = 'TS_SR_task_delete_03_2' + get_random_str(2)

# 初始化
task = Task(projectName, userName=env.USERNAME_PM)


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    1.存在多条我执行的任务和子任务
    '''

    # 创建任务
    resp = task.create_task(taskName=taskName1,
                            userName=env.USERNAME_PM)
    assert resp['content']['code'] == 0
    assert resp['content']['msg'] == 'success'

    # 创建子任务
    resp = task.create_task(taskName=taskName2,
                            userName=env.USERNAME_PM)
    assert resp['content']['code'] == 0
    assert resp['content']['msg'] == 'success'


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('项目管理角色删除我执行的任务')
def test_step_01():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.项目管理角色用户登录
    2.删除我执行的任务,有预期结果1

    预期结果
    1.任务删除成功
    '''

    # 领取任务
    resp = task.get_task(taskName=taskName1, userName=env.USERNAME_PG)
    assert resp['content']['code'] == 0

    resp = task.query_tasks(assign=1, userName=env.USERNAME_PG)
    assert taskName1 in json.dumps(resp['content'])

    # 删除任务
    resp = task.delete_task(taskName=taskName1, assign=1, executor=env.USERNAME_PG, userName=env.USERNAME_PM)
    assert resp['content']['code'] == 0
    assert resp['content']['msg'] == 'success'

    resp = task.query_tasks(assign=1, userName=env.USERNAME_PG)
    assert taskName1 not in json.dumps(resp['content'])


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('非项目管理角色删除我执行的任务')
def test_step_02():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.非项目管理角色用户登录
    2.删除我执行的任务,有预期结果1

    预期结果
    1.任务删除失败
    '''

    # 领取任务
    resp = task.get_task(taskName=taskName2, userName=env.USERNAME_PG)
    assert resp['content']['code'] == 0

    resp = task.query_tasks(assign=1, userName=env.USERNAME_PG)
    assert taskName2 in json.dumps(resp['content'])

    # 删除任务
    resp = task.delete_task(taskName=taskName2, assign=1, executor=env.USERNAME_PG, userName=env.USERNAME_PG)
    assert resp['content']['code'] == 403
    assert resp['content']['msg'] == '没有修改项目权限'

    resp = task.query_tasks(assign=1, userName=env.USERNAME_PG)
    assert taskName2 in json.dumps(resp['content'])


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        task.delete_tasks(taskNameList=[taskName2])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
