#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_apply_04.py
@time:2021/08/25
*/

开发人员申请当前参与项目的岗位，申请岗位失败

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

person = Personnel(projectName=projectName, userName=env.USERNAME_PM)
recruit = Recruitment()


def setup_module():
    log.info('-----测试用例预制-----')
    # 添加项目成员
    person.add_member(env.USERNAME_RD_Recruit_1, roleName=roleName, percent=10, userName=env.USERNAME_PM)


@pytest.mark.usefixtures('open_init_position')
@allure.feature('项目招聘')
@allure.story('岗位申请')
@allure.title('开发人员申请当前参与项目的岗位，申请岗位失败')
def test_apply():
    log.info('-----测试用例执行-----')
    # 申请岗位
    res = recruit.apply_position(postName, projectName, applyUserDescription='该人员已在项目中',
                                 userName=env.USERNAME_RD_Recruit_1)
    pytest.assume(res['content']['code'] == -1)
    pytest.assume(res['content']['msg'] == '已在项目中，不可申请')


def teardown_module():
    log.info('-----环境操作-----')
    person.delete_member(env.USERNAME_RD_Recruit_1, userName=env.USERNAME_PM)

