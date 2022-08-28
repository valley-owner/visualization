import sqlite3
import time

import variable


class Data:
    def __init__(self):
        self.db_path = variable.GlobalParams.db_file
        self.conn = sqlite3.connect(self.db_path)
        # self.conn.isolation_level = None  # 这个就是事务隔离级别，默认是需要自己commit才能修改数据库，置为None则自动每次修改都提交,否则为""
        # 获取到游标对象
        self.cur = self.conn.cursor()

    def create_user_table(self):
        # 下面就是创建一个表
        self.conn.execute(
            '''create table if not exists user(
            id integer primary key autoincrement, 
            username varchar(128), 
            email varchar(128),
            password varchar(128),
            join_time TEXT,
            last_login TEXT)''')
        # 提交
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def insert_user(self, username, email, password, join_time):
        sql = r"insert into user(username, email, password, join_time) values (?,?,?,?);"
        date = (username, email, password, join_time)
        # 插入数据
        self.conn.execute(sql, date)
        # 提交
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def select_user(self, username):
        sql = f"select * from user where username=?"
        # 用游标来查询就可以获取到结果
        data = (username, )
        self.cur.execute(sql, data)
        # 这次查询后只取一个结果，就是一维列表
        res = self.cur.fetchone()
        # res = self.cur.fetchall()
        self.cur.close()
        self.conn.close()
        return res

    def update_user(self, username):
        sql = '''UPDATE user set last_login=? where username=?'''
        last_time = str(time.strftime('%Y-%m-%d %H:%M:%S'))
        data = (last_time, username)
        self.conn.execute(sql, data)
        self.cur.close()
        self.conn.close()




