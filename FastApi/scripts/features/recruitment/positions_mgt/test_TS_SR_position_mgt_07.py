#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_mgt_07.py
@time:2021/08/26
*/

测试删除招聘岗位，能够成功删除
"""

import allure

from FastApi.aws.project import Project, Personnel
from FastApi.common.logs_handle import Logger
from FastApi.common.yaml_handle import read_data_from_file_to_params, get_field_name
from FastApi.conf import env
from FastApi.scripts.conftest import projectName, startTime, endTime, postName

log = Logger().logger
pro = Project()

# 提取测试数据
params = read_data_from_file_to_params("recruitment_data.yaml", case_name='recruitment_data')
roleName = get_field_name('recruitment_data.yaml', 'recruitment_data', 'roleType')[0]

person_1 = Personnel(projectName=projectName, userName=env.USERNAME_PM)


def setup_module(module):
    log.info('-----测试用例预制-----')
    # 添加招募岗位
    person_1.create_recruit(postName=postName,
                            postSum='2',
                            postType='6',
                            roleType=roleName,
                            postJobShare='10',
                            postDescription='招聘测试人员',
                            startTime=startTime,
                            endTime=endTime,
                            userName=env.USERNAME_PM)


@allure.feature('项目招聘')
@allure.story('岗位管理')
@allure.title('测试删除招聘岗位，能够成功删除')
def test_del_recruitment():
    """
    前置条件：
        1- 创建招聘岗位

    测试步骤：
        1- 删除招聘岗位

    预期结果：
        1- 删除成功
    """
    # 删除招募岗位
    res = person_1.delete_recruit(postName=postName, userName=env.USERNAME_PM)
    assert res['content']['code'] == 0


def teardown_module(module):
    log.info('-----环境操作-----')
