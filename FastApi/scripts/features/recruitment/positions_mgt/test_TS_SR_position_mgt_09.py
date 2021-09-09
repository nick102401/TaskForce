#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_mgt_09.py
@time:2021/09/01
*/

普通用户登录账号时，不能进行项目岗位管理操作

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
person_1 = Personnel(projectName, userName=env.USERNAME_PM)
USERNAME_RD = '19911111111'


def setup_module(module):
    log.info('-----测试用例预制-----')

@pytest.mark.xfail(reason='接口无权限校验')
@pytest.mark.usefixtures('init_position')
@allure.feature('项目招聘')
@allure.story('岗位审批')
@allure.title('普通用户登录账号时，不能进行项目岗位管理操作')
def test_approve():
    """
    前置条件：
        1- 创建项目
        2- 开发人员加入项目


    测试步骤：
        1- 开发人员查看项目岗位
        2- 开发人员打开岗位
        3- 开发人员修改岗位

    预期结果：
        1- 开发人员查看项目岗位失败
        2- 开发人员打开岗位失败
        3- 开发人员修改岗位失败


    """
    log.info('-----测试用例执行-----')
    person_1.add_member(USERNAME_RD,roleName,userName=env.USERNAME_PM)
    person = Personnel(projectName, userName=USERNAME_RD)

    recruits_list = person.query_recruits(userName=USERNAME_RD)
    pytest.assume(not recruits_list)

    resp = person.operate_recruit(postName, openFlag=True,userName=USERNAME_RD)
    pytest.assume(not resp)

    resp = person.modify_recruit(postName, userName=env.USERNAME_PM, postJobShare='50')
    pytest.assume(not resp)


def teardown_module(module):
    log.info('-----环境操作-----')
    try:
        # 1- 删除成员
        person_1.delete_member(USERNAME_RD, userName=env.USERNAME_PM)
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)


