#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:conftest.py
@time:2021/08/25
*/
"""
import time

import pytest

from FastApi.aws.project import Project, Personnel
from FastApi.conf import env
from datetime import datetime, timedelta

projectName = '接口测试' + time.strftime('%m%d', time.localtime())

startTime = datetime.strftime(datetime.now(), '%Y-%m-%d')

endTime = datetime.strftime(datetime.now() + timedelta(days=3), '%Y-%m-%d')

postName = '功能测试'
postName_1 = '自动化测试'
roleName = '测试人员'

@pytest.fixture(scope='function')
def project_init():
    pro = Project()
    # 创建项目申请
    pro.create_project(projectName=projectName,
                       startTime=startTime,
                       endTime=endTime,
                       templateName='基本模板',
                       userName=env.USERNAME_PM)
    # 创建项目申请审批通过
    pro.approve_project(projectName=projectName,
                        approveDescription='ok',
                        approveStatus=1,
                        userName=env.USERNAME_PMO)

@pytest.fixture(scope='function')
def position_init():
    pro = Project()
    pro.create_role(roleName=roleName,projectName=projectName, updateTask=1, userName=env.USERNAME_PM)
    global person
    person = Personnel(projectName=projectName, userName=env.USERNAME_PM)
    person.create_recruit(postName=postName,
                          postSum='2',
                          postType='6',
                          roleType=roleName,
                          postJobShare='10',
                          postDescription='招聘测试人员',
                          startTime=startTime,
                          endTime=endTime,
                          userName=env.USERNAME_PM)
    yield person

@pytest.fixture(scope='function')
def position_init_open(position_init):
    position_init.operate_recruit(postName,openFlag=True)




