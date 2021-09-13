@echo off
set date=%date:~0,4%%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%%time:~6,2%

rmdir %~dp0\allure-results

mkdir %~dp0\allure-results

cd %~dp0\..

pytest -s -q \FastApi\scripts\preset --html=\run\log\report_preset.html --json=preset.json --alluredir=\run\allure-results

pytest -s -q \FastApi\scripts\features\project_mgt --html=\run\log\report_project_mgt.html --json=project_mgt.json --alluredir=\run\allure-results

pytest -s -q \FastApi\scripts\features\recruitment --html=\run\log\report_recruitment.html --json=recruitment.json --alluredir=\run\allure-results

pytest -s -q \FastApi\scripts\features\system_funtion --html=\run\log\report_system_funtion.html --json=system_funtion.json --alluredir=\run\allure-results

pytest -s -q \FastApi\scripts\features\project_assess --html=\run\log\report_project_assess.html --json=project_assess.json --alluredir=\run\allure-results

pytest -s -q \FastApi\scripts\features\homepage --html=\run\log\report_homepage.html --json=homepage.json --alluredir=\run\allure-results

pytest -s -q \FastApi\scripts\features\message --html=\run\log\report_message.html --json=message.json --alluredir=\run\allure-results

pytest -s -q \FastApi\scripts\features\report --html=\run\log\report_report.html --json=report.json --alluredir=\run\allure-results

::allure serve --port 30000 allure-results

send_mail.py

Pause
