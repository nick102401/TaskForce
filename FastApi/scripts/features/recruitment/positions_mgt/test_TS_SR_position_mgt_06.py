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
from FastApi.aws.project import Project, Personnel
from FastApi.aws.recruitment import Recruitment
from FastApi.common.logs_handle import Logger
from FastApi.common.yaml_handle import read_data_from_file_to_params
from FastApi.conf import env
from FastApi.scripts.features.recruitment.conftest import projectName, postName

log = Logger().logger
pro = Project()

person = Personnel(projectName=projectName, userName=env.USERNAME_PM)
rec = Recruitment()
def setup():
    log.info('-----测试用例预制-----')



@allure.feature('项目招聘')
@allure.story('岗位管理')
@allure.title('项目经理查看项目招聘信息')
def test_projectRecuitment():
    res = rec.query_recruitment_by_project(projectName)
    print(res)
    assert  res['content']['code'] == 0
    assert  res['content']['data']['item']['projectRecruit'] is not None






@pytest.mark.usefixtures('position_init_open')
@allure.feature('项目招聘')
@allure.story('岗位管理')
@allure.title('项目经理查看招聘岗位信息')
def test_positionInfo():
    res = rec.query_position_info_by_name(postName,projectName)
    print(res)
    assert  res['postName'] == postName































def teardown_module():
    log.info('-----环境操作-----')
    res = person.query_recruits()
    for one in res['content']['data']['list']:
        post = one['postName']
        person.delete_recruit(postName=post)
