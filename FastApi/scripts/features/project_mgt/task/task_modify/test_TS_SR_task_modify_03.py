#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TS_SR_task_modify_03.py
@time:2021/08/31
*/

修改任务:名称必填校验
01:修改任务名称为空
02:修改子任务名称为空
"""

import allure
import pytest

from FastApi.aws.project import Task
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName

log = Logger().logger

# 生成随机字符串
taskName = 'TS_SR_task_modify_03_1' + get_random_str(2)
subtaskName = 'TS_SR_task_modify_03_2' + get_random_str(2)
newTaskName = ''

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
    assert resp['content']['code'] == 0
    assert resp['content']['msg'] == 'success'

    # 新建默认配置子任务
    resp = task.create_task(taskName=subtaskName,
                            broTaskName=taskName,
                            userName=env.USERNAME_PM)
    assert resp['content']['code'] == 0
    assert resp['content']['msg'] == 'success'


@pytest.mark.xfail()
@allure.feature('我的项目')
@allure.story('任务')
@allure.title('修改任务名称为空')
def test_step_01():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.PM账号登录
    2.修改任务名称为空,有预期结果1

    预期结果
    1.任务修改失败
    '''

    resp = task.modify_task(taskName=taskName,
                            newTaskName=newTaskName,
                            userName=env.USERNAME_PM)
    assert resp['content']['code'] == -1


@pytest.mark.xfail()
@allure.feature('我的项目')
@allure.story('任务')
@allure.title('修改子任务名称为空')
def test_step_02():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.PM账号登录
    2.修改子任务名称为空,有预期结果1

    预期结果
    1.子任务修改失败
    '''

    resp = task.modify_task(taskName=subtaskName,
                            newTaskName=newTaskName,
                            userName=env.USERNAME_PM)
    assert resp['content']['code'] == -1


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        task.delete_tasks(taskNameList=[taskName])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
    try:
        task.delete_tasks(taskNameList=[subtaskName])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
    try:
        task.delete_tasks(taskNameList=[newTaskName])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
    try:
        task.delete_tasks(taskNameList=[newTaskName])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
