from FastApi.base.base_api import req_exec
from FastApi.base.common import Common
from FastApi.common.helper import get_value_from_resp
from FastApi.conf import env


class User(Common):
    """
    用户管理
    """

    def __init__(self):
        super(User, self).__init__()

    @staticmethod
    def get_personal_info(userName='', password=env.USER_PWD):
        """
        个人中心
        :param userName:
        :param password:
        :return:
        """
        method = 'GET'
        url = '/api/task/case/task/user/user'
        resp = req_exec(method, url, username=userName, password=password)
        return resp

    def get_user_info(self, searchKey='', username=env.USERNAME, password=env.PASSWORD):
        """
        管理员登录获取用户信息
        :param searchKey: 查询条件
        :param username:
        :param password:
        :return:
        """
        self.currentPage = 1
        self.perPage = 200
        method = 'GET'
        url = '/api/task/case/task/user/page?currentPage={0}&pageSize={1}'.format(self.currentPage, self.perPage)
        if searchKey:
            url += '&searchKey=' + searchKey
        resp = req_exec(method, url, username=username, password=password)
        return resp

    def get_user_id(self, username=env.USERNAME_PM):
        """
        获取用户ID
        :param username: 待查询的用户名
        :return:
        """
        resp = self.get_user_info()
        return get_value_from_resp(resp['content'], 'userId', 'realName', username)

    def modify_user_role(self, userName='', userId='', role=''):
        """
        修改用户角色
        :param userName: 待修改用户名称
        :param userId: 用户ID
        :param role: 待修改角色
        :return:
        """
        if userName:
            userId = self.get_user_id(username=userName)

        if userId:
            method = 'PUT'
            data = {
                'role': role
            }
            url = '/api/task/case/task/user/user/role/{0}'.format(userId)
            resp = req_exec(method, url, data=data, username=env.USERNAME, password=env.PASSWORD)
            return resp
        else:
            raise Exception('用户不存在,请核对后再操作')


