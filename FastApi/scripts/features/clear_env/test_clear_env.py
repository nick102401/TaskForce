#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:王东
@file:test_clear_env.py
@time:2021/09/15
"""
import allure

# 初始化
from FastApi.aws.project import Task, Personnel
from FastApi.common.logs_handle import Logger
from FastApi.conf import env
from FastApi.scripts.conftest import projectName

# 日志
log = Logger().logger

task = Task(projectName, userName=env.USERNAME_PM)
person = Personnel(projectName, userName=env.USERNAME_PM)


@allure.feature('环境清理')
@allure.title('项目数据清理')
def test_clear_env():
    # 清理未完结任务
    try:
        task.delete_tasks(ifDeleteAll=True, userName=env.USERNAME_PM)
    except Exception as ex:
        log.info(ex)

    # 清理项目成员
    try:
        person.delete_members(ifDeleteAll=True, userName=env.USERNAME_PM)
    except Exception as ex:
        log.info(ex)
