#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_mgt_02.py
@time:2021/08/25
*/

岗位招聘人数修改为等于到位人数，岗位自动关闭


"""

import allure
import pytest

from FastApi.aws.project import Project, Personnel
from FastApi.aws.recruitment import Recruitment
from FastApi.common.logs_handle import Logger
from FastApi.common.yaml_handle import read_data_from_file_to_params
from FastApi.conf import env
from FastApi.scripts.conftest import projectName, postName

log = Logger().logger
pro = Project()
recruit = Recruitment()
person_1 = Personnel(projectName=projectName, userName=env.USERNAME_PM)


def setup_module(module):
    log.info('-----测试用例预制-----')


@pytest.mark.usefixtures('open_init_position')
@pytest.mark.parametrize('title,postSum,expected_code,expected_openFlag',
                         read_data_from_file_to_params("recruitment_data.yaml", case_name='recruitment_data_alter',
                                                       index=5))
@allure.feature('项目招聘')
@allure.story('岗位管理')
@allure.title('{title}')
def test_alter_postSum(title, postSum, expected_code, expected_openFlag):
    """
    前置条件：
        1- 创建招募岗位，并打开岗位


    测试步骤：
        1- 开发人员申请项目招募岗位，审批通过
        2- 岗位招聘人数修改为等于到位人数

    预期结果：
        1- 岗位状态变更为关闭
    """
    log.info('-----测试用例执行-----')

    # 申请岗位
    recruit.apply_position(postName, projectName, applyUserDescription='申请', userName=env.USERNAME_RD_Recruit_1)
    # 审批通过，到位人数为1
    recruit.approve_position_goal(projectName, applyUserName=env.USERNAME_RD_Recruit_1, approveDescription='接口测试描述',
                                  approveStatus='1', userName=env.USERNAME_PM)

    # 修改岗位人数
    resp = person_1.modify_recruit(postName, userName=env.USERNAME_PM, postSum=postSum)
    assert resp['content']['code'] == expected_code
    assert resp['content']['data']['item']['postSum'] == int(postSum)
    assert resp['content']['data']['item']['openFlag'] == expected_openFlag


def teardown_module(module):
    log.info('-----环境操作-----')
    # 1- 删除项目成员
    try:
        person_1.delete_member(del_userName=env.USERNAME_RD_Recruit_1, userName=env.USERNAME_PM)
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
