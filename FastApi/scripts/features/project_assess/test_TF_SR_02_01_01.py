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
from FastApi.conf import env

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
@allure.title('PMO新增考核项可以新增成功')
def test_step():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
    1.点击考核项管理-新增考核项
    2.正确输入信息，点击完成

    预期结果
    1.新增考核项增加考核项类型选择框，考核项类型分为项目考核和人员考核两种类型
    2.点击完成可以新增成功
    '''

    resp = assessmentItem.create_assess_item(itemName=itemName,
                                             assessType='1',
                                             executorRole='4',
                                             defaultScore='60',
                                             userName=env.USERNAME_PMO)
    assert resp['content']['code'] == 0
    assert resp['content']['msg'] == 'success'
    assert resp['content']['data']['item']['itemName'] == itemName


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        assessmentItem.delete_assess_item(itemName=[itemName])
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
