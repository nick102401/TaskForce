#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_apply_01.py
@time:2021/08/25
*/

开发人员查看项目招聘岗位

"""

import allure
import pytest

from FastApi.aws.project import Project, Personnel
from FastApi.aws.recruitment import Recruitment
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName

log = Logger().logger
pro = Project()

person = Personnel(projectName=projectName, userName=env.USERNAME_PM)
recruit = Recruitment()


def setup_module(module):
    log.info('-----测试用例预制-----')


@pytest.mark.usefixtures('open_init_position')
@allure.feature('项目招聘')
@allure.story('岗位申请')
@allure.title('开发人员查看项目招聘已打开岗位')
def test_project_recruitment_all():
    res = recruit.query_project_recruitment(userName=env.USERNAME_RD_Recruit_1)
    pytest.assume(res['content']['code'] == 0)
    flag = 0
    if res['content']['data']['list']:
        for rec in res['content']['data']['list']:
            if rec['projectName'] == projectName:
                flag = 1
                pytest.assume(rec['projectRecruit'] is not None)
    else:
        assert False
    pytest.assume(flag)


@pytest.mark.usefixtures('init_position')
@allure.feature('项目招聘')
@allure.story('岗位申请')
@allure.title('开发人员无法查看项目招聘未打开岗位')
def test_project_recruitment_all():
    res = recruit.query_project_recruitment(userName=env.USERNAME_RD_Recruit_1)
    pytest.assume(res['content']['code'] == 0)
    flag = 1
    if res['content']['data']['list']:
        for rec in res['content']['data']['list']:
            if rec['projectName'] == projectName:
                flag = 0
    else:
        pytest.assume(True)
    pytest.assume(flag)


def teardown_module(module):
    log.info('-----环境操作-----')
