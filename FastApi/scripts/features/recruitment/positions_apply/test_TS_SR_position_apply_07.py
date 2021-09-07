#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_apply_07.py
@time:2021/08/25
*/

开发人员同时申请同一项目的不同岗位，申请岗位失败

"""

import allure
import pytest

from FastApi.aws.project import Project, Personnel
from FastApi.aws.recruitment import Recruitment
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName, roleName, startTime, endTime, postName

log = Logger().logger
pro = Project()
postName_1 = '自动化测试'
recruit = Recruitment()


def setup():
    log.info('-----测试用例预制-----')


@pytest.mark.usefixtures('open_init_position')
@allure.feature('项目招聘')
@allure.story('岗位申请')
@allure.title('开发人员同时申请同一项目的不同岗位，申请岗位失败')
def test_apply():
    log.info('-----测试用例执行-----')
    global person
    person = Personnel(projectName=projectName, userName=env.USERNAME_PM)
    person.create_recruit(postName=postName_1,
                          postSum='2',
                          postType='6',
                          roleType=roleName,
                          postJobShare='10',
                          postDescription='招聘测试人员',
                          startTime=startTime,
                          endTime=endTime,
                          userName=env.USERNAME_PM)
    person.operate_recruit(postName_1, openFlag=True)
    recruit.apply_position(postName, projectName, applyUserDescription=f'申请{projectName}{postName}岗位',
                           userName=env.USERNAME_RD_Recruit_1)
    # 申请岗位
    res = recruit.apply_position(postName_1, projectName, applyUserDescription=f'申请{projectName}{postName_1}岗位',
                                 userName=env.USERNAME_RD_Recruit_1)
    pytest.assume(res['content']['code'] == -1)
    pytest.assume(res['content']['msg'] == '已申请过此项目，正在审核中')




def teardown():
    log.info('-----环境操作-----')
    # 1- 审批驳回
    recruit.approve_position_goal(projectName, applyUserName=env.USERNAME_RD_Recruit_1, approveDescription='接口测试描述',
                                  approveStatus='2', userName=env.USERNAME_PM)

    # 2- 删除招募信息
    person.delete_recruit(postName=postName_1)


