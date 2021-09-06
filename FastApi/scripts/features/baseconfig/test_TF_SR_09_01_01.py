#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:CAT
@file:test_TF_SR_08_01_01.py
@time:2021/08/24
*/

测试新增考核项，能够成功新增
"""

import allure

from FastApi.aws.assessment import ProjectAssessment
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger

log = Logger().logger

# 生成随机字符串
randomStr = get_random_str(6)

# pro = Project()
# person = Personnel(projectName=projectName, userName=env.USERNAME_PM)
pm = ProjectAssessment()


def setup():
    log.info('-----测试用例预制-----')


@allure.feature('项目经理报告')
@allure.story('综评')
@allure.title('项目成员报告')
def test_step():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
          1.查看开发人员报告信息明细是否正确

    预期结果
         "1.开发人员可以查看到当期完成的工作点概要、合格项合格情况、排名情况
          2.排名：本项目内的所有合格人员，按照各合格项超线分值总和形成的排名"

    '''
    resp = pm.query_pm_report("黄大宝", "2021-9-1", "2021-9-2")
    assert resp['content']['code'] == 0
    # assert resp['content']['data']['item']['assessIndicatorName'] == '接口测试添加'


def teardown():
    log.info('-----环境操作-----')
