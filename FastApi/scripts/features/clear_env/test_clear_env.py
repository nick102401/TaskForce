#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:王东
@file:test_clear_env.py
@time:2021/09/15
"""
import allure

# 初始化
from FastApi.aws.project import Task, Personnel, Project
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName, preset_data

# 加载预置数据
preset_role_data_1 = preset_data['PRESET_ROLE_1']  # 项目角色
preset_role_data_2 = preset_data['PRESET_ROLE_2']  # 项目角色
preset_task_type_data = preset_data['TASK_TYPE']  # 任务类型
preset_task_status_data = preset_data['TASK_STATUS']  # 任务状态
preset_bug_status_data_1 = preset_data['BUG_STATUS_1']  # BUG状态
preset_bug_status_data_2 = preset_data['BUG_STATUS_2']  # BUG状态
preset_bug_status_data_3 = preset_data['BUG_STATUS_3']  # BUG状态

# 日志
log = Logger().logger

project = Project()
task = Task(projectName, userName=env.USERNAME_PM)
person = Personnel(projectName, userName=env.USERNAME_PM)


@allure.feature('环境清理')
@allure.title('项目数据清理')
def test_clear_env():
    # 清理未完结任务
    try:
        task.delete_tasks(ifDeleteAll=True, userName=env.USERNAME_PM)
    except Exception as ex:
        log.info(ex)

    # 清理项目成员
    try:
        person.delete_members(ifDeleteAll=True, userName=env.USERNAME_PM)
    except Exception as ex:
        log.info(ex)

    # 清理项目角色
    try:
        project.delete_role(roleName=preset_role_data_1['roleName'], projectName=projectName, userName=env.USERNAME_PM)
        project.delete_role(roleName=preset_role_data_2['roleName'], projectName=projectName, userName=env.USERNAME_PM)
    except Exception as ex:
        log.info(ex)

    # 清理项目任务类型
    try:
        project.delete_task_type(typeName=preset_task_type_data['typeName'], projectName=projectName,
                                 userName=env.USERNAME_PM)
    except Exception as ex:
        log.info(ex)

    # 清理项目任务状态
    try:
        project.delete_status(statusName=preset_task_status_data['statusName'], projectName=projectName,
                              userName=env.USERNAME_PM)
    except Exception as ex:
        log.info(ex)

    # 清理项目BUG状态
    try:
        project.delete_status(statusName=preset_bug_status_data_1['statusName'], projectName=projectName, bugFlag=1,
                              userName=env.USERNAME_PM)
        project.delete_status(statusName=preset_bug_status_data_2['statusName'], projectName=projectName, bugFlag=1,
                              userName=env.USERNAME_PM)
        project.delete_status(statusName=preset_bug_status_data_3['statusName'], projectName=projectName, bugFlag=1,
                              userName=env.USERNAME_PM)
    except Exception as ex:
        log.info(ex)
