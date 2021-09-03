#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TS_SR_task_modify_05.py
@time:2021/09/01
*/

修改子任务:名称长度校验(512位)
01:名称输入512位中文/英文字符
02:名称输入超过512位中文/英文字符
"""

import allure

from FastApi.aws.project import Task
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName

log = Logger().logger

# 生成随机字符串
taskName = 'TS_SR_task_modify_05_1' + get_random_str(2)
subtaskName1 = 'TS_SR_task_modify_05_2' + get_random_str(2)
subtaskName2 = 'TS_SR_task_modify_05_3' + get_random_str(2)
subtaskName3 = 'TS_SR_task_modify_05_4' + get_random_str(2)

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
    1.项目已存在新建子任务
    '''

    # 新建默认配置任务
    resp = task.create_task(taskName=taskName,
                            userName=env.USERNAME_PM)
    assert resp['content']['code'] == 0
    assert resp['content']['msg'] == 'success'

    # 新建默认配置子任务
    resp = task.create_task(taskName=subtaskName1,
                            broTaskName=taskName,
                            userName=env.USERNAME_PM)
    assert resp['content']['code'] == 0
    assert resp['content']['msg'] == 'success'

    resp = task.create_task(taskName=subtaskName2,
                            broTaskName=taskName,
                            userName=env.USERNAME_PM)
    assert resp['content']['code'] == 0
    assert resp['content']['msg'] == 'success'

    resp = task.create_task(taskName=subtaskName3,
                            broTaskName=taskName,
                            userName=env.USERNAME_PM)
    assert resp['content']['code'] == 0
    assert resp['content']['msg'] == 'success'


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('修改子任务名称长度为512位')
def test_step_01():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.修改项目子任务,名称长度为512位,有预期结果1

    预期结果
    1.子任务修改成功
    '''
    # 修改子任务,名称长度为512位
    resp = task.modify_task(taskName=subtaskName1,
                            newTaskName=taskName_cn,
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    resp = task.modify_task(taskName=taskName_cn,
                            newTaskName=taskName_en,
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('修改子任务名称长度大于512位')
def test_step_02():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.修改项目子任务,名称长度大于512位,有预期结果1

    预期结果
    1.子任务修改失败,提示合理
    '''
    # 修改子任务,名称长度大于512位
    resp = task.modify_task(taskName=subtaskName2,
                            newTaskName=taskName1_cn,
                            userName=env.USERNAME_PM)
    assert resp['content']['code'] == -1
    assert resp['content']['msg'] == 'SYSTEM_ERROR'

    resp = task.modify_task(taskName=subtaskName3,
                            newTaskName=taskName1_en,
                            userName=env.USERNAME_PM)
    assert resp['content']['code'] == -1
    assert resp['content']['msg'] == 'SYSTEM_ERROR'


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        task.delete_tasks(taskNameList=[taskName_en, taskName_cn])
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
    try:
        task.delete_tasks(taskNameList=[subtaskName1])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
    try:
        task.delete_tasks(taskNameList=[subtaskName2])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
    try:
        task.delete_tasks(taskNameList=[subtaskName3])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
    try:
        task.delete_tasks(taskNameList=[taskName])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
