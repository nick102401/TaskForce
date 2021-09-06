#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TS_SR_task_modify_11.py
@time:2021/09/01
*/

修改任务关联所有配置(项目计划除外)
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
preTaskName = 'TS_SR_task_modify_11_' + get_random_str(3)
description = preTaskName
taskGetDateLine = datetime.strftime(datetime.now() + timedelta(days=1), '%Y-%m-%d')
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
    resp = task.create_task(taskName=preTaskName,
                            userName=env.USERNAME_PM)
    assert resp['content']['code'] == 0
    assert resp['content']['msg'] == 'success'


@allure.feature('我的项目')
@allure.story('任务')
@allure.title('修改任务关联所有配置')
def test_step():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.修改任务关联所有配置,有预期结果1

    预期结果
    1.任务创建成功
    '''
    # 新建任务,名称包含英文+数字
    resp = task.modify_task(taskName=preTaskName,
                            description=description,
                            deadLine=deadLine,
                            taskGetDateLine=taskGetDateLine,
                            points=10,
                            countedPoints=10,
                            priceFlag=False,
                            priorityName="普通",
                            typeName=preset_task_type_data['typeName'],
                            statusName=preset_task_status_data['statusName'],
                            bugStatusName=preset_bug_status_data_1['statusName'],
                            executor=env.USERNAME_RD,
                            userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        task.delete_tasks(taskNameList=[preTaskName])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
