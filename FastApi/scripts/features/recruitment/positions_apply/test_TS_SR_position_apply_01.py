#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_mgt_02.py
@time:2021/08/25
*/

开发人员申请岗位

"""

import allure
import pytest
from FastApi.aws.project import Project, Personnel
from FastApi.aws.recruitment import Recruitment
from FastApi.common.logs_handle import Logger
from FastApi.common.yaml_handle import read_data_from_file_to_params
from FastApi.conf import env
from FastApi.scripts.features.recruitment.conftest import projectName, postName, startTime, endTime

log = Logger().logger
pro = Project()

person = Personnel(projectName=projectName, userName=env.USERNAME_PM)
recruit = Recruitment()
def setup():
    log.info('-----测试用例预制-----')




@pytest.mark.usefixtures('position_init_open')
@allure.feature('项目招聘')
@allure.story('岗位管理')
@allure.title('开发人员查看项目招聘信息')
def test_project_recruitment_all():
    res = recruit.query_project_recruitment(userName=env.USERNAME_RD)
    print(res)
    assert  res['content']['code'] == 0
    assert  res['content']['data']['list'] is not None


@pytest.mark.usefixtures('position_init_open')
@allure.feature('项目招聘')
@allure.story('岗位申请')
@allure.title('开发人员申请岗位')
def test_apply_recruitment():
    res = recruit.apply_position(postName, projectName, applyUserDescription='', userName=env.USERNAME_RD)
    assert res['content']['code'] == 0
    assert res['content']['data']['item']['applyId']


@allure.feature('项目招聘')
@allure.story('岗位申请')
@allure.title('开发人员查看岗位申请结果')
def test_my_apply():
    res = recruit.query_my_apply_by_project(projectName,userName=env.USERNAME_RD)
    assert res['projectName'] == projectName


def teardown_module():
    log.info('-----环境操作-----')
    res = person.query_recruits()
    for one in res['content']['data']['list']:
        post = one['postName']
        person.delete_recruit(postName=post)
