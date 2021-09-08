#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:conftest.py
@time:2021/09/03
*/
"""
import time
from datetime import datetime, timedelta

import pytest

from FastApi.aws.project import Project
from FastApi.conf import env

project = Project()
projectName_1 = '接口测试当前项目A' + time.strftime('%m%d%H%M', time.localtime())
projectName_2 = '接口测试当前项目B' + time.strftime('%m%d%H%M', time.localtime())
startTime = datetime.strftime(datetime.now(), '%Y-%m-%d')
endTime = datetime.strftime(datetime.now() + timedelta(days=3), '%Y-%m-%d')
roleName = '功能测试'

@pytest.fixture(scope='session', autouse=True)
def init_project():
    # 创建项目申请projectName_1
    project.create_project(projectName=projectName_1,
                           startTime=startTime,
                           endTime=endTime,
                           templateName='基本模板',
                           userName=env.USERNAME_PM_1)
    # 创建项目申请审批通过
    project.approve_project(projectName=projectName_1,
                            approveDescription='ok',
                            approveStatus=1,
                            userName=env.USERNAME_PMO)
    project.create_role(roleName=roleName, projectName=projectName_1, updateTask=1, userName=env.USERNAME_PM_1)




    # 创建项目申请projectName_2
    project.create_project(projectName=projectName_2,
                           startTime=startTime,
                           endTime=endTime,
                           templateName='基本模板',
                           userName=env.USERNAME_PM_2)
    # 创建项目申请审批通过
    project.approve_project(projectName=projectName_2,
                            approveDescription='ok',
                            approveStatus=1,
                            userName=env.USERNAME_PMO)

    project.create_role(roleName=roleName, projectName=projectName_2, updateTask=1, userName=env.USERNAME_PM_2)


