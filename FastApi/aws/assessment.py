import json
import time
from urllib.parse import quote

from FastApi.aws.user import User
from FastApi.base.base_api import req_exec
from FastApi.base.common import Common
from FastApi.common.helper import get_value_from_resp, utc_to_bjs
from FastApi.conf import env


class AssessmentItem(Common):
    """
    考核项管理
    """

    def __init__(self):
        super(AssessmentItem, self).__init__()
        self.user = User()

    @staticmethod
    def query_assess_item_list(userName=env.USERNAME_PMO):
        """
        查询考核项列表
        :param userName: 默认为PMO角色
        :return:
        """
        method = 'GET'
        url = '/api/task/case/task/assess/item/assess/items'

        resp = req_exec(method, url, username=userName)
        return resp

    @staticmethod
    def create_assess_item(itemName='', assessType='1', parentId='', executorRole='4', defaultScore='',
                           userName=env.USERNAME_PMO):
        """
        新增考核项
        :param itemName: 考核项名称
        :param assessType: 考核类型,1:项目考核,2:人员考核
        :param parentId: 父id
        :param executorRole: 执行人角色, 1:开发人员, 2:PM, 3:职能人员, 4:PMO, 5:EPG, 6:QA
        :param defaultScore: 默认分值
        :param userName: 默认为PMO角色
        :return:
        """

        method = 'POST'
        data = {
            'itemName': itemName,
            'assessType': assessType,
            'parentId': parentId,
            'executorRole': executorRole,
            'defaultScore': defaultScore
        }
        if not parentId:
            del data['parentId']
        url = '/api/task/case/task/assess/item/items'

        resp = req_exec(method, url, data=data, username=userName)
        return resp

    def modify_assess_item(self, itemName='', userName=env.USERNAME_PMO, **modifyParams):
        """
        修改考核项
        :param itemName: 考核项名称
        :param userName: 默认为PMO角色
        :param modifyParams:待修改入参: newItemName:待修改考核项名称
                                       assessType:考核类型,1:项目考核,2:人员考核
                                       executorRole:执行人角色, 1:开发人员, 2:PM, 3:职能人员, 4:PMO, 5:EPG, 6:QA
                                       defaultScore:默认分值
                                       parentName:父考核项名称
        :return:
        """

        # 复制原有考核项配置
        resp = self.query_assess_item_list(userName=userName)
        defaultScore = get_value_from_resp(resp['content'], 'defaultScore', 'itemName', itemName)
        executorRole = get_value_from_resp(resp['content'], 'executorRole', 'itemName', itemName)
        assessType = get_value_from_resp(resp['content'], 'assessType', 'itemName', itemName)
        parentId = get_value_from_resp(resp['content'], 'parentId', 'itemName', itemName)
        defaultName = get_value_from_resp(resp['content'], 'itemId', 'itemName', itemName)
        itemId = get_value_from_resp(resp['content'], 'itemId', 'itemName', itemName)
        modifyBody = {
            'itemName': itemName,
            'assessType': assessType,
            'parentId': parentId,
            'executorRole': executorRole,
            'defaultScore': defaultScore,
            'defaultName': defaultName,
            'itemId': itemId
        }

        for modifyParamsKey in modifyParams.keys():
            if modifyParamsKey == 'newItemName':
                modifyBody['itemName'] = modifyParams[modifyParamsKey]
            if modifyParamsKey == 'assessType':
                modifyBody['assessType'] = modifyParams[modifyParamsKey]
            if modifyParamsKey == 'executorRole':
                modifyBody['executorRole'] = modifyParams[modifyParamsKey]
            if modifyParamsKey == 'defaultScore':
                modifyBody['defaultScore'] = modifyParams[modifyParamsKey]
            if modifyParamsKey == 'parentName':
                modifyBody['parentId'] = get_value_from_resp(resp['content'], 'itemId', 'itemName',
                                                             modifyParams[modifyParamsKey])

        method = 'PUT'
        data = modifyBody
        url = '/api/task/case/task/assess/item/{0}'.format(modifyBody['itemId'])

        resp = req_exec(method, url, data=data, username=userName)
        return resp

    def delete_assess_item(self, itemName=[], userName=env.USERNAME_PMO):
        """
        删除考核项
        :param itemName: 考核项名称
        :param userName: 默认为PMO角色
        :return:
        """

        resp = self.query_assess_item_list(userName=userName)
        itemId = []
        for ele in itemName:
            item_id = get_value_from_resp(resp['content'], 'itemId', 'itemName', ele)
            itemId.append(item_id)
        itemId = ','.join(itemId)

        method = 'DELETE'
        data = {
            'itemIds': itemId
        }
        url = '/api/task/case/task/assess/item'

        resp = req_exec(method, url, data=data, username=userName)
        return resp


