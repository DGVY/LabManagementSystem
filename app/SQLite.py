#coding=utf-8

'''
此文件用于SQLite的操作
'''

import sqlite3
import os

class SQLiteOp(object):
    
    def __init__(self, db_path):
        '''初始化'''
        self.db_path = db_path
        self.conn = None
        self.cursor = None

    def __get_conn(self):
        '''获取到数据库的连接对象，参数为数据库文件的绝对路径
        如果传递的参数是存在，并且是文件，那么就返回硬盘上面改
        路径下的数据库文件的连接对象；否则，返回内存中的数据接
        连接对象'''
        dbconn = sqlite3.connect(self.db_path)
        if os.path.exists(self.db_path) and os.path.isfile(self.db_path):
            self.conn = dbconn
        else:
            dbconn = None
            self.conn = sqlite3.connect(':memory:')

    def __get_cursor(self):
        '''该方法是获取数据库的游标对象，参数为数据库的连接对象
        如果数据库的连接对象不为None，则返回数据库连接对象所创
        建的游标对象；否则返回一个游标对象，该对象是内存中数据
        库连接对象所创建的游标对象'''
        if self.conn is not None:
            self.cursor =  self.conn.cursor()
        else:
            self.db_path = ''
            self.__get_conn('')
            self.cursor = self.conn.cursor()

    def __close_all(self):
        '''关闭数据库游标对象和数据库连接对象'''
        try:
            if self.cursor is not None:
                self.cursor.close()
        finally:
            if self.cursor is not None:
                self.cursor.close()
    

    def create_table(self,sql):
        '''创建表'''
        if SQLITE_DEBUG:
            print("# 创建数据库表")
        self.__get_conn()
        if sql is not None and sql != '':
            self.__get_cursor()
            if SQLITE_DEBUG:
                print('执行sql:[{}]'.format(sql))
            self.cursor.execute(sql)
            self.conn.commit()
            if SQLITE_DEBUG:
                print('创建数据库表成功!')
            self.__close_all()
        else:
            if SQLITE_DEBUG:
                print('the [{}] is empty or equal None!'.format(sql))

    def add_data(self,sql,data):
        '''插入数据'''
        if SQLITE_DEBUG:
            print("# 创建数据库表")       
        self.__get_conn()
        if sql is not None and sql != '':
            if data is not None:
                self.__get_cursor()
                for d in data:
                    if SQLITE_DEBUG:
                        print('执行sql:[{}],参数:[{}]'.format(sql, d))
                    self.cursor.execute(sql, d)
                    self.conn.commit()
                self.__close_all()
        else:
            if SQLITE_DEBUG:
                print('the [{}] is empty or equal None!'.format(sql))

    def fetch_one_data(self,sql,data):
        '''查询一条数据'''
        if SQLITE_DEBUG:
            print("# 查询一条数据")   
        self.__get_conn()
        if sql is not None and sql != '':
            if data is not None:
                # Do this instead
                d = (data,)
                self.__get_cursor()
                if SQLITE_DEBUG:
                    print('执行sql:[{}],参数:[{}]'.format(sql, data))
                self.cursor.execute(sql, d)
                return self.cursor.fetchall()[0][0]
                # r = self.cursor.fetchall()
                # if len(r) > 0:
                #     for e in range(len(r)):
                #         print(r[e])
            else:
                print('the [{}] equal None!'.format(data))
                return None
        else:
            print('the [{}] is empty or equal None!'.format(sql))
            return None
        
    def fetch_all_data(self,table):
        sql = 'SELECT * FROM ' + table
        self.__get_conn()
        if sql is not None and sql != '':
            self.__get_cursor()
            if SQLITE_DEBUG:
                print('执行sql:[{}]'.format(sql))
            self.cursor.execute(sql)
            r = self.cursor.fetchall()
            if len(r) > 0:
                for e in range(len(r)):
                    print(r[e])
        else:
            print('the [{}] is empty or equal None!'.format(sql))


# create_table_sql = '''CREATE TABLE `student` (
#                         `id` int(11) NOT NULL,
#                         `name` varchar(20) NOT NULL,
#                         `gender` varchar(4) DEFAULT NULL,
#                         `age` int(11) DEFAULT NULL,
#                         `address` varchar(200) DEFAULT NULL,
#                         `phone` varchar(20) DEFAULT NULL,
#                         PRIMARY KEY (`id`)
#                     )'''

# save_sql = '''INSERT INTO student values (?, ?, ?, ?, ?, ?)'''
# save_data = [(1, 'Hongten', u'男', 20, u'广东省广州市', '13423****62'),
#             (2, 'Tom', u'男', 22, u'美国旧金山', '15423****63'),
#             (3, 'Jake', u'女', 18, u'广东省广州市', '18823****87'),
#             (4, 'Cate', u'女', 21, u'广东省广州市', '14323****32')]

# fetchone_sql = 'SELECT * FROM student WHERE ID = ? '
# fetchone_data = 1

# DB_PATH = "test.db"



global SQLITE_DEBUG
SQLITE_DEBUG = False

def main():
    db = SQLiteOp(DB_PATH)
    # db.create_table(create_table_sql)
    # db.add_data(save_sql,save_data)
    db.fetch_one_data(fetchone_sql,fetchone_data)
    # db.fetch_all_data('student')

if __name__ == "__main__":
    main()
            
            
        