## 一些常见的SQL的技巧

1.负向条件查询不能使用索引
比如 select * from order where status!=0 and status !=1
not in/not exists都不是好习惯

2.前导模糊查询不能使用索引

select * from order where desc like '%xx'

而非前导的模糊查询是可以使用索引的

