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

    if (gem.isalpha() and len(gem) <= 50) or (stone.isalpha() and len(stone) <= 50):
        count = 0;
        for c in gem:
          count = stone.count(c, 0, len(stone))
        print(count)
    else:
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
    cursor.execute("SELECT * FROM word WHERE area > 3000000 or population > 25500000;")
    rows = cursor.fetchall()
    print(rows)

def main():
    #gemAndStone("Ha","HHAssaHjj")
    openDb()

if __name__ == '__main__':
    main()