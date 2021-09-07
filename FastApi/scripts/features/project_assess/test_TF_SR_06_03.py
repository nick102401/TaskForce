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

from FastApi.aws.assessment import ProjectAssessment, AssessmentItem
from FastApi.aws.project import Project
from FastApi.common.helper import get_random_str
from FastApi.common.logs_handle import Logger
from FastApi.common.yaml_handle import read_data_from_file
from FastApi.conf import env
from FastApi.scripts.conftest import projectName

log = Logger().logger

# 操作类实例化
project = Project()
assessment_item = AssessmentItem()
project_assessment = ProjectAssessment()

# 加载预置数据
file_name = 'preset_project_body.yaml'
preset_data = read_data_from_file(file_name)
preset_assess_item_data_1 = preset_data['ASSESS_ITEM_1']  # PMO考核项
preset_assess_item_data_2 = preset_data['ASSESS_ITEM_2']  # EPG考核项
preset_assess_item_data_3 = preset_data['ASSESS_ITEM_3']  # QA考核项


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
    random_str = get_random_str(5)
    notice_name = "考核" + random_str
    new_notice_name = "新考核" + random_str
    start_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    end_time = time.strftime('%Y-%m-%d', time.localtime(time.time() + 24 * 3600))

    # 步骤1.新增考核内容
    resp = project_assessment.create_assess_notice(noticeName=notice_name,
                                                   assessTimeStart=start_time,
                                                   assessTimeEnd=end_time,
                                                   assessItemList=[
                                                       {
                                                           preset_assess_item_data_1['itemName']: [projectName]
                                                       }
                                                   ],
                                                   userName=env.USERNAME_PMO)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert resp['content']['data']['item']['noticeName'] == notice_name

    # 步骤2.修改考核内容
    resp = project_assessment.modify_assess_notice(noticeName=notice_name,
                                                   projectName=projectName,
                                                   userName=env.USERNAME_PMO,
                                                   newNoticeName=new_notice_name,
                                                   description='描述',
                                                   assessItemList=[
                                                       {
                                                           preset_assess_item_data_1['itemName']: [projectName]
                                                       }
                                                   ])
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
    random_str = get_random_str(5)
    notice_name = "考核" + random_str
    new_notice_name = "新考核" + random_str
    start_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    end_time = time.strftime('%Y-%m-%d', time.localtime(time.time() + 24 * 3600))

    # 步骤1.新增考核内容
    resp = project_assessment.create_assess_notice(noticeName=notice_name,
                                                   assessTimeStart=start_time,
                                                   assessTimeEnd=end_time,
                                                   assessItemList=[
                                                       {
                                                           preset_assess_item_data_2['itemName']: [projectName]
                                                       }
                                                   ],
                                                   userName=env.USERNAME_EPG)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert resp['content']['data']['item']['noticeName'] == notice_name

    # 步骤2.修改考核内容
    resp = project_assessment.modify_assess_notice(noticeName=notice_name,
                                                   projectName=projectName,
                                                   userName=env.USERNAME_EPG,
                                                   newNoticeName=new_notice_name,
                                                   description='描述',
                                                   assessItemList=[
                                                       {
                                                           preset_assess_item_data_2['itemName']: [projectName]
                                                       }
                                                   ])
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
    random_str = get_random_str(5)
    notice_name = "考核" + random_str
    new_notice_name = "新考核" + random_str
    start_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    end_time = time.strftime('%Y-%m-%d', time.localtime(time.time() + 24 * 3600))

    # 步骤1.新增考核内容
    resp = project_assessment.create_assess_notice(noticeName=notice_name,
                                                   assessTimeStart=start_time,
                                                   assessTimeEnd=end_time,
                                                   assessItemList=[
                                                       {
                                                           preset_assess_item_data_3['itemName']: [projectName]
                                                       }
                                                   ],
                                                   userName=env.USERNAME_QA)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert resp['content']['data']['item']['noticeName'] == notice_name

    # 步骤2.修改考核内容
    resp = project_assessment.modify_assess_notice(noticeName=notice_name,
                                                   projectName=projectName,
                                                   userName=env.USERNAME_QA,
                                                   newNoticeName=new_notice_name,
                                                   description='描述',
                                                   assessItemList=[
                                                       {
                                                           preset_assess_item_data_3['itemName']: [projectName]
                                                       }
                                                   ])
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert resp['content']['data']['item']['noticeName'] == new_notice_name


def teardown():
    log.info('-----环境操作-----')
