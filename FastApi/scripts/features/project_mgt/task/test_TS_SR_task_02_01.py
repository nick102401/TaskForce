#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TS_SR_task_02_01.py
@time:2021/08/30
*/

根据不同条件查询任务，查询到的任务信息正确
"""
import json

import allure

from FastApi.aws.project import Project, Task
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger
from FastApi.common.yaml_handle import read_data_from_file
from FastApi.conf import env

log = Logger().logger

# 加载预置数据
file_name = 'preset_project_body.yaml'
preset_data = read_data_from_file(file_name)
preset_project_data = preset_data['PRESET_PROJECT']
projectName = preset_project_data['projectName']
preset_task_type_data = preset_data['TASK_TYPE']
preset_task_status_data = preset_data['TASK_STATUS']
preset_bug_status_data_1 = preset_data['BUG_STATUS_1']
preset_bug_status_data_2 = preset_data['BUG_STATUS_2']
preset_bug_status_data_3 = preset_data['BUG_STATUS_3']

# 自定义参数
taskName1 = 'TS_SR_task_02_01_1' + get_random_str(2)
taskName2 = 'TS_SR_task_02_01_2' + get_random_str(2)
taskName3 = 'TS_SR_task_02_01_3' + get_random_str(2)
taskName4 = 'TS_SR_task_02_01_4' + get_random_str(2)
taskName5 = 'TS_SR_task_02_01_5' + get_random_str(2)
taskName6 = 'TS_SR_task_02_01_6' + get_random_str(2)

# 初始化
project = Project()
task = Task(projectName, userName=env.USERNAME_PM)


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    1.构造多条任务(不同任务类型、任务状态、BUG状态、完结状态、执行人)
    '''

    # 预置默认配置任务
    resp = task.create_task(taskName=taskName1,
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 创建不同任务类型任务
    resp = task.create_task(taskName=taskName2,
                            typeName=preset_task_type_data['typeName'],
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 创建不同任务状态任务
    resp = task.create_task(taskName=taskName3,
                            statusName=preset_task_status_data['statusName'],
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 创建不同BUG状态任务
    resp = task.create_task(taskName=taskName4,
                            bugStatusName=preset_bug_status_data_1['statusName'],
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    resp = task.create_task(taskName=taskName5,
                            bugStatusName=preset_bug_status_data_2['statusName'],
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    resp = task.create_task(taskName=taskName6,
                            bugStatusName=preset_bug_status_data_3['statusName'],
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 领取任务并完结
    resp = task.get_task(taskName=taskName1, userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    resp = task.archive_task(taskName=taskName1, userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('根据单个条件查询任务')
def test_step():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.PM用户登录
    2.分别根据任务类型/任务状态/BUG状态/完结状态/执行人筛选任务

    预期结果
    1.返回任务信息正确
    '''
    # 任务类型
    resp = task.query_tasks(typeName=preset_task_type_data['typeName'])
    assert taskName2 in json.dumps(resp['content']['data']['list'])

    # 任务状态
    resp = task.query_tasks(statusName=preset_task_status_data['statusName'])
    assert taskName3 in json.dumps(resp['content']['data']['list'])

    # BUG状态
    resp = task.query_tasks(bugStatusName=preset_bug_status_data_1['statusName'])
    assert taskName4 in json.dumps(resp['content']['data']['list'])

    resp = task.query_tasks(bugStatusName=preset_bug_status_data_2['statusName'])
    assert taskName5 in json.dumps(resp['content']['data']['list'])

    resp = task.query_tasks(bugStatusName=preset_bug_status_data_3['statusName'])
    assert taskName6 in json.dumps(resp['content']['data']['list'])

    # 完结状态
    resp = task.query_tasks(archive=1)
    assert taskName1 in json.dumps(resp['content']['data']['list'])

    # 执行人
    resp = task.query_tasks(executor=env.USERNAME_PM)
    assert taskName1 in json.dumps(resp['content']['data']['list'])


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        task.delete_tasks(taskNameList=[taskName2, taskName3, taskName4, taskName5, taskName6])
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
