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

from FastApi.aws.report import WorkReport
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger

log = Logger().logger

# 生成随机字符串
randomStr = get_random_str(6)

# pro = Project()
# person = Personnel(projectName=projectName, userName=env.USERNAME_PM)
wp = WorkReport()


def setup():
    log.info('-----测试用例预制-----')


@allure.feature('项目报告')
@allure.story('综评')
@allure.title('项目报告')
def test_step():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
        1.查看项目经理合格项得分是否正确

    预期结果
        1.根据部门主任为项目经理设置的合格分值、基础分值、超线转换分值计算该部门项目经理的月绩效合格情况

    '''
    resp = wp.query_manager_report_of_pm()
    assert resp['content']['code'] == 0
    # assert resp['content']['data']['item']['assessIndicatorName'] == '接口测试添加'


def teardown():
    log.info('-----环境操作-----')
