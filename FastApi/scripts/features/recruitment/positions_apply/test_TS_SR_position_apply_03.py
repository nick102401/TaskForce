#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_mgt_02.py
@time:2021/08/25
*/

申请人的剩余全时率不满足岗位要求，申请岗位失败

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
postName = '开发'
roleName = '开发人员'


def setup():
    log.info('-----测试用例预制-----')
    # 1- 创建项目角色
    pro.create_role(roleName=roleName, projectName=projectName, updateTask=1, userName=env.USERNAME_PM)
    # 2- 新增岗位
    person.create_recruit(postName=postName,
                          postSum='2',
                          postType='1',  # Java后端
                          roleType=roleName,
                          postJobShare='50',
                          postDescription='招聘开发人员',
                          startTime=startTime,
                          endTime=endTime,
                          userName=env.USERNAME_PM)
    # 3- 打开岗位开关
    person.operate_recruit(postName, openFlag=True)



@allure.feature('项目招聘')
@allure.story('岗位申请')
@allure.title('申请人的剩余全时率不满足岗位要求，申请岗位失败')
def test_my_apply():
    # 申请岗位         申请人的剩余全时率不满足岗位要求
    res = recruit.apply_position(postName, projectName, applyUserDescription='剩余全时率为10%', userName='18435156019')
    assert res['content']['code'] == -1
    assert res['content']['msg']  == '剩余工时不足岗位要求'






























def teardown_module():
    log.info('-----环境操作-----')
    # res = person.query_recruits()
    # for one in res['content']['data']['list']:
    #     post = one['postName']
    #     person.delete_recruit(postName=post)