class BaseConfig(Common):
    """
    基础配置
    """

    def __init__(self):
        super(BaseConfig, self).__init__()

    """
    基础设置
    """

    @staticmethod
    def query_base_config(userName=env.USERNAME_SUP):
        """
        查询基础设置
        :param userName:
        :return:
        """
        method = "GET"
        url = "/api/task/case/task/basecfg"

        resp = req_exec(method, url, username=userName)
        return resp

    """
    级别基数点配置
    """

    @staticmethod
    def query_level_config(userName=env.USERNAME_SUP):
        """
        查询级别基数点配置
        :param userName:
        :return:
        """
        method = "GET"
        url = "/api/task/case/task/levelBasePoint/list"

        resp = req_exec(method, url, username=userName)
        return resp

    def modify_level_config(self, id, userName=env.USERNAME_SUP, **modifyParams):
        """
        修改级别技术点配置
        :param id: 级别
        :param userName:
        :param modifyParams: basePoint: 基数点
                             evaluateQualifiedScore: 互评合格分
        :return:
        """
        resp = self.query_level_config(userName=userName)
        list = resp["content"]["data"]["list"]

        # 复制原有配置
        for ele in list:
            if ele["id"] == id:
                modifyBody = ele
                break
        else:
            raise Exception("无此设置级别,请核对后操作")

        # 根据传入修改参数赋值
        modifyParamsKeys = modifyParams.keys()
        for modifyParamsKey in modifyParamsKeys:
            """
            basePoint:基数点
            evaluateQualifiedScore：互评合格分
            """
            if modifyParamsKey == "basePoint":
                modifyBody["basePoint"] = modifyParams[modifyParamsKey]
            if modifyParamsKey == "evaluateQualifiedScore":
                modifyBody["evaluateQualifiedScore"] = modifyParams[modifyParamsKey]

        if not modifyBody["createTime"]:
            del modifyBody["createTime"]

        method = "PATCH"
        data = modifyBody
        url = "/api/task/case/task/levelBasePoint/updatePoint"
        resp = req_exec(method, url, data=data, username=userName)
        return resp

    """
    合格项点配置
    """

    @staticmethod
    def create_pass_item(assessIndicatorId, assessIndicatorName, userName=env.USERNAME_SUP):
        """
        创建合格项
        :param assessIndicatorId: 项目基准名称: 1:互评
                                              2:项目
                                              3:任务
        :param assessIndicatorName: 项点名称
        :param userName:
        :return:
        """
        method = "POST"
        data = {"assessIndicatorId": assessIndicatorId, "assessIndicatorName": assessIndicatorName}
        url = "/api/task/case/task/assessIndicator/addDict"
        resp = req_exec(method, url, data=data, username=userName)
        return resp

    @staticmethod
    def query_pass_item(userName=env.USERNAME_SUP):
        """
        查询合格项
        :param userName:
        :return:
        """
        method = "GET"
        url = "/api/task/case/task/assessIndicator/list"

        resp = req_exec(method, url, username=userName)
        return resp

    def modify_pass_item(
            self, assessIndicatorName, newAssessIndicatorName, userName=env.USERNAME_SUP
    ):
        """
        修改合格项
        :param assessIndicatorName:
        :param newAssessIndicatorName:
        :param userName:
        :return:
        """
        resp = self.query_pass_item()
        assessIndicatorId = get_value_from_resp(resp["content"], "id", "assessIndicatorName", assessIndicatorName)

        method = "PATCH"
        data = {"assessIndicatorName": newAssessIndicatorName, "id": assessIndicatorId}
        url = "/api/task/case/task/assessIndicator/updateDict"
        resp = req_exec(method, url, data=data, username=userName)
        return resp

    """
    合格项点分值设置
    
    userType:角色
    qualifiedScore:合格分值
    baseScore:基础分值
    initialScore:超合格线转换分值
    assessIndicatorId:名称对应ID
    assessIndicatorName:项点名称
    """

    @staticmethod
    def create_item_score(
            userType,
            qualifiedScore,
            baseScore,
            initialScore,
            assessIndicatorId,
            assessIndicatorName,
            userName=env.USERNAME_SUP,
    ):
        """
        创建合格项点分值设置
        :param userType:
        :param qualifiedScore:
        :param baseScore:
        :param initialScore:
        :param assessIndicatorId:
        :param assessIndicatorName:
        :param userName:
        :return:
        """
        method = "POST"
        url = "/api/task/case/task/assessIndicator/addConfig"
        data = {
            "userType": userType,
            "qualifiedScore": qualifiedScore,
            "baseScore": baseScore,
            "initialScore": initialScore,
            "assessIndicatorId": assessIndicatorId,
            "assessIndicatorName": assessIndicatorName,
        }
        resp = req_exec(method, url, data=data, username=userName)
        return resp

    @staticmethod
    def query_item_score(userName=env.USERNAME_SUP):
        """
        查看合格项点分值设置
        :param userName:
        :return:
        """
        method = "GET"
        url = "/api/task/case/task/assessIndicator/getConfig"

        resp = req_exec(method, url, username=userName)
        return resp

    def modify_item_score(self, assessIndicatorName, userName=env.USERNAME_SUP, **modifyParams):
        """
        编辑合格项点分值设置
        :param assessIndicatorName:项点名称
        :param userName:登陆账号
        :param modifyParams:
        :return:
        """
        resp = self.query_item_score(userName=userName)
        list = resp["content"]["data"]["list"]

        # 复制原有配置
        for ele in list:
            if ele["assessIndicatorName"] == assessIndicatorName:
                modifyBody = ele
                break
        else:
            raise Exception("无此合格项点分值名称,请核对后操作")

        # 根据传入修改参数赋值
        modifyParamsKeys = modifyParams.keys()
        for modifyParamsKey in modifyParamsKeys:
            if modifyParamsKey == "qualifiedScore":
                modifyBody["qualifiedScore"] = modifyParams[modifyParamsKey]
            if modifyParamsKey == "initialScore":
                modifyBody["initialScore"] = modifyParams[modifyParamsKey]
            if modifyParamsKey == "baseScore":
                modifyBody["baseScore"] = modifyParams[modifyParamsKey]

        if not modifyBody["updateTime"]:
            del modifyBody["updateTime"]

        method = "PATCH"
        data = modifyBody
        url = "/api/task/case/task/assessIndicator/updateScore"
        resp = req_exec(method, url, data=data, username=userName)
        return resp


if __name__ == "__main__":
    pass
    # base = BaseConfig()
    # base.create_pass_item()
    # base.query_pass_item()
    # print(base.create_pass_item(3,'接口测试添加')['content']['code'])
    # base.modify_pass_item('合格项3', '合格项33')
