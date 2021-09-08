#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_apply_08.py
@time:2021/08/25
*/

开发人员申请岗位被拒绝后，继续申请此岗位，申请成功

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
person_1 = Personnel(projectName=projectName, userName=env.USERNAME_PM)


def setup():
    log.info('-----测试用例预制-----')


@pytest.mark.usefixtures('open_init_position')
@allure.feature('项目招聘')
@allure.story('岗位申请')
@allure.title('开发人员申请岗位被拒绝后，继续申请此岗位，申请成功')
def test_apply():
    """
    前置条件：
        1- 创建项目招募岗位，打开岗位
    测试步骤：
        1- 开发人员申请项目岗位招募岗位,审批驳回
        2- 开发人员继续申请已驳回招募岗位
    预期结果：
        1- 申请成功
    """
    log.info('-----测试用例执行-----')

    # 1- 申请岗位
    recruit.apply_position(postName, projectName, applyUserDescription=f'第一次申请{projectName}{postName}岗位',
                           userName=env.USERNAME_RD_Recruit_1)

    # 2- 审批驳回
    recruit.approve_position_goal(projectName, applyUserName=env.USERNAME_RD_Recruit_1,
                                  approveDescription=f'申请{projectName}{postName}岗位审批驳回',
                                  approveStatus='2', userName=env.USERNAME_PM)

    # 3- 申请岗位
    res = recruit.apply_position(postName, projectName,
                                 applyUserDescription=f'第一次申请审批驳回后，再次申请{projectName}{postName}岗位',
                                 userName=env.USERNAME_RD_Recruit_1)
    assert res['content']['code'] == 0
    assert res['content']['msg'] == 'success'


def teardown():
    log.info('-----环境操作-----')
    try:
        # 1- 审批驳回
        recruit.approve_position_goal(projectName, applyUserName=env.USERNAME_RD_Recruit_1, approveDescription='接口测试描述',
                                      approveStatus='2', userName=env.USERNAME_PM)
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)


