#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TS_SR_task_create_03.py
@time:2021/09/01
*/

新建任务:关联除计划外所有配置
"""
from datetime import datetime, timedelta

import allure

from FastApi.aws.project import Task
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName

log = Logger().logger

# 生成随机字符串
taskName = 'TS_SR_task_create_03_' + get_random_str(3)
description = taskName
taskGetDateLine = datetime.strftime(datetime.now(), '%Y-%m-%d')
deadLine = datetime.strftime(datetime.now() + timedelta(days=3), '%Y-%m-%d')

# 初始化
task = Task(projectName, userName=env.USERNAME_PM)


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    '''


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('新建任务满关联')
def test_step():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.新建项目任务,关联除计划外所有配置,有预期结果1

    预期结果
    1.任务创建成功
    '''
    # 新建任务,名称包含英文+数字
    resp = task.create_task(taskName=taskName,
                            description=description,
                            deadLine=deadLine,
                            taskGetDateLine=taskGetDateLine,
                            points=10,
                            countedPoints=10,
                            priceFlag=False,
                            priorityName="普通",
                            typeName="开发任务",
                            statusName="未开发",
                            bugStatusName="轻微",
                            executor=env.USERNAME_RD,
                            userName=env.USERNAME_PM, )
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        task.delete_tasks(taskNameList=[taskName])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
