#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TS_SR_task_create_06.py
@time:2021/09/01
*/

新建任务:
01:bug任务和悬赏任务不同时选择
02:bug任务和悬赏任务同时选择
"""

import allure

from FastApi.aws.project import Task
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName

log = Logger().logger

# 生成随机字符串
taskName1 = 'TS_SR_task_create_06_1' + get_random_str(2)
taskName2 = 'TS_SR_task_create_06_2' + get_random_str(2)

# 初始化
task = Task(projectName, userName=env.USERNAME_PM)


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    '''


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('新建任务_bug任务和悬赏任务不同时选择')
def test_step_01():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.新建项目任务,bug任务和悬赏任务不同时选择,有预期结果1

    预期结果
    1.任务创建成功
    '''
    # 新建任务,名称包含英文+数字
    resp = task.create_task(taskName=taskName1,
                            priceFlag=False,
                            bugStatusName="轻微",
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('新建任务_bug任务和悬赏任务同时选择')
def test_step_02():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.新建项目任务,bug任务和悬赏任务同时选择,有预期结果1

    预期结果
    1.任务创建失败,提示信息合理
    '''
    # 新建任务,名称包含英文+数字
    resp = task.create_task(taskName=taskName2,
                            priceFlag=True,
                            bugStatusName="轻微",
                            userName=env.USERNAME_PM)
    assert resp['content']['code'] == -1
    assert resp['content']['msg'] == '不能同时bug任务、悬赏任务'


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        task.delete_tasks(taskNameList=[taskName1])
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
