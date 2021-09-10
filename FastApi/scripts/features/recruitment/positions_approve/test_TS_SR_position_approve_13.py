#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_approve_13.py
@time:2021/09/02
*/

两个用户同时申请招募人数为1的岗位，审批能够正确处理
"""

import allure
import pytest

from FastApi.aws.project import Project, Personnel
from FastApi.aws.recruitment import Recruitment
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName, postName

log = Logger().logger

project = Project()
recruit = Recruitment()
person_1 = Personnel(projectName, userName=env.USERNAME_PM)
USERNAME_RD = '19911111111'


def setup():
    log.info('-----测试用例预制-----')


@pytest.mark.usefixtures('open_init_position')
@allure.feature('项目招聘')
@allure.story('岗位审批')
@allure.title('两个用户同时申请招募人数为1的岗位，审批能够正确处理')
def test_step():
    """
          前置条件：
              1- 创建招募岗位，并打开岗位，岗位招募人数为1
              2- 开发人员1申请岗位
              3- 开发人员2申请岗位


          测试步骤：
              1- 项目经理审批通过申请2
              2- 项目经理审批通过申请1
              3- 项目经理审批驳回申请1

          预期结果：
              1- 项目经理审批通过申请2审批成功，该申请为已通过状态，岗位自动关闭
              2- 项目经理审批通过申请1审批失败，提示'到位人数已满'
              3- 项目经理审批驳回申请1审批成功，该申请为已驳回状态
    """
    log.info('-----测试用例执行-----')

    # 1- 修改招聘岗位为1
    person_1.modify_recruit(postName, postSum='1')

    # 2- 开发人员申请项目岗位1
    recruit.apply_position(postName, projectName, applyUserDescription=f'申请{projectName}{postName}岗位',
                           userName=env.USERNAME_RD_Recruit_1)
    # 3- 开发人员申请项目岗位2
    recruit.apply_position(postName, projectName, applyUserDescription=f'申请{projectName}{postName}岗位',
                           userName=USERNAME_RD)

    # 4- 项目经理审批通过申请2
    resp = recruit.approve_position_goal(projectName, applyUserName=USERNAME_RD, approveDescription='目标项目组长审批',
                                         approveStatus='1', userName=env.USERNAME_PM)
    pytest.assume(resp['content']['code'] == 0)
    pytest.assume(resp['content']['data']['item']['approveStatus'] == '1')

    # 5- 项目经理审批通过申请1
    resp = recruit.approve_position_goal(projectName, applyUserName=env.USERNAME_RD_Recruit_1,
                                         approveDescription='目标项目组长审批',
                                         approveStatus='1', userName=env.USERNAME_PM)
    pytest.assume(resp['content']['code'] == -1)
    pytest.assume(resp['content']['msg'] == '到位人数已满')

    # 6- 项目经理审批驳回申请1
    resp = recruit.approve_position_goal(projectName, applyUserName=env.USERNAME_RD_Recruit_1,
                                         approveDescription='目标项目组长审批',
                                         approveStatus='2', userName=env.USERNAME_PM)
    pytest.assume(resp['content']['code'] == 0)
    pytest.assume(resp['content']['data']['item']['approveStatus'] == '2')


def teardown():
    log.info('-----环境操作-----')
    try:
        # 1- 删除项目成员
        person_1.delete_member(USERNAME_RD, userName=env.USERNAME_PM)
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
