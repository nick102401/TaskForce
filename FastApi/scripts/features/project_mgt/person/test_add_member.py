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

from FastApi.aws.project import Personnel, Task
from FastApi.aws.project import Project
from FastApi.aws.system_function import User
from FastApi.base.base_api import req_exec
from FastApi.common.helper import get_value_from_resp, get_random_str, get_timestamp
from FastApi.common.logs_handle import Logger
from FastApi.common.yaml_handle import read_data_from_file
from FastApi.conf import env

log = Logger().logger

# 加载预置数据
file_name = 'preset_project_body.yaml'
preset_data = read_data_from_file(file_name)
preset_role_data_1 = preset_data['PRESET_ROLE_1']  # 项目角色
preset_role_data_2 = preset_data['PRESET_ROLE_2']  # 项目角色

# 自定义参数
projectName = '项目人员测试-' + str(get_timestamp())
taskName = 'add_member_' + get_random_str(3)

# 类实例化
project = Project()
user = User()


def setup_module(module):
    log.info('-----测试用例预制-----')
    '''
    预置条件
    1.使用管理员账号登录项目考核系统

    '''

    # 创建项目申请
    project.create_project(projectName=projectName,
                           userName=env.USERNAME_YK)
    # 创建项目申请审批通过
    project.approve_project(projectName=projectName,
                            approveDescription='ok',
                            approveStatus=1,
                            userName=env.USERNAME_PMO)

    # 初始化项目角色
    # 测试
    project.create_role(roleName=preset_role_data_1['roleName'],
                        projectName=projectName,
                        manage=preset_role_data_1['manage'],
                        createTask=preset_role_data_1['createTask'],
                        updateTask=preset_role_data_1['updateTask'],
                        filterType=preset_role_data_1['filterType'],
                        userName=env.USERNAME_YK)
    # 开发
    project.create_role(roleName=preset_role_data_2['roleName'],
                        projectName=projectName,
                        manage=preset_role_data_2['manage'],
                        createTask=preset_role_data_2['createTask'],
                        updateTask=preset_role_data_2['updateTask'],
                        filterType=preset_role_data_2['filterType'],
                        userName=env.USERNAME_YK)

    global person
    # 项目人员
    person = Personnel(projectName, userName=env.USERNAME_YK)
    # 添加职能人员
    person.add_member(memberName='13289859620',
                      roleName='项目管理',
                      percent=20,
                      userName=env.USERNAME_YK)
    # 添加开发人员
    person.add_member(memberName=env.USERNAME_EPG,
                      roleName='项目管理',
                      percent=20,
                      userName=env.USERNAME_YK)

    # ID参数获取
    global projectId, userId, roleId, roleId1, roleId2
    projectId = project.query_project_id_by_name(projectName=projectName, userName=env.USERNAME_YK)
    userId = user.get_user_id(env.USERNAME_QA)
    roleId = project.query_role_id_by_name(roleName='项目管理', projectName=projectName, userName=env.USERNAME_YK)
    roleId1 = project.query_role_id_by_name(roleName=preset_role_data_1['roleName'], projectName=projectName,
                                            userName=env.USERNAME_YK)
    roleId2 = "PR-36fbd0af150044468933bfc28c46b344"


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加已经存在的用户（无ID）')
# 添加已经存在的用户（无ID）
def test_step1():
    log.info('-----测试用例执行-----')
    res = person.add_member(memberName='13289859620', roleName='项目管理', percent=20, userName=env.USERNAME_YK)
    assert res['content']['code'] == -1
    assert res['content']['msg'] == '该人员在项目下已添加'


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加已经存在的用户（有ID）')
# 添加已经存在的用户（有ID）
def test_step2():
    log.info('-----测试用例执行-----')
    res = person.add_member(memberName=env.USERNAME_EPG, roleName='项目管理', percent=20, userName=env.USERNAME_YK)
    assert res['content']['code'] == -1
    assert res['content']['msg'] == '该人员在项目下已添加'


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加未注册用户')
# 添加未注册用户
def test_step3():
    log.info('-----测试用例执行-----')
    res = person.add_member(memberName=env.USERNAME_noIfo, roleName='项目管理', percent=20, userName=env.USERNAME_YK)
    assert not res


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加占比大于100%')
# 添加占比大于100%
def test_step4():
    log.info('-----测试用例执行-----')
    res = person.add_member(memberName=env.USERNAME_PMO, roleName='项目管理', percent=120, userName=env.USERNAME_YK)
    assert res['content']['msg'] == '该人员参加项目全时率不能超过100%'


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加新用户')
# 添加新用户
def test_step5():
    log.info('-----测试用例执行-----')
    res = person.add_member(env.USERNAME_QA, roleName='项目管理', percent=20, userName=env.USERNAME_YK)
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
    url = '/api/task/case/task/projects/{0}/users/{1}/role/{2}'.format(projectId, userId, roleId1)
    res = req_exec(method, url, data=data, username=env.USERNAME_YK, password=env.USER_PWD)
    assert get_value_from_resp(res['content'], 'proRoleId', 'percent', 31.0) == roleId1


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('为人员指定空角色')
# 为人员指定空角色
def test_step8():
    method = 'PATCH'
    data = {
        "percent": 30
    }
    url = '/api/task/case/task/projects/{0}/users/{1}/role/{2}'.format(projectId, userId, roleId2)
    res = req_exec(method, url, data=data, username=env.USERNAME_YK, password=env.USER_PWD)
    assert res['content']['msg'] == "参数错误"


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加新用户百分比大于剩余百分比')
# 添加新用户百分比大于剩余百分比
def test_step9():
    log.info('-----测试用例执行-----')
    res = person.add_member(env.USERNAME_RD, roleName='项目管理', percent=100, userName=env.USERNAME_YK)
    assert res['content']['msg'] == '该人员参加项目全时率不能超过100%'


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('删除添加的新用户数据')
# 删除添加的新用户数据
def test_step10():
    log.info('-----清空添加的项目-----')
    project_id = project.query_project_id_by_name(projectName=projectName, userName=env.USERNAME_YK)
    user_id = user.get_user_id(env.USERNAME_QA)
    method = 'DELETE'
    url = '/api/task/case/task/projects/{0}/users/{1}'.format(project_id, user_id)
    req_exec(method, url, data={}, username=env.USERNAME_YK, password=env.USER_PWD)


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加新用户百分比为0')
# 添加新用户百分比为0
def test_step11():
    log.info('-----测试用例执行-----')
    res = person.add_member(env.USERNAME_QA, roleName='项目管理', percent=0, userName=env.USERNAME_YK)
    assert res['content']['msg'] == 'success'
    assert res['content']['code'] == 0
    test_step10()


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('添加新用户百分比为100')
# 添加新用户百分比为100
def test_step12():
    log.info('-----测试用例执行-----')
    res = person.add_member(env.USERNAME_QA, roleName='项目管理', percent=100, userName=env.USERNAME_YK)
    assert res['content']['msg'] == 'success'
    assert res['content']['code'] == 0
    test_step10()


