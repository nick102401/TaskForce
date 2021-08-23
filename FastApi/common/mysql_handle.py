import warnings

import pymysql

from FastApi.common.logs_handle import Logger

warnings.filterwarnings('ignore')
log = Logger().logger


class MySql:
    def __init__(self, host, port, user='', password='', dbName=''):
        db = pymysql.connect(host=host, port=port, user=user, passwd=password, db=dbName, charset='utf8')
        self.cursor = db.cursor()

    def exec_sql(self, sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        log.info('result: ' + data)
        return data


if __name__ == '__main__':
    pass
