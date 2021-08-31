#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TS_SR_task_03_01.py
@time:2021/08/30
*/

执行中任务按任务状态展示
"""
import allure

from FastApi.aws.project import Project, Task
from FastApi.common.helper import get_random_str, get_value_from_resp
from FastApi.common.logs_handle import Logger
from FastApi.common.yaml_handle import read_data_from_file
from FastApi.conf import env
from FastApi.scripts.conftest import projectName

log = Logger().logger

# 加载预置数据
file_name = 'preset_project_body.yaml'
preset_data = read_data_from_file(file_name)
preset_task_status_data = preset_data['TASK_STATUS']

# 自定义参数
taskName1 = 'TS_SR_task_03_01_1' + get_random_str(2)
taskName2 = 'TS_SR_task_03_01_2' + get_random_str(2)

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

    # 创建不同任务状态任务
    resp = task.create_task(taskName=taskName2,
                            statusName=preset_task_status_data['statusName'],
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('执行中任务按任务状态展示')
def test_step():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.PM用户登录
    2.检查执行中任务

    预期结果
    1.按不同任务状态正确展示
    '''

    # 执行中任务
    resp = task.query_tasks(archive=0)
    dataList = resp['content']['data']
    metaList = resp['content']['data']['meta']
    taskNameId1 = task.query_task_id_by_name(taskName=taskName1)
    taskNameId2 = task.query_task_id_by_name(taskName=taskName2)

    assert get_value_from_resp(dataList, 'statusId', 'taskId', taskNameId1) \
           == get_value_from_resp(metaList, 'taskStatusId', 'statusName', '未开发')

    assert get_value_from_resp(dataList, 'statusId', 'taskId', taskNameId2) \
           == get_value_from_resp(metaList, 'taskStatusId', 'statusName', preset_task_status_data['statusName'])


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        task.delete_tasks(taskNameList=[taskName1, taskName2])
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
