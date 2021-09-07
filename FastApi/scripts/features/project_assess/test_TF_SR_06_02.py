#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:zxf
@file:test_TF_SR_06_02.py
@time:2021/08/30
*/

01.PMO考核内容查询
02.EPG考核内容查询
03.QA考核内容查询
"""

import allure

from FastApi.aws.assessment import ProjectAssessment
from FastApi.aws.project import Project
from FastApi.common.logs_handle import Logger
from FastApi.conf import env

log = Logger().logger

# 操作类实例化
project = Project()
project_assessment = ProjectAssessment()


def setup():
    log.info('-----测试用例预制-----')
    """
    预置条件：
    1.项目考核系统登录成功
    """


@allure.feature('项目考核')
@allure.story('考核内容查询')
@allure.title('PMO考核内容查询')
def test_step_01():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用PMO账号登录成功
    
    测试步骤：
    1.进入考核内容发布列表
    2.考核人员对已发布的考核内容进行条件查询
    
    预期结果：
    1.不同考核项执行角色，只能查看到考核内容中包含了本角色负责考核项的考核内容记录
    2.如果考核内容中包含了对多个角色负责的考核项，则这些角色都可以查询到此记录
    
    """

    # 步骤1.PMO角色考核内容查询
    resp = project_assessment.query_assess_notice(userName=env.USERNAME_PMO)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('项目考核')
@allure.story('考核内容查询')
@allure.title('EPG考核内容查询')
def test_step_02():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用EPG账号登录成功

    测试步骤：
    1.进入考核内容发布列表
    2.考核人员对已发布的考核内容进行条件查询

    预期结果：
    1.不同考核项执行角色，只能查看到考核内容中包含了本角色负责考核项的考核内容记录
    2.如果考核内容中包含了对多个角色负责的考核项，则这些角色都可以查询到此记录

    """

    # 步骤1.EPG角色考核内容查询
    resp = project_assessment.query_assess_notice(userName=env.USERNAME_EPG)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('项目考核')
@allure.story('考核内容查询')
@allure.title('QA考核内容查询')
def test_step_03():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用QA账号登录成功

    测试步骤：
    1.进入考核内容发布列表
    2.考核人员对已发布的考核内容进行条件查询

    预期结果：
    1.不同考核项执行角色，只能查看到考核内容中包含了本角色负责考核项的考核内容记录
    2.如果考核内容中包含了对多个角色负责的考核项，则这些角色都可以查询到此记录

    """

    # 步骤1.QA角色考核内容查询
    resp = project_assessment.query_assess_notice(userName=env.USERNAME_QA)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
