#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:zxf
@file:test_TF_SR_07_01.py
@time:2021/09/01
*/

01.项目经理收到项目考核新增通知
02.项目经理收到项目考核编辑通知
03.项目经理收到项目考核取消通知
04.项目组人员收到小红花奖励通知
"""

import time

import allure

from FastApi.aws.assessment import ProjectAssessment, AssessmentItem
from FastApi.aws.homepage import PersonalHomepage
from FastApi.aws.project import Project, Personnel
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
personnel = Personnel(projectName)

# 加载预置数据
file_name = 'preset_project_body.yaml'
preset_data = read_data_from_file(file_name)
preset_assess_item_data_1 = preset_data['ASSESS_ITEM_1']  # PMO考核项


def setup():
    log.info('-----测试用例预制-----')
    """
    预置条件：
    1.项目考核系统登录成功
    """


@allure.feature('消息通知')
@allure.story('消息通知')
@allure.title('项目经理收到项目考核新增通知')
def test_step_01():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用项目经理账号登录项目考核系统

    测试步骤：
    1.考核项执行人新增考核项成功
    2.点击被考核人首页消息通知按钮
    3.点击该考核内容新增消息

    预期结果：
    1.被考核人消息通知按钮有红点显示
    2.点击后展示消息通知列表
    3.展示考核内容新增消息详情，通知项目经理接受考核，点击后该消息通知变为已读状态

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
    resp = personal_homepage.query_message_detail(noticeType='0', changeMessage=notice_name, userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('消息通知')
@allure.story('消息通知')
@allure.title('项目经理收到项目考核编辑通知')
def test_step_02():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用项目经理账号登录项目考核系统

    测试步骤：
    1.考核项执行人编辑考核项成功
    2.点击被考核人首页消息通知按钮
    3.点击该考核内容编辑消息

    预期结果：
    1.被考核人消息通知按钮有红点显示
    2.点击后展示消息通知列表
    3.展示考核内容编辑消息详情，通知项目经理考核内容变更，点击后该消息通知变为已读状态

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

    # 步骤3.被考核人查看考核内容详情
    resp = personal_homepage.query_message_detail(noticeType='1', changeMessage=new_notice_name,
                                                  userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('消息通知')
@allure.story('消息通知')
@allure.title('项目经理收到项目考核取消通知')
def test_step_03():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用项目经理账号登录项目考核系统

    测试步骤：
    1.考核项执行人取消考核项成功
    2.点击被考核人首页消息通知按钮
    3.点击该考核内容取消消息

    预期结果：
    1.被考核人消息通知按钮有红点显示
    2.点击后展示消息通知列表
    3.展示考核内容取消消息详情，通知项目经理考核内容取消，点击后该消息通知变为已读状态

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

    # 步骤3.被考核人查看考核内容详情
    resp = personal_homepage.query_message_detail(noticeType='2', changeMessage=notice_name,
                                                  userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


@allure.feature('消息通知')
@allure.story('消息通知')
@allure.title('项目组人员收到小红花奖励通知')
def test_step_04():
    log.info('-----测试用例执行-----')
    """
    前置条件：
    1.使用项目组人员账号登录项目考核系统

    测试步骤：
    1.项目经理向项目组人员赠送小红花
    2.点击项目组人员首页消息通知按钮
    3.点击该小红花奖励消息通知

    预期结果：
    1.项目组人员消息通知按钮有红点显示
    2.点击后展示消息通知列表
    3.展示小红花奖励消息详情，通知用户有新的小红花奖励，点击后该消息通知变为已读状态

    """

    # 生成随机字符串
    global personnel

    # 步骤1.赠送小红花
    resp = personnel.give_red_flower(memberName=env.USERNAME_RD,
                                     remark='描述',
                                     userName=env.USERNAME_PM)
    assert resp['retCode'] == 200
    assert resp['content']['msg'] == 'success'


def teardown():
    log.info('-----环境操作-----')
