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
    """
    前置条件：
        1- 创建项目招募岗位1，打开岗位
        2- 创建项目招募岗位2，打开岗位

    测试步骤：
        1- 开发人员申请项目岗位招募岗位1
        2- 开发人员申请项目岗位招募岗位2
    预期结果：
        1- 申请招募岗位1成功
        2- 申请招募岗位2失败，提示'已申请过此项目，正在审核中'
    """
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
    try:
        # 1- 审批驳回
        recruit.approve_position_goal(projectName, applyUserName=env.USERNAME_RD_Recruit_1, approveDescription='接口测试描述',
                                      approveStatus='2', userName=env.USERNAME_PM)

        # 2- 删除招募信息
        person.delete_recruit(postName=postName_1)

        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
