#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_mgt_02.py
@time:2021/08/25
*/

项目经理查看项目招聘信息
"""

import allure
import pytest
from FastApi.scripts.conftest import projectName, postName

from FastApi.aws.project import Project, Personnel
from FastApi.aws.recruitment import Recruitment
from FastApi.common.logs_handle import Logger
from FastApi.conf import env

log = Logger().logger
pro = Project()

person = Personnel(projectName=projectName, userName=env.USERNAME_PM)
rec = Recruitment()


def setup():
    log.info('-----测试用例预制-----')


@pytest.mark.usefixtures('init_position')
@allure.feature('项目招聘')
@allure.story('岗位管理')
@allure.title('项目经理查看项目招聘关闭岗位')
def test_projectRecuitment():
    res = rec.query_recruitment_by_project(projectName)
    assert res['content']['code'] == 0
    projectRecruit = res['content']['data']['item']['projectRecruit']
    if projectRecruit:
        for recruit in projectRecruit:
            if recruit['postName'] == postName:
                assert recruit['openFlag'] == '0'
    else:
        assert False


@pytest.mark.usefixtures('open_init_position')
@allure.feature('项目招聘')
@allure.story('岗位管理')
@allure.title('项目经理查看项目招聘打开岗位')
def test_projectRecuitment():
    res = rec.query_recruitment_by_project(projectName)
    assert res['content']['code'] == 0
    projectRecruit = res['content']['data']['item']['projectRecruit']
    if projectRecruit:
        for recruit in projectRecruit:
            if recruit['postName'] == postName:
                assert recruit['openFlag'] == '1'
    else:
        assert False


@pytest.mark.usefixtures('open_init_position')
@allure.feature('项目招聘')
@allure.story('岗位管理')
@allure.title('项目经理查看已打开招聘岗位详细信息')
def test_positionInfo_open():
    res = rec.query_position_info_by_name(postName, projectName)
    assert res['postName'] == postName
    assert res['openFlag'] == '1'


@pytest.mark.usefixtures('init_position')
@allure.feature('项目招聘')
@allure.story('岗位管理')
@allure.title('项目经理查看已关闭招聘岗位详细信息')
def test_positionInfo_close():
    res = rec.query_position_info_by_name(postName, projectName)
    assert res['postName'] == postName
    assert res['openFlag'] == '0'


def teardown_module():
    log.info('-----环境操作-----')
