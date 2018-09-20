# 某城市开了一家新的电影院，吸引了很多人过来看电影。该电影院特别注意用户体验，专门有个
# LED显示板做电影推荐，上面公布着影评和相关电影描述。
#
# 作为该电影院的信息部主管，您需要编写一个
# SQL查询，找出所有影片描述为非
# boring(不无聊)
# 的并且
# id
# 为奇数
# 的影片，结果请按等级
# rating
# 排列。
#
#
#
# 例如，下表
# cinema:
#
# +---------+-----------+--------------+-----------+
# | id | movie | description | rating |
# +---------+-----------+--------------+-----------+
# | 1 | War | great
# 3
# D | 8.9 |
# | 2 | Science | fiction | 8.5 |
# | 3 | irish | boring | 6.2 |
# | 4 | Ice
# song | Fantacy | 8.6 |
# | 5 | House
# card | Interesting | 9.1 |
# +---------+-----------+--------------+-----------+
# 对于上面的例子，则正确的输出是为：
#
# +---------+-----------+--------------+-----------+
# | id | movie | description | rating |
# +---------+-----------+--------------+-----------+
# | 5 | House
# card | Interesting | 9.1 |
# | 1 | War | great
# 3
# D | 8.9 |
# +---------+-----------+--------------+-----------+


import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def openDb():
    path = os.path.join(BASE_DIR, 'db.sqlite3')
    mydb = sqlite3.connect(path)
    cursor = mydb.cursor()


    # #不存在则创建表 id 自增型
    create_table_sql = 'CREATE TABLE IF NOT EXISTS cinema (id INTEGER DEFAULT NULL,movie varchar(100) NOT NULL,description varchar(100) NOT NULL , \
                                 rating INTEGER DEFAULT NULL)'
    cursor.execute(create_table_sql)

    # 删除数据
    drop_table_sql = 'DELETE FROM cinema'
    cursor.execute(drop_table_sql)
    mydb.commit()

    #插入数据
    insert_sql = "INSERT INTO cinema (id,movie,description,rating) VALUES (?,?,?,?)"
    for i in  range(5):
        cursor.execute(insert_sql,(i,'War','Science',9))
        mydb.commit()

    data = [ ('War','great 3D',8.9,0),
             ('Science', 'fiction',8.5,1),
             ('irish', 'boring',6.2,2),
             ('Ice song', 'Fantacy',8.6,3),
             ('House card', 'Interesting', 9.1,4)]

    #更新数据
    for item in data:
        update_sql = "UPDATE cinema SET movie = ?,description = ?,rating = ?  WHERE id = ?"
        cursor.execute(update_sql,item)
        mydb.commit()
    #查询数据
    cursor.execute("SELECT movie,description,rating FROM cinema WHERE id%2 = 1 and description NOT LIKE 'boring';")
    rows = cursor.fetchall()
    print(rows)

def main():
    openDb()

if __name__ == '__main__':
    main()