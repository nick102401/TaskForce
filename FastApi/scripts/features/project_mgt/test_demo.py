#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:王东
@file:test_demo.py
@time:2021/08/19
"""
import json

import allure

from FastApi.aws.project import Project
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger
from FastApi.conf import env

log = Logger().logger

# 生成随机字符串
projectName = get_random_str(3) + '_test_demo'

# 操作类实例化
project = Project()


def setup():
    log.info('-----这是测试用例预制步骤-----')


@allure.feature('项目管理')
@allure.story('基本操作')
@allure.title('创建项目')
def test_step():
    log.info('-----这是测试用例执行步骤-----')

    # 步骤1.创建项目
    resp = project.create_project(projectName=projectName,
                                  startTime='2021-08-19',
                                  endTime='2021-10-19',
                                  templateName='基本模板',
                                  userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert json.loads(resp['content']['data']['item']['applyUserDescription'])['projectName'] == projectName

    # 步骤2.审批通过
    resp = project.approve_project(projectName=projectName,
                                   approveDescription='ok',
                                   approveStatus=1,
                                   userName=env.USERNAME_PMO)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


def teardown():
    log.info('-----这是测试用例清理环境操作-----')
    try:
        # 完结项目
        project.disable_or_archive_project(projectName, operationType='archive', userName=env.USERNAME_PM)
    except BaseException:
        log.info('环境清理失败')
