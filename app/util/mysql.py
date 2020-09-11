# -*- coding: utf-8 -*-
import pymysql as ps
import util.getconfig as getconfig
from sqlalchemy import create_engine


class MySqlHelper():
    def __init__(self):
        self.host = '120.92.76.12'
        self.port = 3306
        self.user = 'root'
        self.password = 'Trading@it1851'
        self.db = 'trading'
        self.charset = 'utf8'

    def connet(self):
        self.conn = ps.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                               db=self.db, charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_one(self, sql, param=()):
        result = None
        try:
            self.connet()
            self.cursor.execute(sql, param)
            result = self.cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            self.close()
        return result

    def get_all(self, sql, param=()):
        result = None
        try:
            self.connet()
            self.cursor.execute(sql, param)
            result = self.cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            self.close()
        return result

    def __edit(self, sql, params):

        count = 0
        try:
            self.connet()
            count = self.cursor.execute(sql, params)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.close()
        return count

    def insert(self, sql, params):
        self.__edit(sql, params)

    def update(self, sql, params):
        self.__edit(sql, params)

    def delete(self, sql, params):
        self.__edit(sql, params)

    def writetodatabase(self, datas, tablename):
        engine = create_engine(
            "mysql+pymysql://" + self.user + ":" + self.password + "@" + self.host + ":" + str(
                3306) + "/" + self.db + "?charset=utf8")
        con = engine.connect()
        try:
            datas.to_sql(name=tablename, con=con, if_exists='append', index=False, index_label=False)
        except Exception as e:
            print(e)
        finally:
            con.close()


if __name__ == '__main__':
    strs = "mysql+pymysql://" + "aa" + ":" + "bb" + "@" + "cc" + ":" + str(3306) + "/" + "Dd" + "?charset=utf8"
    print(strs)
