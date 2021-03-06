@echo off
set date=%date:~0,4%%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%%time:~6,2%

pytest -s -v --capture=sys %~dp0\..\FastApi\scripts\features\project_mgt --html=%~dp0\log\report_project_mgt.html --self-contained-html --json=%~dp0\project_mgt.json --alluredir=%~dp0\allure-results

pytest -s -v --capture=sys %~dp0\..\FastApi\scripts\features\recruitment --html=%~dp0\log\report_recruitment.html --self-contained-html --json=%~dp0\recruitment.json --alluredir=%~dp0\allure-results

pytest -s -v --capture=sys %~dp0\..\FastApi\scripts\features\system_funtion --html=%~dp0\log\report_system_funtion.html --self-contained-html --json=%~dp0\system_funtion.json --alluredir=%~dp0\allure-results

pytest -s -v --capture=sys %~dp0\..\FastApi\scripts\features\project_assess --html=%~dp0\log\report_project_assess.html --self-contained-html --json=%~dp0\project_assess.json --alluredir=%~dp0\allure-results

pytest -s -v --capture=sys %~dp0\..\FastApi\scripts\features\homepage --html=%~dp0\log\report_homepage.html --self-contained-html --json=%~dp0\homepage.json --alluredir=%~dp0\allure-results

pytest -s -v --capture=sys %~dp0\..\FastApi\scripts\features\message --html=%~dp0\log\report_message.html --self-contained-html --json=%~dp0\message.json --alluredir=%~dp0\allure-results

pytest -s -v --capture=sys %~dp0\..\FastApi\scripts\features\project_report --html=%~dp0\log\report_project_report.html --self-contained-html --json=%~dp0\project_report.json --alluredir=%~dp0\allure-results

pytest -s -v --capture=sys %~dp0\..\FastApi\scripts\features\clear_env --html=%~dp0\log\clear_env.html --self-contained-html --json=%~dp0\clear_env.json --alluredir=%~dp0\allure-results

::allure serve --port 30000 allure-results

python %~dp0\..\send_mail.py