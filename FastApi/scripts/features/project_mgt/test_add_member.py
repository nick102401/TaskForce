#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
/*
@author:86181
@file:test_add_member.py
@time:2021/08/25
*/

用例标题/描述
"""

import allure

from FastApi.base.base_api import req_exec
from FastApi.common.logs_handle import Logger
from FastApi.aws.project import Personnel
from FastApi.aws.project import Project
from FastApi.aws.user import User
from FastApi.conf import env

log = Logger().logger
projectName1 = 'l7W_test_demo'
projectName2 = '5nz_test_demo'
# 类实例化
proj = Project()
usid = User()
proname1 = Personnel(projectName1, env.USERNAME_YK)
proname2 = Personnel(projectName2, env.USERNAME_YK)


# def setup():
#     log.info('-----测试用例预制-----')
#     '''
#     预置条件
#     1.使用管理员账号登录项目考核系统
#
#     '''


@allure.feature('特性名称')
@allure.story('需求名称')
@allure.title('用例名称')
# 添加已经存在的用户（无ID）
def test_step1():
    log.info('-----测试用例执行-----')
    res = proname1.add_member(memberName='13289859620', roleName='项目管理', percent=20, userName=env.USERNAME_YK)
    print(res)
    assert res['content']['code'] == -1
    assert res['content']['msg'] == '该人员在项目下已添加'


# 添加已经存在的用户（有ID）
def test_step2():
    log.info('-----测试用例执行-----')
    res = proname2.add_member(memberName=env.USERNAME_EPG, roleName='项目管理', percent=20, userName=env.USERNAME_YK)
    assert res['content']['code'] == -1
    assert res['content']['msg'] == '该人员在项目下已添加'


# 添加未注册用户
def test_step3():
    log.info('-----测试用例执行-----')
    res = proname1.add_member(memberName=env.USERNAME_noIfo, roleName='项目管理', percent=20, userName=env.USERNAME_YK)
    assert res == False


# 添加占比大于100%
def test_step4():
    log.info('-----测试用例执行-----')
    res = proname1.add_member(memberName=env.USERNAME_PMO, roleName='项目管理', percent=120, userName=env.USERNAME_YK)
    assert res['content']['msg'] == '该人员参加项目全时率不能超过100%'


# 添加新用户
def test_step5():
    log.info('-----测试用例执行-----')
    res = proname1.add_member(env.USERNAME_QA, roleName='项目管理', percent=20, userName=env.USERNAME_YK)
    assert res['content']['msg'] == 'success'
    assert res['content']['code'] == 0


# 修改成员百分比
def test_step6():
    projectId = proj.query_project_id_by_name(projectName=projectName1, userName=env.USERNAME_YK)
    userId = usid.get_user_id(env.USERNAME_QA)
    roleId = proj.query_role_id_by_name(roleName='项目管理', projectName=projectName1, userName=env.USERNAME_YK)
    method = 'PATCH'
    data = {
        "percent": 30
    }
    url = '/api/task/case/task/projects/{0}/users/{1}/role/{2}'.format(projectId, userId, roleId)
    res = req_exec(method, url, data=data, username=env.USERNAME_YK, password=env.USER_PWD)
    assert res['content']['data']['meta']['projectUsers'][1]['userId'] == userId
    assert res['content']['data']['meta']['projectUsers'][1]['percent'] == 30


# 清空添加的新用户数据，避免报错
def teardown_module():
    log.info('-----清空添加的项目-----')
    projectId = proj.query_project_id_by_name(projectName=projectName1, userName=env.USERNAME_YK)
    userId = usid.get_user_id(env.USERNAME_QA)
    method = 'DELETE'
    url = '/api/task/case/task/projects/{0}/users/{1}'.format(projectId, userId)
    req_exec(method, url, data={}, username=env.USERNAME_YK, password=env.USER_PWD)
