#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_approve_06.py
@time:2021/09/01
*/

测试岗位项目组长能够查看所有岗位申请

"""

import allure
import pytest

from FastApi.aws.project import Project, Personnel
from FastApi.aws.recruitment import Recruitment
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName, postName

log = Logger().logger
pro = Project()

recruit = Recruitment()
USERNAME_RD = '19911111111'


def setup():
    log.info('-----测试用例预制-----')


@pytest.mark.usefixtures('open_init_position')
@allure.feature('项目招聘')
@allure.story('岗位审批')
@allure.title('测试岗位项目组长能够查看所有岗位申请')
def test_approve():
    """
    前置条件：
        1- 创建招募岗位，并打开岗位
        2- 开发人员申请其他项目岗位


    测试步骤：
        1- 岗位项目组长查看所有岗位申请
        2- 项目经理审批驳回申请
        3- 驳回后岗位项目组长查看所有岗位申请

    预期结果：
        1- 岗位项目组长成功查看所有岗位申请，岗位状态变更正确
    """
    log.info('-----测试用例执行-----')

    # 1- 开发人员申请其他项目岗位
    recruit.apply_position(postName, projectName, applyUserDescription=f'申请{projectName}{postName}岗位',
                           userName=env.USERNAME_RD_Recruit_1)
    recruit.apply_position(postName, projectName, applyUserDescription=f'申请{projectName}{postName}岗位',
                           userName=USERNAME_RD)

    # 2- 岗位项目组长查看所有岗位申请
    apply_list = recruit.get_approve_position_goal_by_postName(projectName, postName, userName=env.USERNAME_PM)
    flag = -1
    for apply in apply_list:
        if apply['applyUserId'] == Personnel.get_user_info(userName=env.USERNAME_RD_Recruit_1, userId=True) and apply[
            'approveStatus'] == '0':
            flag += 1
        if apply['applyUserId'] == Personnel.get_user_info(userName=USERNAME_RD, userId=True) and apply[
            'approveStatus'] == '0':
            flag += 1
    pytest.assume(flag)

    # 3- 项目经理审批驳回申请
    recruit.approve_position_goal(projectName, applyUserName=env.USERNAME_RD_Recruit_1, approveDescription='目标项目组长审批',
                                  approveStatus='2', userName=env.USERNAME_PM)

    recruit.approve_position_goal(projectName, applyUserName=USERNAME_RD, approveDescription='目标项目组长审批',
                                  approveStatus='2', userName=env.USERNAME_PM)

    # 4- 驳回后岗位项目组长查看所有岗位申请
    apply_list = recruit.get_approve_position_goal_by_postName(projectName, postName, userName=env.USERNAME_PM)
    flag = -1
    if apply_list:
        for apply in apply_list:
            if apply['applyUserId'] == Personnel.get_user_info(userName=env.USERNAME_RD_Recruit_1, userId=True) and \
                    apply[
                        'approveStatus'] == '2':
                flag += 1
            if apply['applyUserId'] == Personnel.get_user_info(userName=USERNAME_RD, userId=True) and apply[
                'approveStatus'] == '2':
                flag += 1
        pytest.assume(flag)
    else:
        pytest.assume(False)


def teardown():
    log.info('-----环境操作-----')
