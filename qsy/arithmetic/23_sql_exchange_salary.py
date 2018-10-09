'''
    交换工资：
    给定一个 salary表，如下所示，有m=男性 和 f=女性的值 。交换所有的 f 和 m 值(例如，将所有 f 值更改为 m，反之亦然)。要求使用一个更新查询，并且没有中间临时表。

例如:

| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
运行你所编写的查询语句之后，将会得到以下表:

| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | f   | 2500   |
| 2  | B    | m   | 1500   |
| 3  | C    | f   | 5500   |
| 4  | D    | m   | 500    |
'''
# 方式1
# update_sql = 'update salary set sex = if(sex = "m","f","m")'

# 方式2
# UPDATE salary SET sex  = (CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END)

import sqlite3, os, re

# 判断数据库中tab是否存在
def table_exist(cursor, table_name):
    show_table_sql = 'select * from sqlite_master'
    cursor.execute(show_table_sql)
    tables = [cursor.fetchall()]
    table_list = re.findall('(\'.*?\')',str(tables))
    table_list = [re.sub("'",'',each) for each in table_list]
    if table_name in table_list:
        return  True
    else:
        return False
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR,'23_test.sqlite3')
conn = sqlite3.connect(path)
cursor = conn.cursor()
if table_exist(cursor,'salary'):
    sql_del = 'drop table if exists salary'
    cursor.execute(sql_del)
# 建表
create_sql_table = 'create table if not exists salary' \
             '(id varchar(255) primary key not null,' \
             ' name varchar(255) default null,' \
             ' sex varchar(255) default null,' \
             ' salary varchar(255) default null)'
cursor.execute(create_sql_table)

# 增加 insert into salary(id,name,sex,salary)
insert_sql = 'insert into salary(id,name,sex,salary) values()'
for i in range(6):
    cursor.execute(insert_sql,(i+1,'A','a',2500))

# 删除
dele_sql = 'delete'

# 修改

# 查找



cursor.close()
conn.commit()
conn.close()

