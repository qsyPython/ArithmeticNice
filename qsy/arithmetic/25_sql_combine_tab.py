'''
 组合2个表：
 表1: Person

+-------------+---------+
| 列名         | 类型     |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId 是上表主键
表2: Address

+-------------+---------+
| 列名         | 类型    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId 是上表主键


编写一个 SQL 查询，满足条件：无论 person 是否有地址信息，都需要基于上述两表提供 person 的以下信息：



FirstName, LastName, City, State
'''
# 合并成新的表，根据PersonId获取到对应所有信息
# 合并重复数据：select * from Person union select * from Address
# 不和并重复数据：select * from Person union all select * from Address

#search_sql = 'select p.FirstName, p.LastName, a.City, a.State from Person p left join Address a on p.PersonId = a.PersonId';