class ProjectAssessment(Common):
    """
    项目考核
    """

    def __init__(self):
        super(ProjectAssessment, self).__init__()
        self.user = User()
        self.assessmentItem = AssessmentItem()

    def query_assess_notice(self, userName=env.USERNAME_PMO):
        """
        查询项目考核
        :param userName: 默认为PMO角色
        :return:
        """
        method = 'GET'
        url = '/api/task/case/task/assessNotice?currentPage={0}&perPage={1}'.format(self.currentPage, self.perPage)

        resp = req_exec(method, url, username=userName)
        return resp

    def create_assess_notice(self, noticeName, assessTimeStart='', assessTimeEnd='', description='', assessItemList=[],
                             userName=env.USERNAME_PMO):
        """
        创建项目考核
        :param noticeName: 考核内容名称
        :param assessTimeStart:开始时间
        :param assessTimeEnd:结束时间
        :param description:描述
        :param assessItemList:[{考核项:[被考核人员/项目,...]},...]
        :param userName:默认为PMO角色
        :return:
        """
        if not assessTimeStart:
            assessTimeStart = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        resp = self.query_projects_items(userName=userName)
        assessItemsList = resp['content']['data']['item']['assessItemList']
        resp = self.query_projects_users(userName=userName)
        usersList = resp['content']['data']['list']
        resp = self.query_assess_projects(userName=userName)
        assessProjectsList = resp['content']['data']['list']

        assessItemBodyList = []
        assessItemBody = {}
        for assessItemDict in assessItemList:
            for k, v in assessItemDict.items():
                for assessItem in assessItemsList:
                    if assessItem['itemName'] == k:
                        assessItemBody = assessItem
                        if assessItem['assessType'] == '2':
                            userIdList = []
                            for user in usersList:
                                for ele in v:
                                    if user['userName'] == ele:
                                        userIdList.append(user['userId'])
                            assessItemBody['managerId'] = ','.join(userIdList)
                        elif assessItem['assessType'] == '1':
                            projectIdList = []
                            for assessProject in assessProjectsList:
                                for ele in v:
                                    if assessProject['projectName'] == ele:
                                        projectIdList.append(assessProject['projectId'])
                            assessItemBody['projectId'] = ','.join(projectIdList)
            assessItemBodyList.append(assessItemBody)

        method = 'POST'
        data = {
            'noticeName': noticeName,
            'assessTimeStart': assessTimeStart,
            'assessTimeEnd': assessTimeEnd,
            'assessStatus': '0',
            'description': description,
            'assessItemList': json.dumps(assessItemBodyList)
        }
        if not data['description']:
            del data['description']
        url = '/api/task/case/task/assessNotice'

        resp = req_exec(method, url, data=data, username=userName)
        return resp

    def modify_assess_notice(self, noticeName, projectName='', managerName='', userName=env.USERNAME_PMO,
                             **modifyParams):
        """
        修改考核内容
        :param noticeName: 考核名称
        :param projectName: 被考核项目
        :param managerName: 被考核人员
        :param userName: 默认为PMO角色
        :param modifyParams: 待修改入参:  newNoticeName:待修改考核名称
                                        description:描述
                                        assessTimeStart:格式: %Y-%m-%d
                                        assessTimeEnd:格式: %Y-%m-%d
                                        newProjectName:待修改考核项目名称列表
                                        newManagerName:待修改考核人员名称列表
                                        assessItemList:[{考核项:[被考核人员/项目,...]},...]
        :return:
        """
        resp = self.query_assess_notice_info_by_name(noticeName=noticeName, projectName=projectName,
                                                     managerName=managerName, userName=userName)
        assessNoticeId = resp['assessNoticeId']

        modifyBody = resp
        del modifyBody['assessNoticeId']
        del modifyBody['assessStatus']
        del modifyBody['createdAt']
        del modifyBody['creatorId']
        del modifyBody['executorRole']
        del modifyBody['itemList']
        del modifyBody['projectId']
        del modifyBody['updatedAt']
        del modifyBody['updaterId']
        modifyBody['assessTimeStart'] = utc_to_bjs(modifyBody['assessTimeStart'].split('+')[0]).split(' ')[0]
        modifyBody['assessTimeEnd'] = utc_to_bjs(modifyBody['assessTimeEnd'].split('+')[0]).split(' ')[0]

        for modifyParamsKey in modifyParams.keys():
            if modifyParamsKey == 'newNoticeName':
                modifyBody['noticeName'] = modifyParams[modifyParamsKey]
            elif modifyParamsKey == 'description':
                modifyBody['description'] = modifyParams[modifyParamsKey]
            elif modifyParamsKey == 'assessTimeStart':
                modifyBody['assessTimeStart'] = modifyParams[modifyParamsKey]
            elif modifyParamsKey == 'assessTimeEnd':
                modifyBody['assessTimeEnd'] = modifyParams[modifyParamsKey]
            elif modifyParamsKey == 'assessItemList':
                resp = self.query_projects_users(userName=userName)
                usersList = resp['content']['data']['list']
                resp = self.query_assess_projects(userName=userName)
                assessProjectsList = resp['content']['data']['list']

                for assessItemDict in modifyParams[modifyParamsKey]:
                    for k, v in assessItemDict.items():
                        for preAssessItem in modifyBody['assessItemList']:
                            if preAssessItem['itemName'] == k:
                                assessItemBody = preAssessItem
                                if preAssessItem['assessType'] == '2':
                                    userIdList = []
                                    if not v:
                                        userIdList.append('')
                                    else:
                                        for ele in v:
                                            for user in usersList:
                                                if user['userName'] == ele:
                                                    userIdList.append(user['userId'])
                                    assessItemBody['managerId'] = ','.join(userIdList)
                                elif preAssessItem['assessType'] == '1':
                                    projectIdList = []
                                    if not v:
                                        projectIdList.append('')
                                    else:
                                        for ele in v:
                                            for assessProject in assessProjectsList:
                                                if assessProject['projectName'] == ele:
                                                    projectIdList.append(assessProject['projectId'])
                                    assessItemBody['projectId'] = ','.join(projectIdList)

        # 无考核人员或项目时需删除对应列表
        assessItemList = modifyBody['assessItemList']
        for assessItem in assessItemList[:]:
            if assessItem['managerId'] is None and assessItem['projectId'] is None:
                assessItemList.remove(assessItem)
        modifyBody['assessItemList'] = json.dumps(assessItemList)

        method = 'PATCH'
        data = modifyBody
        url = '/api/task/case/task/assessNotice/{0}'.format(assessNoticeId)

        resp = req_exec(method, url, data=data, username=userName)
        return resp

    def query_assess_notice_id(self, noticeName, projectName='', managerName='', assessStatus='',
                               userName=env.USERNAME_PMO):
        """
        查询项目考核ID
        :param noticeName: 考核名称
        :param projectName: 被考核项目名称: 用','隔开
        :param managerName: 被考核人: 用','隔开
        :param assessStatus: 考核状态: 1:已完成
                                     0:未完成
        :param userName: 默认为PMO角色
        :return:
        """
        resp = self.query_assess_notice(userName=userName)
        assessNoticeList = resp['content']['data']['list']
        for assessNotice in assessNoticeList:
            if assessNotice['noticeName'] == noticeName:
                if projectName:
                    if assessNotice['projectName'] == projectName:
                        pass
                    else:
                        continue
                if managerName:
                    if assessNotice['managerName'] == managerName:
                        pass
                    else:
                        continue
                if assessStatus:
                    if assessNotice['assessStatus'] == assessStatus:
                        pass
                    else:
                        continue
                assessNoticeId = assessNotice['assessNoticeId']
                return assessNoticeId
        else:
            raise Exception('未查到考核信息,请核实后操作')

    def query_assess_notice_detail_by_name(self, noticeName, projectName='', managerName='', assessStatus='',
                                           userName=env.USERNAME_PMO):
        """
        根据名称查询项目考核详情
        :param noticeName: 考核名称
        :param projectName: 被考核项目名称
        :param managerName: 被考核人
        :param assessStatus: 考核状态: 1:已完成
                                     0:未完成
        :param userName: 默认为PMO角色
        :return:
        """
        assessNoticeId = self.query_assess_notice_id(noticeName=noticeName, projectName=projectName,
                                                     managerName=managerName, assessStatus=assessStatus,
                                                     userName=userName)

        method = 'GET'
        url = '/api/task/case/task/assessRecord/{0}'.format(assessNoticeId)

        resp = req_exec(method, url, username=userName)
        return resp

    def query_assess_notice_info_by_name(self, noticeName, projectName='', managerName='', userName=env.USERNAME_PMO):
        """
        根据名称查询项目考核信息
        :param noticeName: 考核名称
        :param projectName: 被考核项目名称
        :param managerName: 被考核人
        :param userName: 默认为PMO角色
        :return:
        """
        # 默认查询未考核完成考核内容
        assessStatus = '0'
        assessNoticeId = self.query_assess_notice_id(noticeName=noticeName, projectName=projectName,
                                                     managerName=managerName, assessStatus=assessStatus,
                                                     userName=userName)

        method = 'GET'
        url = '/api/task/case/task/assess/item/notice/role/items?assessNoticeId={0}'.format(assessNoticeId)

        resp = req_exec(method, url, username=userName)
        return resp['content']['data']['item']

    def cancle_assess_notice(self, noticeName, projectName='', managerName='', userName=env.USERNAME_PMO):
        """
        取消考核内容
        :param noticeName: 考核名称
        :param projectName: 被考核项目
        :param managerName: 被考核人员
        :param userName: 默认为PMO角色
        :return:
        """
        # 默认查询未完成项目
        assessStatus = '0'
        assessNoticeId = self.query_assess_notice_id(noticeName=noticeName, projectName=projectName,
                                                     managerName=managerName, assessStatus=assessStatus,
                                                     userName=userName)

        method = 'PATCH'
        data = {
            'assessStatus': '2'
        }
        url = '/api/task/case/task/assessNotice/{0}'.format(assessNoticeId)

        resp = req_exec(method, url, data=data, username=userName)
        return resp

    def query_assess_notice_execute_info(self, noticeName, projectName='', managerName='', userName=env.USERNAME_PMO):
        """
        查询考核内容执行信息
        :param noticeName: 考核名称
        :param projectName: 被考核项目名称
        :param managerName: 被考核人
        :param userName: 默认为PMO角色
        :return:
        """
        # 默认查询未完成项目
        assessStatus = '0'
        assessNoticeId = self.query_assess_notice_id(noticeName=noticeName, projectName=projectName,
                                                     managerName=managerName, assessStatus=assessStatus,
                                                     userName=userName)

        method = 'GET'
        url = '/api/task/case/task/assessNotice/execute/{0}'.format(assessNoticeId)

        resp = req_exec(method, url, username=userName)
        return resp['content']['data']['list']

    def execute_assess_notice(self, noticeName, projectName='', managerName='', projectAssess=None,
                              personnelAssess=None, userName=env.USERNAME_PMO):
        """
        执行考核内容
        :param noticeName: 考核名称
        :param projectName: 被考核项目
        :param managerName: 被考核人员
        :param projectAssess:   {
                                    'projectName': {
                                        'itemScore': ''
                                    },
                                    'projectName': {
                                        'itemScore': '',
                                        'content': '',
                                    },
                                    'projectName': {
                                        'itemScore': '',
                                        'content': '',
                                        'itemDescription': ''
                                    },...
                                }
        :param personnelAssess: {
                                    'personnelName': {
                                        'itemScore': ''
                                    },
                                    'personnelName': {
                                        'itemScore': '',
                                        'content': '',
                                    },
                                    'personnelName': {
                                        'itemScore': '',
                                        'content': '',
                                        'itemDescription': ''
                                    },...
                                }
        :param userName: 默认为PMO角色
        :return:
        """
        # 获取考核内容执行信息
        resp = self.query_assess_notice_execute_info(noticeName=noticeName, projectName=projectName,
                                                     managerName=managerName, userName=userName)
        assessRecordForm = []
        for noticeItem in resp:
            assessRecordForm += [ele for ele in noticeItem['second']]

        for assessRecord in assessRecordForm:
            # 项目打分
            if projectAssess:
                for projectAssessKey in projectAssess.keys():
                    if assessRecord['projectName'] == projectAssessKey:
                        if 'itemScore' in projectAssess[projectAssessKey].keys():
                            assessRecord['itemScore'] = projectAssess[projectAssessKey]['itemScore']
                        if 'content' in projectAssess[projectAssessKey].keys():
                            assessRecord['content'] = projectAssess[projectAssessKey]['content']
                        if 'itemDescription' in projectAssess[projectAssessKey].keys():
                            assessRecord['itemDescription'] = projectAssess[projectAssessKey]['itemDescription']
            # 人员打分
            if personnelAssess:
                for personnelAssessKey in personnelAssess.keys():
                    if assessRecord['managerName'] == personnelAssessKey:
                        if 'itemScore' in personnelAssess[personnelAssessKey].keys():
                            assessRecord['itemScore'] = personnelAssess[personnelAssessKey]['itemScore']
                        if 'content' in personnelAssess[personnelAssessKey].keys():
                            assessRecord['content'] = personnelAssess[personnelAssessKey]['content']
                        if 'itemDescription' in personnelAssess[personnelAssessKey].keys():
                            assessRecord['itemDescription'] = personnelAssess[personnelAssessKey]['itemDescription']
        assessRecordForm = json.dumps(assessRecordForm)

        method = 'POST'
        data = {
            'assessRecordForm': assessRecordForm
        }
        url = '/api/task/case/task/assessRecord'

        resp = req_exec(method, url, data=data, username=userName)
        return resp

    def query_personnel_report_by_date(self, date='', userName=env.USERNAME_PMO):
        """
        根据日期查询项目成员报告
        :param date: 日期 格式: %Y-%m-%d 不传默认取最新日期
        :param userName: 默认为PMO角色
        :return:
        """
        resp = self.query_reports_date()
        dateList = resp['content']['data']['list']

        if dateList:
            if not date:
                for dateEle in dateList:
                    date = dateEle[0]
            method = 'GET'
            url = '/api/task/case/task/user/reports?reportName={0}'.format(quote(date))

            resp = req_exec(method, url, username=userName)
            return resp
        elif not (dateList and date):
            raise Exception('暂无项目成员报告,请核实后操作')
        else:
            return resp

    def query_pm_report(self, searchKey='', startDate='', endDate='', userName=env.USERNAME_PMO):
        """
        查询项目经理报告
        :param searchKey: 关键字 -- 姓名
        :param startDate: 考核报告开始日期 格式: %Y-%m-%d
        :param endDate: 考核报告结束日期 格式: %Y-%m-%d
        :param userName: 默认为PMO角色
        :return:
        """
        # 只传一个日期默认为结束日期
        if startDate and not endDate:
            endDate = startDate
            startDate = ''

        method = 'GET'
        url = '/api/task/case/task/manageReport/pmo?currentPage={0}&perPage={1}'.format(self.currentPage, self.perPage)
        if searchKey:
            url += '&searchKey=' + quote(searchKey)
        if startDate:
            url += '&startDate=' + startDate
        if endDate:
            url += '&endDate=' + endDate

        resp = req_exec(method, url, username=userName)
        return resp

    def query_detail_by_name(self, name, startDate='', endDate='', userName=env.USERNAME_PMO):
        """
        根据姓名查看最近一次打分明细
        :param name: 姓名
        :param startDate: 考核报告开始日期 格式: %Y-%m-%d
        :param endDate: 考核报告结束日期 格式: %Y-%m-%d
        :param userName: 默认为PMO角色
        :return:
        """
        # 获取最近一次报告ID
        resp = self.query_pm_report(searchKey=name, startDate=startDate, endDate=endDate, userName=userName)
        managerReportId = resp['content']['data']['list'][0]['managerReportId']

        method = 'GET'
        url = '/api/task/case/task/manageReport/{0}/detail'.format(managerReportId)

        resp = req_exec(method, url, username=userName)
        return resp

    @staticmethod
    def query_reports_date(userName=env.USERNAME_PMO):
        """
        查询报告日期
        :param userName: 默认为PMO角色
        :return:
        """
        method = 'GET'
        url = '/api/task/case/task/user/reports/date'

        resp = req_exec(method, url, username=userName)
        return resp

    @staticmethod
    def query_projects_items(userName=env.USERNAME_PMO):
        """
        查询当前角色可考核项
        :param userName: 默认为PMO角色
        :return:
        """
        method = 'GET'
        url = '/api/task/case/task/assess/item/notice/role/items'

        resp = req_exec(method, url, username=userName)
        return resp

    @staticmethod
    def query_projects_users(userName=env.USERNAME_PMO):
        """
        查询可考核项目人员
        :param userName: 默认为PMO角色
        :return:
        """
        method = 'GET'
        url = '/api/task/case/task/projects/users'

        resp = req_exec(method, url, username=userName)
        return resp

    @staticmethod
    def query_assess_projects(userName=env.USERNAME_PMO):
        """
        查询可考核项目
        :param userName: 默认为PMO角色
        :return:
        """
        method = 'GET'
        url = '/api/task/case/task/projects/assess'

        resp = req_exec(method, url, username=userName)
        return resp


