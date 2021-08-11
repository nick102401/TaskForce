from FastApi.aws.user import User
from FastApi.base.base_api import req_exec
from FastApi.common.helper import get_value_from_resp
from FastApi.conf import env


class WorkReport:
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
        resp = self.query_manager_report_of_pm(userName=userName)
        managerReportId = get_value_from_resp(resp['content'], 'managerReportId', 'sumScore', float(sumScore))
        method = 'GET'
        url = '/api/task/case/task/manageReport/{0}/detail'.format(managerReportId)

        resp = req_exec(method, url, username=userName)
        return resp


if __name__ == '__main__':
    wr = WorkReport()
    # wr.query_manager_report_of_pm()
    # wr.query_detail_by_score(sumScore=826.3)
