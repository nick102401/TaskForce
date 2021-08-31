#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_mgt_02.py
@time:2021/08/30
*/

当前组长查看项目组成员的其他项目岗位申请

"""

import allure
import pytest
from FastApi.aws.project import Project, Personnel
from FastApi.aws.recruitment import Recruitment
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.features.recruitment.conftest import projectName, postName, postName_1, roleName, startTime, \
    endTime, projectName_new

log = Logger().logger
pro = Project()


recruit = Recruitment()


def setup_module(module):
    log.info('-----测试用例预制-----')


    # # 创建项目申请
    pro.create_project(projectName=projectName_new,
                       startTime=startTime,
                       endTime=endTime,
                       templateName='基本模板',
                       userName=env.USERNAME_PM_1)
    # # 创建项目申请审批通过
    pro.approve_project(projectName=projectName_new,
                        approveDescription='ok',
                        approveStatus=1,
                        userName=env.USERNAME_PMO)
    # 创建项目角色
    pro.create_role(roleName=roleName, projectName=projectName_new, updateTask=1, userName=env.USERNAME_PM_1)
    global person
    person = Personnel(projectName=projectName_new, userName=env.USERNAME_PM_1)

    # 开发人员加入项目
    person.add_member('sun', roleName, 10, userName=env.USERNAME_PM_1)


@pytest.mark.usefixtures('position_init_open')
@allure.feature('项目招聘')
@allure.story('岗位申请')
@allure.title('当前组长查看项目组成员的其他项目岗位申请')
def test_apply():
    log.info('-----测试用例执行-----')


    # 1- 开发人员申请其他项目岗位
    recruit.apply_position(postName, projectName, applyUserDescription=f'申请{projectName}{postName}岗位', userName=env.USERNAME_RD)
    # 当前项目组长查看人员岗位申请列表
    approvals = pro.query_my_approvals(userName=env.USERNAME_PM_1)['content']['data']['list']
    for approval in approvals:
        if approval['projectName'] == projectName and approval['postName'] == postName:
            assert approval['approveStatus'] == '2'










def teardown_module(module):
    log.info('-----环境操作-----')
    # 1- 审批驳回
    recruit.approve_position_current(projectName, applyUserName=env.USERNAME_RD, approveDescription='当前项目组长审批',
                                  approveStatus='2', userName=env.USERNAME_PM_1)
    # 2- 删除项目成员
    person.delete_member(projectName_new,env.USERNAME_RD,env.USERNAME_PM_1)

    # 1- 删除招募信息
    person1 = Personnel(projectName=projectName, userName=env.USERNAME_PM)
    res = person1.query_recruits()
    for one in res['content']['data']['list']:
        post = one['postName']
        person1.delete_recruit(postName=post)

    # 2- 删除项目角色
    roles_list = person1.query_roles(projectName)['content']['data']['list']
    if roles_list:
        for role in roles_list:
            if role['roleName'] != '项目管理':
                person1.delete_role(role['roleName'], projectName)