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
from FastApi.common.logs_handle import Logger
from FastApi.common.yaml_handle import read_data_from_file_to_params
from FastApi.conf import env
from FastApi.scripts.conftest import projectName, postName

log = Logger().logger
pro = Project()

person_1 = Personnel(projectName=projectName, userName=env.USERNAME_PM)


def setup_module(module):
    log.info('-----测试用例预制-----')


@pytest.mark.usefixtures('init_position')
@pytest.mark.parametrize('title,postJobShare,expected_code,expected_msg',
                         read_data_from_file_to_params("recruitment_data.yaml", case_name='recruitment_data_alter',
                                                       index='0-1'))
@allure.feature('项目招聘')
@allure.story('岗位管理')
@allure.title('{title}')
def test_alter_alterPostJobShare(title, postJobShare, expected_code, expected_msg):
    log.info('-----测试用例执行-----')
    resp = person_1.modify_recruit(postName, userName=env.USERNAME_PM, postJobShare=postJobShare)
    pytest.assume(resp['content']['code'] == expected_code)
    pytest.assume(resp['content']['msg'] == expected_msg)

    if expected_code == 0:
        pytest.assume(int(resp['content']['data']['item']['postJobShare']) == int(postJobShare))


@pytest.mark.usefixtures('init_position')
@pytest.mark.parametrize('title,roleType,expected_code,expected_msg',
                         read_data_from_file_to_params("recruitment_data.yaml", case_name='recruitment_data_alter',
                                                       index=2))
@allure.feature('项目招聘')
@allure.story('岗位管理')
@allure.title('{title}')
def test_alter_roleType(title, roleType, expected_code, expected_msg):
    log.info('-----测试用例执行-----')
    resp = person_1.modify_recruit(postName, userName=env.USERNAME_PM, roleType=roleType)
    pytest.assume(resp['content']['code'] == expected_code)
    pytest.assume(resp['content']['msg'] == expected_msg)


@pytest.mark.usefixtures('init_position')
@pytest.mark.parametrize('title,openFlag,expected_code,expected_openFlag',
                         read_data_from_file_to_params("recruitment_data.yaml", case_name='recruitment_data_alter',
                                                       index='3-4'))
@allure.feature('项目招聘')
@allure.story('岗位管理')
@allure.title('{title}')
def test_alter_operateRecuit(title, openFlag, expected_code, expected_openFlag):
    """
    岗位打开，岗位关闭
    :param title: 用例标题
    :param openFlag: 岗位开关：
                        True:  打开
                        False: 关闭
    :param expected_code: 预期code
    :param expected_openFlag: 预期openFlag
    :return:
    """

    log.info('-----测试用例执行-----')
    resp = person_1.operate_recruit(postName, openFlag=openFlag)
    pytest.assume(resp['content']['code'] == expected_code)
    pytest.assume(resp['content']['data']['item']['openFlag'] == expected_openFlag)


def teardown_module(module):
    log.info('-----环境操作-----')
