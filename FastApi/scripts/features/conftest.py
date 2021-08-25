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
from FastApi.conf import env

# 项目名称
projectName = 'PRESET_PROJECT'
# 任务名称
taskName = 'PRESET_TASK'
subtaskName = 'PRESET_SUBTASK'
# 计划名称
planName1 = '测试计划'
planName2 = '开发计划'
# 计划任务名称
planTaskName1 = 'PRESET_PLAN_TASK1'
planTaskName2 = 'PRESET_PLAN_TASK2'
# 招募岗位
postName1 = '测试岗位'
postName2 = '开发岗位'
# 角色
roleName1 = '测试'
roleName2 = '开发'

# 项目初始化
project = Project()


@pytest.fixture(scope='function')
def init_project():
    # 创建项目
    project.create_project(projectName=projectName,
                           templateName='基本模板',
                           userName=env.USERNAME_PM)

    # 审批通过
    project.approve_project(projectName=projectName,
                            approveDescription='ok',
                            approveStatus=1,
                            userName=env.USERNAME_PMO)


@pytest.fixture(scope='function')
def init_task():
    # 初始化项目任务
    task = Task(projectName)
    # 创建任务
    task.create_task(taskName)
    # 创建子任务
    task.create_task(subtaskName, broTaskName=taskName)


@pytest.fixture(scope='function')
def init_plan():
    # 初始化项目计划
    plan = Plan(projectName)
    # 创建测试计划
    plan.create_plan(planName=planName1)
    # 创建开发计划
    plan.create_plan(planName=planName2)
    # 创建计划任务
    plan.create_task_for_plan(planTaskName1, planName=planName1)
    plan.create_task_for_plan(planTaskName2, planName=planName2)


@pytest.fixture(scope='function')
def init_recruit_info():
    # 初始化项目招聘信息
    personnel = Personnel(projectName)
    # 测试岗位
    personnel.create_recruit(postName=postName1,
                             postSum=10,
                             postJobShare=100,
                             postType=6)
    # 开发岗位
    personnel.create_recruit(postName=postName2,
                             postSum=10,
                             postJobShare=100,
                             postType=1)


@pytest.fixture(scope='function')
def init_project_role():
    # 初始化项目角色
    # 测试
    project.create_role(roleName1, projectName=projectName, createTask=1, updateTask=1)
    # 开发
    project.create_role(roleName2, projectName=projectName, createTask=1, updateTask=1)