if __name__ == '__main__':
    ass = AssessmentItem()
    # ass.create_assess_item(itemName='86865', assessType='1', executorRole='4', defaultScore='60',
    #                        userName=env.USERNAME_PMO)
    # ass.modify_assess_item('11111', newItemName='22222', assessType='2', executorRole='4', defaultScore='60',
    #                        parentName='考核项5')
    # ass.delete_assess_item(itemName=['sss', 'ttt'])
    pa = ProjectAssessment()
    # pa.create_assess_notice(noticeName='64156645', assessItemList=[{'PMO人员考核': [env.USERNAME_RD, env.USERNAME_PM]},
    #                                                                  {'PMO项目考核': ['项目一', '项目二']}])
    # pa.query_pm_report(searchKey='开发', startDate='2021-7-30', endDate='2021-8-12')
    # pa.query_detail_by_name(name='开发', startDate='2021-7-30', endDate='2021-8-12')
    # pa.query_personnel_report_by_date()
    # pa.query_assess_notice()
    # pa.query_assess_notice_detail_by_name(noticeName='项目三考核', projectName='项目三', assessStatus='0')
    # pa.query_assess_notice_info_by_name(noticeName='项目三考核', projectName='项目二,项目三')
    # pa.modify_assess_notice(noticeName='test0831',
    #                         assessItemList=[{'考核项名称': []}, {'4456485': ['18392473277', '18111111111']}])
    # pa.cancle_assess_notice(noticeName='项目三考核', projectName='AutoTest_Project,test_中文名称项目', managerName='开发,职能')
    # pa.execute_assess_notice(noticeName='sdad',
    #                          projectAssess={
    #                              '蔡旭光测试项目': {
    #                                  'itemScore': '10'
    #                              },
    #                              '程飞扬测试项目': {
    #                                  'itemScore': '20',
    #                                  'content': '20',
    #                              },
    #                              '胡平测试项目': {
    #                                  'itemScore': '30',
    #                                  'content': '30',
    #                                  'itemDescription': '30'
    #                              }
    #                          },
    #                          personnelAssess={
    #                              '开发': {
    #                                  'itemScore': '10',
    #                                  'content': '10',
    #                              },
    #                              '职能': {
    #                                  'itemScore': '20',
    #                                  'content': '20',
    #                                  'itemDescription': '20'
    #                              }
    #                          })
