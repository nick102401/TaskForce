#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_apply_05.py
@time:2021/08/25
*/

申请人的剩余全时率不满足岗位要求，申请岗位失败

"""
import time

import allure
import pytest

from FastApi.aws.project import Project, Personnel
from FastApi.aws.recruitment import Recruitment
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName, startTime, endTime, roleName, postName

log = Logger().logger
pro = Project()
projectName_1 = '接口测试随机项目' + time.strftime('%m%d%H%M', time.localtime())
person = Personnel(projectName=projectName, userName=env.USERNAME_PM)
person_1 = Personnel(projectName=projectName_1, userName=env.USERNAME_PM_1)
recruit = Recruitment()


def setup():
    log.info('-----测试用例预制-----')
    # # 创建项目申请
    pro.create_project(projectName=projectName_1,
                       startTime=startTime,
                       endTime=endTime,
                       templateName='基本模板',
                       userName=env.USERNAME_PM_1)
    # # 创建项目申请审批通过
    pro.approve_project(projectName=projectName_1,
                        approveDescription='ok',
                        approveStatus=1,
                        userName=env.USERNAME_PMO)
    # 创建项目角色
    pro.create_role(roleName=roleName, projectName=projectName_1, updateTask=1, userName=env.USERNAME_PM_1)
    global person_1
    person_1 = Personnel(projectName=projectName_1, userName=env.USERNAME_PM_1)

    # 开发人员加入项目
    person_1.add_member(env.USERNAME_RD_Recruit_1, roleName, 80, userName=env.USERNAME_PM_1)


@pytest.mark.usefixtures('open_init_position')
@allure.feature('项目招聘')
@allure.story('岗位申请')
@allure.title('申请人的剩余全时率不满足岗位要求，申请岗位失败')
def test_my_apply():
    """
    前置条件：
        1- 创建随机项目，审批通过
        2- 创建随机项目角色，开发人员加入项目，开发人员剩余占比为20%
    测试步骤：
        1- 创建目标项目招募岗位，打开岗位,岗位要求修改为占比为30%
        1- 开发人员申请项目岗位
    预期结果：
        1- 申请失败，提示'剩余工时不足岗位要求'
    """
    log.info('-----测试用例执行-----')
    person.modify_recruit(postName, userName=env.USERNAME_PM, postJobShare='30')
    # 申请岗位         申请人的剩余全时率不满足岗位要求
    res = recruit.apply_position(postName, projectName, applyUserDescription='剩余全时率为20%',
                                 userName=env.USERNAME_RD_Recruit_1)
    pytest.assume(res['content']['code'] == -1)
    pytest.assume(res['content']['msg'] == '剩余工时不足岗位要求')


def teardown_module():
    log.info('-----环境操作-----')
    try:
        person_1.delete_member(env.USERNAME_RD_Recruit_1, userName=env.USERNAME_PM_1)
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
