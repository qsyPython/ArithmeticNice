'''
大的国家：sqlite的增删改查
这里有张 World 表

+-----------------+------------+------------+--------------+---------------+
| name            | continent  | area       | population   | gdp           |
+-----------------+------------+------------+--------------+---------------+
| Afghanistan     | Asia       | 652230     | 25500100     | 20343000      |
| Albania         | Europe     | 28748      | 2831741      | 12960000      |
| Algeria         | Africa     | 2381741    | 37100000     | 188681000     |
| Andorra         | Europe     | 468        | 78115        | 3712000       |
| Angola          | Africa     | 1246700    | 20609294     | 100990000     |
+-----------------+------------+------------+--------------+---------------+
如果一个国家的面积超过300万平方公里，或者人口超过2500万，那么这个国家就是大国家。

编写一个SQL查询，输出表中所有大国家的名称、人口和面积。

例如，根据上表，我们应该输出:

+--------------+-------------+--------------+
| name         | population  | area         |
+--------------+-------------+--------------+
| Afghanistan  | 25500100    | 652230       |
| Algeria      | 37100000    | 2381741      |
+--------------+-------------+--------------+
'''

# 查询语句
# select name,population,area from Wrold where population>25000000 or area>3000000
#返回结果： {"headers":["name","population","area"],"values":[["Afghanistan",25500100,652230],["Algeria",37100000,2381741]]}

import sqlite3,os,re

# 判断表是否存在
def table_exists(cusor,table_name):
    # sqlite_master为内建table，sqlite中有一个内建表sqlite_master，
    # 这个表中存储这所有自建表的表名称等信息
    show_table_sql = 'select * from sqlite_master'
    cusor.execute(show_table_sql)
    tables = [cusor.fetchall()]
    table_list = re.findall('(\'.*?\')',str(tables))
    table_list = [re.sub("'",'',each) for each in table_list]
    if table_name in table_list:
        return True
    else:
        return False

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR,'4_1_test.sqlite3')
conn = sqlite3.connect(path)
cusor = conn.cursor()

if table_exists(cusor,'World'): #若表存在，删除旧表
    sql_del = 'drop table if exists World'
    cusor.execute(sql_del)

# 建表
create_table_sql = 'create table if not exists World'\
                   '(id varchar(50) primary key NOT NULL, name varchar(50) DEFAULT NULL,'\
                   'continent integer (50) DEFAULT NULL, area integer(50) DEFAULT NULL,' \
                   'population integer(50) DEFAULT NULL, gdp integer (50) DEFAULT NULL )'
cusor.execute(create_table_sql)

# 添加:
insert_sql = 'insert into World (id,name,continent,area,population,gdp) values (?,?,?,?,?,?)'
for i in range(6):
    cusor.execute(insert_sql,(i+1,'Afghanistan', 'Asia',652230,25500100,20343000))

#删除:最后1组数据
delete_sql = 'delete from World where id=?'
cusor.execute(delete_sql,(6,))

# 更新:
update_sql = 'update World set name=?,continent=?,area=?,population=?,gdp=? where id=?'
cusor.execute(update_sql,('Albania','Europe',28748,2831741,12960000,2))
cusor.execute(update_sql,('Algeria','Africa',2381741,37100000,188681000,3))
cusor.execute(update_sql,('Andorra','Europe',468,78115,3712000,4))
cusor.execute(update_sql,('Angola','Africa',1246700,20609294,100990000,5))

# 查询
search_sql = 'select name,population,area from World where population>? or area>?'
cusor.execute(search_sql,(25000000,3000000))
values = cusor.fetchall()
print('获取当前光标所触发sql条件的数据：%s' % values)
cusor.close()
conn.commit()
conn.close()




