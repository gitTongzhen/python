## sql 语句学习
### 基础部分
1.改
update 表名称 set 列名称 = 新值 where 列名称 = 某值
2.删
delete from 表名称 where 列名称 = 值
删除所有行
delete * from table_name
3.增
insert into 表名称 values (值1,值2,...)
也可以制定所要插入数据的列
insert into table_name (列1，列2,...) values (值1，值2,...)
4.查
select 列名称 FROM 表名称

### 高级部分
**1.like语法**
LIKE 操作符用于在where子句中搜索指定的模式

比如 select * from persons where city like 'N%'

接下来，我们希望从person表中选取包含 'lon'的城市里面的人

select * From persons where City Like '%lon%'

**2.SQL通配符**

在所搜数据库中的数据的时候，SQL通配符可以替代一个或者多个字符。
SQL 通配符必须与LIKE运算符一起使用
通配符 | 描述
-| -
% | 代替一个或者多个字符|
_ | 仅仅代替一个字符 |
[charlist] | 字符列表中的任意单一字符
[^charlist] | 不存在于字符列表中的任何一个单一字符


Select * from person
where city like 'Ne%'

Select * from person 
where city like '_eorge'

**3.IN操作符**

IN和Where搭配使用
IN操作符允许我们在where子句中规定多个值
Select * From Persons
Where LastName IN('Adams','Carter')

**4.betwwen操作符**
操作符 BETWEEN...AND 会选取两个值之间的数值范围，这个值可以是数值，文本或者日期

Select * from persons
where LastName
Between 'adam' AND 'carter'

**5.Alias**
使用别名
Select column AS alias_name
from table_name


**6.join**
join 根据两个或者多个表之间的关系，从这些表中查询数据

**7.UNION合并来自两个或者多个表的数据**
SELECT column_name(s) FROM table_name1
UNION ALL
SELECT column_name(s) FROM table_name2


**8.SQL DROP INDEX语句**
功能删除索引，表和数据库

DROP INDEX index_name ON table_name

删除表

DROP TABLE 表名称

DROP DATABASE 数据库名称

**9.ALTER TABLE语句**
ALTER TABLE 语句用于在已有的表中添加修改和删除列
比如要在表中添加列，需要使用如下爱的语法
ALTER TABLE table_name
ADD column_name datatype

要删除表中的列，要使用如下的语法：
ALTER TABLE table_name
DROP COLUMN column_name




-------------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
1.常用命令
```
select 某列 from table
select distinct 某列 from table; 列出不同(distinct)的值
select 列名称 from 表名称 where 列 运算符 值；
select * from table where 列 运算符 值；条件查询(运算符： + <> >= between like)
select * from table where name = 'asdf' and id =1 ; and 运算符
select * from table where (name = 'dasdf' or id =23) and a_id =23
select * from table order by 列名称
insert into table values ('值'，'值'，'值','值') 插入新的行
insert into table (列名称,列名称) values('值'，'值'); 给指定的列插入数据
update table set 列名称 = 新值，列名称 = 新值 where id = 2; update 修改表中的数据
delete from table where id =1 删除某行
SQL高级语法：
select * from table limit 5 ;
select top 2 * from table; 取前两条
select top 50 percent * from table ; 取50%的数据
select * from table where 列名称 like 'n%'
可用于做通配符（% 代替一个或者多个字符 _：仅代表一个字符）
select * from table where id in (1,2,3,4)
select * from table where id between  between操作符
select * from 
```



---------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
2.sql性能和故障排查

show processlist;
