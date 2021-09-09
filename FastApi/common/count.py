#!/usr/bin/python
# -*- coding: UTF-8 -*-

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 22:49
# @Author  : Qiufen.Chen
# @Email   : 1760812842@qq.com
# @File    : count_file_line.py
# @Software: PyCharm

"""
@author:王东
@file:count.py
@time:2021/09/03
"""
from FastApi.common.excel_handle import Excel

"""统计一个文件夹里总共有多少文件以及每一个文件里的行数"""

import os

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_dir = os.path.join(project_path, "scripts/features/project_mgt/task")
print(file_dir)

file_num = 0
fileList = []
for (root, dirs, files) in os.walk(file_dir):
    # print(root)
    # print(dirs)
    # print(files)
    for file in files:
        fileList.append(root + '\\' + file)
    # fileList += files
    # for file_name in files:
    #     file_num += 1
    #
    #     with open(os.path.join(root, file_name), 'r') as f1:
    #         line_num = 0
    #         lines = f1.readlines()
    #         for line in lines:
    #             line_num += 1
    #         print(str(file_name.split('.')[0]), line_num)
    # print('此文件夹共有 %s 个文件' % file_num)

for file in fileList[:]:
    if ".pyc" in file or "init" in file:
        fileList.remove(file)

# print(fileList)
# print(len(fileList))

a = Excel('task_case.xlsx', 'sheet1', 0)
a.create_excel()

rowNum = 0
for file in fileList:
    if rowNum == 0:
        rowNum = fileList.index(file) + 1
    with open(file, "rb") as response:
        # resLines = f.read()
        resLines = str(response.read(), "utf-8")
        # print(str(resLines))
        # print('*************************************************************************')
        # print((str(resLines).split("@allure.title('")[1].split("')")[0]).strip())
        # print((str(resLines).split("预置条件")[1].split("'''")[0]).strip())
        # print((str(resLines).split("测试步骤")[1].split("    预期结果")[0]).strip())
        # print((str(resLines).split("    预期结果")[1].split("'''")[0]).strip())

        # print('==========================================================================')
        resLines = str(resLines)
        # print(resLines)
        caseCount = resLines.count('@allure.title')
        # print(caseCount)
        # print('==========================================================================')

        caseName = (resLines.split("@file:test_")[1].split(".py")[0]).strip()
        Setup = (resLines.split("预置条件")[1].split("'''")[0]).strip()
        # sss = (resLines.split("*/")[1].split('"""')[0]).strip()
        filePath = file.split('E:\GitHubProject\TaskForce\\')[1].replace('\\', '/')
        if caseCount > 1:
            sss = (resLines.split("01:")[1].split('"""')[0]).strip()
            for i in range(caseCount):
                a.write_date(rowNum + i, 1, caseName)
                a.write_date(rowNum + i, 2, (resLines.split("@allure.title('")[1].split("')")[0]).strip())
                a.write_date(rowNum + i, 3, Setup)
                a.write_date(rowNum + i, 4, (resLines.split("测试步骤")[1].split("    预期结果")[0]).strip())
                a.write_date(rowNum + i, 5, (resLines.split("    预期结果")[1].split("'''")[0]).strip())
                a.write_date(rowNum + i, 6, sss.split('\n')[i])
                a.write_date(rowNum + i, 7, filePath)

                print('***************************************************************************')
                print(rowNum + i)
                resLines = resLines.partition('    预期结果')[2]
                # print(resLines)
        else:
            a.write_date(rowNum, 1, caseName)
            a.write_date(rowNum, 2, (resLines.split("@allure.title('")[1].split("')")[0]).strip())
            a.write_date(rowNum, 3, Setup)
            a.write_date(rowNum, 4, (resLines.split("测试步骤")[1].split("    预期结果")[0]).strip())
            a.write_date(rowNum, 5, (resLines.split("    预期结果")[1].split("'''")[0]).strip())
            a.write_date(rowNum, 6, (resLines.split("*/")[1].split('"""')[0]).strip())
            a.write_date(rowNum, 7, filePath)
            print('***************************************************************************')
            print(rowNum)
        rowNum = rowNum + caseCount
        # print('======================================' + str(rowNum) + '======================================')
