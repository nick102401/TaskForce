#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TS_SR_task_modify_06.py
@time:2021/08/31
*/

修改任务:
01:bug任务和悬赏任务不同时选择
02:bug任务和悬赏任务同时选择
"""
from datetime import datetime, timedelta

import allure

from FastApi.aws.project import Task
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger
from FastApi.common.yaml_handle import read_data_from_file
from FastApi.conf import env
from FastApi.scripts.conftest import projectName

log = Logger().logger

# 加载预置数据
file_name = 'preset_project_body.yaml'
preset_data = read_data_from_file(file_name)
preset_task_type_data = preset_data['TASK_TYPE']  # 任务类型
preset_task_status_data = preset_data['TASK_STATUS']  # 任务状态
preset_bug_status_data_1 = preset_data['BUG_STATUS_1']  # BUG状态
preset_bug_status_data_2 = preset_data['BUG_STATUS_2']  # BUG状态
preset_bug_status_data_3 = preset_data['BUG_STATUS_3']  # BUG状态

# 生成随机字符串
taskName = 'TS_SR_task_modify_06_' + get_random_str(3)
preTaskGetDateLine = datetime.strftime(datetime.now(), '%Y-%m-%d')
taskGetDateLine = datetime.strftime(datetime.now() + timedelta(days=1), '%Y-%m-%d')
preDeadLine = datetime.strftime(datetime.now() + timedelta(days=1), '%Y-%m-%d')
deadLine = datetime.strftime(datetime.now() + timedelta(days=3), '%Y-%m-%d')

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
                            description='',
                            deadLine=preDeadLine,
                            taskGetDateLine=preTaskGetDateLine,
                            points=1,
                            countedPoints=1,
                            priceFlag=False,
                            priorityName="普通",
                            typeName="开发任务",
                            statusName="未开发",
                            bugStatusName="",
                            executor='',
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('修改任务_bug任务和悬赏任务不同时选择')
def test_step_01():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.修改任务所有配置,bug任务和悬赏任务不同时选择,有预期结果1

    预期结果
    1.任务修改成功
    '''
    resp = task.modify_task(taskName=taskName,
                            description=taskName,
                            deadLine=deadLine,
                            taskGetDateLine=taskGetDateLine,
                            points=10,
                            countedPoints=10,
                            priceFlag=False,
                            priorityName="普通",
                            typeName=preset_task_type_data['typeName'],
                            statusName=preset_task_status_data['statusName'],
                            bugStatusName=preset_bug_status_data_1['statusName'],
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    resp = task.modify_task(taskName=taskName,
                            description=taskName,
                            deadLine=deadLine,
                            taskGetDateLine=taskGetDateLine,
                            points=10,
                            countedPoints=10,
                            priceFlag=True,
                            priorityName="普通",
                            typeName=preset_task_type_data['typeName'],
                            statusName=preset_task_status_data['statusName'],
                            bugStatusName='',
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('修改任务_bug任务和悬赏任务同时选择')
def test_step_02():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.修改任务所有配置,bug任务和悬赏任务同时选择,有预期结果1

    预期结果
    1.任务修改失败
    '''
    resp = task.modify_task(taskName=taskName,
                            description=taskName,
                            deadLine=deadLine,
                            taskGetDateLine=taskGetDateLine,
                            points=10,
                            countedPoints=10,
                            priceFlag=True,
                            priorityName="普通",
                            typeName=preset_task_type_data['typeName'],
                            statusName=preset_task_status_data['statusName'],
                            bugStatusName=preset_bug_status_data_1['statusName'],
                            userName=env.USERNAME_PM)
    assert resp['content']['code'] == -1
    assert resp['content']['msg'] == '不能同时bug任务、悬赏任务！'


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        task.delete_tasks(taskNameList=[taskName])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
