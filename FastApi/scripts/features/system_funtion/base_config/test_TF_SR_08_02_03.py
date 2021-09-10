#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TF_SR_02_01_01.py
@time:2021/09/03
*/

PMO新增考核项可以新增成功
"""

import allure

from FastApi.aws.assessment import AssessmentItem
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger

log = Logger().logger

# 生成随机字符串
itemName = 'TF_SR_02_01_01_' + get_random_str(3)

# 初始化
assessmentItem = AssessmentItem()


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    1.使用PMO账号登录成功
    '''


@allure.feature('项目考核')
@allure.story('考核项管理')
@allure.title('考核项查看')
def test_step():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.点击考核项管理

    预期结果
    1.查看成功
    '''

    resp = assessmentItem.query_assess_item_list()


def teardown_module(module):
    log.info('-----清理环境操作-----')
