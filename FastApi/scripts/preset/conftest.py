#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:王东
@file:conftest.py
@time:2021/08/25

项目初始化文件
"""
import pytest

from FastApi.aws.project import Project, Task, Plan, Personnel
from FastApi.common.yaml_handle import read_data_from_file
from FastApi.conf import env

# 加载预置数据
file_name = '../../../../../11111/preset_project_body.yaml'
preset_data = read_data_from_file(file_name)
preset_project_data = preset_data['PRESET_PROJECT']
preset_task_data = preset_data['PRESET_TASK']
preset_subtask_data = preset_data['PRESET_SUBTASK']
preset_plan_data_1 = preset_data['PRESET_PLAN_1']
preset_plan_data_2 = preset_data['PRESET_PLAN_2']
preset_plan_task_data_1 = preset_data['PRESET_PLAN_TASK_1']
preset_plan_task_data_2 = preset_data['PRESET_PLAN_TASK_2']
preset_post_data_1 = preset_data['PRESET_POST_1']
preset_post_data_2 = preset_data['PRESET_POST_2']
preset_role_data_1 = preset_data['PRESET_ROLE_1']
preset_role_data_2 = preset_data['PRESET_ROLE_2']

# 项目初始化
project = Project()


@pytest.fixture(scope='function')
def init_project():
    # 创建项目
    project.create_project(projectName=preset_project_data['projectName'],
                           startTime=preset_project_data['startTime'],
                           endTime=preset_project_data['endTime'],
                           templateName=preset_project_data['templateName'],
                           description=preset_project_data['description'],
                           userName=env.USERNAME_PM)

    # 审批通过
    project.approve_project(projectName=preset_project_data['projectName'],
                            approveDescription='ok',
                            approveStatus=1,
                            userName=env.USERNAME_PMO)


@pytest.fixture(scope='function')
def archive_init_project():
    # 完结初始化项目
    project.disable_or_archive_project(projectName=preset_project_data['projectName'],
                                       operationType='archive',
                                       userName=env.USERNAME_PM)


@pytest.fixture(scope='function')
def init_task():
    # 初始化项目任务
    task = Task(preset_project_data['projectName'])
    # 创建任务
    task.create_task(taskName=preset_task_data['taskName'],
                     broTaskName=preset_task_data['broTaskName'],
                     description=preset_task_data['description'],
                     deadLine=preset_task_data['deadLine'],
                     taskGetDateLine=preset_task_data['taskGetDateLine'],
                     points=preset_task_data['points'],
                     countedPoints=preset_task_data['countedPoints'],
                     priceFlag=preset_task_data['priceFlag'],
                     priorityName=preset_task_data['priorityName'],
                     typeName=preset_task_data['typeName'],
                     statusName=preset_task_data['statusName'],
                     bugStatusName=preset_task_data['bugStatusName'],
                     executor=preset_task_data['executor'],
                     userName=env.USERNAME_PM)


@pytest.fixture(scope='function')
def init_subtask():
    # 初始化项目子任务
    task = Task(preset_project_data['projectName'])
    # 创建子任务
    task.create_task(taskName=preset_subtask_data['taskName'],
                     broTaskName=preset_subtask_data['broTaskName'],
                     description=preset_subtask_data['description'],
                     deadLine=preset_subtask_data['deadLine'],
                     taskGetDateLine=preset_subtask_data['taskGetDateLine'],
                     points=preset_subtask_data['points'],
                     countedPoints=preset_subtask_data['countedPoints'],
                     priceFlag=preset_subtask_data['priceFlag'],
                     priorityName=preset_subtask_data['priorityName'],
                     typeName=preset_subtask_data['typeName'],
                     statusName=preset_subtask_data['statusName'],
                     bugStatusName=preset_subtask_data['bugStatusName'],
                     executor=preset_subtask_data['executor'],
                     userName=env.USERNAME_PM)


@pytest.fixture(scope='function')
def init_plan():
    # 初始化项目计划
    plan = Plan(preset_project_data['projectName'])
    # 创建测试计划
    plan.create_plan(planName=preset_plan_data_1['planName'],
                     description=preset_plan_data_1['description'],
                     startTime=preset_plan_data_1['startTime'],
                     endTime=preset_plan_data_1['endTime'],
                     userName=env.USERNAME_PM)
    # 创建计划任务
    plan.create_task_for_plan(taskName=preset_plan_task_data_1['taskName'],
                              broTaskName=preset_plan_task_data_1['broTaskName'],
                              description=preset_plan_task_data_1['description'],
                              deadLine=preset_plan_task_data_1['deadLine'],
                              taskGetDateLine=preset_plan_task_data_1['taskGetDateLine'],
                              points=preset_plan_task_data_1['points'],
                              countedPoints=preset_plan_task_data_1['countedPoints'],
                              priceFlag=preset_plan_task_data_1['priceFlag'],
                              priorityName=preset_plan_task_data_1['priorityName'],
                              typeName=preset_plan_task_data_1['typeName'],
                              statusName=preset_plan_task_data_1['statusName'],
                              bugStatusName=preset_plan_task_data_1['bugStatusName'],
                              executor=preset_plan_task_data_1['executor'],
                              planName=preset_plan_task_data_1['planName'],
                              userName=env.USERNAME_PM)

    # 创建开发计划
    plan.create_plan(planName=preset_plan_data_2['planName'],
                     description=preset_plan_data_2['description'],
                     startTime=preset_plan_data_2['startTime'],
                     endTime=preset_plan_data_2['endTime'],
                     userName=env.USERNAME_PM)
    # 创建计划任务
    plan.create_task_for_plan(taskName=preset_plan_task_data_2['taskName'],
                              broTaskName=preset_plan_task_data_2['broTaskName'],
                              description=preset_plan_task_data_2['description'],
                              deadLine=preset_plan_task_data_2['deadLine'],
                              taskGetDateLine=preset_plan_task_data_2['taskGetDateLine'],
                              points=preset_plan_task_data_2['points'],
                              countedPoints=preset_plan_task_data_2['countedPoints'],
                              priceFlag=preset_plan_task_data_2['priceFlag'],
                              priorityName=preset_plan_task_data_2['priorityName'],
                              typeName=preset_plan_task_data_2['typeName'],
                              statusName=preset_plan_task_data_2['statusName'],
                              bugStatusName=preset_plan_task_data_2['bugStatusName'],
                              executor=preset_plan_task_data_2['executor'],
                              planName=preset_plan_task_data_2['planName'],
                              userName=env.USERNAME_PM)


@pytest.fixture(scope='function')
def init_recruit_info():
    # 初始化项目招聘信息
    personnel = Personnel(preset_project_data['projectName'])
    # 测试岗位
    personnel.create_recruit(postName=preset_post_data_1['postName'],
                             postSum=preset_post_data_1['postSum'],
                             postJobShare=preset_post_data_1['postJobShare'],
                             postType=preset_post_data_1['postType'],
                             roleType=preset_post_data_1['roleType'],
                             postDescription=preset_post_data_1['postDescription'],
                             startTime=preset_post_data_1['startTime'],
                             endTime=preset_post_data_1['endTime'],
                             userName=env.USERNAME_PM)
    # 开发岗位
    personnel.create_recruit(postName=preset_post_data_2['postName'],
                             postSum=preset_post_data_2['postSum'],
                             postJobShare=preset_post_data_2['postJobShare'],
                             postType=preset_post_data_2['postType'],
                             roleType=preset_post_data_2['roleType'],
                             postDescription=preset_post_data_2['postDescription'],
                             startTime=preset_post_data_2['startTime'],
                             endTime=preset_post_data_2['endTime'],
                             userName=env.USERNAME_PM)


@pytest.fixture(scope='function')
def init_project_role():
    # 初始化项目角色
    # 测试
    project.create_role(roleName=preset_role_data_1['roleName'],
                        projectName=preset_project_data['projectName'],
                        manage=preset_role_data_1['manage'],
                        createTask=preset_role_data_1['createTask'],
                        updateTask=preset_role_data_1['updateTask'],
                        filterType=preset_role_data_1['filterType'],
                        userName=env.USERNAME_PM)
    # 开发
    project.create_role(roleName=preset_role_data_2['roleName'],
                        projectName=preset_project_data['projectName'],
                        manage=preset_role_data_2['manage'],
                        createTask=preset_role_data_2['createTask'],
                        updateTask=preset_role_data_2['updateTask'],
                        filterType=preset_role_data_2['filterType'],
                        userName=env.USERNAME_PM)
