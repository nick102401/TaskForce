#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_approve_01.py
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
from FastApi.scripts.conftest import projectName, postName
from FastApi.scripts.features.recruitment.positions_approve.conftest import projectName_1, roleName

log = Logger().logger
pro = Project()

recruit = Recruitment()


def setup():
    log.info('-----测试用例预制-----')
    """
    预置条件：
        1- 开发人员加入一个项目
        2- 开发人员申请项目招募岗位
    """

    global person
    person = Personnel(projectName=projectName_1, userName=env.USERNAME_PM_1)

    # 开发人员加入项目
    person.add_member(env.USERNAME_RD_Recruit_1, roleName, 10, userName=env.USERNAME_PM_1)

    # 开发人员申请项目招募岗位
    recruit.apply_position(postName, projectName, applyUserDescription=f'申请{projectName}{postName}岗位',
                           userName=env.USERNAME_RD_Recruit_1)


@pytest.mark.usefixtures('open_init_position')
@allure.feature('项目招聘')
@allure.story('岗位审批')
@allure.title('当前组长查看项目组成员的其他项目岗位申请')
def test_apply():
    """
    前置条件：
        1- 开发人员加入一个项目
        2- 开发人员申请项目招募岗位

    测试步骤：
        1- 当前项目组长查看人员岗位申请列表

    预期结果：
        1- 人员岗位申请列表能够查询到该人员申请
    """
    log.info('-----测试用例执行-----')
    # 当前项目组长查看人员岗位申请列表
    approvals = pro.query_my_approvals_by_project(projectName, userName=env.USERNAME_PM_1)
    for approval in approvals:
        pytest.assume(approval['projectName'] == projectName)


def teardown():
    log.info('-----环境操作-----')
    try:
        # # 1- 审批驳回
        recruit.approve_position_current(projectName, applyUserName=env.USERNAME_RD_Recruit_1,
                                         approveDescription='当前项目组长审批',
                                         approveStatus='2', userName=env.USERNAME_PM_1)
        # 2- 删除项目成员
        person.delete_member(env.USERNAME_RD_Recruit_1, userName=env.USERNAME_PM_1)

        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
