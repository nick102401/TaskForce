#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TS_SR_task_modify_09.py
@time:2021/09/01
*/

修改任务:截止日期必填校验
"""

import allure

from FastApi.aws.project import Task
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName

log = Logger().logger

# 生成随机字符串
preTaskName = 'TS_SR_task_modify_09_1' + get_random_str(2)

# 初始化
task = Task(projectName, userName=env.USERNAME_PM)
deadLine = ''


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    1.项目已存在新建任务
    '''
    # 新建默认配置任务
    resp = task.create_task(taskName=preTaskName,
                            userName=env.USERNAME_PM)
    assert resp['content']['code'] == 0
    assert resp['content']['msg'] == 'success'


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('修改任务截止日期为空')
def test_step():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.修改任务截止日期为空,有预期结果1

    预期结果
    1.任务修改成功
    '''
    resp = task.modify_task(taskName=preTaskName,
                            deadLine=deadLine,
                            userName=env.USERNAME_PM)
    assert resp['content']['code'] == 0
    assert resp['content']['msg'] == 'success'


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        task.delete_tasks(taskNameList=[preTaskName])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
