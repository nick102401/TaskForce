#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_approve_10.py
@time:2021/09/01
*/

岗位关闭后，继续审批提交的岗位申请，申请失败

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
@allure.title('岗位关闭后，继续审批提交的岗位申请,申请失败')
def test_approve():
    """
      前置条件：
          1- 创建招募岗位，并打开岗位
          2- 关闭招募岗位


      测试步骤：
          1- 开发人员查看关闭的招募岗位

      预期结果：
          1- 无法查看
      """
    log.info('-----测试用例执行-----')

    # 关闭岗位开关
    person.operate_recruit(postName, openFlag=False)

    # 开发人员查询岗位
    resp = recruit.query_position_by_project(postName, projectName, userName=env.USERNAME_RD_Recruit_1)
    assert not resp  # 开发人员无法查看已关闭岗位


def teardown_module(module):
    log.info('-----环境操作-----')

