import ast
import json

from FastApi.base.base_api import req_exec
from FastApi.base.common import Common
from FastApi.common.helper import get_value_from_resp
from FastApi.conf import env


class PersonalHomepage(Common):
    """
    个人主页
    """

    def __init__(self):
        super(PersonalHomepage, self).__init__()
        self.perPage = 100

    @staticmethod
    def query_participant_project(userName=env.USERNAME_PM):
        """
        查询参与的项目信息
        :param userName: 默认为PM角色
        :return:
        """
        method = 'GET'
        url = '/api/task/case/task/mine/tasks/summary'

        resp = req_exec(method, url, username=userName)
        return resp

    def query_my_applications(self, userName=env.USERNAME_PM):
        """
        查询我的所有申请
        :param userName: 默认为PM角色
        :return:
        """
        method = 'GET'
        url = '/api/task/case/task/projects/apply?currentPage={0}&perPage={1}'.format(self.currentPage,
                                                                                      self.perPage)

        resp = req_exec(method, url, username=userName)
        return resp

    def query_application_detail(self, projectName='', applyId='', userName=env.USERNAME_PM):
        """
        查询申请详情
        :param projectName:
        :param applyId: 申请ID
        :param userName:默认为PM角色
        :return:
        """
        if projectName:
            resp = self.query_my_applications(userName=userName)
            list = resp['content']['data']['list']
            if list:
                for ele in list:
                    # 获取审批事件ID
                    applyUserDescription = ele['applyUserDescription']
                    if applyUserDescription and 'projectName' in applyUserDescription:
                        try:
                            applyUserDescription = ast.literal_eval(applyUserDescription)
                        except BaseException:
                            applyUserDescription = json.loads(applyUserDescription)
                        if applyUserDescription['projectName'] == projectName:
                            applyId = ele['applyId']
                    else:
                        if ele['projectName'] == projectName:
                            applyId = ele['applyId']
        method = 'GET'
        url = '/api/task/case/task/projects/{0}/approve'.format(applyId)
        resp = req_exec(method, url, username=userName)
        return resp

    def query_application_detail_by_approveProject(self, applyId, approveProject, userName=env.USERNAME_PM):
        approve_list = self.query_application_detail(userName=userName)['content']['data']['list']
        for approve in approve_list:
            if approve['projectName'] == approveProject:
                return approve

    def query_pending_applications(self, userName=env.USERNAME_PM):
        """
        查询我的待审批申请
        :param userName: 默认为PM角色
        :return:
        """
        pendingApplications = []
        resp = self.query_my_applications(userName=userName)
        applicationList = resp['content']['data']['list']
        if applicationList:
            for application in applicationList:
                if application['applyStatus'] == '0':
                    pendingApplications.append(application)
            return pendingApplications
        else:
            raise Exception('暂无我的申请,请核实后操作')

    def query_my_applications_by_applyId(self, applyId, userName=env.USERNAME_PM):
        """
        根据applyId查询我的申请
        :param applyId: 申请ID
        :param userName: 默认为PM角色
        :return:
        """

        resp = self.query_my_applications(userName=userName)
        applicationList = resp['content']['data']['list']
        if applicationList:
            for application in applicationList:
                if application['applyId'] == applyId:
                    return application
        else:
            raise Exception('暂无查询申请,请核实后操作')

    def query_my_approvals(self, userName=env.USERNAME_PMO):
        """
        查询我的所有审批
        :param userName: 默认PMO角色
        :return:
        """
        method = 'GET'
        url = '/api/task/case/task/projects/approve/current?currentPage={0}&perPage={1}'.format(self.currentPage,
                                                                                                self.perPage)

        resp = req_exec(method, url, username=userName)
        return resp

    def query_pending_approvals(self, userName=env.USERNAME_PMO):
        """
        查询我的待审批
        :param userName: 默认PMO角色
        :return:
        """
        pendingApprovals = []
        resp = self.query_my_approvals(userName=userName)
        approvalList = resp['content']['data']['list']
        if approvalList:
            for approval in approvalList:
                if approval['approveStatus'] == '0':
                    pendingApprovals.append(approval)
            return pendingApprovals
        else:
            raise Exception('暂无我的审批,请核实后操作')

    def query_assessment_content(self, userName=env.USERNAME_PM):
        """
        查询考核内容
        :param userName: 默认PM角色
        :return:
        """
        method = 'GET'
        url = '/api/task/case/task/assessNotice/manager?currentPage={0}&perPage={1}'.format(self.currentPage,
                                                                                            self.perPage)

        resp = req_exec(method, url, username=userName)
        return resp

    def query_message_list(self, userName=env.USERNAME_PM):
        """
        获取消息通知列表
        :param userName: 默认为PM角色
        :return:
        """
        method = 'GET'
        url = '/api/task/case/task/assessNotice/assessChange'

        resp = req_exec(method, url, username=userName)
        return resp

    def query_message_detail(self, noticeType, changeMessage, userName=env.USERNAME_PM):
        """
        查看消息通知详情
        :param noticeType: 消息类型： 0：新增项目考核
                                    1：更新项目考核
                                    2：取消项目考核
                                    3：考核项变动
                                    4：收到小红花
        :param changeMessage:考核内容名称/项目名称/小红花
        :param userName:默认为PM角色
        :return:
        """
        message_id = ''
        resp = self.query_message_list(userName=userName)
        u_list = resp['content']['data']['U']
        for r in u_list:
            for k, v in r.items():
                v = json.loads(v)
                if v['noticeType'] == noticeType and v['readFlag'] == '0' and changeMessage in v['changeMessage']:
                    message_id = k
                    break

        method = 'POST'
        data = {
            'data': message_id
        }
        url = '/api/task/case/task/assessNotice/assessChange'

        resp = req_exec(method, url, data=data, username=userName)
        return resp


if __name__ == '__main__':
    ph = PersonalHomepage()
    # ph.query_participant_project()
    # ph.query_my_approvals()
    # ph.query_application_detail('iLJtest_demo')
    # ph.query_message_detail(noticeType='0', changeMessage='项目xlQc4')
