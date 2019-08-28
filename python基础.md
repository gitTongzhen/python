
## 1.模块（Module）的使用

1.格式与概念
模块好比是工具包，要想使用工具包中的工具，就需要导入这个模块
python使用import的方法来导入模块
import module1,module2

2.注意点
在调用math模块中的函数时，必须这样引用：
模块名.函数名
为什么必须加上模块名调用呢？
答：可能用多个模块中有重名的函数，此时如果只是通过函数名来调用就无法得知具体是哪个函数了

3.from .,. import ...
有时候我们只需要用到模块中的某个函数，只需要引入该函数即可，此时可以使用下面的方法来实现
from 模块名 import 函数名1，函数名2
这不仅可以引入函数，还可以引入一些全局变量

4.在引入模块的时候改名：

import math as t

5.定位模块

当你导入一个模块时，python解析器对于模块搜索的顺序是：
1.当前目录
2.shell下面的pythonpath目录
3.查看默认路径下的目录
4.寻找system.path下面的目录

6.模块的制作
1.定义自己的模块，模块的名字就是一个文件
调用自己的模块
import test
result = test.add(1,2)

测试模块
def add(a,b):


5.模块中的__all__
没有all模块的时候，模块中所有的函数都可以被导入，但是有all模块的时候，只有all模块中定义的函数才可以被导入
```python
__all__=["test1","test2"]'''设置了在from test import *时只有test1()与test2()可以被导入'''
class Test():
    def test(self):
        print("---我执行了--")
def test1():
    print("---我也执行了")
def test2():
    print("---哈哈我也执行了---")

```
8.包的概念

1) 概念
包将有联系的模块组织在一起，放在同一个文件夹下面，并且在这个文件夹下面创建一个__init__.py的文件，那么这个文件夹就被称为包
可以有效的避免文件名称冲突，让应用组织更加清晰

2) __init__.py文件
__init__.py文件的有什么作用
__init__.py文件为空的时候，仅仅把这个包导入，不会导入包中的模块
__all__ :在__init__.py文件中定义一个__all__变量，它控制from 包名 import *时导入的模块
可以在__init__.py文件中编写内容：可以在这个文件中编写语言，当导入，这些语句就会被执行


## 2.python基础之字符串
1.概念
1.双引号或者单引号的数据就是字符串
2.字符串本质上在python中就是字符的数组

2.切片访问

切片是对操作的对象截取其中一部分的操作。字符串，列表，元组都支持切片操作

语法：[起始点：结束：步长]

选取的区间是左闭右开型的，从起始位开始到终止位的前一位停止（不包含结束符的那一个）

```python
name = "linghuchong"
print(name[2:5])
print(name[2:])
print(name[2:-1])
print(name[:3])
print(name[::2])
print(name[1:5:2])
print(name[::-2])
```
3.字符串的常见操作
1.find:检测str是否包含在mystr中，如果是返回开始的索引值，否则返回-1
```python
name = "linghuchong"
print(name.find("huch"))

```
2.index :和find()方法一样，不过没有的话会报告异常
3.count计算出现的次数
4.replace 吧mystr 中的str1替换为str2,如果count指定，则替换不超过count次
5.split 以str为分隔符切片mystr，如果maxsplit有指定值，则仅仅分隔maxsplit
6.join链接字符串


## 列表

1.列表格式
namelist = ["huiyao","longxin"]

比C语言强大之处在于列表中的元素可以使不同的类型
列表的下标也是从0开始的
2.列表的循环遍历

3.列表的相关操作(append,extend,insert)
1.append :向列表添加一个元素
2.extend:将另一个列表中所有元素逐一加到列表中
3.insert ：在指定的位置插入某个元素
insert(index,object)在指定的位置index前插入元素object

4.index ,count 

5.列表推导式

1.基本方式
a = [x for x in range(10)]
print(a)
a = [x for x in range(3,19)]
print(a)
a = [x for x in range(3,19,2)]
print(a)
2.在循环中使用if
a = [x for x in range(10) if x%2 == 0]
3.多个for循环
a = [(x,y) for x in range(1,3) for y in range(3)]

set list tuple 可以任意转化
### 使用set可以快速的完成对list中的元素去重复的功能
补充：
带下标的索引的遍历
enumrate()

a = [1,2,3,4,5,6,7,8,9]
for i,num in enumerate(a):
    print(i,num)




## 3.python基础篇之字典

1.相关知识点
格式：info = {'name':"fg",'id':102,"sex":"man"}

说明：
1.字典跟列表一样，也能够存储多个数据
2.列表中查找某个元素的时候，是根据下标进行的
3.字典中查找某个元素的时候，是根据'名字进行的'(就是冒号前面的那个值，例如上面代码中的)
4.字典的每个元素由两部分构成，键：值

当我们想要获取字典中的某个元素的时候，可以使用get方法，还可以设置为默认值
```python
info = {'name':"fg",'id':102,"sex":"man"}
age = info.get('age')  #因为'age'不存在，所以age为none
age = info.get('get',18) #若 info中不存在'age'这个键，就返回默认值18
```
3.字典的遍历
1.遍历字典的key
```python
info = {'name':"fg",'id':102,"sex":"man"}
for key in info.keys():
    print(key)
```
2.遍历字典的values
```python
info = {'name':"fg",'id':102,"sex":"man"}
for value in info.values():
    print(value)

```
3.遍历字典的项
```python
info = {'name':"fg",'id':102,"sex":"man"}
for item in info.items():
    print(item)

```

4.遍历字典的键值对
```python
info = {'name':"fg",'id':102,"sex":"man"}
for key,value in info.items():
    print("key = %s,value = %s"%(key,value))

```

## 5.文件操作
#### 1.打开文件
在python中，使用open函数的时候，可以打开一个已经存在的文件，或者创建一个新的文件
f = open('test.txt',w)
常用模式
1.w+ 打开一个文件用于读写，如果已经存在则将其覆盖，如果不存在则创建新文件
2.a+ 打开一个文件用于读写，如果该文件已经存在则将其覆盖，如果不存在，则创建新文件

#### 2.关闭文件
f.close()

#### 3.文件的读写（write）
1.写数据（write）
f = open('test.txt','w')
f.write("hello world ,i m here")
f.close()

## 3.读数据（readlines）
就像read没有参数时一样，readlines 可以按照行的方式把整个文件中的内容进行一次性的读取
并且返回的是一个列表
```python
f = open("test.txt",'r')
content = f.readlines()
print(type(content))

for temp in content:
    print(temp)
f.close()
```

### 4.文件夹相关的操作
就像对文件夹操作需要os模块一样，如果操作os模块同样需要os模块
1.创建文件夹
import os
os.mkdir("fengge")

2.获取当前目录
import os
print(os.getcwd())

3.改变默认目录
import os 
os.chdir("../")
os.mkdir("xiong")

4.获取目录列表
import os
print(os.listdir("./"))

5.删除文件夹
import os
os.chdir("./")
os.rmdir("xiong")
