#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_mgt_02.py
@time:2021/08/25
*/

开发人员申请当前参与项目的岗位，申请岗位失败

"""

import allure
import pytest
from FastApi.aws.project import Project, Personnel
from FastApi.aws.recruitment import Recruitment
from FastApi.common.logs_handle import Logger
from FastApi.common.yaml_handle import read_data_from_file_to_params
from FastApi.conf import env
from FastApi.scripts.features.recruitment.conftest import projectName, postName, startTime, endTime, roleName

log = Logger().logger
pro = Project()

person = Personnel(projectName=projectName, userName=env.USERNAME_PM)
recruit = Recruitment()


@pytest.mark.usefixtures('position_init_open')
def setup_module():
    log.info('-----测试用例预制-----')
    # 添加项目成员
    person.add_member('sun', roleName=roleName, percent=10, userName=env.USERNAME_PM)


@allure.feature('项目招聘')
@allure.story('岗位申请')
@allure.title('开发人员申请当前参与项目的岗位，申请岗位失败')
def test_apply():
    # 申请岗位
    res = recruit.apply_position(postName, projectName, applyUserDescription='该人员已在项目中', userName=env.USERNAME_RD)
    assert res['content']['code'] == -1
    assert res['content']['msg'] == '已在项目中，不可申请'


def teardown_module():
    log.info('-----环境操作-----')
    # 1- 删除招募信息
    res = person.query_recruits()
    for one in res['content']['data']['list']:
        post = one['postName']
        person.delete_recruit(postName=post)

    # 2- 删除项目角色
    roles_list = person.query_roles(projectName)['content']['data']['list']
    if roles_list:
        for role in roles_list:
            if role['roleName'] != '项目管理':
                person.delete_role(role['roleName'], projectName)
