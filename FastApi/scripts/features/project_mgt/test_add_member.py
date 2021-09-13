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

from FastApi.aws.project import Personnel
from FastApi.aws.project import Project
from FastApi.aws.system_function import User
from FastApi.base.base_api import req_exec
from FastApi.common.helper import get_value_from_resp
from FastApi.common.logs_handle import Logger
from FastApi.conf import env

log = Logger().logger
projectName1 = 'l7W_test_demo'
projectName2 = '5nz_test_demo'
# 类实例化
proj = Project()
user = User()
person_name1 = Personnel(projectName1, env.USERNAME_YK)
person_name2 = Personnel(projectName2, env.USERNAME_YK)

projectId = proj.query_project_id_by_name(projectName=projectName1, userName=env.USERNAME_YK)
userId = user.get_user_id(env.USERNAME_QA)
roleId = proj.query_role_id_by_name(roleName='项目管理', projectName=projectName1, userName=env.USERNAME_YK)
roleId_sec = "PR-36fbd0af150044468933bfc28c46bf99"
roleId_none = "PR-36fbd0af150044468933bfc28c46b344"


def setup():
    log.info('-----测试用例预制-----')
    '''
    预置条件
    1.使用管理员账号登录项目考核系统

    '''

    try:
        log.info('清理已存在人员')
        person_name1.delete_member(del_userName='13289859620', userName=env.USERNAME_YK)
        person_name1.delete_member(del_userName=env.USERNAME_QA, userName=env.USERNAME_YK)
        person_name1.delete_member(del_userName=env.USERNAME_noIfo, userName=env.USERNAME_YK)
        person_name1.delete_member(del_userName=env.USERNAME_PMO, userName=env.USERNAME_YK)
    except Exception as ex:
        log.info('人员不存在,无需清除')
        log.info(ex)

    try:
        log.info('清理已存在人员')
        person_name2.delete_member(del_userName=env.USERNAME_EPG, userName=env.USERNAME_YK)
    except Exception as ex:
        log.info('人员不存在,无需清除')
        log.info(ex)


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加已经存在的用户（无ID）')
# 添加已经存在的用户（无ID）
def test_step1():
    log.info('-----测试用例执行-----')
    res = person_name1.add_member(memberName='13289859620', roleName='项目管理', percent=20, userName=env.USERNAME_YK)
    print(res)
    assert res['content']['code'] == -1
    assert res['content']['msg'] == '该人员在项目下已添加'


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加已经存在的用户（有ID）')
# 添加已经存在的用户（有ID）
def test_step2():
    log.info('-----测试用例执行-----')
    res = person_name2.add_member(memberName=env.USERNAME_EPG, roleName='项目管理', percent=20, userName=env.USERNAME_YK)
    assert res['content']['code'] == -1
    assert res['content']['msg'] == '该人员在项目下已添加'


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加未注册用户')
# 添加未注册用户
def test_step3():
    log.info('-----测试用例执行-----')
    res = person_name1.add_member(memberName=env.USERNAME_noIfo, roleName='项目管理', percent=20, userName=env.USERNAME_YK)
    assert res == False


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加占比大于100%')
# 添加占比大于100%
def test_step4():
    log.info('-----测试用例执行-----')
    res = person_name1.add_member(memberName=env.USERNAME_PMO, roleName='项目管理', percent=120, userName=env.USERNAME_YK)
    assert res['content']['msg'] == '该人员参加项目全时率不能超过100%'


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加新用户')
# 添加新用户
def test_step5():
    log.info('-----测试用例执行-----')
    res = person_name1.add_member(env.USERNAME_QA, roleName='项目管理', percent=20, userName=env.USERNAME_YK)
    assert res['content']['msg'] == 'success'
    assert res['content']['code'] == 0


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('修改成员百分比')
# 修改成员百分比
def test_step6():
    method = 'PATCH'
    data = {
        "percent": 31
    }
    url = '/api/task/case/task/projects/{0}/users/{1}/role/{2}'.format(projectId, userId, roleId)
    res = req_exec(method, url, data=data, username=env.USERNAME_YK, password=env.USER_PWD)
    assert get_value_from_resp(res['content'], 'userId', 'percent', 31.0) == userId


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('为人员指定角色')
# 为人员指定角色
def test_step7():
    method = 'PATCH'
    data = {
        "percent": 31.0
    }
    url = '/api/task/case/task/projects/{0}/users/{1}/role/{2}'.format(projectId, userId, roleId_sec)
    res = req_exec(method, url, data=data, username=env.USERNAME_YK, password=env.USER_PWD)
    assert get_value_from_resp(res['content'], 'proRoleId', 'percent', 31.0) == roleId_sec


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('为人员指定空角色')
# 为人员指定空角色
def test_step8():
    method = 'PATCH'
    data = {
        "percent": 30
    }
    url = '/api/task/case/task/projects/{0}/users/{1}/role/{2}'.format(projectId, userId, roleId_none)
    res = req_exec(method, url, data=data, username=env.USERNAME_YK, password=env.USER_PWD)
    assert res['content']['msg'] == "参数错误"


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加新用户百分比大于剩余百分比')
# 添加新用户百分比大于剩余百分比
def test_step9():
    log.info('-----测试用例执行-----')
    res = person_name1.add_member(env.USERNAME_RD, roleName='项目管理', percent=100, userName=env.USERNAME_YK)
    assert res['content']['msg'] == '该人员参加项目全时率不能超过100%'


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('删除添加的新用户数据')
# 删除添加的新用户数据
def test_step10():
    log.info('-----清空添加的项目-----')
    projectId = proj.query_project_id_by_name(projectName=projectName1, userName=env.USERNAME_YK)
    userId = user.get_user_id(env.USERNAME_QA)
    method = 'DELETE'
    url = '/api/task/case/task/projects/{0}/users/{1}'.format(projectId, userId)
    req_exec(method, url, data={}, username=env.USERNAME_YK, password=env.USER_PWD)


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加新用户百分比为0')
# 添加新用户百分比为0
def test_step11():
    log.info('-----测试用例执行-----')
    res = person_name1.add_member(env.USERNAME_QA, roleName='项目管理', percent=0, userName=env.USERNAME_YK)
    assert res['content']['msg'] == 'success'
    assert res['content']['code'] == 0
    test_step10()


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加新用户百分比为100')
# 添加新用户百分比为100
def test_step12():
    log.info('-----测试用例执行-----')
    res = person_name1.add_member(env.USERNAME_QA, roleName='项目管理', percent=100, userName=env.USERNAME_YK)
    assert res['content']['msg'] == 'success'
    assert res['content']['code'] == 0
    test_step10()


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('删除存在未完结任务的人员')
# 删除存在未完结任务的人员
def test_step13():
    log.info('-----清空添加的项目-----')
    projectId = proj.query_project_id_by_name(projectName=projectName1, userName=env.USERNAME_YK)
    userId = user.get_user_id(env.USERNAME_EPG)
    method = 'DELETE'
    url = '/api/task/case/task/projects/{0}/users/{1}'.format(projectId, userId)
    res = req_exec(method, url, data={}, username=env.USERNAME_YK, password=env.USER_PWD)
    assert res['content']['msg'] == '该人员还有未完成任务不能删除'
    print(res)
