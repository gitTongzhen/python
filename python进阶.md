### 1.map函数的使用

map()函数会根据提供的函数指定的序列做映射
map函数的语法如下：
map(function,iterable,...)


参数
function -- 函数
iterable -- 一个或者多个序列

返回值
python3.6返回迭代器


```python
def square(x):
    return x ** 2

a = [1,2,3,4,5]

b = list(map(square,a))

print(b)


```



使用lamda匿名函数

map(lambda x: x ** 2, [1,2,3,4,5])

也可以使用两个输入列表做相加

map(lambda x,y :x + y, [1,2,3,4,5],[6,7,8,9,10])




