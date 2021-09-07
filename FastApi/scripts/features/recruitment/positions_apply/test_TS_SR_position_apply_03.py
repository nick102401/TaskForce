#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:sun
@file:test_TS_SR_position_apply_01.py
@time:2021/08/25
*/

开发人员查看岗位申请结果

"""
import time

import allure
import pytest

from FastApi.aws.project import Project, Personnel
from FastApi.aws.recruitment import Recruitment
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName, postName

log = Logger().logger
pro = Project()

strTime = time.strftime('%m%d %H%M',time.localtime())

person = Personnel(projectName=projectName, userName=env.USERNAME_PM)
recruit = Recruitment()


def setup():
    log.info('-----测试用例预制-----')
    global applyId
    applyId = recruit.apply_position(postName, projectName, applyUserDescription='', userName=env.USERNAME_RD_Recruit_1,applyId=True)


@pytest.mark.usefixtures('open_init_position')
@allure.feature('项目招聘')
@allure.story('岗位申请')
@allure.title('开发人员查看岗位申请结果')
def test_my_apply():
    # 查看申请成功结果
    res = recruit.query_my_apply_by_applyId(applyId=applyId, userName=env.USERNAME_RD_Recruit_1)
    pytest.assume(res['postName'] == postName)
    pytest.assume(res['applyStatus'] == '0')











def teardown():
    log.info('-----环境操作-----')
    # 审批驳回
    recruit.approve_position_goal(projectName, applyUserName=env.USERNAME_RD_Recruit_1,
                                  approveDescription=f'目标项目组长审批{strTime}',
                                  approveStatus='2', userName=env.USERNAME_PM)

