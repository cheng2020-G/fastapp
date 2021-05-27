import pymysql


# db = pymysql.connect(host='192.168.0.92', user='root', password='aikan', database='glory', port=3306, charset='utf8')
# curses = db.cursor()
# curses.execute("SELECT * FROM glory.b_book_chapter WHERE book_id= '11000125127'")
# data_db = curses.fetchone()
# print(data_db)
# curses.close()
# db.close()

# class FastAppMysql(object):
#     def __init__(self, host, user, passwd, port, db, charset):
#         self.host = host
#         self.user = user
#         self.port = port
#         self.passwd = passwd
#         self.db = db
#         self.charset = charset
#
#     def open_conne(self):
#         self.conn = pymysql.connect(host=self.host, user=self.user, password=self.passwd, port=self.port, db=self.db,
#                                     charset=self.charset)
#         self.curses = self.conn.cursor()
#
#     def close_conne(self):
#         self.curses.close()
#         self.conn.close()
#
#     def get_db_sql(self, sql):
#         try:
#             self.open_conne()
#             self.curses.execute(sql)
#             return self.curses.fetchone()
#         except Exception as error:
#             print(error)
#         finally:
#             self.conn.close()


# if __name__ == '__main__':
#     sql_95 = FastAppMysql('192.168.0.92', 'root', 'aikan', 3306, 'glory', 'utf8')
#     print(sql_95.get_db_sql("SELECT * FROM glory.b_book_chapter WHERE book_id= '11000125127'"))


class FastAppMysql:

    def open_conne(self):
        self.conn = pymysql.connect(host='192.168.0.92', user='root', password='aikan', port=3306, db='glory',
                                    charset='utf8')
        self.curses = self.conn.cursor()

    def close_conne(self):
        self.curses.close()
        self.conn.close()

    def get_db_sql(self, sql):
        try:
            self.open_conne()
            self.curses.execute(sql)
            return self.curses.fetchone()
        except Exception as error:
            print(error)
        finally:
            self.conn.close()


if __name__ == '__main__':
    sql_95 = FastAppMysql().get_db_sql("SELECT * FROM glory.b_book_chapter WHERE book_id= '11000125127'")
    print(sql_95)
