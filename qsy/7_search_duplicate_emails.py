'''
   查找重复邮箱：
编写一个 SQL 查询，查找 Person 表中所有重复的电子邮箱。

示例：

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
根据以上输入，你的查询应返回以下结果：

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
说明：所有电子邮箱都是小写字母。
'''
# 查询到重复邮件的 sql 语句：select email from Person group by email having count(email)>1

import os,re,sqlite3

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

if table_exists(cusor,'Person'):# 存在，删除重建
    sql_table = 'drop table if exists Person'
    cusor.execute(sql_table)

# 建表
create_table_sql = 'create table if not exists Person(id varchar(50) primary key  not NULL ,email varchar (50) default NULL )'
cusor.execute(create_table_sql)


# 少：处理数据时，不用每条都commit，commit后会统一把所有语句执行打包
# 添加:
insert_sql = 'insert into Person (id,email) values (?,?)'
for i in range(6):
    cusor.execute(insert_sql,[i+1,'1129331905@qq.com'])

#删除:删除最后1组
del_sql = 'delete from Person where id=?'
cusor.execute(del_sql,[6])

# 更改
update_sql = 'update Person set email=? where id = ?'
cusor.execute(update_sql,['1129331903@qq.com',3])
cusor.execute(update_sql,['1129331903@qq.com',4])
cusor.execute(update_sql,['1129331902@qq.com',5])

# 查找
search_sql = 'select email from Person group by email having count(email)>1 '
cusor.execute(search_sql)
values = cusor.fetchall()
print('获取查询重复的邮件:%s' % values)
cusor.close()
conn.commit()
conn.close()
