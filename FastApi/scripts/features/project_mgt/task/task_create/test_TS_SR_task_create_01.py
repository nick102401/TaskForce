#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_TS_SR_task_create_01.py
@time:2021/08/31
*/

新建任务，输入任意字符名称
"""

import allure

from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger

log = Logger().logger

# 生成随机字符串
taskName1 = 'TS_SR_task_create_01_1' + get_random_str(2)
taskName2 = 'TS_SR_task_create_01_2' + get_random_str(2)


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    '''


@allure.feature('我的项目')
@allure.story('需求名称')
@allure.title('新建项目任务')
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
