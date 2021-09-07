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
@allure.story('合格项点分值配置')
@allure.title('修改合格项点分值')
def test_step():
    log.info('-----测试用例执行-----')
    '''
    测试步骤
        "1.进入合格分值列表，点击编辑按钮
         2.修改项点、角色、项点合格分值、项点基础分值、超线转换分值
         3.点击保存"

    预期结果
        "1.点击编辑按钮进入编辑合格分值页面
         2.点击保存该合格分值编辑成功"

    '''
    resp = base.modify_item_score('互评合格项1', qualifiedScore='21', initialScore='11', baseScore='10')
    assert resp['content']['code'] == 0

    return resp


def teardown():
    log.info('-----环境操作-----')
