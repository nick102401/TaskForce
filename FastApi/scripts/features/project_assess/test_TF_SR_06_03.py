#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:zxf
@file:test_TF_SR_06_03.py
@time:2021/08/31
*/

01.PMO考核内容可以编辑成功
02.EPG考核内容可以编辑成功
03.QA考核内容可以编辑成功
"""

import allure
import time
import json

from FastApi.aws.assessment import ProjectAssessment, AssessmentItem
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
@allure.story('考核内容编辑')
@allure.title('PMO考核内容可以编辑成功')
def test_step_01():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用PMO账号登录成功
    2.已经存在执行角色为PMO的考核内容

    测试步骤：
    1.进入考核内容列表，点击未执行状态考核编辑按钮
    2.进入编辑页面，正确修改信息，点击保存

    预期结果：
    1.不同考核项执行角色，只能编辑考核内容中包含了本角色负责考核项的考核内容记录
    2.如果考核内容中包含了对多个角色负责的考核项，则这些角色都可以编辑此记录
    3.只有未执行状态考核内容可以编辑，编辑后可以发布成功，状态为未执行

    """

    # 生成随机字符串
    global project_name
    random_str = get_random_str(5)
    project_name = "项目" + random_str
    item_name = "考核项" + random_str
    notice_name = "考核" + random_str
    new_notice_name = "新考核" + random_str
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

    # 步骤7.修改考核内容
    resp = project_assessment.modify_assess_notice(noticeName=notice_name,
                                                   projectName=project_name,
                                                   userName=env.USERNAME_PMO,
                                                   newNoticeName=new_notice_name)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert resp['content']['data']['item']['noticeName'] == new_notice_name


@allure.feature('项目考核')
@allure.story('考核内容编辑')
@allure.title('EPG考核内容可以编辑成功')
def test_step_02():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用EPG账号登录成功
    2.已经存在执行角色为EPG的考核内容

    测试步骤：
    1.进入考核内容列表，点击未执行状态考核编辑按钮
    2.进入编辑页面，正确修改信息，点击保存

    预期结果：
    1.不同考核项执行角色，只能编辑考核内容中包含了本角色负责考核项的考核内容记录
    2.如果考核内容中包含了对多个角色负责的考核项，则这些角色都可以编辑此记录
    3.只有未执行状态考核内容可以编辑，编辑后可以发布成功，状态为未执行

    """

    # 生成随机字符串
    global project_name
    random_str = get_random_str(5)
    project_name = "项目" + random_str
    item_name = "考核项" + random_str
    notice_name = "考核" + random_str
    new_notice_name = "新考核" + random_str
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

    # 步骤7.修改考核内容
    resp = project_assessment.modify_assess_notice(noticeName=notice_name,
                                                   projectName=project_name,
                                                   userName=env.USERNAME_EPG,
                                                   newNoticeName=new_notice_name)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert resp['content']['data']['item']['noticeName'] == new_notice_name


@allure.feature('项目考核')
@allure.story('考核内容编辑')
@allure.title('QA考核内容可以编辑成功')
def test_step_03():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用QA账号登录成功
    2.已经存在执行角色为QA的考核内容

    测试步骤：
    1.进入考核内容列表，点击未执行状态考核编辑按钮
    2.进入编辑页面，正确修改信息，点击保存

    预期结果：
    1.不同考核项执行角色，只能编辑考核内容中包含了本角色负责考核项的考核内容记录
    2.如果考核内容中包含了对多个角色负责的考核项，则这些角色都可以编辑此记录
    3.只有未执行状态考核内容可以编辑，编辑后可以发布成功，状态为未执行

    """

    # 生成随机字符串
    global project_name
    random_str = get_random_str(5)
    project_name = "项目" + random_str
    item_name = "考核项" + random_str
    notice_name = "考核" + random_str
    new_notice_name = "新考核" + random_str
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

    # 步骤7.修改考核内容
    resp = project_assessment.modify_assess_notice(noticeName=notice_name,
                                                   projectName=project_name,
                                                   userName=env.USERNAME_QA,
                                                   newNoticeName=new_notice_name)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert resp['content']['data']['item']['noticeName'] == new_notice_name


def teardown():
    log.info('-----环境操作-----')
    try:
        # 完结项目
        project.disable_or_archive_project(project_name, operationType='archive', userName=env.USERNAME_PM)
    except Exception as ex:
        log.info('环境清理失败')
        log.info(ex)
