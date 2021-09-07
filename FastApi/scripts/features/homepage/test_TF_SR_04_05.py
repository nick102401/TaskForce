#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:zxf
@file:test_TF_SR_04_05.py
@time:2021/08/26
*/

01.PMO查看申请审批列表，能够成功查看
02.用户查看待审批项目申请详情，能够成功查看
03.用户查看已审批项目申请详情，能够成功查看
04.用户查看已提交申请审批列表，能够成功查看
"""

import allure
import time
import json

from FastApi.aws.homepage import PersonalHomepage
from FastApi.aws.project import Project
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger
from FastApi.conf import env

log = Logger().logger
project_name = ''
apply_id = ''

# 操作类实例化
project = Project()
PersonalHomepage = PersonalHomepage()


def setup():
    log.info('-----测试用例预制-----')
    """
    预置条件：
    1.项目考核系统登录成功
    """


@allure.feature('首页')
@allure.story('申请查看')
@allure.title('PMO查看申请审批列表，能够成功查看')
def test_step_01():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.PMO登录账号

    测试步骤：
    1.查看申请审批列表

    预期结果：
    1.审批列表展示所有待审核项目，列表包含申请项目、申请人、申请状态、申请类别等信息

    """

    # 步骤1.获取审批列表
    resp = PersonalHomepage.query_my_approvals(userName=env.USERNAME_PMO)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('首页')
@allure.story('申请查看')
@allure.title('用户查看待审批项目申请详情，能够成功查看')
def test_step_02():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.项目创建者登录账号

    测试步骤：
    1.选择一个待审批项目申请，查看申请详情

    预期结果：
    1.进入项目申请详情页面，查看项目申请详情

    """

    # 生成随机字符串
    global project_name
    global apply_id
    random_str = get_random_str(5)
    project_name = "项目" + random_str
    start_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    end_time = time.strftime('%Y-%m-%d', time.localtime(time.time() + 24 * 3600))

    # 步骤1.提交项目创建申请
    resp = project.create_project(projectName=project_name,
                                  startTime=start_time,
                                  endTime=end_time,
                                  templateName='基本模板',
                                  userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert json.loads(resp['content']['data']['item']['applyUserDescription'])['projectName'] == project_name
    apply_id = resp['content']['data']['item']['applyId']

    # 步骤2.查看待审批申请详情
    resp = PersonalHomepage.query_application_detail(applyId=apply_id,
                                                     userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert resp['content']['data']['list'][0]['applyId'] == apply_id


@allure.feature('首页')
@allure.story('申请查看')
@allure.title('用户查看已审批项目申请详情，能够成功查看')
def test_step_03():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.项目管理角色登录账号

    测试步骤：
    1.选择一个已审批项目申请，查看申请详情

    预期结果：
    1.进入项目申请详情页面，查看项目申请详情，能够查看审批历史信息，包含申请项目、申请人、申请状态、申请类别、审核结果、审批意见等信息

    """

    # 生成随机字符串
    global project_name
    global apply_id
    random_str = get_random_str(5)
    project_name = "项目" + random_str
    start_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    end_time = time.strftime('%Y-%m-%d', time.localtime(time.time() + 24 * 3600))

    # 步骤1.提交项目创建申请
    resp = project.create_project(projectName=project_name,
                                  startTime=start_time,
                                  endTime=end_time,
                                  templateName='基本模板',
                                  userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert json.loads(resp['content']['data']['item']['applyUserDescription'])['projectName'] == project_name
    apply_id = resp['content']['data']['item']['applyId']

    # 步骤2.项目创建申请审批通过
    resp = project.approve_project(projectName=project_name,
                                   approveDescription='ok',
                                   approveStatus=1,
                                   userName=env.USERNAME_PMO)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 步骤2.查看已审批申请详情
    resp = PersonalHomepage.query_application_detail(applyId=apply_id,
                                                     userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert resp['content']['data']['list'][0]['applyId'] == apply_id


@allure.feature('首页')
@allure.story('申请查看')
@allure.title('用户查看已提交申请审批列表，能够成功查看')
def test_step_04():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.项目创建者登录账号

    测试步骤：
    1.查看申请审批列表

    预期结果：
    1.审批列表展示所有待审批项目

    """

    resp = PersonalHomepage.query_my_applications(userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


def teardown():
    log.info('-----环境操作-----')
    try:
        # 完结项目
        project.disable_or_archive_project(project_name, operationType='archive', userName=env.USERNAME_PM)
    except Exception as ex:
        log.info('环境清理失败')
        log.info(ex)
