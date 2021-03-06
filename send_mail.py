import json
import os
import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from FastApi.common.logs_handle import Logger
from FastApi.conf.config import ReadConfig
# 日志
from FastApi.scripts.conftest import projectName

log = Logger().logger


def create_html_body():
    td = '<td>%s</td>'
    featureDict = {'preset': '环境预置',
                   'homepage': '首页',
                   'message': '通知',
                   'project_mgt': '我的项目',
                   'recruitment': '项目招聘',
                   'project_report': '我的报告',
                   'project_assess': '项目考核',
                   'system_funtion': '系统功能',
                   'clear_env': '环境清理'
                   }
    tbody = ''

    total_num_tests = 0
    total_passed = 0
    total_xfailed = 0
    total_duration = 0

    for k, v in featureDict.items():
        trStr = parse_file(k, v)
        if trStr.split('<td>')[2].split('</td>')[0] != 'NA':
            total_num_tests += int(trStr.split('<td>')[2].split('</td>')[0])
            total_passed += int(trStr.split('<td>')[3].split('</td>')[0])
            total_xfailed += int(trStr.split('<td>')[4].split('</td>')[0])
            total_duration += float(trStr.split('<td>')[7].split('</td>')[0])
        tbody += '''<tr>''' + trStr
    tbody += td % '合计' + \
             td % total_num_tests + \
             td % total_passed + \
             td % total_xfailed + td % (total_num_tests - total_passed - total_xfailed) + \
             td % '{:.2%}'.format(total_passed / total_num_tests) + \
             td % round(total_duration, 2) + '''</tr>'''

    html_body = '''
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <style type="text/css">
            body {background: rgb(204,232,207);}
            table {width: 70%;text-align:center;}
            a {text-decoration: none;}
            </style>
        </head>
        <body>
            <h1><center><font>Task Force项目自动化通过率信息</font><center></h1>
            <br>
            <hr>
            <h3>项目名称：''' + projectName + '''</h3>
            <h3>项目描述：项目管理</h3>
            <a href="http://172.30.1.58:30000/index.html">【点击查看Allure Report】</a>
            <br>
            <br>
            <a href="http://172.30.1.58:8090/C%3A/Windows/System32/config/systemprofile/AppData/Local/Jenkins/.jenkins/workspace/TaskForce/run/log">【点击查看Html日志】</a>
            <br>
            <hr>
            <table align="center" BORDER=3 cellspacing=3>
                <!--页头-->
                <thead>
                    <tr>
                        <th>特性名称</th>
                        <th>总用例数</th>
                        <th>通过数</th>
                        <th>预期失败数</th>
                        <th>失败数</th>
                        <th>通过率</th>
                        <th>执行时间(小时)</th>
                    </tr>
                </thead>
                <tbody>
                    <!--内容-->
                    ''' + tbody + '''
                </tbody>
            </table>
            <br BORDER=3>
        </body>
    </html>
    '''
    return html_body


def parse_file(json_file, feature_name):
    # 表格html代码
    td = '<td>%s</td>'

    # json日志存放路径
    path = os.path.dirname(__file__)
    log_file = path + '/run/' + json_file + '.json'

    # 解析json文件
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            summary = json.loads(f.read())['report']['summary']
            passed = summary['passed']
            num_tests = summary['num_tests']
            duration = summary['duration']
            xfailed = 0
            if 'xfailed' in summary.keys():
                xfailed = summary['xfailed']

            failed = num_tests - passed - xfailed
            pass_rate = '{:.2%}'.format(passed / num_tests)
            duration = round(duration / 3600, 2)
            logBody = td % feature_name + td % num_tests + td % passed + td % xfailed + td % failed + td % pass_rate + td % duration
    except Exception as ex:
        logBody = td % feature_name + td % 'NA' + td % 'NA' + td % 'NA' + td % 'NA' + td % 'NA' + td % 'NA'
        log.info(ex)

    return logBody


class SendMail:
    """邮件发送"""

    def __init__(self):
        self.config = ReadConfig()
        self.log = Logger().logger

    def send_mail(self):
        # 第三方服务
        mail_host = self.config.get_mail('mail_host')  # 设置服务器
        mail_user = self.config.get_mail('mail_user')  # 用户名
        mail_pass = self.config.get_mail('mail_pass')  # 口令

        sender = self.config.get_mail('sender')
        receivers = self.config.get_mail('receiver')

        # 邮件正文
        html_body = create_html_body()

        message = MIMEMultipart()
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

        message['Subject'] = Header("接口自动化测试报告" + "_" + tm, 'utf-8')
        message['From'] = Header("TaskForce项目执行详细信息", 'utf-8')  # 邮件里展示用户名
        message['To'] = receivers

        message.attach(MIMEText(html_body, 'html', 'utf-8'))

        smtp_obj = smtplib.SMTP()
        smtp_obj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtp_obj.login(mail_user, mail_pass)
        smtp_obj.sendmail(sender, receivers, message.as_string())
        self.log.info('邮件发送成功,请查收')


if __name__ == '__main__':
    mail = SendMail()
    mail.send_mail()
