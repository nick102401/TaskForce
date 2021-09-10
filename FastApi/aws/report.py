from FastApi.aws.system_function import User
from FastApi.base.base_api import req_exec
from FastApi.base.common import Common
from FastApi.common.helper import get_value_from_resp
from FastApi.conf import env


class WorkReport(Common):
    """
    工作报告
    """

    def __init__(self):
        super(WorkReport, self).__init__()
        self.user = User()

    @staticmethod
    def query_manager_report_of_pm(userName=env.USERNAME_PM):
        """
        查询PM的个人报告
        :param userName: 默认为PM角色
        :return:
        """
        method = 'GET'
        url = '/api/task/case/task/manageReport/pm'

        resp = req_exec(method, url, username=userName)
        return resp

    def query_detail_by_score(self, sumScore, userName=env.USERNAME_PM):
        """
        根据考核总分查看打分明细
        :param sumScore: 考核总分
        :param userName: 默认为PM角色
        :return:
        """
        # 获取考核明细ID
        resp = self.query_manager_report_of_pm(userName=userName)
        managerReportId = get_value_from_resp(resp['content'], 'managerReportId', 'sumScore', float(sumScore))

        method = 'GET'
        url = '/api/task/case/task/manageReport/{0}/detail'.format(managerReportId)

        resp = req_exec(method, url, username=userName)
        return resp

    def query_report_projects(self, userName=env.USERNAME_PG):
        """
        查询工作报告项目
        :param userName: 默认为开发角色
        :return:
        """
        # 获取用户ID
        userId = self.user.get_user_id(username=userName)

        method = 'GET'
        url = '/api/task/case/task/report/user/{0}/project'.format(userId)

        resp = req_exec(method, url, username=userName)
        return resp

    def query_report_detail_by_project(self, projectName, userName=env.USERNAME_PG):
        """
        根据项目名称查询工作报告项目详情
        :param projectName: 项目名称
        :param userName: 默认为职能角色
        :return:
        """
        # 获取用户ID
        userId = self.user.get_user_id(username=userName)
        # 获取工作报告项目ID
        resp = self.query_report_projects(userName=userName)
        reportProjectId = get_value_from_resp(resp['content'], 'projectId', 'projectName', projectName)

        method = 'GET'
        url = '/api/task/case/task/report/{0}/{1}'.format(userId, reportProjectId)

        resp = req_exec(method, url, username=userName)
        return resp


if __name__ == '__main__':
    wr = WorkReport()
    # wr.query_manager_report_of_pm()
    # wr.query_detail_by_score(sumScore=826.3)
    # wr.query_report_projects()
    # wr.query_report_detail_by_project(projectName='项目三')
