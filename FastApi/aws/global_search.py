import json

from FastApi.base.base_api import req_exec
from FastApi.base.common import Common
from FastApi.conf import env


class GlobalSearch(Common):
    """
    全局搜索
    """

    def __init__(self):
        super(GlobalSearch, self).__init__()

    def search(self, searchKey='', fileEnd='', allOnly=True, userName=env.USERNAME_PG):
        """
        全局搜索
        :param searchKey: 关键字
        :param fileEnd: 文件后缀
        :param allOnly:
        :param userName: 默认为职能人员
        :return:
        """
        method = 'GET'
        url = '/api/task/case/task/search?pageNum={0}&size={1}&'.format(self.currentPage, self.perPage)

        if searchKey:
            url += 'searchkey=' + searchKey + '&'
        if fileEnd:
            url += 'fileEnd=' + fileEnd + '&'
        else:
            url += 'fileEnd=&'
        if allOnly:
            url += 'allOnly=' + json.dumps(allOnly)

        resp = req_exec(method, url, username=userName)
        return resp


if __name__ == '__main__':
    pass
    gs = GlobalSearch()
    gs.search()