@allure.feature('项目管理')
@allure.story('人员管理')
@allure.title('删除存在未完结任务的人员')
# 删除存在未完结任务的人员
def test_step13():
    log.info('-----删除存在未完结任务的人员-----')
    global task
    task = Task(projectName, userName=env.USERNAME_YK)
    # 新建任务指定执行人
    resp = task.create_task(taskName=taskName,
                            executor=env.USERNAME_EPG,
                            userName=env.USERNAME_YK)
    assert resp['content']['code'] == 0
    assert resp['content']['msg'] == 'success'

    user_id = user.get_user_id(env.USERNAME_EPG)
    method = 'DELETE'
    url = '/api/task/case/task/projects/{0}/users/{1}'.format(projectId, user_id)
    res = req_exec(method, url, data={}, username=env.USERNAME_YK, password=env.USER_PWD)
    assert res['content']['msg'] == '该人员还有未完成任务不能删除'


def teardown_module(module):
    log.info('-----清理环境操作-----')
    try:
        task.delete_task(taskName=taskName, userName=env.USERNAME_YK)
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
    try:
        person.delete_member(del_userName='13289859620', userName=env.USERNAME_YK)
        person.delete_member(del_userName=env.USERNAME_QA, userName=env.USERNAME_YK)
        person.delete_member(del_userName=env.USERNAME_EPG, userName=env.USERNAME_YK)
        person.delete_member(del_userName=env.USERNAME_RD, userName=env.USERNAME_YK)
        log.info('清理环境成功')
    except Exception as ex:
        log.info('清理环境失败')
        log.info(ex)
