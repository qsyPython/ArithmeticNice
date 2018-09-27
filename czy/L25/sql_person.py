# 表1: Person
#
# +-------------+---------+
# | 列名 | 类型 |
# +-------------+---------+
# | PersonId | int |
# | FirstName | varchar |
# | LastName | varchar |
# +-------------+---------+
# PersonId
# 是上表主键
# 表2: Address
#
# +-------------+---------+
# | 列名 | 类型 |
# +-------------+---------+
# | AddressId | int |
# | PersonId | int |
# | City | varchar |
# | State | varchar |
# +-------------+---------+
# AddressId
# 是上表主键
#
# 编写一个
# SQL
# 查询，满足条件：无论
# person
# 是否有地址信息，都需要基于上述两表提供
# person
# 的以下信息：
#
#
#
# FirstName, LastName, City, State


import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def openDb():
    path = os.path.join(BASE_DIR, 'db.sqlite3')
    mydb = sqlite3.connect(path)
    cursor = mydb.cursor()


    #不存在则创建表 Person
    create_table_person_sql = 'CREATE TABLE IF NOT EXISTS Person (PersonId INTEGER DEFAULT NULL,FirstName varchar(100) NOT NULL,LastName varchar(100) NOT NULL)'
    cursor.execute(create_table_person_sql)

    # #不存在则创建表 Address
    create_table_Address_sql = 'CREATE TABLE IF NOT EXISTS Address(AddressId INTEGER DEFAULT NULL,PersonId INTEGER DEFAULT NULL,City varchar(100) NOT NULL,State varchar(100) NOT NULL)'
    cursor.execute(create_table_Address_sql)

    # 删除数据
    drop_table_sql = 'DELETE FROM Person'
    cursor.execute(drop_table_sql)
    mydb.commit()

    # 删除数据
    drop_table_sql = 'DELETE FROM Address'
    cursor.execute(drop_table_sql)
    mydb.commit()

    #插入数据
    insert_sql = "INSERT INTO Address (AddressId,PersonId,City,State) VALUES (?,?,?,?)"
    for i in  range(5):
        cursor.execute(insert_sql,(i,i,'china','chinachina'))
        mydb.commit()

        # 插入数据
    insert_sql = "INSERT INTO Person (PersonId,FirstName,LastName) VALUES (?,?,?)"
    for i in range(5):
        cursor.execute(insert_sql, (i,'china', 'chinachina'))
        mydb.commit()


    data = [ ('Afghanistan','Asia',0),
             ('Albania', 'Europe',1),
             ('Algeria', 'Aftica',2),
             ('Andorra', 'Europe',3),
             ('Angola', 'Africa',4)]

    dataAdress = [('Afghanistan', 'Asia', 0),
            ('Albania', 'Europe', 1),
            ('Algeria', 'Aftica', 2),
            ('Andorra', 'Europe', 3),
            ('Angola', 'Africa', 4)]

    #更新数据
    for item in data:
        update_sql = "UPDATE Person SET FirstName = ?,LastName = ? WHERE PersonId = ?"
        cursor.execute(update_sql,item)
        mydb.commit()
        # 更新数据
    for item in dataAdress:
        update_sql = "UPDATE Address SET City = ?,State = ? WHERE PersonId = ?"
        cursor.execute(update_sql, item)
        mydb.commit()
    #查询数据
    cursor.execute("SELECT Person.FirstName,Person.FirstName,Address.City,Address.State FROM Person,Address WHERE Address.PersonId = Person.PersonId;")
    rows = cursor.fetchall()
    print(rows)

def main():
    #gemAndStone("Ha","HHAssaHjj")
    openDb()

if __name__ == '__main__':
    main()