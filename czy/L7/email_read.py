# 编写一个 SQL 查询，查找 Person 表中所有重复的电子邮箱。
#
# 示例：
#
# +----+---------+
# | Id | Email   |
# +----+---------+
# | 1  | a@b.com |
# | 2  | c@d.com |
# | 3  | a@b.com |
# +----+---------+
# 根据以上输入，你的查询应返回以下结果：
#
# +---------+
# | Email   |
# +---------+
# | a@b.com |
# +---------+


import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def openDb():
    path = os.path.join(BASE_DIR, 'db.sqlite3')
    mydb = sqlite3.connect(path)
    cursor = mydb.cursor()

    # #不存在则创建表 id 自增型
    create_table_sql = 'CREATE TABLE IF NOT EXISTS Person (Id INTEGER DEFAULT NULL,Email varchar(100) NOT NULL)'
    cursor.execute(create_table_sql)

    # 删除数据
    drop_table_sql = 'DELETE FROM Person'
    cursor.execute(drop_table_sql)
    mydb.commit()

    #插入数据
    insert_sql = "INSERT INTO Person (Id,Email) VALUES (?,?)"
    for i in  range(3):
        cursor.execute(insert_sql,(i,'china@google.com'))
        mydb.commit()

    data = [ ('a@b.com',0),
             ('c@d.com',1),
             ('a@b.com',2)
             ]

    #更新数据
    for item in data:
        update_sql = "UPDATE Person SET Email = ? WHERE id = ?"
        cursor.execute(update_sql,item)
        mydb.commit()
    #查询数据
    filter_sql = "SELECT Email FROM Person group BY Email HAVING COUNT(*) > 1;"
    cursor.execute(filter_sql)
    rows = cursor.fetchall()
    print(rows)

def main():
    openDb()

if __name__ == '__main__':
    main()