#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TS_SR_task_create_08.py
@time:2021/09/01
*/

01:新建任务有效点数大于任务点数
02:单个任务的点数不能大于每周饱和工作点数
"""

import allure
import pytest

from FastApi.aws.system_function import BaseConfig
from FastApi.aws.project import Task
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName

log = Logger().logger

# 生成随机字符串
taskName1 = 'TS_SR_task_create_08_1' + get_random_str(3)
taskName2 = 'TS_SR_task_create_08_2' + get_random_str(3)

# 初始化
task = Task(projectName, userName=env.USERNAME_PM)
base = BaseConfig()


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    '''
    global fullDayPoints
    resp = base.query_base_config()
    fullDayPoints = resp['content']['data']['fullDayPoints']


@pytest.mark.xfail()
@allure.feature('我的项目')
@allure.story('任务')
@allure.title('新建任务有效点数大于任务点数')
def test_step_01():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.新建任务有效点数大于任务点数,有预期结果1

    预期结果
    1.任务创建失败,提示合理
    '''
    resp = task.create_task(taskName=taskName1,
                            points=1,
                            countedPoints=5,
                            userName=env.USERNAME_PM)
    assert resp['content']['code'] == -1


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('新建单个任务的点数不能大于每周饱和工作点数')
def test_step_02():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.新建单个任务的点数大于每周饱和工作点数,有预期结果1

    预期结果
    1.任务创建失败,提示合理
    '''
    resp = task.create_task(taskName=taskName2,
                            points=100,
                            countedPoints=fullDayPoints + 1,
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == '单个任务的点数不能大于每周饱和工作点数！'


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        task.delete_tasks(taskNameList=[taskName1, taskName2])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
