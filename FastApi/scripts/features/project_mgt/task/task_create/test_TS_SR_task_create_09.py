#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TS_SR_task_create_09.py
@time:2021/09/01
*/

新建任务:截止日期必填校验
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
taskName = 'TS_SR_task_create_09_' + get_random_str(3)
deadLine = ' '

# 初始化
task = Task(projectName, userName=env.USERNAME_PM)


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    '''


@pytest.mark.xfail()
@allure.feature('我的项目')
@allure.story('任务')
@allure.title('新建任务截止日期为空')
def test_step():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.新建项目任务,不输入截止日期,有预期结果1

    预期结果
    1.任务创建失败,提示合理
    '''
    # 新建任务,名称包含英文+数字
    resp = task.create_task(taskName=taskName,
                            deadLine=deadLine,
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
