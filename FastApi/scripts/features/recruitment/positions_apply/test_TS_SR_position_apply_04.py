#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_mgt_02.py
@time:2021/08/25
*/

开发人员重复申请同一岗位，申请岗位失败

"""

import allure
import pytest
from FastApi.aws.project import Project, Personnel
from FastApi.aws.recruitment import Recruitment
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.features.recruitment.conftest import projectName, postName

log = Logger().logger
pro = Project()

person = Personnel(projectName=projectName, userName=env.USERNAME_PM)
recruit = Recruitment()


def setup():
    log.info('-----测试用例预制-----')


@pytest.mark.usefixtures('position_init_open')
# @pytest.mark.usefixtures('project_init')
@allure.feature('项目招聘')
@allure.story('岗位申请')
@allure.title('开发人员重复申请同一岗位，申请岗位失败')
def test_apply():
    pass
    recruit.apply_position(postName, projectName, applyUserDescription='第一次申请', userName=env.USERNAME_RD)
    # 申请岗位
    res = recruit.apply_position(postName, projectName, applyUserDescription='第二次申请', userName=env.USERNAME_RD)
    assert res['content']['code'] == -1
    assert res['content']['msg'] == '已申请过此项目，正在审核中'


def teardown():
    log.info('-----环境操作-----')
    # 1- 审批驳回
    recruit.approve_position_goal(projectName, applyUserName=env.USERNAME_RD, approveDescription='接口测试描述',
                                  approveStatus='2', userName=env.USERNAME_PM)

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

