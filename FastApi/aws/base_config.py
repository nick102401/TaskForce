# utf-8
from FastApi.base.base_api import req_exec
from FastApi.base.common import Common
from FastApi.common.helper import get_value_from_resp
from FastApi.conf import env


class BaseConfig(Common):
    """
    基础配置
    """

    def __init__(self):
        super(BaseConfig, self).__init__()

    """
    添加合格项点
    """

    @staticmethod
    def create_passItem(assessIndicatorId, assessIndicatorName, userName=env.USERNAME_SUP):
        method = 'POST'
        data = {
            'assessIndicatorId': assessIndicatorId,
            'assessIndicatorName': assessIndicatorName
        }
        url = '/api/task/case/task/assessIndicator/addDict'
        resp = req_exec(method, url, data=data, username=userName)
        return resp

    """
    assessIndicatorId:项目基准名称，1，2，3
    assessIndicatorName：项点名称
    """

    @staticmethod
    def query_passItem(userName=env.USERNAME_SUP):
        method = 'GET'
        url = '/api/task/case/task/assessIndicator/list'

        resp = req_exec(method, url, username=userName)
        return resp

    """
    修改合格项点
    """

    def modify_passItem(self, assessIndicatorName, newAssessIndicatorName, userName=env.USERNAME_SUP):
        resp = self.query_passItem()
        id = get_value_from_resp(resp['content'], 'id', 'assessIndicatorName', assessIndicatorName)

        method = 'PATCH'
        data = {
            'assessIndicatorName': newAssessIndicatorName,
            'id': id
        }
        url = '/api/task/case/task/assessIndicator/updateDict'
        resp = req_exec(method, url, data=data, username=userName)
        return resp

    """
    添加分值设置
    """

    @staticmethod
    def create_itemScore(userType, qualifiedScore, baseScore, initialScore, assessIndicatorId
                         , assessIndicatorName,
                         userName=env.USERNAME_SUP):
        method = 'POST'
        url = '/api/task/case/task/assessIndicator/addConfig'
        data = {
            'userType': userType,
            'qualifiedScore': qualifiedScore,
            'baseScore': baseScore,
            'initialScore': initialScore,
            'assessIndicatorId': assessIndicatorId,
            'assessIndicatorName': assessIndicatorName,
        }
        resp = req_exec(method, url, data=data, username=userName)
        return resp

    """
     查看合格项点分值设置
    """

    @staticmethod
    def query_itemScore(userName=env.USERNAME_SUP):
        method = 'GET'
        url = '/api/task/case/task/assessIndicator/getConfig'

        resp = req_exec(method, url, username=userName)
        return resp

    """
      编辑合格项点分值设置
    """

    def modify_itemScore(self, assessIndicatorName, userName=env.USERNAME_SUP, **modifyParams):
        """

        :param assessIndicatorName:项点名称
        :param userName:登陆账号
        :param modifyParams:
        :return:
        """
        resp = self.query_itemScore(userName=userName)
        list = resp['content']['data']['list']

        # 复制原有配置
        for ele in list:
            if ele['assessIndicatorName'] == assessIndicatorName:
                modifyBody = ele
                break
        else:
            raise Exception('无此合格项点分值名称,请核对后操作')

        # 根据传入修改参数赋值
        modifyParamsKeys = modifyParams.keys()
        for modifyParamsKey in modifyParamsKeys:
            if modifyParamsKey == 'qualifiedScore':
                modifyBody['qualifiedScore'] = modifyParams[modifyParamsKey]
            if modifyParamsKey == 'initialScore':
                modifyBody['initialScore'] = modifyParams[modifyParamsKey]
            if modifyParamsKey == 'baseScore':
                modifyBody['baseScore'] = modifyParams[modifyParamsKey]

        if not modifyBody['updateTime']:
            del modifyBody['updateTime']

        method = 'PATCH'
        data = modifyBody
        url = '/api/task/case/task/assessIndicator/updateScore'
        resp = req_exec(method, url, data=data, username=userName)
        return resp

    """
    userType:角色
    qualifiedScore:合格分值
    baseScore:基础分值
    initialScore:超合格线转换分值
    assessIndicatorId:名称对应ID
    assessIndicatorName:项点名称

    """

    '''
    级别基数点配置
    '''

    @staticmethod
    def query_levelConfig(userName=env.USERNAME_SUP):
        method = 'GET'
        url = '/api/task/case/task/levelBasePoint/list'

        resp = req_exec(method, url, username=userName)
        return resp

    """
    级别技术点修改
    """

    def modify_levelConfig(self, id, userName=env.USERNAME_SUP, **modifyParams):

        """
        id:级别
        """
        resp = self.query_levelConfig(userName=userName)
        list = resp['content']['data']['list']

        # 复制原有配置
        for ele in list:
            if ele['id'] == id:
                modifyBody = ele
                break
        else:
            raise Exception('无此设置级别,请核对后操作')

        # 根据传入修改参数赋值
        modifyParamsKeys = modifyParams.keys()
        for modifyParamsKey in modifyParamsKeys:
            """
            basePoint:基数点
            evaluateQualifiedScore：互评合格分
            """
            if modifyParamsKey == 'basePoint':
                modifyBody['basePoint'] = modifyParams[modifyParamsKey]
            if modifyParamsKey == 'evaluateQualifiedScore':
                modifyBody['evaluateQualifiedScore'] = modifyParams[modifyParamsKey]

        if not modifyBody['createTime']:
            del modifyBody['createTime']

        method = 'PATCH'
        data = modifyBody
        url = '/api/task/case/task/levelBasePoint/updatePoint'
        resp = req_exec(method, url, data=data, username=userName)
        return resp

    @staticmethod
    def query_baseConfig(userName=env.USERNAME_SUP):
        method = 'GET'
        url = '/api/task/case/task/basecfg'

        resp = req_exec(method, url, username=userName)
        return resp


if __name__ == '__main__':
    pass
    # base = BaseConfig()
    # base.create_passItem()
    # base.query_passItem()
    # print(base.create_passItem(3,'接口测试添加')['content']['code'])
    # base.modify_passItem('合格项3', '合格项33')
