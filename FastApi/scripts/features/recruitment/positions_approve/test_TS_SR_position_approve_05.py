#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_approve_05.py
@time:2021/09/01
*/

多个当前组长对项目组成员的其他项目岗位申请审批驳回

"""

import allure
import pytest

from FastApi.aws.project import Project, Personnel
from FastApi.aws.recruitment import Recruitment
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName, postName
from FastApi.scripts.features.recruitment.positions_approve.conftest import projectName_1, roleName, projectName_2

log = Logger().logger
pro = Project()
recruit = Recruitment()


def setup():
    """
    预置条件：
        1- 开发人员加入两个项目
    """
    log.info('-----测试用例预制-----')
    #
    # ---------------------------------PM_1--------------------------
    global person_1
    person_1 = Personnel(projectName=projectName_1, userName=env.USERNAME_PM_1)
    #
    # # 开发人员加入项目
    person_1.add_member(env.USERNAME_RD_Recruit_1, roleName, 10, userName=env.USERNAME_PM_1)

    # # --------------------------------PM_2-------------------------
    global person_2
    person_2 = Personnel(projectName=projectName_2, userName=env.USERNAME_PM_2)

    # # 开发人员加入项目
    person_2.add_member(env.USERNAME_RD_Recruit_1, roleName, 10, userName=env.USERNAME_PM_2)


@pytest.mark.usefixtures('open_init_position')
@allure.feature('项目招聘')
@allure.story('岗位审批')
@allure.title('多个当前组长对项目组成员的其他项目岗位申请审批驳回')
def test_approve():
    log.info('-----测试用例执行-----')
    """
    前置条件：
        1- 创建招募岗位，并打开岗位
        2- 开发人员申请其他项目岗位


    测试步骤：
        1- 当前项目组长USERNAME_PM_1审批驳回
        2- 当前项目组长USERNAME_PM_2审批驳回

    预期结果：
        1- 当前项目组长审批成功,岗位详情相应审批状态变为已驳回

    """

    # 1- 开发人员申请其他项目岗位
    applyId = recruit.apply_position(postName, projectName, applyUserDescription=f'申请{projectName}{postName}岗位',
                                     userName=env.USERNAME_RD_Recruit_1, applyId=True)

    # # # 当前项目组长USERNAME_PM_1审批驳回
    resp = recruit.approve_position_current(projectName, applyUserName=env.USERNAME_RD_Recruit_1,
                                            approveDescription='当前项目组长1审批',
                                            approveStatus='2', userName=env.USERNAME_PM_1)
    pytest.assume(resp['content']['code'] == 0)
    pytest.assume(pro.query_application_detail_by_approveProject(applyId=applyId, approveProject=projectName_1,
                                                                 userName=env.USERNAME_RD_Recruit_1)[
                      'approveStatus'] == '2')

    # # 当前项目组长USERNAME_PM_2审批驳回
    resp = recruit.approve_position_current(projectName, applyUserName=env.USERNAME_RD_Recruit_1,
                                            approveDescription='当前项目组长2审批',
                                            approveStatus='2', userName=env.USERNAME_PM_2)

    pytest.assume(resp['content']['code'] == 0)
    pytest.assume(pro.query_application_detail_by_approveProject(applyId=applyId, approveProject=projectName_2,
                                                                 userName=env.USERNAME_RD_Recruit_1)[
                      'approveStatus'] == '2')

    pytest.assume(pro.query_application_detail_by_approveProject(applyId=applyId, approveProject=projectName,
                                                                 userName=env.USERNAME_RD_Recruit_1)[
                      'approveStatus'] == '0')


def teardown():
    log.info('-----环境操作-----')

    try:
        # 1- 删除项目成员
        person_1.delete_member(env.USERNAME_RD_Recruit_1, env.USERNAME_PM_1)
        person_2.delete_member(env.USERNAME_RD_Recruit_1, env.USERNAME_PM_2)
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
