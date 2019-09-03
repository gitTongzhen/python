
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


面向对象
1.概念
面向过程：根据业务逻辑从上到下写代码
面向对象：将函数和数据进行绑定到一起，进行封装，这样子能够更快的开发程序，减少重复代码的重写过程
OOP是一种解决软件复用的设计和编程方法，这种方法把软件系统中相近相似的操作逻辑和操作应用数据，状态，类的形式描述出来
2.类和对象
1.类
类是抽象的，在使用的时候通常会找到一个这个类的具体的存在，使用这个具体的存在，一个类可以找到多个对象
2.对象
某一个具体事物的存在，在现实世界中可以看得到摸得到，可以直接使用的
3.类和对象之间的关系
类就是创建对象的模板

4.类的构成

类由三部构成
类的名称：类名
类的属性：一组数据
类的方法：允许对进行操作的方法

举例：
人类设计，只关心三样东西：
事物的名称：人
属性：身高（height）年龄（age）
方法：跑（run）,打架（fight）
2狗类的设计
类名：狗（dog）
属性：品种，毛色，性别
方法（行为/功能）：叫，跑，咬人，吃，摇尾巴

6.定义一个类

class 类名：
    方法列表

```python
class Car:
    #方法
    def getCarInfo(self):
        print('车轮子个数')


```

### __init__()方法
1.使用方式
```python
def 类名
# 初始化函数，用来完成一些默认的设定
def __init__():
    pass
```
2.__init__()方法的调用

```python
class Car:
    ## 方法
    def __init__(self):
        self.color = "blue"
        self.wheelNum = 4
    def getCarInfo(self):
        print('车轮子的个数%d,颜色%s'%(self.wheelNum,self.color))
    
    def move(self):
        print("车在移动....")

bens = Car()

bens.getCarInfo()

bens.move()

```
1.__init__()方法在创建一个对象的时候默认被调用，不需要手动去调用
2.__init__(self)默认有一个参数的名字为self，如果在创建对象的时候传递了两个实参，那么
__init__(self) 中出了self作为一个参数外还需要两个形参，例如__init__(self,x,y)
3.__init__(self) 中的self参数，不需要开发者传递，python解释器会自动

10.self 

```python
class Animal:
    def __init__(self,name):
        self.name = name
    def printName(self):
        print('名字为：%s'%self.name)

def myPrint(animal):
    animal.printName()

dog1 =Animal("西西")

myPrint(dog1)
dog2 = Animal("北北")
myPrint(dog2)

```

所谓self,可以理解为自己
可以把self当成是C++类里面的this指针一样理解，就是对象本身的意思
某个对象调用其方法的时候，python解释器会把这个对象的第一个参数传递给self
所以开发者只需要传递后面的参数就好了

面向对象
1.保护对象的属性
如果有一个对象，当需要对其进行修改属性的时候，有两种方法
1.对象名.属性名 = 数据 --->直接修改
2.对象名.方法名 ----->间接修改

为了更好的保护属性的安全，即不能够随意的更改，一般的处理方式为
1.将属性定义为私有属性
2.添加一个可以调用的方法，供调用

```python 
class People:
    def __init__(self,name):
        self.__name = name
    def getName(self): #提供调用私有属性的方法
        return self.__name
    def setName(self,nameName):
        if len(newName)>5:
            self.__name = newName
        else:
            print("长大了")
xiaoming = People("xaioming")
xiaoming = setName("xiaohuang")
print(xiaoming.getName())
```
2.__del__()方法
当删除一个对象的时候，python解析器，也会默认调用一个方法，这个方法就是__del__()
方法

```python
class Animal:
    # 初始化方法
    def __init__(self,name):
        print("__init__方法被调用")
        self.__name = name
    
    ##析构的方法： 当对象被删除的时候会自动调用
    def __del__(self):
        print("__del__ 方法被调用")
        print("%s对象马上狗带。。"%self.__name)

dog = Animal("柯基")
del dog

```
#### 8.静态方法和类方法
1.类方法
1.是类对象所拥有的方法，需要用装饰器@classmethod来标识其为类方法，对于类方法，第一个参数，必须是类对象，一般以cls作为第一个参数（当然可以用其他名称的变量作为其第一个参数，但是大部分人都习惯以cls作为第一个参数的名称，就最好用cls），能够通过实例对象和类对象去访问

```python
class People(object):
    country = 'china'
    ## 类方法，使用classmethod 来进行修饰
    @classmethod
    def getCountry(cls):
        return cls.country

p = People()
print(p.getCountry())  #可以用过实例对象引用

print(People.getCountry())

```

