#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:zxf
@file:test_TF_SR_04_04.py
@time:2021/08/26
*/

01.PMO审批“创建项目申请”，能够成功审批通过
02.PMO审批“创建项目申请”，能够成功审批驳回
03.PMO审批“考核项目申请”，能够成功审批通过
04.PMO审批“考核项目申请”，能够成功审批驳回
05.PMO审批“恢复项目申请”，能够成功审批通过
06.PMO审批“恢复项目申请”，能够成功审批驳回
"""

import allure
import time
import json

from FastApi.aws.project import Project
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger
from FastApi.conf import env

log = Logger().logger
project_name = ''

# 操作类实例化
project = Project()


def setup():
    log.info('-----测试用例预制-----')
    """
    预置条件：
    1.PMO登录账号
    """


@allure.feature('项目管理')
@allure.story('项目申请审批')
@allure.title('PMO审批“创建项目申请”，能够成功审批通过')
def test_step_01():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.存在一个创建项目申请

    测试步骤：
    1.选择一个创建项目申请，输入审批意见，选择审批通过

    预期结果：
    1.审批成功，自动按申请信息创建项目

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


@allure.feature('项目管理')
@allure.story('项目申请审批')
@allure.title('PMO审批“创建项目申请”，能够成功审批驳回')
def test_step_02():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.存在一个创建项目申请

    测试步骤：
    1.选择一个创建项目申请，输入审批意见，选择审批驳回

    预期结果：
    1.审批成功，未创建项目

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
                                   approveStatus=2,
                                   userName=env.USERNAME_PMO)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('项目管理')
@allure.story('项目申请审批')
@allure.title('PMO审批“考核项目申请”，能够成功审批通过')
def test_step_03():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.存在一个考核项目申请

    测试步骤：
    1.选择一个考核项目申请，输入审批意见，选择审批通过

    预期结果：
    1.审批成功，变更申请项目为考核项目，将项目纳入考核计算范围，进行绩效考核

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

    # 步骤3.提交项目考核申请
    resp = project.operate_project(projectName=project_name,
                                   applyType=2,
                                   filterType='filter',
                                   userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 步骤4.项目考核申请审批通过
    resp = project.approve_project(projectName=project_name,
                                   approveDescription='ok',
                                   approveStatus=1,
                                   userName=env.USERNAME_PMO)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('项目管理')
@allure.story('项目申请审批')
@allure.title('PMO审批“考核项目申请”，能够成功审批驳回')
def test_step_04():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.存在一个考核项目申请

    测试步骤：
    1.选择一个考核项目申请，输入审批意见，选择审批驳回

    预期结果：
    1.审批成功，申请项目未纳入考核

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

    # 步骤3.提交项目考核申请
    resp = project.operate_project(projectName=project_name,
                                   applyType=2,
                                   filterType='filter',
                                   userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'

    # 步骤4.项目考核申请审批驳回
    resp = project.approve_project(projectName=project_name,
                                   approveDescription='ok',
                                   approveStatus=2,
                                   userName=env.USERNAME_PMO)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('项目管理')
@allure.story('项目申请审批')
@allure.title('PMO审批“恢复项目申请”，能够成功审批通过')
def test_step_05():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.存在一个恢复项目申请

    测试步骤：
    1.选择一个恢复项目申请，输入审批意见，选择审批通过

    预期结果：
    1.审批成功，变更申请项目状态为正常状态

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

    # 步骤5.项目恢复申请审批通过
    resp = project.approve_project(projectName=project_name,
                                   approveDescription='ok',
                                   approveStatus=1,
                                   userName=env.USERNAME_PMO)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('项目管理')
@allure.story('项目申请审批')
@allure.title('PMO审批“恢复项目申请”，能够成功审批驳回')
def test_step_06():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.存在一个恢复项目申请

    测试步骤：
    1.选择一个恢复项目申请，输入审批意见，选择审批驳回

    预期结果：
    1.审批成功，申请项目仍为中止状态

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

    # 步骤5.项目恢复申请审批驳回
    resp = project.approve_project(projectName=project_name,
                                   approveDescription='ok',
                                   approveStatus=2,
                                   userName=env.USERNAME_PMO)
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
