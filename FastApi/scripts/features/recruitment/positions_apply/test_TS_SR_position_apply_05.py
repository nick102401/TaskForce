#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_apply_05.py
@time:2021/08/25
*/

申请人的剩余全时率不满足岗位要求，申请岗位失败

"""
import time

import allure
import pytest

from FastApi.aws.project import Project, Personnel
from FastApi.aws.recruitment import Recruitment
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName, startTime, endTime, roleName, postName

log = Logger().logger
pro = Project()
projectName_1 = '接口测试随机项目' + time.strftime('%m%d%H%M', time.localtime())

person = Personnel(projectName=projectName_1, userName=env.USERNAME_PM_1)
recruit = Recruitment()


def setup():
    log.info('-----测试用例预制-----')
    # # 创建项目申请
    pro.create_project(projectName=projectName_1,
                       startTime=startTime,
                       endTime=endTime,
                       templateName='基本模板',
                       userName=env.USERNAME_PM_1)
    # # 创建项目申请审批通过
    pro.approve_project(projectName=projectName_1,
                        approveDescription='ok',
                        approveStatus=1,
                        userName=env.USERNAME_PMO)
    # 创建项目角色
    pro.create_role(roleName=roleName, projectName=projectName_1, updateTask=1, userName=env.USERNAME_PM_1)
    global person
    person = Personnel(projectName=projectName_1, userName=env.USERNAME_PM_1)

    # 开发人员加入项目
    person.add_member(env.USERNAME_RD_Recruit_1, roleName, 95, userName=env.USERNAME_PM_1)


@pytest.mark.usefixtures('open_init_position')
@allure.feature('项目招聘')
@allure.story('岗位申请')
@allure.title('申请人的剩余全时率不满足岗位要求，申请岗位失败')
def test_my_apply():
    log.info('-----测试用例执行-----')

    # 申请岗位         申请人的剩余全时率不满足岗位要求
    res = recruit.apply_position(postName, projectName, applyUserDescription='剩余全时率为5%',
                                 userName=env.USERNAME_RD_Recruit_1)
    pytest.assume(res['content']['code'] == -1)
    pytest.assume(res['content']['msg'] == '剩余工时不足岗位要求')


def teardown_module():
    log.info('-----环境操作-----')

    person.delete_member(env.USERNAME_RD_Recruit_1, userName=env.USERNAME_PM_1)
