'''
    某城市开了一家新的电影院，吸引了很多人过来看电影。该电影院特别注意用户体验，专门有个 LED显示板做电影推荐，上面公布着影评和相关电影描述。

作为该电影院的信息部主管，您需要编写一个 SQL查询，找出所有影片描述为非 boring (不无聊) 的并且 id 为奇数 的影片，结果请按等级 rating 排列。



例如，下表 cinema:

+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   1     | War       |   great 3D   |   8.9     |
|   2     | Science   |   fiction    |   8.5     |
|   3     | irish     |   boring     |   6.2     |
|   4     | Ice song  |   Fantacy    |   8.6     |
|   5     | House card|   Interesting|   9.1     |
+---------+-----------+--------------+-----------+
对于上面的例子，则正确的输出是为：

+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   5     | House card|   Interesting|   9.1     |
|   1     | War       |   great 3D   |   8.9     |
+---------+-----------+--------------+-----------+
'''

# 'select * from cinema where description is not ? and id%2 != ? order by desc'


import sqlite3,os,re

def table_exist(cursor,table_name):
    show_table_sql = 'select * from sqlite_master'
    cursor.execute(show_table_sql)
    tables = [cursor.fetchall()]
    table_list = re.findall('(\'.*?\')', str(tables))
    table_list = [re.sub("'", '', each) for each in table_list]
    if table_name in table_list:
        return True
    else:
        return False

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR,'22_1_test.sqlite3')
conn = sqlite3.connect(path)
cursor = conn.cursor()
if table_exist(cursor,'cinema'):
    sql_del = 'drop table if exists cinema'
    cursor.execute(sql_del)
# 建表
create_sql_table = 'create table if not exists cinema'\
                   '(id varchar(50) primary key not null ,movie varchar (50) default null,'\
                   'description varchar (50) default null ,rating varchar (50) default null)'
cursor.execute(create_sql_table)

# 增
insert_sql = 'insert into cinema(id,movie,description,rating) values(?,?,?,?)'
for i in range(6):
    cursor.execute(insert_sql,(i+1,'War','great 3D','8.9'))

# 删除
dele_sql = 'delete from cinema where id=?'
cursor.execute(dele_sql,(6,))

# 更新
update_sql = 'update cinema set movie=?,description=?,rating=? where id=?'
cursor.execute(update_sql,('Science','fiction','8.5','2'))
cursor.execute(update_sql,('irish','boring','6.3','3'))
cursor.execute(update_sql,('Ice song','Fantacy','8.6','4'))
cursor.execute(update_sql,('House card','Interesting','9.1','5'))

# 查找
select_sql = 'select * from cinema where description is not ? and id%2 != ? order by rating desc'
cursor.execute(select_sql,('boring',0))


values = cursor.fetchall()
print(values)
cursor.close()
conn.commit()
conn.close()