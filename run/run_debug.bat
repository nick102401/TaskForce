@echo off
set date=%date:~0,4%%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%%time:~6,2%

rmdir %~dp0/run/allure-results

mkdir %~dp0/run/allure-results

pytest %~dp0\..\FastApi\scripts\preset --html=log\report_preset_%date%.html --json=preset.json --alluredir=allure_report

pytest %~dp0\..\FastApi\scripts\features\project_mgt --html=log\report_project_mgt_%date%.html --json=project_mgt.json --alluredir=allure_report

pytest %~dp0\..\FastApi\scripts\features\recruitment --html=log\report_recruitment_%date%.html --json=recruitment.json --alluredir=allure_report

pytest %~dp0\..\FastApi\scripts\features\system_funtion --html=log\report_system_funtion_%date%.html --json=system_funtion.json --alluredir=allure_report

pytest %~dp0\..\FastApi\scripts\features\project_assess --html=log\report_project_assess_%date%.html --json=project_assess.json --alluredir=allure_report

pytest %~dp0\..\FastApi\scripts\features\homepage --html=log\report_homepage_%date%.html --json=homepage.json --alluredir=allure_report

pytest %~dp0\..\FastApi\scripts\features\message --html=log\report_message_%date%.html --json=message.json --alluredir=allure_report

pytest %~dp0\..\FastApi\scripts\features\report --html=log\report_report_%date%.html --json=report.json --alluredir=allure_report

::allure serve --port 30000 allure_report

%~dp0\send_mail.py

Pause
