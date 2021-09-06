from FastApi.aws.project import Project
from FastApi.aws.user import User
from FastApi.base.base_api import req_exec
from FastApi.base.common import Common
from FastApi.conf import env


class Recruitment(Common):
    """
    项目招聘
    """

    def __init__(self):
        super(Recruitment, self).__init__()
        self.perPage = 100
        self.project = Project()
        self.user = User()

    def query_project_recruitment(self, postType=0, userName=env.USERNAME_PG):
        """
        查询项目招聘信息
        :param postType: 职位类型:  0:全部类型
                                  1:Java后端
                                  2:Web前端
                                  3:手机前端
                                  4:小程序
                                  5:UI
                                  6:测试
        :param userName: 默认为职能人员
        :return:
        """
        method = 'GET'
        url = '/api/task/case/task/project/recruit/?'
        if postType != 0:
            url += 'postType=' + str(postType) + '&'

        url += 'currentPage={0}&perPage={1}'.format(self.currentPage, self.perPage)

        resp = req_exec(method, url, username=userName)
        return resp

    def query_recruitment_by_project(self, projectName, userName=env.USERNAME_PG):
        """
        查询项目招聘信息
        :param projectName: 项目名称
        :param userName: 默认为职能人员
        :return:
        """
        # 获取项目ID
        projectId = self.project.query_project_id_by_name(projectName, userName=userName)
        method = 'GET'
        url = '/api/task/case/task/project/{0}/project/recruit/'.format(projectId)

        resp = req_exec(method, url, username=userName)
        return resp

    def query_position_info_by_name(self, postName, projectName, userName=env.USERNAME_PG):
        """
        根据职位名称查询职位信息
        :param postName: 职位名称
        :param projectName: 项目名称
        :param userName: 默认为职能人员
        :return:
        """
        resp = self.query_recruitment_by_project(projectName=projectName, userName=userName)
        projectRecruitList = resp['content']['data']['item']['projectRecruit']
        if projectRecruitList:
            for projectRecruit in projectRecruitList:
                if projectRecruit['postName'] == postName:
                    return projectRecruit
            else:
                raise Exception('暂无该职位招聘信息,请核实后操作')
        else:
            raise Exception('暂无该项目招聘信息,请核实后操作')

    def query_position_id_by_name(self, postName, projectName, userName=env.USERNAME_PG):
        """
        根据职位名称查询职位ID
        :param postName: 职位名称
        :param projectName: 项目名称
        :param userName: 默认为职能人员
        :return:
        """
        resp = self.query_recruitment_by_project(projectName=projectName, userName=userName)
        projectRecruitList = resp['content']['data']['item']['projectRecruit']
        if projectRecruitList:
            for projectRecruit in projectRecruitList:
                if projectRecruit['postName'] == postName:
                    return projectRecruit['recruitId']
            else:
                raise Exception('暂无该职位招聘信息,请核实后操作')
        else:
            raise Exception('暂无该项目招聘信息,请核实后操作')

    def query_position_by_project(self, postName, projectName, userName=env.USERNAME_RD):
        """
        查询正在招聘岗位信息
        :param postName: 职位名称
        :param projectName: 项目名称
        :return: 岗位信息
        """
        project_list = self.query_project_recruitment(userName=userName)['content']['data']['list']
        for project in project_list:
            if project['projectName'] == projectName:
                for projectRecruit in project['projectRecruit']:
                    if projectRecruit['postName'] == postName:
                        return projectRecruit

    def apply_position(self, postName, projectName, applyUserDescription='', userName=env.USERNAME_RD, applyId=False):
        """
        申请职位
        :param postName: 职位名称
        :param projectName: 项目名称
        :param applyUserDescription: 申请描述
        :param userName: 默认为职能人员
        :return:
        """
        # 获取项目ID
        positionInfo = self.query_position_by_project(postName, projectName)
        if positionInfo:
            # 获取项目ID
            projectId = positionInfo['projectId']
            # 获取角色ID
            proRoleId = positionInfo['proRoleId']
            # 获取职位ID
            recruitId = positionInfo['recruitId']

            method = 'POST'
            data = {
                'applyStatus': 0,
                'applyUserDescription': applyUserDescription,
                'applyUserId': proRoleId,
                'projectId': projectId,
                'recruitId': recruitId,
                'applyType': 1
            }
            url = '/api/task/case/task/projects/apply'
            resp = req_exec(method, url, data=data, username=userName)
            if applyId:
                return resp['content']['data']['item']['applyId']
            else:
                return resp
        else:
            raise Exception('申请职位不存在,请核实后操作')

    def approve_position_goal(self, projectName, applyUserName, approveDescription, approveStatus,
                              userName=env.USERNAME_PM):
        """

        :param projectName: 职位名称
        :param applyUserName:  申请用户账号
        :param approveDescription: 审批意见
        :param approveStatus:   审批状态
                                '0': 未审批
                                '1': 审批通过
                                '2': 审批驳回
        :param userName:
        :return:
        """
        apply_user_id = self.user.get_user_id(username=applyUserName)
        approveId = ''
        approvals_goals = self.get_approve_position_goal(projectName, userName=userName)['content']['data']['list']
        if approvals_goals:
            for approval in approvals_goals:
                # 获取审批事件ID
                if approval['approveStatus'] == '0' and approval['applyUserId'] == apply_user_id:
                    approveId = approval['approveId']
            if approveId:
                method = 'PATCH'
                data = {
                    'approveDescription': approveDescription,
                    'approveId': approveId,
                    'approveStatus': approveStatus
                }
                url = '/api/task/case/task/projects/{0}/approve'.format(approveId)

                resp = req_exec(method, url, data=data, username=userName)
                return resp
            else:
                raise Exception('暂无该项目申请,请核实后操作')
        else:
            raise Exception('暂无审批申请,请核实后操作')

    def get_approve_position_goal(self, projectName, userName=env.USERNAME_PM):
        """
        查看目标项目审核列表
        :param projectName: 职位名称
        :param userName: 默认为项目经理
        :return:
        """
        # 获取项目ID
        projectId = self.project.query_project_id_by_name(projectName, userName=userName)
        url = '/api/task/case/task/projects/{0}/approve/goal'.format(projectId)
        method = 'GET'
        resp = req_exec(method, url, username=userName)
        return resp

    def get_approve_position_goal_by_postName(self, projectName, postName, userName=env.USERNAME_PM):
        position_goals = self.get_approve_position_goal(projectName, userName=userName)['content']['data']['list']
        position_list = []
        for position in position_goals:
            if position['projectName'] == projectName and position['postName'] == postName:
                position_list.append(position)
        return position_list

    def approve_position_current(self, projectName, applyUserName, approveDescription='', approveStatus='1',
                                 userName=env.USERNAME_PM):
        """
        审批项目
        :param projectName: 项目名称
        :param approveDescription: 审批描述
        :param approveStatus: 审批方式: 1:审批通过
                                      2:驳回
        :param userName: 默认为PMO角色
        :return:
        """
        approveId = ''
        applyUserId = self.user.get_user_id(username=applyUserName)
        pending_approvals = self.project.query_pending_approvals(userName=userName)
        if pending_approvals:
            for approval in pending_approvals:
                if approval['projectName'] == projectName and approval['applyUserId'] == applyUserId:
                    approveId = approval['approveId']
            if approveId:
                method = 'PATCH'
                data = {
                    'approveDescription': approveDescription,
                    'approveId': approveId,
                    'approveStatus': approveStatus
                }
                url = '/api/task/case/task/projects/{0}/approve'.format(approveId)
                resp = req_exec(method, url, data=data, username=userName)
                return resp

    def query_my_apply(self, userName=env.USERNAME_RD):
        method = 'GET'
        url = '/api/task/case/task/projects/apply?'
        url += 'currentPage={0}&perPage={1}'.format(self.currentPage, self.perPage)
        resp = req_exec(method, url, username=userName)
        return resp

    def query_my_apply_by_project(self, projectName, userName=env.USERNAME_RD):
        apply_list = self.query_my_apply(userName=userName)['content']['data']['list']
        for apply in apply_list:
            if apply['projectName'] == projectName:
                return apply


if __name__ == '__main__':
    rec = Recruitment()
    # print('\n', rec.get_approve_position_goal('接口测试0827'))
    # print('\n', rec.get_approve_position_goal_by_postName('接口测试0830',''))

    # rec.query_project_recruitment(postType=4)
    # rec.query_recruitment_by_project(projectName='中文名称项目111')
    # rec.apply_position(postName='中文测试', projectName='中文名称项目111')
    # resp = rec.add_project_recruitment("接口测试0823",startTime="2021/8/23",endTime='2021/8/24',postName='测试',postSum=2,postJobShare=20,postDescription='接口测试',postType='6')
    # print(rec.query_position_info_by_name("测试",'接口测试0825')

    rec.approve_position_current('接口测试0901', applyUserName=env.USERNAME_RD, approveDescription='目标项目组长审批',
                                 approveStatus='2', userName=env.USERNAME_PM)
