#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_approve_07.py
@time:2021/09/01
*/

岗位申请被岗位项目组长审核通过，申请人能够自动加入项目组

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
person = Personnel(projectName, userName=env.USERNAME_PM)


def setup_module(module):
    log.info('-----测试用例预制-----')


@pytest.mark.usefixtures('open_init_position')
@allure.feature('项目招聘')
@allure.story('岗位审批')
@allure.title('岗位申请被岗位项目组长审核通过，申请人能够自动加入项目组')
def test_approve():
    """
    前置条件：
        1- 创建招募岗位，并打开岗位
        2- 开发人员申请其他项目岗位


    测试步骤：
        1- 岗位项目组长审核通过

    预期结果：
        1- 申请人自动加入项目组
    """
    log.info('-----测试用例执行-----')

    # 1- 开发人员申请项目岗位
    recruit.apply_position(postName, projectName, applyUserDescription=f'申请{projectName}{postName}岗位',
                           userName=env.USERNAME_RD_Recruit_1)

    # # 2- 项目经理审批通过
    recruit.approve_position_goal(projectName, applyUserName=env.USERNAME_RD_Recruit_1, approveDescription='目标项目组长审批',
                                  approveStatus='1', userName=env.USERNAME_PM)
    member_list = person.query_personnels(userName=env.USERNAME_PM)['content']['data']['list']
    flag = 0
    for member in member_list:
        if member['operatorNo'] == env.USERNAME_RD_Recruit_1:
            flag = 1
    assert flag


def teardown_module(module):
    log.info('-----环境操作-----')

    # 1- 删除成员
    person.delete_member(env.USERNAME_RD_Recruit_1, userName=env.USERNAME_PM)


