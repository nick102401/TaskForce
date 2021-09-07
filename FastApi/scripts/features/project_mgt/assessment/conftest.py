#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:conftest.py
@time:2021/09/03
*/

用例标题/描述
"""

import pytest

from FastApi.aws.project import Project, Personnel
from FastApi.common.helper import get_timestamp
from FastApi.common.yaml_handle import read_data_from_file
from FastApi.conf import env

# 加载预置数据
file_name = 'preset_project_body.yaml'
preset_data = read_data_from_file(file_name)
preset_role_data_1 = preset_data['PRESET_ROLE_1']  # 项目角色
preset_role_data_2 = preset_data['PRESET_ROLE_2']  # 项目角色

# 生成随机字符串
projectName = '项目综评测试-' + str(get_timestamp())
projectName1 = '项目综评测试1-' + str(get_timestamp())

# 项目初始化
project = Project()


@pytest.fixture(scope='function')
def init_project_and_member():
    # 创建项目申请
    project.create_project(projectName=projectName,
                           userName=env.USERNAME_PM)
    # 创建项目申请审批通过
    project.approve_project(projectName=projectName,
                            approveDescription='ok',
                            approveStatus=1,
                            userName=env.USERNAME_PMO)

    # 初始化项目角色
    # 测试
    project.create_role(roleName=preset_role_data_1['roleName'],
                        projectName=projectName,
                        manage=preset_role_data_1['manage'],
                        createTask=preset_role_data_1['createTask'],
                        updateTask=preset_role_data_1['updateTask'],
                        filterType=preset_role_data_1['filterType'],
                        userName=env.USERNAME_PM)
    # 开发
    project.create_role(roleName=preset_role_data_2['roleName'],
                        projectName=projectName,
                        manage=preset_role_data_2['manage'],
                        createTask=preset_role_data_2['createTask'],
                        updateTask=preset_role_data_2['updateTask'],
                        filterType=preset_role_data_2['filterType'],
                        userName=env.USERNAME_PM)

    # 项目人员
    personnel = Personnel(projectName)
    # 添加职能人员
    personnel.add_member(memberName=env.USERNAME_PG,
                         roleName=preset_role_data_1['roleName'],
                         percent=1,
                         userName=env.USERNAME_PM)
    # 添加开发人员
    personnel.add_member(memberName=env.USERNAME_RD,
                         roleName=preset_role_data_2['roleName'],
                         percent=1,
                         userName=env.USERNAME_PM)

    return projectName


@pytest.fixture(scope='function')
def init_project_and_member_1():
    # 创建项目申请
    project.create_project(projectName=projectName1,
                           userName=env.USERNAME_PM)
    # 创建项目申请审批通过
    project.approve_project(projectName=projectName1,
                            approveDescription='ok',
                            approveStatus=1,
                            userName=env.USERNAME_PMO)

    # 初始化项目角色
    # 测试
    project.create_role(roleName=preset_role_data_1['roleName'],
                        projectName=projectName1,
                        manage=preset_role_data_1['manage'],
                        createTask=preset_role_data_1['createTask'],
                        updateTask=preset_role_data_1['updateTask'],
                        filterType=preset_role_data_1['filterType'],
                        userName=env.USERNAME_PM)
    # 开发
    project.create_role(roleName=preset_role_data_2['roleName'],
                        projectName=projectName1,
                        manage=preset_role_data_2['manage'],
                        createTask=preset_role_data_2['createTask'],
                        updateTask=preset_role_data_2['updateTask'],
                        filterType=preset_role_data_2['filterType'],
                        userName=env.USERNAME_PM)

    # 项目人员
    personnel = Personnel(projectName1)
    # 添加职能人员
    personnel.add_member(memberName=env.USERNAME_PG,
                         roleName=preset_role_data_1['roleName'],
                         percent=1,
                         userName=env.USERNAME_PM)
    # 添加开发人员
    personnel.add_member(memberName=env.USERNAME_RD,
                         roleName=preset_role_data_2['roleName'],
                         percent=1,
                         userName=env.USERNAME_PM)

    return projectName1
