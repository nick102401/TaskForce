@echo off
set date=%date:~0,4%%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%%time:~6,2%

rmdir %~dp0\allure-results

mkdir %~dp0\allure-results

::pytest -s -q %~dp0\..\FastApi\scripts\preset --html=%~dp0\log\report_preset.html --json=preset.json --alluredir=%~dp0\allure-results

pytest -s -q %~dp0\..\FastApi\scripts\features\project_mgt --html=%~dp0\log\report_project_mgt.html --json=project_mgt.json --alluredir=%~dp0\allure-results

pytest -s -q %~dp0\..\FastApi\scripts\features\recruitment --html=%~dp0\log\report_recruitment.html --json=recruitment.json --alluredir=%~dp0\allure-results

pytest -s -q %~dp0\..\FastApi\scripts\features\system_funtion --html=%~dp0\log\report_system_funtion.html --json=system_funtion.json --alluredir=%~dp0\allure-results

pytest -s -q %~dp0\..\FastApi\scripts\features\project_assess --html=%~dp0\log\report_project_assess.html --json=project_assess.json --alluredir=%~dp0\allure-results

pytest -s -q %~dp0\..\FastApi\scripts\features\homepage --html=%~dp0\log\report_homepage.html --json=homepage.json --alluredir=%~dp0\allure-results

pytest -s -q %~dp0\..\FastApi\scripts\features\message --html=%~dp0\log\report_message.html --json=message.json --alluredir=%~dp0\allure-results

pytest -s -q %~dp0\..\FastApi\scripts\features\report --html=%~dp0\log\report_report.html --json=report.json --alluredir=%~dp0\allure-results

::allure serve --port 30000 allure-results

%~dp0\..\send_mail.py

Pause
