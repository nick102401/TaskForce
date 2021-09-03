#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TS_SR_task_modify_07.py
@time:2021/08/31
*/

01:修改任务_添加执行人
02:修改任务_更换执行人
"""
import json

import allure

from FastApi.aws.project import Task
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName

log = Logger().logger

# 生成随机字符串
taskName = 'TS_SR_task_modify_07_' + get_random_str(3)

# 初始化
task = Task(projectName, userName=env.USERNAME_PM)


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    1.项目已存在新建任务
    '''
    # 新建默认配置任务
    resp = task.create_task(taskName=taskName,
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('修改任务_添加执行人')
def test_step_01():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.修改任务,添加执行人,有预期结果1

    预期结果
    1.任务修改成功,我执行的任务中显示该任务
    '''

    resp = task.query_tasks(assign=1, executor=env.USERNAME_PG, userName=env.USERNAME_PG)
    assert taskName not in json.dumps(resp['content']['data']['list'])

    resp = task.modify_task(taskName=taskName,
                            executor=env.USERNAME_PG,
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    resp = task.query_tasks(assign=1, executor=env.USERNAME_PG, userName=env.USERNAME_PG)
    assert taskName in json.dumps(resp['content']['data']['list'])


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('修改任务_更换执行人')
def test_step_02():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.PM账号登录
    2.修改任务,更换执行人,有预期结果1

    预期结果
    1.任务修改成功
    '''

    resp = task.query_tasks(assign=1, executor=env.USERNAME_RD, userName=env.USERNAME_RD)
    assert taskName not in json.dumps(resp['content']['data']['list'])

    resp = task.modify_task(taskName=taskName,
                            executor=env.USERNAME_RD,
                            userName=env.USERNAME_PM)
    assert resp['content']['code'] == 0
    assert resp['content']['msg'] == 'success'

    resp = task.query_tasks(assign=1, executor=env.USERNAME_RD, userName=env.USERNAME_RD)
    assert taskName in json.dumps(resp['content']['data']['list'])


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        task.delete_tasks(taskNameList=[taskName])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
