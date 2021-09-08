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

person_1 = Personnel(projectName=projectName, userName=env.USERNAME_PM)
recruit = Recruitment()


def setup_module():
    log.info('-----测试用例预制-----')
    # 添加项目成员
    person_1.add_member(env.USERNAME_RD_Recruit_1, roleName=roleName, percent=10, userName=env.USERNAME_PM)


@pytest.mark.usefixtures('open_init_position')
@allure.feature('项目招聘')
@allure.story('岗位申请')
@allure.title('开发人员申请当前参与项目的岗位，申请岗位失败')
def test_apply():
    """
    前置条件：
        1- 创建招募岗位，并打开岗位
        2- 开发人员加入项目
    测试步骤：
        1- 开发人员申请项目岗位
    预期结果：
        1- 申请失败，提示'已在项目中，不可申请'
    """
    log.info('-----测试用例执行-----')
    # 申请岗位
    res = recruit.apply_position(postName, projectName, applyUserDescription='该人员已在项目中',
                                 userName=env.USERNAME_RD_Recruit_1)
    pytest.assume(res['content']['code'] == -1)
    pytest.assume(res['content']['msg'] == '已在项目中，不可申请')


def teardown_module():
    log.info('-----环境操作-----')

    try:
        person_1.delete_member(env.USERNAME_RD_Recruit_1, userName=env.USERNAME_PM)
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
