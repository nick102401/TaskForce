#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_mgt_01.py
@time:2021/08/23
*/

测试添加招聘岗位，能够成功添加
"""

import allure
import pytest

from FastApi.aws.project import Project, Personnel
from FastApi.common.logs_handle import Logger
from FastApi.common.yaml_handle import read_data_from_file_to_params, get_field_name
from FastApi.conf import env
from FastApi.scripts.conftest import projectName, startTime, endTime

log = Logger().logger
pro = Project()

# 提取测试数据
params = read_data_from_file_to_params("recruitment_data.yaml", case_name='recruitment_data')
roleName = get_field_name('recruitment_data.yaml', 'recruitment_data', 'roleType')[0]

person_1 = Personnel(projectName=projectName, userName=env.USERNAME_PM)


def setup_module(module):
    log.info('-----测试用例预制-----')
    """
    前置条件：
        1- PM登录账号,创建项目
        2- PMO登录账号，审批通过
        3- 添加项目角色
    """




@pytest.mark.parametrize('title,postName,postSum,postType,roleType,postJobShare,postDescription,expected',
                         read_data_from_file_to_params("recruitment_data.yaml", case_name='recruitment_data',index='0-6'))
@allure.feature('项目招聘')
@allure.story('岗位管理')
@allure.title('{title}')
def test_create_recruitment_01(title, postName, postSum, postType, roleType, postJobShare, postDescription, expected):
    """
    :param title:           用例标题
    :param postName:        职位名称
    :param postSum:         招募人数
    :param postType:        职位类型
    :param roleType:        角色类型
    :param postJobShare:    职位全是率%
    :param postDescription: 职位描述
    :param expected:        预期结果
    :return:
    """

    resp = person_1.create_recruit(postName=postName,
                                   postSum=postSum,
                                   postType=postType,
                                   roleType=roleType,
                                   postJobShare=postJobShare,
                                   postDescription=postDescription,
                                   startTime=startTime,
                                   endTime=endTime,
                                   userName=env.USERNAME_PM)
    pytest.assume(resp['content']['code'] == expected)
    if expected == 0:
        pytest.assume(resp['content']['data']['item']['postName'] == postName)

@pytest.mark.xfail(reason='接口无必填校验')
@pytest.mark.parametrize('title,postName,postSum,postType,roleType,postJobShare,postDescription,expected',
                         read_data_from_file_to_params("recruitment_data.yaml", case_name='recruitment_data',index='7-9'))
@allure.feature('项目招聘')
@allure.story('岗位管理')
@allure.title('{title}')
def test_create_recruitment_02(title, postName, postSum, postType, roleType, postJobShare, postDescription, expected):
    """

    :param title:           用例标题
    :param postName:        职位名称
    :param postSum:         招募人数
    :param postType:        职位类型
    :param roleType:        角色类型
    :param postJobShare:    职位全是率%
    :param postDescription: 职位描述
    :param expected:        预期结果
    :return:
    """

    resp = person_1.create_recruit(postName=postName,
                                   postSum=postSum,
                                   postType=postType,
                                   roleType=roleType,
                                   postJobShare=postJobShare,
                                   postDescription=postDescription,
                                   startTime=startTime,
                                   endTime=endTime,
                                   userName=env.USERNAME_PM)
    pytest.assume(resp['content']['code'] == expected)
    if expected == 0:
        pytest.assume(resp['content']['data']['item']['postName'] == postName)




@pytest.mark.xfail(reason='接口无日期校验')
@pytest.mark.parametrize('title,postName,postSum,postType,roleType,postJobShare,postDescription,expected',
                         read_data_from_file_to_params("recruitment_data.yaml", case_name='recruitment_data_date'))
@allure.feature('项目招聘')
@allure.story('岗位管理')
@allure.title('{title}')
def test_create_recruitment_03(title, postName, postSum, postType, roleType, postJobShare, postDescription, expected):
    """
        开始日期大于结束日期，添加招聘岗位失败
    :param title:           用例标题
    :param postName:        职位名称
    :param postSum:         招募人数
    :param postType:        职位类型
    :param roleType:        角色类型
    :param postJobShare:    职位全是率%
    :param postDescription: 职位描述
    :param expected:        预期结果
    :return:
    """
    global person_1
    person = Personnel(projectName=projectName, userName=env.USERNAME_PM)
    resp = person.create_recruit(postName=postName,
                                 postSum=postSum,
                                 postType=postType,
                                 roleType=roleType,
                                 postJobShare=postJobShare,
                                 postDescription=postDescription,
                                 startTime=endTime,
                                 endTime=startTime,
                                 userName=env.USERNAME_PM)
    pytest.assume(resp['content']['code'] == expected)



def teardown_module(module):
    """
    删除招聘信息
    :return:
    """
    log.info('-----环境操作-----')
    try:
        # 1- 删除创建成功的招聘信息
        person_1.delete_all_recruit(userName=env.USERNAME_PM)
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)




