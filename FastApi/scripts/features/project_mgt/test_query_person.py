#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:王东
@file:test_query_person.py
@time:2021/08/19
"""
import allure

from FastApi.aws.project import Personnel
from FastApi.aws.project import Project
from FastApi.common.logs_handle import Logger
from FastApi.conf import env

log = Logger().logger

# 项目名称
projectName = 'l7W_test_demo'
# 操作类实例化
project = Project()
p = Personnel(projectName)


@allure.feature('项目申请审批')
@allure.story('创建项目申请')
@allure.title('创建新项目审批通过')
def setup():
    log.info('-----这是测试用例预制步骤-----')
    # 创建新项目
    project.create_project(projectName=projectName,
                           startTime='2021-08-19',
                           endTime='2021-10-18',
                           templateName='基本模板',
                           userName=env.USERNAME_YK)
    # 审批通过
    project.approve_project(projectName=projectName,
                            approveDescription='ok',
                            approveStatus=1,
                            userName=env.USERNAME_PMO)


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加系统中已注册的号码')
# 输入数据库存在的号码
def test_step1():
    log.info('-----这是测试用例执行步骤-----')
    res = p.get_user_info(searchKey='18109219499', username=env.USERNAME_YK, password=env.USER_PWD)
    print(res)
    assert res['content']['data']['list'][0]['operatorNo'] == '18109219499'


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加系统中未注册的号码')
# 输入数据库不存在的号码
def test_step2():
    log.info('-----这是测试用例执行步骤-----')
    res = p.get_user_info(searchKey='479849878974849878678798', username=env.USERNAME_YK, password=env.USER_PWD)
    print(res)
    assert res['content']['data']['list'] == []


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加系统中未注册的姓名')
# 数入数据库不存在的姓名
def test_step3():
    log.info('-----这是测试用例执行步骤-----')
    res = p.get_user_info(searchKey='你好', username=env.USERNAME_YK, password=env.USER_PWD)
    print(res)
    assert res['content']['data']['list'] == []


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加系统中已注册的姓名')
# 输入数据库存在的姓名
def test_step4():
    log.info('-----这是测试用例执行步骤-----')
    res = p.get_user_info(searchKey='部门主任', username=env.USERNAME_YK, password=env.USER_PWD)
    print(res)
    assert res['content']['data']['list'][0]['userName'] == '部门主任'


@allure.feature('项目申请审批')
@allure.story('创建项目申请')
@allure.title('完结项目')
def test_step5():
    log.info('-----这是测试用例清理环境操作-----')
    try:
        # 完结项目
        project.disable_or_archive_project(projectName, operationType='archive', userName=env.USERNAME_YK)
    except Exception as ex:
        log.info('环境清理失败')
        log.info(ex)
