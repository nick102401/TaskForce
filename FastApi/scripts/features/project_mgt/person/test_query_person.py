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
from FastApi.scripts.features.project_mgt.person.test_add_member import projectName

log = Logger().logger

# 操作类实例化
project = Project()
p = Personnel(projectName)


def setup_module(module):
    log.info('-----测试用例预制-----')


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加系统中已注册的号码')
# 输入数据库存在的号码
def test_step1():
    log.info('-----这是测试用例执行步骤-----')
    res = p.get_user_info(searchKey='18109219499', userName=env.USERNAME_YK, password=env.USER_PWD)
    assert res['content']['data']['list'][0]['operatorNo'] == '18109219499'


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加系统中未注册的号码')
# 输入数据库不存在的号码
def test_step2():
    log.info('-----这是测试用例执行步骤-----')
    res = p.get_user_info(searchKey='479849878974849878678798', userName=env.USERNAME_YK, password=env.USER_PWD)
    assert res['content']['data']['list'] == []


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加系统中未注册的姓名')
# 数入数据库不存在的姓名
def test_step3():
    log.info('-----这是测试用例执行步骤-----')
    res = p.get_user_info(searchKey='你好', userName=env.USERNAME_YK, password=env.USER_PWD)
    assert res['content']['data']['list'] == []


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加系统中已注册的姓名')
# 输入数据库存在的姓名
def test_step4():
    log.info('-----这是测试用例执行步骤-----')
    res = p.get_user_info(searchKey='部门主任', userName=env.USERNAME_YK, password=env.USER_PWD)
    assert res['content']['data']['list'][0]['userName'] == '部门主任'


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        project.disable_or_archive_project(projectName, operationType='archive', userName=env.USERNAME_YK)
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
