#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:zxf
@file:test_TF_SR_06_06.py
@time:2021/09/01
*/

01.被考核人查看PMO考核内容成功
02.被考核人查看EPG考核内容成功
03.被考核人查看QA考核内容成功
"""

import allure
import time

from FastApi.aws.assessment import ProjectAssessment, AssessmentItem
from FastApi.aws.homepage import PersonalHomepage
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
personal_homepage = PersonalHomepage()

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
@allure.story('被考核人考核内容查看')
@allure.title('被考核人查看PMO考核内容成功')
def test_step_01():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用考核人员账号登录成功
    2.已经存在PMO创建的考核内容
    
    测试步骤：
    1.进入考核内容查看页面，可以查看该考核详细信息
    
    预期结果：
    1.被考核项目经理，仅可见考核内容中，范围是本人或本项目的考核内容数据，非本人本项目的考核内容数据不可见
    
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

    # 步骤2.被考核人查看考核内容详情
    resp = personal_homepage.query_assessment_content(userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('项目考核')
@allure.story('被考核人考核内容查看')
@allure.title('被考核人查看EPG考核内容成功')
def test_step_02():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用考核人员账号登录成功
    2.已经存在EPG创建的考核内容

    测试步骤：
    1.进入考核内容查看页面，可以查看该考核详细信息

    预期结果：
    1.被考核项目经理，仅可见考核内容中，范围是本人或本项目的考核内容数据，非本人本项目的考核内容数据不可见

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

    # 步骤2.被考核人查看考核内容详情
    resp = personal_homepage.query_assessment_content(userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('项目考核')
@allure.story('被考核人考核内容查看')
@allure.title('被考核人查看QA考核内容成功')
def test_step_03():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用考核人员账号登录成功
    2.已经存在QA创建的考核内容

    测试步骤：
    1.进入考核内容查看页面，可以查看该考核详细信息

    预期结果：
    1.被考核项目经理，仅可见考核内容中，范围是本人或本项目的考核内容数据，非本人本项目的考核内容数据不可见

    """

    # 生成随机字符串
    random_str = get_random_str(5)
    notice_name = "考核" + random_str
    start_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    end_time = time.strftime('%Y-%m-%d', time.localtime(time.time() + 24 * 3600))

    # 步骤6.新增考核内容
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

    # 步骤7.被考核人查看考核内容详情
    resp = personal_homepage.query_assessment_content(userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


def teardown():
    log.info('-----环境操作-----')
