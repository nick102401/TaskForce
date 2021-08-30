#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:zxf
@file:test_TF_SR_06_01.py
@time:2021/08/27
*/

01.PMO考核内容可以发布成功
02.PMO发布考核内容，必填字段未填
03.EPG考核内容可以发布成功
04.EPG发布考核内容，必填字段未填
05.QA考核内容可以发布成功
06.QA发布考核内容，必填字段未填
"""

import allure
import time
import json

from FastApi.aws.assessment import AssessmentItem, ProjectAssessment
from FastApi.aws.project import Project
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger
from FastApi.conf import env

log = Logger().logger
project_name = ''

# 操作类实例化
project = Project()
assessment_item = AssessmentItem()
project_assessment = ProjectAssessment()


def setup():
    log.info('-----测试用例预制-----')
    """
    预置条件：
    1.项目考核系统登录成功
    
    """


@allure.feature('项目考核')
@allure.story('考核内容发布')
@allure.title('PMO考核内容可以发布成功')
def test_step_01():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用PMO账号登录成功

    测试步骤：
    1.进入发布考核内容页面，正确输入信息，点击保存

    预期结果：
    1.考核项只能从本角色负责的若干考核项中进行选择，非本角色负责的考核项不可见
    2.考核内容可以发布成功，为未执行状态

    """

    # 生成随机字符串
    global project_name
    random_str = get_random_str(5)
    project_name = "项目" + random_str
    item_name = "考核项" + random_str
    notice_name = "考核" + random_str
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

    # 步骤5.新增考核项
    resp = assessment_item.create_assess_item(itemName=item_name,
                                              assessType='1',
                                              executorRole='4',
                                              defaultScore='60',
                                              userName=env.USERNAME_PMO)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert resp['content']['data']['item']['itemName'] == item_name

    # 步骤6.新增考核内容
    resp = project_assessment.create_assess_notice(noticeName=notice_name,
                                                   assessTimeStart=start_time,
                                                   assessTimeEnd=end_time,
                                                   assessItemList=[
                                                       {
                                                           item_name: [project_name]
                                                       }
                                                   ],
                                                   userName=env.USERNAME_PMO)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert resp['content']['data']['item']['noticeName'] == notice_name


@allure.feature('项目考核')
@allure.story('考核内容发布')
@allure.title('EPG考核内容可以发布成功')
def test_step_02():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用EPG账号登录成功

    测试步骤：
    1.进入发布考核内容页面，正确输入信息，点击保存

    预期结果：
    1.考核项只能从本角色负责的若干考核项中进行选择，非本角色负责的考核项不可见
    2.考核内容可以发布成功，为未执行状态

    """

    # 生成随机字符串
    global project_name
    random_str = get_random_str(5)
    project_name = "项目" + random_str
    item_name = "考核项" + random_str
    notice_name = "考核" + random_str
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

    # 步骤5.新增考核项
    resp = assessment_item.create_assess_item(itemName=item_name,
                                              assessType='1',
                                              executorRole='5',
                                              defaultScore='60',
                                              userName=env.USERNAME_PMO)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert resp['content']['data']['item']['itemName'] == item_name

    # 步骤6.新增考核内容
    resp = project_assessment.create_assess_notice(noticeName=notice_name,
                                                   assessTimeStart=start_time,
                                                   assessTimeEnd=end_time,
                                                   assessItemList=[
                                                       {
                                                           item_name: [project_name]
                                                       }
                                                   ],
                                                   userName=env.USERNAME_EPG)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert resp['content']['data']['item']['noticeName'] == notice_name


@allure.feature('项目考核')
@allure.story('考核内容发布')
@allure.title('QA考核内容可以发布成功')
def test_step_03():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用QA账号登录成功

    测试步骤：
    1.进入发布考核内容页面，正确输入信息，点击保存

    预期结果：
    1.考核项只能从本角色负责的若干考核项中进行选择，非本角色负责的考核项不可见
    2.考核内容可以发布成功，为未执行状态

    """

    # 生成随机字符串
    global project_name
    random_str = get_random_str(5)
    project_name = "项目" + random_str
    item_name = "考核项" + random_str
    notice_name = "考核" + random_str
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

    # 步骤5.新增考核项
    resp = assessment_item.create_assess_item(itemName=item_name,
                                              assessType='1',
                                              executorRole='6',
                                              defaultScore='60',
                                              userName=env.USERNAME_PMO)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert resp['content']['data']['item']['itemName'] == item_name

    # 步骤6.新增考核内容
    resp = project_assessment.create_assess_notice(noticeName=notice_name,
                                                   assessTimeStart=start_time,
                                                   assessTimeEnd=end_time,
                                                   assessItemList=[
                                                       {
                                                           item_name: [project_name]
                                                       }
                                                   ],
                                                   userName=env.USERNAME_QA)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert resp['content']['data']['item']['noticeName'] == notice_name


def teardown():
    log.info('-----环境操作-----')
    try:
        # 完结项目
        project.disable_or_archive_project(project_name, operationType='archive', userName=env.USERNAME_PM)
    except Exception as ex:
        log.info('环境清理失败')
        log.info(ex)
