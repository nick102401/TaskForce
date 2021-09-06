#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TF_SR_03_01_03.py
@time:2021/09/03
*/

测试小红花赠送累计数量小于指定数量，能够成功赠送
"""

import allure

from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger

log = Logger().logger

# 生成随机字符串
randomStr = get_random_str(6)


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    '''


@allure.feature('我的项目')
@allure.story('综评')
@allure.title('小红花赠送累计数量小于指定数量')
def test_step():
    log.info('-----测试用例执行-----')
    '''
    测试步骤

    预期结果
    '''


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
