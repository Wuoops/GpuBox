import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.path.join(BASE_DIR, 'db.sqlite3')
# print(os.path.join(BASE_DIR, 'db.sqlite3'))


sql3Path = os.path.join(BASE_DIR, 'db.sqlite3')


class sqlDao():
    def __init__(self):
        self.connectDB()
    def connectDB(self):
        self.conn = sqlite3.connect(sql3Path)
        self.cursor = self.conn.cursor()
    #########
    #基本方法
    #断开连接
    def closeConn(self):
        self.conn.commit()
        self.conn.close()
    #查询一条数据
    def getOneP(self,sql,arg):
        self.cursor.execute(sql,arg)
        values = self.cursor.fetchone()
        return values
    def getOne(self,sql):
        self.cursor.execute(sql)
        values = self.cursor.fetchone()
        return values
    #查询全部数据
    def getAllP(self,sql,arg):
        self.cursor.execute(sql,arg)
        values = self.cursor.fetchall()
        return values
    def getAll(self,sql):
        self.cursor.execute(sql)
        values = self.cursor.fetchall()
        return values
    #查询多条数据
    def getManyP(self,sql,arg,size):
        self.cursor.execute(sql,arg)
        values = self.cursor.fetchmany(size=size)
        return values
    def getMany(self,sql,size):
        self.cursor.execute(sql)
        values = self.cursor.fetchmany(size=size)
        return values
    #x修改
    def modify(self,sql):
        self.cursor.execute(sql)
    def modifyP(self,sql,args):
        self.cursor.execute(sql,args)
        # self.connect.commit()
    #批量修改
    def multiple_modeify(self,sql,args):
        self.cursor.executemany(sql,args)
        # self.connect.commit()

    #创建插入，返回rowid
    def create(self,sql,args):
        self.cursor.execute(sql,args)
        return self.cursor.lastrowid
