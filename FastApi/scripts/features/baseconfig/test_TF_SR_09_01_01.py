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
    resp = pm.query_pm_report("黄大宝", "2021-9-1", "2021-9-2", userName="13219060807", password="WlgbcSkzxc")
    assert resp['content']['code'] == 0
    # assert resp['content']['data']['item']['assessIndicatorName'] == '接口测试添加'


def teardown():
    log.info('-----环境操作-----')
