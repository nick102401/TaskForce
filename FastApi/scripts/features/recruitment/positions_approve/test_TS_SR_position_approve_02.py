#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_approve_02.py
@time:2021/08/30
*/

当前组长对项目组成员的其他项目岗位申请审批通过

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
     """
    global person
    person = Personnel(projectName=projectName_1, userName=env.USERNAME_PM_1)

    # # # 开发人员加入项目
    person.add_member(env.USERNAME_RD_Recruit_1, roleName, 10, userName=env.USERNAME_PM_1)


@pytest.mark.usefixtures('open_init_position')
@allure.feature('项目招聘')
@allure.story('岗位审批')
@allure.title('当前组长对项目组成员的其他项目岗位申请审批通过')
def test_approve():
    """
    前置条件：
        1- 创建招募岗位，并打开岗位
        2- 开发人员申请其他项目岗位


    测试步骤：
        1- 当前项目组长审批通过

    预期结果：
        1- 当前项目组长审批状态为已通过
        2- 进入目标项目组长审批

    """
    log.info('-----测试用例执行-----')
    #
    # # 1- 开发人员申请其他项目岗位
    recruit.apply_position(postName, projectName, applyUserDescription=f'申请{projectName}{postName}岗位',
                           userName=env.USERNAME_RD_Recruit_1)
    #
    # # 2- 当前项目组长审批通过
    resp = recruit.approve_position_current(projectName, applyUserName=env.USERNAME_RD_Recruit_1,
                                            approveDescription='当前项目组长审批',
                                            approveStatus='1', userName=env.USERNAME_PM_1)
    pytest.assume(resp['content']['code'] == 0)
    pytest.assume(resp['content']['data']['item']['approveStatus'] == '1')
    #
    # # 3- 待目标项目组长审批
    positions = recruit.get_approve_position_goal_by_postName(projectName, postName, userName=env.USERNAME_PM)
    for position in positions:
        if position['applyUserId'] == Personnel.get_user_info(userName=env.USERNAME_RD_Recruit_1, userId=True):
            pytest.assume(position['approveStatus'] == '0')


def teardown():
    log.info('-----环境操作-----')

    try:
        # 1- 目标项目组长审批驳回
        recruit.approve_position_goal(projectName, applyUserName=env.USERNAME_RD_Recruit_1,
                                      approveDescription='目标项目组长审批',
                                      approveStatus='2', userName=env.USERNAME_PM)
        # # 2- 删除项目成员
        person.delete_member(env.USERNAME_RD_Recruit_1, env.USERNAME_PM_1)
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
