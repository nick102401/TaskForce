#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_mgt_02.py
@time:2021/08/25
*/

项目经理修改岗位信息：
    岗位招聘人数修改为小于到位人数，岗位自动关闭


"""

import allure
import pytest

from FastApi.aws.project import Project, Personnel
from FastApi.aws.recruitment import Recruitment
from FastApi.common.logs_handle import Logger
from FastApi.common.yaml_handle import read_data_from_file_to_params
from FastApi.conf import env
from FastApi.scripts.conftest import projectName, startTime, endTime, postName, roleName

log = Logger().logger
pro = Project()
recruit = Recruitment()
person = Personnel(projectName=projectName, userName=env.USERNAME_PM)


def setup():
    log.info('-----测试用例预制-----')
    # 新增招募信息
    person.create_recruit(postName=postName,
                          postSum='3',
                          postType='6',
                          roleType=roleName,
                          postJobShare='10',
                          postDescription='招聘测试人员',
                          startTime=startTime,
                          endTime=endTime,
                          userName=env.USERNAME_PM)
    person.operate_recruit(postName, openFlag=True)
    # 申请岗位
    recruit.apply_position(postName, projectName, applyUserDescription='申请', userName=env.USERNAME_RD_Recruit_1)
    # # 审批通过，到位人数为1
    recruit.approve_position_goal(projectName, applyUserName=env.USERNAME_RD_Recruit_1, approveDescription='接口测试描述',
                                  approveStatus='1', userName=env.USERNAME_PM)
    recruit.apply_position(postName, projectName, applyUserDescription='申请', userName=env.USERNAME_RD_Recruit_2)

    recruit.approve_position_current(projectName, applyUserName=env.USERNAME_RD_Recruit_2,
                                     approveDescription='这是当前项目组组长审批', userName=env.USERNAME_PM)
    # 审批通过，到位人数为2
    recruit.approve_position_goal(projectName, applyUserName=env.USERNAME_RD_Recruit_2, approveDescription='这是岗位项目组长审批',
                                  approveStatus='1', userName=env.USERNAME_PM)


@pytest.mark.parametrize('title,postSum,expected_code,expected_msg',
                         read_data_from_file_to_params("recruitment_data.yaml", case_name='recruitment_data_alter',
                                                       index=6))
@allure.feature('项目招聘')
@allure.story('岗位管理')
@allure.title('{title}')
def test_alter_postSum(title, postSum, expected_code, expected_msg):
    log.info('-----测试用例执行-----')
    resp = person.modify_recruit(postName, userName=env.USERNAME_PM, postSum=postSum)
    assert resp['content']['code'] == expected_code
    assert resp['content']['msg'] == expected_msg


def teardown_module():
    log.info('-----环境操作-----')
    # # 1- 删除项目成员
    person.delete_member(del_userName=env.USERNAME_RD_Recruit_1,userName=env.USERNAME_PM)
    person.delete_member(del_userName=env.USERNAME_RD_Recruit_2,userName=env.USERNAME_PM)
    # # 2- 删除招募信息
    person.delete_recruit(postName, userName=env.USERNAME_PM)

