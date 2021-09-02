#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TS_SR_task_query_04.py
@time:2021/08/30
*/

根据所有条件查询任务,查询到的任务信息正确
"""
import json

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
preset_task_type_data = preset_data['TASK_TYPE']
preset_task_status_data = preset_data['TASK_STATUS']
preset_bug_status_data_1 = preset_data['BUG_STATUS_1']

# 自定义参数
taskName1 = 'TS_SR_task_query_04_1' + get_random_str(2)

# 初始化
task = Task(projectName, userName=env.USERNAME_PM)


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    1.构造多条任务(不同任务类型、任务状态、BUG状态、完结状态、执行人)
    '''

    # 预置默认配置任务
    resp = task.create_task(taskName=taskName1,
                            typeName=preset_task_type_data['typeName'],
                            statusName=preset_task_status_data['statusName'],
                            bugStatusName=preset_bug_status_data_1['statusName'],
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
@allure.title('根据所有条件查询任务')
def test_step():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.PM用户登录
    2.选择所有条件查询任务

    预期结果
    1.返回任务信息正确
    '''

    # 选择所有条件查询任务
    resp = task.query_tasks(typeName=preset_task_type_data['typeName'],
                            statusName=preset_task_status_data['statusName'],
                            bugStatusName=preset_bug_status_data_1['statusName'],
                            archive=1, executor=env.USERNAME_PM)
    assert taskName1 in json.dumps(resp['content']['data']['list'])


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        task.delete_tasks(taskNameList=[taskName1])
    except Exception as ex:
        log.info('已完结任务无法删除')
        log.info(ex)
