#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_approve_08.py
@time:2021/09/01
*/

岗位到位人数等于招聘人数时，岗位自动关闭

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
person_1 = Personnel(projectName, userName=env.USERNAME_PM)
USERNAME_RD = '19911111111'


def setup_module(module):
    log.info('-----测试用例预制-----')


@pytest.mark.usefixtures('open_init_position')
@allure.feature('项目招聘')
@allure.story('岗位审批')
@allure.title('岗位到位人数等于招聘人数时，岗位自动关闭')
def test_approve():
    """
    前置条件：
        1- 创建招募岗位，并打开岗位
        2- 两个开发人员申请其他项目岗位,并审核通过


    测试步骤：
        1- 岗位项目组长查看岗位招募信息

    预期结果：
        1- 当前岗位变为关闭状态
    """
    log.info('-----测试用例执行-----')

    # 1- 开发人员申请项目岗位
    recruit.apply_position(postName, projectName, applyUserDescription=f'申请{projectName}{postName}岗位',
                           userName=env.USERNAME_RD_Recruit_1)
    recruit.apply_position(postName, projectName, applyUserDescription=f'申请{projectName}{postName}岗位',
                           userName=USERNAME_RD)

    # # 2- 项目经理审批通过
    recruit.approve_position_goal(projectName, applyUserName=env.USERNAME_RD_Recruit_1, approveDescription='目标项目组长审批',
                                  approveStatus='1', userName=env.USERNAME_PM)

    recruit.approve_position_goal(projectName, applyUserName=USERNAME_RD, approveDescription='目标项目组长审批',
                                  approveStatus='1', userName=env.USERNAME_PM)

    recruits_list = person_1.query_recruits()['content']['data']['list']
    if recruits_list:
        for recruits in recruits_list:
            if recruits['postName'] == postName:
                assert recruits['openFlag'] == '0'
    else:
        assert False


def teardown_module(module):
    log.info('-----环境操作-----')
    try:
        # 1- 删除成员
        person_1.delete_member(env.USERNAME_RD_Recruit_1, userName=env.USERNAME_PM)
        person_1.delete_member(USERNAME_RD, userName=env.USERNAME_PM)
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)