类方法还有一个用途就是可以对类属性进行修改：

```python
class People(object):
    country = 'china'
    #类方法 用classmethod 来进行修饰
    @classmethod
    def getCountry(cls):
        return cls.country
    @classmethod
    def setCountry(cls,country):
        cls.country = country

p = People()

print(p.getCountry())   #可以用实例对象引用
print(People.getCountry())   #可以用类对象进行引用
People.setCountry('japen')
print(p.getCountry())
print(People.getCountry())

```



2.静态方法

需要通过修饰器@staticmethod 来进行修饰，静态方法不需要定义参数

```python
class People(object):
    country = 'china'

    @staticmethod
    #静态方法
    def getCountry():
        return People.country

print(People.getCountry())


```

从类方法和实例方法以及静态方法的定义形式可以看出来，类方法的第一个参数是类对象，那么通过cls引用的必定是类对象的属性和方法；,而实例方法的第一个第一个对象是实例对象self,那么通过self引用的可能是类属性，也有可能是实例属性（这个需要具体去分析），不过存在相同的名称的类属性和实例属性的情况下，实例属性优先级更高，静态方法中不需要额外定义参数，因此在静态方法中引用类属性的话，必须通过类对象来引用



### 公共方法

python常用的内置函数
cmp(item1,item2) 比较两个数值
len(item) 计算容器中的元素个数
max(item) 返回容器中的元素的最大值
min(item) 返回容器中元素的最小值
del(item) 删除变量

引用
在python中，值是靠引用来传递的
我们可以用id()来判断两个两个变量是否为同一个值的引用，我们可以将id值理解为那块内存的地址标志
下面演示的是不可变类型的数值
```python
a = 1
b = a
print(id(a))
print(id(b))  #此时a,b的数值一样
a =2
print(b)
print(id(a))
print(id(b))   #a和b的地址已经变了
```

下面演示一下可变类型的赋值

```python
a = [1,2]
b = a
print(id(a))
print(id(b))

a.append(3)

for i in b:
    print(i)
print(id(a))
print(id(b))

```

可变类型与不可变的类型

可变类型，数值可以改变：
列表list
字典dict

不可变类型，值不可以改变：
数值类型 int long bool float
字符串 str
元组tuple

## python基础之函数

1.函数可以有多个返回值
```python
def divid(a,b):
    shang = a//b
    yushu = a%b
    return shang,yushu
sh,yu = divid(5,2)
print(sh,yu)

```
本质上是利用了元组

### 2.缺省参数
1.调用函数时，缺省参数的值如果没有传入，则被默认值

注意：带有默认值的参数一定要位于参数列表的最后面

### 3.不定长参数
有时可能需要一个函数能够处理比当初声明时更多的参数，这些参数叫做不定长的参数，声明的时候不会命名

基本语法：
```python
def functionname([formal_args,]*srgs,**kwargs):
    "函数_文档字符串"
    function_suite
    return [expression]

```
加了星号（*）的变量args会存放所有未命名的变量参数，args是元组，而加了**的变量kwargs会存放命名参数，就是以key = value的形式，kwargs为字典结构

```python

def fun(a,b,*args,**kwargs):
    print("a = ",a)
    print("b = ",b)
    print("args = ",args)
    print("kwargs = ")
    for key ,value in keargs.items():
        print(key,"=",value)

fun(1,2,3,4,5,c=6,d=7,e=8)
```

### python基础之面向对象3

1.__new__方法
加强记忆
```python
class A(onject):
    def __init__(self):
        print("这是init方法")
    
    def __new__(cls):
        print("这是new方法")
        return object.__new__(cls)
a=()
```

__new__ 至少要有一个参数cls，代表要实例化的类，此参数在实例化由python解释器自动提供

__new__ 必须要有返回值，返回实例化出来的实例，这点在自己实现 __new__ 时候要特别注意，可以return父类的__new__出来的实例，或者直接是object的__new__出来的实例

__init__ 有一个参数self,这个就是__new__返回的实例，__init__ 在__new__ 的基础上可以完成其他初始化的动作，__init__ 不需要返回值

我们将类比作制造商，__new__ 方法是前期的原材料购买环节，__init__方法就是在原来材料的基础上，加工，初始化商品环节


2.异常

1.概念
当python 检测到一个错误的时候，解释器就无法继续执行了，反而会出现一些错误的提示，这就是所谓的异常
2.捕获异常
```python
try:
    print("---------------")
    open("222.txt",'r')
    print("-------------")
except IOError
    pass
2.