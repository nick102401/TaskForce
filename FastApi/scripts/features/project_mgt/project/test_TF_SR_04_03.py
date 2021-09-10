#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:zxf
@file:test_TF_SR_04_03.py
@time:2021/08/25
*/

01.用户查询个人创建项目，能够成功查询
02.用户提交项目恢复申请，能够成功提交
03.用户重复提交项目恢复申请，系统能够正确处理
04.非项目创建者对项目提交恢复申请，系统能够正确处理
"""

import json
import time

import allure
import pytest

from FastApi.aws.project import Project, Personnel
from FastApi.common.helper import get_random_str, get_value_from_resp
from FastApi.common.logs_handle import Logger
from FastApi.conf import env

log = Logger().logger
project_name = ''

# 操作类实例化
project = Project()
personnel = None


def setup():
    log.info('-----测试用例预制-----')
    """
    预置条件：
    1.项目创建者登录账号
    """


@allure.feature('项目管理')
@allure.story('恢复项目申请')
@allure.title('用户查询个人创建项目，能够成功查询')
def test_step_01():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.已成功创建项目

    测试步骤：
    1.进入我的项目

    预期结果：
    1.查看已创建和参与的所有项目

    """

    # 查询当前用户参与的项目
    resp = project.query_projects(filterType='filter',
                                  userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 查询当前用户已完结的项目
    resp = project.query_projects(filterType='archive',
                                  userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 查询当前用户已终止的项目
    resp = project.query_projects(filterType='disable',
                                  userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('项目管理')
@allure.story('恢复项目申请')
@allure.title('用户提交项目恢复申请，能够成功提交')
def test_step_02():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.存在已中止状态的项目

    测试步骤：
    1.选择一个已中止状态的项目，提交项目恢复申请

    预期结果：
    1.提交成功，项目为待审批状态

    """

    # 生成随机字符串
    global project_name
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

    # 步骤2.项目创建申请审批通过
    resp = project.approve_project(projectName=project_name,
                                   approveDescription='ok',
                                   approveStatus=1,
                                   userName=env.USERNAME_PMO)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 步骤3.终止项目
    resp = project.disable_or_archive_project(projectName=project_name,
                                              operationType='disable',
                                              filterType='filter',
                                              userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 步骤4.提交项目恢复申请
    resp = project.operate_project(projectName=project_name,
                                   applyType=3,
                                   filterType='disable',
                                   userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('项目管理')
@allure.story('恢复项目申请')
@allure.title('用户重复提交项目恢复申请，系统能够正确处理')
def test_step_03():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.存在已中止状态的项目

    测试步骤：
    1.选择一个中止状态已提交项目恢复申请待审批的项目，提交项目恢复申请

    预期结果：
    1.提交失败，提示已提交申请，不可重复提交

    """

    # 生成随机字符串
    global project_name
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

    # 步骤2.项目创建申请审批通过
    resp = project.approve_project(projectName=project_name,
                                   approveDescription='ok',
                                   approveStatus=1,
                                   userName=env.USERNAME_PMO)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 步骤3.终止项目
    resp = project.disable_or_archive_project(projectName=project_name,
                                              operationType='disable',
                                              filterType='filter',
                                              userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 步骤4.提交项目恢复申请
    resp = project.operate_project(projectName=project_name,
                                   applyType=3,
                                   filterType='disable',
                                   userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 步骤5.重复提交项目恢复申请
    resp = project.operate_project(projectName=project_name,
                                   applyType=3,
                                   filterType='disable',
                                   userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == '已申请重开此项目，正在审核中'


@pytest.mark.xfail()
@allure.feature('项目管理')
@allure.story('恢复项目申请')
@allure.title('非项目创建者对项目提交恢复申请，系统能够正确处理')
def test_step_04():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.存在已中止状态的项目

    测试步骤：
    1.非项目创建者，提交考核申请

    预期结果：
    1.无法提交恢复申请

    """

    # 生成随机字符串
    global project_name
    global personnel
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

    # 步骤2.项目创建申请审批通过
    resp = project.approve_project(projectName=project_name,
                                   approveDescription='ok',
                                   approveStatus=1,
                                   userName=env.USERNAME_PMO)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 步骤3.添加角色
    resp = project.create_role(roleName='修改任务',
                               projectName=project_name,
                               manage=0,
                               createTask=0,
                               updateTask=1,
                               filterType='filter',
                               userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert get_value_from_resp(resp['content'], 'manage', 'roleName', '修改任务') == 0
    assert get_value_from_resp(resp['content'], 'createTask', 'roleName', '修改任务') == 0
    assert get_value_from_resp(resp['content'], 'updateTask', 'roleName', '修改任务') == 1

    # 步骤4.添加人员
    personnel = Personnel(project_name)
    resp = personnel.add_member(memberName=env.USERNAME_RD,
                                roleName='修改任务',
                                percent=10,
                                userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert get_value_from_resp(resp['content'], 'realName', 'mobile', '18111111111') == '18111111111'

    # 步骤5.终止项目
    resp = project.disable_or_archive_project(projectName=project_name,
                                              operationType='disable',
                                              filterType='filter',
                                              userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 步骤6.非项目管理员提交项目恢复申请
    resp = project.operate_project(projectName=project_name,
                                   applyType=3,
                                   filterType='disable',
                                   userName=env.USERNAME_RD)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == '非项目管理员不能提交项目恢复申请'


def teardown():
    log.info('-----环境操作-----')
    try:
        # 完结项目
        project.disable_or_archive_project(projectName=project_name,
                                           operationType='archive',
                                           filterType='disable',
                                           userName=env.USERNAME_PM)
    except Exception as ex:
        log.info('环境清理失败')
        log.info(ex)
