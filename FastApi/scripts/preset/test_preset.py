#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:王东
@file:test_preset.py
@time:2021/08/24
*/

用例标题/描述
"""
import allure
import pytest

from FastApi.common.logs_handle import Logger

log = Logger().logger


# 操作类实例化


@pytest.mark.usefixtures('init_project_role')
@pytest.mark.usefixtures('init_recruit_info')
@pytest.mark.usefixtures('init_task')
@pytest.mark.usefixtures('init_plan')
@pytest.mark.usefixtures('init_project')
@allure.title('项目数据预置')
def test_step():
    log.info('-----项目数据预置-----')