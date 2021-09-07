#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:zxf
@file:test_TF_SR_06_04.py
@time:2021/08/31
*/

01.PMO考核内容可以取消成功
02.PMO考核内容可以执行成功
03.EPG考核内容可以取消成功
04.EPG考核内容可以执行成功
05.QA考核内容可以取消成功
06.QA考核内容可以执行成功
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
@allure.story('考核内容执行')
@allure.title('PMO考核内容可以取消成功')
def test_step_01():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用PMO账号登录成功
    2.已经存在执行角色为PMO的考核内容

    测试步骤：
    1.进入考核内容列表，点击未执行状态考核内容取消按钮

    预期结果：
    1.只有未执行状态可以取消，取消成功后状态变为已取消状态

    """

    # 生成随机字符串
    random_str = get_random_str(5)
    notice_name = "考核" + random_str
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

    # 步骤2.取消考核内容
    resp = project_assessment.cancle_assess_notice(noticeName=notice_name,
                                                   userName=env.USERNAME_PMO)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert resp['content']['data']['item']['noticeName'] == notice_name
    assert resp['content']['data']['item']['assessStatus'] == '2'


@allure.feature('项目考核')
@allure.story('考核内容执行')
@allure.title('PMO考核内容可以执行成功')
def test_step_02():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用PMO账号登录成功
    2.已经存在执行角色为PMO的考核内容

    测试步骤：
    1.进入考核内容列表，点击未执行状态考核内容执行按钮
    2.输入评分并提交成功

    预期结果：
    1.只有未执行状态可以执行，执行成功后状态变为已执行状态

    """

    # 生成随机字符串
    random_str = get_random_str(5)
    notice_name = "考核" + random_str
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

    # 步骤2.执行考核内容
    resp = project_assessment.execute_assess_notice(noticeName=notice_name,
                                                    projectAssess={
                                                        projectName: {
                                                            'itemScore': '80',
                                                            'content': '内容',
                                                            'itemDescription': '描述'
                                                        }
                                                    },
                                                    userName=env.USERNAME_PMO)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('项目考核')
@allure.story('考核内容执行')
@allure.title('EPG考核内容可以取消成功')
def test_step_03():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用EPG账号登录成功
    2.已经存在执行角色为EPG的考核内容

    测试步骤：
    1.进入考核内容列表，点击未执行状态考核内容取消按钮

    预期结果：
    1.只有未执行状态可以取消，取消成功后状态变为已取消状态

    """

    # 生成随机字符串
    random_str = get_random_str(5)
    notice_name = "考核" + random_str
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

    # 步骤2.取消考核内容
    resp = project_assessment.cancle_assess_notice(noticeName=notice_name,
                                                   userName=env.USERNAME_EPG)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert resp['content']['data']['item']['noticeName'] == notice_name
    assert resp['content']['data']['item']['assessStatus'] == '2'


@allure.feature('项目考核')
@allure.story('考核内容执行')
@allure.title('EPG考核内容可以执行成功')
def test_step_04():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用EPG账号登录成功
    2.已经存在执行角色为EPG的考核内容

    测试步骤：
    1.进入考核内容列表，点击未执行状态考核内容执行按钮
    2.输入评分并提交成功

    预期结果：
    1.只有未执行状态可以执行，执行成功后状态变为已执行状态

    """

    # 生成随机字符串
    random_str = get_random_str(5)
    notice_name = "考核" + random_str
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

    # 步骤2.执行考核内容
    resp = project_assessment.execute_assess_notice(noticeName=notice_name,
                                                    projectAssess={
                                                        projectName: {
                                                            'itemScore': '80',
                                                            'content': '内容',
                                                            'itemDescription': '描述'
                                                        }
                                                    },
                                                    userName=env.USERNAME_EPG)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('项目考核')
@allure.story('考核内容执行')
@allure.title('QA考核内容可以取消成功')
def test_step_05():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用QA账号登录成功
    2.已经存在执行角色为QA的考核内容

    测试步骤：
    1.进入考核内容列表，点击未执行状态考核内容取消按钮

    预期结果：
    1.只有未执行状态可以取消，取消成功后状态变为已取消状态

    """

    # 生成随机字符串
    random_str = get_random_str(5)
    notice_name = "考核" + random_str
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

    # 步骤2.取消考核内容
    resp = project_assessment.cancle_assess_notice(noticeName=notice_name,
                                                   userName=env.USERNAME_QA)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'
    assert resp['content']['data']['item']['noticeName'] == notice_name
    assert resp['content']['data']['item']['assessStatus'] == '2'


@allure.feature('项目考核')
@allure.story('考核内容执行')
@allure.title('QA考核内容可以执行成功')
def test_step_06():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用QA账号登录成功
    2.已经存在执行角色为QA的考核内容

    测试步骤：
    1.进入考核内容列表，点击未执行状态考核内容执行按钮
    2.输入评分并提交成功

    预期结果：
    1.只有未执行状态可以执行，执行成功后状态变为已执行状态

    """

    # 生成随机字符串
    random_str = get_random_str(5)
    notice_name = "考核" + random_str
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

    # 步骤2.执行考核内容
    resp = project_assessment.execute_assess_notice(noticeName=notice_name,
                                                    projectAssess={
                                                        projectName: {
                                                            'itemScore': '80',
                                                            'content': '内容',
                                                            'itemDescription': '描述'
                                                        }
                                                    },
                                                    userName=env.USERNAME_QA)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


def teardown():
    log.info('-----环境操作-----')
