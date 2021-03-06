#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TS_SR_task_archive_02.py
@time:2021/08/31
*/

01:新建任务后完结后奖励小红花
02:修改任务后完结后奖励小红花
03:复制任务后完结后奖励小红花
04:子任务完结后奖励小红花
"""
import time

import allure

from FastApi.aws.project import Task
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
taskName1 = 'TS_SR_task_archive_02_1' + get_random_str(2)
taskName2 = 'TS_SR_task_archive_02_2' + get_random_str(2)
taskName3 = 'TS_SR_task_archive_02_3' + get_random_str(2)
subtaskName = 'TS_SR_task_archive_02_4' + get_random_str(2)

# 初始化
task = Task(projectName, userName=env.USERNAME_PM)


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    '''

    # 新建多条任务
    resp = task.create_task(taskName=taskName1,
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    resp = task.create_task(taskName=taskName2,
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 新建子任务
    resp = task.create_task(taskName=subtaskName,
                            broTaskName=taskName1,
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('已完结任务奖励小红花')
def test_step():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.对已完结任务奖励小红花

    预期结果
    1.奖励成功
    '''

    # 领取任务1并完结
    resp = task.get_task(taskName=taskName1, userName=env.USERNAME_PG)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    resp = task.archive_task(taskName=taskName1, userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 修改任务2
    resp = task.modify_task(taskName2, description='modify')
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 领取任务2并完结
    resp = task.get_task(taskName=taskName2, userName=env.USERNAME_PG)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    resp = task.archive_task(taskName=taskName2, userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 复制任务1并修改
    resp = task.copy_task(taskName1)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    taskGetDateLine = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    resp = task.modify_task(taskName1, archive=0, newTaskName=taskName3, taskGetDateLine=taskGetDateLine)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 领取任务3并完结
    resp = task.get_task(taskName=taskName3, userName=env.USERNAME_RD)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    resp = task.archive_task(taskName=taskName3, userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 领取子任务并完结
    resp = task.get_task(taskName=subtaskName, userName=env.USERNAME_RD)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    resp = task.archive_task(taskName=subtaskName, userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 查询已完结任务
    resp = task.query_tasks(archive=1)
    assert get_value_from_resp(resp['content'], 'archive', 'title', taskName1) == 1
    assert get_value_from_resp(resp['content'], 'archive', 'title', taskName2) == 1
    assert get_value_from_resp(resp['content'], 'archive', 'title', taskName3) == 1
    assert get_value_from_resp(resp['content'], 'archive', 'title', subtaskName) == 1

    # 奖励小红花
    resp = task.give_red_flower(taskName1, userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    resp = task.give_red_flower(taskName2, userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    resp = task.give_red_flower(taskName3, userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    resp = task.give_red_flower(subtaskName, userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        task.delete_tasks(taskNameList=[taskName1, taskName2, taskName3, subtaskName])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
