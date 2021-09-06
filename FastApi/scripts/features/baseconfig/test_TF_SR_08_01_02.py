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

from FastApi.aws.base_config import BaseConfig
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger

log = Logger().logger

# 生成随机字符串
randomStr = get_random_str(6)

base = BaseConfig()


def setup():
    log.info('-----测试用例预制-----')


@allure.feature('基础配置')
@allure.story('合格项点配置')
@allure.title('修改合格项点')
def test_step():
    log.info('-----测试用例执行-----')
    resp = base.modify_passItem('合格项11', newAssessIndicatorName='合格项33')
    assert resp['content']['code'] == 0
    return resp


def teardown():
    log.info('-----环境操作-----')
