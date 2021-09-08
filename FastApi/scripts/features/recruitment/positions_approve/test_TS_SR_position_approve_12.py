#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_approve_12.py
@time:2021/09/02
*/

提交岗位申请后，添加人员到项目，继续进行审核驳回，审核成功

"""

import allure
import pytest

from FastApi.aws.project import Project, Personnel
from FastApi.aws.recruitment import Recruitment
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName, postName, roleName

log = Logger().logger
pro = Project()
recruit = Recruitment()
person = Personnel(projectName, userName=env.USERNAME_PM)


def setup_module(module):
    log.info('-----测试用例预制-----')


@pytest.mark.usefixtures('open_init_position')
@allure.feature('项目招聘')
@allure.story('岗位审批')
@allure.title('提交岗位申请后，添加人员到项目，继续进行审核驳回，审核成功')
def test_approve():
    """
       前置条件：
           1- 创建招募岗位，并打开岗位


       测试步骤：
           1- 开发人员申请岗位
           2- 项目经理将人员加入项目
           3- 项目经理审批驳回

       预期结果：
           1- 审批成功，该申请为已驳回状态
       """
    log.info('-----测试用例执行-----')

    # 1- 开发人员申请项目岗位
    recruit.apply_position(postName, projectName, applyUserDescription=f'申请{projectName}{postName}岗位',
                           userName=env.USERNAME_RD_Recruit_1)
    # 2- 项目经理将人员加入项目
    person.add_member(env.USERNAME_RD_Recruit_1, roleName, 10, userName=env.USERNAME_PM)

    # # 2- 项目经理审批通过
    resp = recruit.approve_position_goal(projectName, applyUserName=env.USERNAME_RD_Recruit_1, approveDescription='目标项目组长审批',
                                         approveStatus='2', userName=env.USERNAME_PM)

    assert resp['content']['code'] == 0
    assert resp['content']['data']['item']['approveStatus'] == '2'


def teardown_module(module):
    log.info('-----环境操作-----')

    # 1-  删除项目成员
    person.delete_member(env.USERNAME_RD_Recruit_1, userName=env.USERNAME_PM)

