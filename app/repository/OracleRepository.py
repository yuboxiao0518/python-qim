import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle
import config.config_util as config


class OracleRepository:

    def __init__(self):
        # 数据库连接
        ip = config.get_value('oracle', 'ip')
        port = config.get_value('oracle', 'port')
        uname = config.get_value('oracle', 'uname')  # 用户名
        pwd = config.get_value('oracle', 'pwd')  # 密码
        tnsname = config.get_value('oracle', 'tnsname')  # 实例名

        dsnStr = cx_Oracle.makedsn(ip, port, service_name=tnsname)
        connect_str = "oracle://%s:%s@%s" % (uname, pwd, dsnStr)
        self.db = create_engine(connect_str, encoding='utf-8')

    # 查询
    def select(self, sql):
        df = pd.read_sql_query(sql, self.db)
        return df

    def execute(self, ttb):
        # 执行
        self.db.execute('truncate table {}'.format(ttb))

    def save(self, df):
        # 保存
        df.to_sql()  # 太慢

    def insert(self, df, ttb):
        # 插入
        conn = self.db.raw_connection()
        cursor = conn.cursor()
        col = ', '.join(df.columns.tolist())
        s = ', '.join([':' + str(i) for i in range(1, df.shape[1] + 1)])
        sql = 'insert into {}({}) values({})'.format(ttb, col, s)
        cursor.executemany(sql, df.values.tolist())
        conn.commit()
        cursor.close()


if __name__ == '__main__':
    sql_select = ''' SELECT * from META_MODEL'''
    repository = OracleRepository()
    repository.select(sql_select)
