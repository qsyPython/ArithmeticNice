# Employee 表包含所有员工，他们的经理也属于员工。每个员工都有一个 Id，此外还有一列对应员工的经理的 Id。
#
# +----+-------+--------+-----------+
# | Id | Name  | Salary | ManagerId |
# +----+-------+--------+-----------+
# | 1  | Joe   | 70000  | 3         |
# | 2  | Henry | 80000  | 4         |
# | 3  | Sam   | 60000  | NULL      |
# | 4  | Max   | 90000  | NULL      |
# +----+-------+--------+-----------+
# 给定 Employee 表，编写一个 SQL 查询，该查询可以获取收入超过他们经理的员工的姓名。在上面的表格中，Joe 是唯一一个收入超过他的经理的员工。
#
# +----------+
# | Employee |
# +----------+
# | Joe      |
# +----------+

import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def openDb():
    path = os.path.join(BASE_DIR, 'db.sqlite3')
    mydb = sqlite3.connect(path)
    cursor = mydb.cursor()


    # #不存在则创建表 id 自增型
    create_table_sql = 'CREATE TABLE IF NOT EXISTS Employee (id INTEGER DEFAULT NULL,Name varchar(100) NOT NULL, \
                                 Salary INTEGER DEFAULT NULL , \
                                 ManagerId INTEGER DEFAULT NULL)'
    cursor.execute(create_table_sql)

    # 删除数据
    drop_table_sql = 'DELETE FROM Employee'
    cursor.execute(drop_table_sql)
    mydb.commit()

    #插入数据
    insert_sql = "INSERT INTO Employee (id,Name,Salary,ManagerId) VALUES (?,?,?,?)"
    for i in  range(5):
        cursor.execute(insert_sql,(i,'china',9600,0))
        mydb.commit()

    data = [ ('Joe',70000,3,1),
             ('Henry',80000,4,2),
             ('Sam',60000,"",3),
             ('Max', 90000,"",4),
              ]

    #更新数据
    for item in data:
        update_sql = "UPDATE Employee SET Name = ?,Salary = ?,ManagerId = ? WHERE id = ?"
        cursor.execute(update_sql,item)
        mydb.commit()
    #查询数据
    cursor.execute("SELECT Worker.Name AS Employee FROM Employee AS Worker, Employee AS Manager WHERE Worker.ManagerId = Manager.Id AND Worker.Salary > Manager.Salary;")
    rows = cursor.fetchall()
    print(rows)

def main():
    #gemAndStone("Ha","HHAssaHjj")
    openDb()

if __name__ == '__main__':
    main()