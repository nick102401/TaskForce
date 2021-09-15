#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_approve_09.py
@time:2021/09/01
*/

岗位申请被岗位项目组长审核驳回，加入项目失败

"""

import allure
import pytest

from FastApi.aws.project import Personnel
from FastApi.aws.recruitment import Recruitment
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName, postName

log = Logger().logger
recruit = Recruitment()
person_1 = Personnel(projectName, userName=env.USERNAME_PM)


def setup_module(module):
    log.info('-----测试用例预制-----')


@pytest.mark.usefixtures('open_init_position')
@allure.feature('项目招聘')
@allure.story('岗位审批')
@allure.title('岗位申请被岗位项目组长审核驳回，加入项目失败')
def test_approve():
    """
    前置条件：
        1- 创建招募岗位，并打开岗位
        2- 两个开发人员申请其他项目岗位


    测试步骤：
        1- 岗位项目组长审批驳回

    预期结果：
        1- 当前岗位申请变为已驳回状态
        2- 该人员未加入项目
    """
    log.info('-----测试用例执行-----')

    # 1- 开发人员申请项目岗位
    recruit.apply_position(postName, projectName, applyUserDescription=f'申请{projectName}{postName}岗位',
                           userName=env.USERNAME_RD_Recruit_1)

    # # 2- 项目经理审批驳回
    resp = recruit.approve_position_goal(projectName, applyUserName=env.USERNAME_RD_Recruit_1,
                                         approveDescription='目标项目组长审批',
                                         approveStatus='2', userName=env.USERNAME_PM)
    pytest.assume(resp['content']['code'] == 0)
    pytest.assume(resp['content']['data']['item']['approveStatus'] == '2')
    # 3- 查询项目成员
    member_list = person_1.query_persons(userName=env.USERNAME_PM)['content']['data']['list']
    flag = 1
    for member in member_list:
        if member['operatorNo'] == env.USERNAME_RD_Recruit_1:
            flag = 0
    pytest.assume(flag)


def teardown_module(module):
    log.info('-----环境操作-----')
