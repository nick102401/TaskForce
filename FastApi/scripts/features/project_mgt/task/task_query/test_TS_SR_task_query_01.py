#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TS_SR_task_query_01.py
@time:2021/08/23
*/

任务-首页
"""

import allure

from FastApi.aws.project import Task
from FastApi.common.logs_handle import Logger
from FastApi.common.yaml_handle import read_data_from_file
from FastApi.conf import env
from FastApi.scripts.conftest import projectName

log = Logger().logger

# 加载预置数据
file_name = 'task_body.yaml'
file_data = read_data_from_file(file_name)
task_data1 = file_data['TASK1']
task_data2 = file_data['TASK2']
task_data3 = file_data['TASK3']
subtask_data = file_data['SUBTASK']
task_status_data = file_data['TASK_STATUS']

# 初始化
task = Task(projectName, userName=env.USERNAME_PM)


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    1.构造不同阶段的任务(包括执行中、已完结、我执行的、未分配的)
    '''

    # 构造不同阶段的任务
    # 创建任务1
    resp = task.create_task(taskName=task_data1['taskName'], userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    # 创建任务2
    resp = task.create_task(taskName=task_data2['taskName'], userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    # 创建任务3
    resp = task.create_task(taskName=task_data3['taskName'], userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    # 创建子任务
    resp = task.create_task(taskName=subtask_data['taskName'], userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 领取任务1并完结
    resp = task.get_task(taskName=task_data1['taskName'], userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    resp = task.archive_task(taskName=task_data1['taskName'], userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 领取任务2并完成
    resp = task.get_task(taskName=task_data2['taskName'], userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    resp = task.modify_task(taskName=task_data2['taskName'],
                            statusName=task_status_data['statusName'],
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('首页')
def test_step():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.PM用户登录
    2.点击任务查看首页,有预期结果1

    预期结果
    1.首页可以查看当前项目任务汇总(包括任务数量以及状态)
    '''
    resp = task.query_index_data()
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert resp['content']['data']['unfinishTaskCountAndSumSimple']['taskCount'] >= 3
    assert resp['content']['data']['finishTaskCountAndSumSimple']['taskCount'] >= 1


def teardown_module(module):
    log.info('-----环境操作-----')
    task.delete_task(taskName=task_data2['taskName'])
    task.delete_task(taskName=task_data3['taskName'])
    task.delete_task(taskName=subtask_data['taskName'])
