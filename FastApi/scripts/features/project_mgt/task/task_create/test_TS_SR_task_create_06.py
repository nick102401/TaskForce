#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TS_SR_task_create_06.py
@time:2021/09/01
*/

新建任务:名称长度校验(512位)
01:名称输入512位中文/英文字符
02:名称输入超过512位中文/英文字符
"""

import allure

from FastApi.aws.project import Task
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName

log = Logger().logger

# 生成随机字符串
taskName_en = 'A' * 512
taskName_cn = '测试' * 256

taskName1_en = 'A' * 513
taskName1_cn = '测试' * 256 + '中'

# 初始化
task = Task(projectName, userName=env.USERNAME_PM)


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    '''


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('新建任务名称长度为512位')
def test_step_01():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.新建项目任务,名称长度为512位,有预期结果1

    预期结果
    1.任务创建失败,提示合理
    '''
    # 新建任务,名称长度为512位
    resp = task.create_task(taskName=taskName_cn,
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    resp = task.create_task(taskName=taskName_en,
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('新建任务名称长度大于512位')
def test_step_02():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.新建项目任务,名称长度大于512位,有预期结果1

    预期结果
    1.任务创建失败,提示合理
    '''
    # 新建任务,名称长度大于512位
    resp = task.create_task(taskName=taskName1_cn,
                            userName=env.USERNAME_PM)
    assert resp['content']['code'] == -1
    assert resp['content']['msg'] == 'SYSTEM_ERROR'

    resp = task.create_task(taskName=taskName1_en,
                            userName=env.USERNAME_PM)
    assert resp['content']['code'] == -1
    assert resp['content']['msg'] == 'SYSTEM_ERROR'


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        task.delete_tasks(taskNameList=[taskName_cn, taskName_en])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
    try:
        task.delete_tasks(taskNameList=[taskName1_cn, taskName1_en])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
