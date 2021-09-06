import warnings

import psycopg2
import pymysql

from FastApi.common.logs_handle import Logger
from FastApi.conf.config import ReadConfig

warnings.filterwarnings('ignore')
log = Logger().logger


class DataBase:
    def __init__(self):
        self.config = ReadConfig()
        host = self.config.get_database('host')
        port = self.config.get_database('port')
        user = self.config.get_database('user')
        password = self.config.get_database('password')
        dbName = self.config.get_database('dbName')

        # 创建连接对象
        self.conn = psycopg2.connect(database=dbName, user=user, password=password, host=host, port=port)
        self.cursor = self.conn.cursor()  # 创建指针对象

    def exec_sql(self, sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        log.info(data)

        # 关闭练级
        self.cursor.close()
        self.conn.close()
        return data


if __name__ == '__main__':
    pass
    db = DataBase()
    db.exec_sql(sql="SELECT * FROM tb_project_apply WHERE apply_id = 'PA-768edf2f91c64671b9c7484995c2b503';")
