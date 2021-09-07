#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:CAT
@file:test_TF_SR_08_01_02.py
@time:2021/08/26
*/

用例标题/描述
"""

import allure

from FastApi.aws.system_function import BaseConfig
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger

log = Logger().logger

# 生成随机字符串
randomStr = get_random_str(6)

base = BaseConfig()


def setup():
    log.info('-----测试用例预制-----')


@allure.feature('基础配置')
@allure.story('级别基数点设置')
@allure.title('修改基数点')
def test_step():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
        "1.进入基数点列表，点击编辑按钮
         2.修改工作任务点基数
         3.点击保存"

    预期结果
        "1.点击编辑按钮进入编辑基数点页面
         2.点击保存该基数点编辑成功"

    '''
    resp = base.modify_level_config('白银', basePoint='9.9', evaluateQualifiedScore='61')
    assert resp['content']['code'] == 0
    assert resp['content']['data']['item']['basePoint'] == 9.9
    assert resp['content']['data']['item']['evaluateQualifiedScore'] == 61


def teardown():
    log.info('-----环境操作-----')
    base.modify_level_config('白银', basePoint='8', evaluateQualifiedScore='60')
