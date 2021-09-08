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

from FastApi.aws.project import Project, ComprehensiveEvaluation
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger

log = Logger().logger

# 生成随机字符串
randomStr = get_random_str(6)

# pro = Project()
# person = Personnel(projectName=projectName, userName=env.USERNAME_PM)
ce = ComprehensiveEvaluation(Project)


def setup():
    log.info('-----测试用例预制-----')


@allure.feature('我的项目')
@allure.story('综评')
@allure.title('附加值查看')
def test_step():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
        1.进入项目综评页面，查看本项目产生的附加值报告是否正确

    预期结果
        "1.可分页查询本项目内产生的附加值记录
         2.展示字段：姓名、附加值类型、分值、时间等"

    '''
    resp = ce.query_added_value_report()
    assert resp['content']['code'] == 0
    # assert resp['content']['data']['item']['assessIndicatorName'] == '接口测试添加'


def teardown():
    log.info('-----环境操作-----')
