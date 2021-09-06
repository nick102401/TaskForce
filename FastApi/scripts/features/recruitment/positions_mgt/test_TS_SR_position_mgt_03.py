#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_mgt_02.py
@time:2021/08/25
*/

项目经理修改岗位信息


"""

import allure
import pytest
from FastApi.aws.project import Project, Personnel
from FastApi.aws.recruitment import Recruitment
from FastApi.common.logs_handle import Logger
from FastApi.common.yaml_handle import read_data_from_file_to_params
from FastApi.conf import env
from FastApi.scripts.features.recruitment.conftest import projectName, startTime, endTime, postName

log = Logger().logger
pro = Project()
recruit = Recruitment()
person = Personnel(projectName=projectName, userName=env.USERNAME_PM)

def setup():
    log.info('-----测试用例预制-----')
    # 申请岗位
    recruit.apply_position(postName, projectName, applyUserDescription='申请', userName=env.USERNAME_RD)
    # 审批通过，到位人数为1
    recruit.approve_position_goal(projectName, applyUserName=env.USERNAME_RD, approveDescription='接口测试描述',
                                  approveStatus='1', userName=env.USERNAME_PM)


@pytest.mark.parametrize('title,postSum,expected_code,expected_openFlag',
                         read_data_from_file_to_params("recruitment_data.yaml", case_name='recruitment_data_alter',
                                                       index=5))
@pytest.mark.usefixtures('position_init_open')
@allure.feature('项目招聘')
@allure.story('岗位管理')
@allure.title('{title}')
def test_alter_postSum(title,postSum,expected_code,expected_openFlag):
    log.info('-----测试用例执行-----')
    resp = person.modify_recruit(postName, userName=env.USERNAME_PM, postSum=postSum)
    assert resp['content']['code'] == expected_code
    assert resp['content']['data']['item']['postSum'] == int(postSum)
    assert resp['content']['data']['item']['openFlag'] == expected_openFlag

def teardown_module():
    log.info('-----环境操作-----')
    # 1- 删除项目成员
    person.delete_member(projectName,del_userName=env.USERNAME_RD)
    # 2- 删除招募信息
    res = person.query_recruits()
    for one in res['content']['data']['list']:
        post = one['postName']
        person.delete_recruit(postName=post)
