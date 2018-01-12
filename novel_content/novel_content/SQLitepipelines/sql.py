#-*- coding:utf-8 -*-
import sqlite3

conn = sqlite3.connect('content.db')
cursor = conn.cursor()
#创建 dd_chaptername 表

cursor.execute('DROP TABLE IF EXISTS dd_chaptername')
cursor.execute('''CREATE TABLE dd_chaptername(name VARCHAR(255) DEFAULT NULL,xs_chaptername VARCHAR(255) DEFAULT NULL ,xs_content TEXT, 
                                                num_id INT(11) DEFAULT NULL ,url VARCHAR(255))''')
class Sql:

    @classmethod
    def insert_dd_chaptername(cls,name,xs_chaptername,xs_content,num_id,url):
        sql = '''INSERT INTO dd_chaptername(name,xs_chaptername , xs_content , num_id ,
                url) VALUES ('%s' ,'%s' ,'%s' ,%s ,'%s')''' % (name,xs_chaptername,xs_content,num_id,url)

        cursor.execute(sql)
        conn.commit()

    @classmethod
    def select_chapter(cls,url):
        sql = "SELECT EXISTS (select 1 from dd_chaptername where url = '%s')" % url
        cursor.execute(sql)
        return cursor.fetchall()[0]