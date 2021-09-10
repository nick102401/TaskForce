#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_apply_01.py
@time:2021/08/25
*/

开发人员申请岗位

"""
import time

import allure
import pytest

from FastApi.aws.project import Project, Personnel
from FastApi.aws.recruitment import Recruitment
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName, postName

log = Logger().logger
pro = Project()

person_1 = Personnel(projectName=projectName, userName=env.USERNAME_PM)
recruit = Recruitment()


def setup():
    log.info('-----测试用例预制-----')


@pytest.mark.usefixtures('open_init_position')
@allure.feature('项目招聘')
@allure.story('岗位申请')
@allure.title('开发人员成功申请岗位')
def test_apply_recruitment_1():
    """
    前置条件：
        1- 创建招募岗位，并打开岗位

    测试步骤：
        1- 开发人员申请岗位

    预期结果：
        1- 申请成功，产生applyId
    """
    res = recruit.apply_position(postName, projectName, applyUserDescription='', userName=env.USERNAME_RD_Recruit_1)
    pytest.assume(res['content']['code'] == 0)
    pytest.assume(res['content']['data']['item']['applyId'])


def teardown():
    log.info('-----环境操作-----')
    try:
        # 目标项目组长审批驳回
        recruit.approve_position_goal(projectName, applyUserName=env.USERNAME_RD_Recruit_1,
                                      approveDescription=f'目标项目组长审批{time.localtime()}',
                                      approveStatus='2', userName=env.USERNAME_PM)
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
