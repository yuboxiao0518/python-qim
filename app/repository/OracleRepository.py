import pandas as pd
from sqlalchemy import create_engine


class OracleRepository:
    def __init__(self):
        # 数据库连接
        self.db = create_engine('oracle://qmcb:qmcb@localhost:1521/tqmcbdb')

    def select(self):
        # 查询
        sql_select = ''' ...'''
        df = pd.read_sql_query(sql_select, self.db)

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
