#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TS_SR_task_modify_01.py
@time:2021/08/31
*/

修改任务名称:输入任意字符名称
"""

import allure

from FastApi.aws.project import Task
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName

log = Logger().logger

# 生成随机字符串
taskName = 'pre_TS_SR_task_modify_01_' + get_random_str(3)
taskName1 = 'TS_SR_task_modify_01_1' + get_random_str(2)
taskName2 = '项目任务测试-2' + get_random_str(2)
taskName3 = '~!@#$%^&*()-3' + get_random_str(2)

# 初始化
task = Task(projectName, userName=env.USERNAME_PM)


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    1.项目已存在新建任务
    '''
    # 预置任务
    resp = task.create_task(taskName=taskName,
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('修改任务名称')
def test_step():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.修改任务名称分别包含英文/中文/特殊字符,有预期结果1

    预期结果
    1.任务修改成功
    '''
    # 修改任务,名称包含英文+数字
    resp = task.modify_task(taskName=taskName,
                            newTaskName=taskName1,
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 修改任务,名称包含中文+数字
    resp = task.modify_task(taskName=taskName1,
                            newTaskName=taskName2,
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 修改任务,名称包含特殊字符+数字
    resp = task.modify_task(taskName=taskName2,
                            newTaskName=taskName3,
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        task.delete_tasks(taskNameList=[taskName3])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
    try:
        task.delete_tasks(taskNameList=[taskName2])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
    try:
        task.delete_tasks(taskNameList=[taskName1])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
