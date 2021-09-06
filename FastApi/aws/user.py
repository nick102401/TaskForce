import json

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


if __name__ == '__main__':
    pass
    user = User()
    # user.get_user_info()
    # print(user.get_user_id())
