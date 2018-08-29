# 宝石与石头：
# 给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
#
# J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。
#
# 示例 1:
#
# 输入: J = "aA", S = "aAAbbbb"
# 输出: 3
# 示例 2:
#
# 输入: J = "z", S = "ZZ"
# 输出: 0
# 注意:
#
# S 和 J 最多含有50个字母。
#  J 中的字符不重复。

def gemAndStone(gem,stone):
    try:
        tempStringLength = len(''.join(set(gem)))
        strCheck = lambda s: s.isalpha() and len(s) <= 50
        if (tempStringLength == len(gem) and strCheck(gem) and strCheck(stone)):
            count = 0;
            for c in gem:
                count = count + stone.count(c, 0, len(stone))
            print(count)
        else:
            print("请输入正确的字符串")
    except:
        print("请输入正确的字符串")

#
# 大的国家：
# 这里有张 World 表
#
# +-----------------+------------+------------+--------------+---------------+
# | name            | continent  | area       | population   | gdp           |
# +-----------------+------------+------------+--------------+---------------+
# | Afghanistan     | Asia       | 652230     | 25500100     | 20343000      |
# | Albania         | Europe     | 28748      | 2831741      | 12960000      |
# | Algeria         | Africa     | 2381741    | 37100000     | 188681000     |
# | Andorra         | Europe     | 468        | 78115        | 3712000       |
# | Angola          | Africa     | 1246700    | 20609294     | 100990000     |
# +-----------------+------------+------------+--------------+---------------+
# 如果一个国家的面积超过300万平方公里，或者人口超过2500万，那么这个国家就是大国家。
#
# 编写一个SQL查询，输出表中所有大国家的名称、人口和面积。
#
# 例如，根据上表，我们应该输出:
#
# +--------------+-------------+--------------+
# | name         | population  | area         |
# +--------------+-------------+--------------+
# | Afghanistan  | 25500100    | 652230       |
# | Algeria      | 37100000    | 2381741      |
# +--------------+-------------+--------------+

import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def openDb():
    path = os.path.join(BASE_DIR, 'db.sqlite3')
    mydb = sqlite3.connect(path)
    cursor = mydb.cursor()


    # #不存在则创建表 id 自增型
    create_table_sql = 'CREATE TABLE IF NOT EXISTS world (id INTEGER DEFAULT NULL,name varchar(100) NOT NULL,continent varchar(100) NOT NULL , \
                                 area INTEGER DEFAULT NULL , \
                                 population INTEGER DEFAULT NULL , \
                                 gdp INTEGER DEFAULT NULL)'
    cursor.execute(create_table_sql)

    # 删除数据
    drop_table_sql = 'DELETE FROM world'
    cursor.execute(drop_table_sql)
    mydb.commit()

    #插入数据
    insert_sql = "INSERT INTO world (id,name,continent,area,population,gdp) VALUES (?,?,?,?,?,?)"
    for i in  range(5):
        cursor.execute(insert_sql,(i,'china','chinachina',9600,130,1000))
        mydb.commit()

    data = [ ('Afghanistan','Asia',652230,25500100,20343000,0),
             ('Albania', 'Europe', 28748,2831741,12960000,1),
             ('Algeria', 'Aftica', 2381741,37100000,188681000,2),
             ('Andorra', 'Europe', 468,78115,3712000,3),
             ('Angola', 'Africa', 1246700, 20609294,100990000,4)]

    #更新数据
    for item in data:
        update_sql = "UPDATE world SET name = ?,continent = ?,area = ?,population =?,gdp = ? WHERE id = ?"
        cursor.execute(update_sql,item)
        mydb.commit()
    #查询数据
    cursor.execute("SELECT name,population,area FROM world WHERE area > 3000000 or population > 25500000;")
    rows = cursor.fetchall()
    print(rows)

def main():
    #gemAndStone("Ha","HHAssaHjj")
    openDb()

if __name__ == '__main__':
    main()