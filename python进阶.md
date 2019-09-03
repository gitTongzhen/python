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




### 元类
1.类也是对象
在大多数的编程语言中，类就是一组用来描述如何生成一个对象的代码段，在python中这点仍然成立，但是远不止如此，在python中，类同样是对象，只要你使用关键字class,python解释器就会在执行的时候创建一个对象
```python
class ObjectCreater(object):
    pass
```

这段代码会在内存中创建一个对象，名字就是ObjectCreater.这个对象(类对象ObjectCreator)
拥有创建对象的能力，但是它本质上来说，仍然是一个对象，于是乎，你可以对它做如下的操作：
1.你可以将它赋值给一个变量
2.你可以拷贝它
3.你可以为它增加属性
4.你可以将它作为函数参数进行传递

2.动态的创建类

1.因为类也是对象，你可以在运行时动态的创建他们，就像其他任何对象一样，首先，你可以在函数中创建类，使用class关键字即可

```python
class choose_class(name):
    if name =='foo':
        class foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar

Myclass = choose_class('foo')
print(Myclass)
print(Myclass())
```

2.使用type创建类
type可以查看对象的类型，当使用type对ObjectCreator查看类型是type
type还有一种完全不同的功能，动态的创建类
格式：type(类名，由父类名称不是"不是字符串"组成的元组，包含属性的字典)
```python
dwx = type("dwx",(),{"age":10})
a = dwx()
print(a.age)
```

1.type的第二个参数，元组是父类的名称，而不是字符串
2.添加的属性是类属性，并不是实例属性

使用type创建带有方法的类

```python
def sum(self,a,b):
    return a+b
test =type("test",(),{"sum":sum})
a = test()
print(a.sum(1,2))

```

类方法和静态方法都一样
python中，类也是对象，你可以动态的创建类，这就是当你使用关键字class时，python在幕后做的事情，而这就是通过元类来实现的


3.元类

元类就是用来创建类的东西

函数type实际上是一个元类，type就是python在背后用来创建所有类的元类

元类就是创建这种对象的东西，type就是python的内建元类

4.__metaclass__ 属性

可以在定义一个类的时候为其添加__metaclass__ 属性
```python
class Foo(object):
    __metaclass__ = something

```
首先写下class Foo(object) ,但是类Foo还没在内存中创建，python会在类的定义中去寻找
__metaclass__ 属性，如果找到了，python就会用它来创建类Foo，如果没有找到，就会用内建的
type来创建这个类

当写下如下的代码时：
```python
class Foo(object):
    __metaclass__ = something
```
首先写下class Foo(object) ,但是类Foo还没有在内存中创建，python会在类的定义中，寻找
__metaclass__ 属性，如果找到了，python就会创建类Foo，如果没找到，就会用内建的type来创建这个类

当写下如下的代码时：
```python
class Foo(Bar):
    pass

```

python做了如下的操作：
1.Foo中有 __metaclass__ 这个属性吗，如果有，python会通过metaclass创建一个名字为Foo的类
2.如果python中没有找到 __metaclass__ 属性，它会继续在Bar(父类)中寻找 __metaclass__ 属性，并尝试着做前面同样的操作
3.如果python在任何父类中都找不到__metaclass__,他就会在模块层次中寻找 __metaclass__ ，并尝试着做同样的操作
4.如果还是找不到__metaclass__ ,它就会用内置的type来创建这个类对象

现在的问题就是，你可以在__metaclass__ 中放置什么代码呢，答案就是：可以创建一个类的东西，那么什么可以用来创建一个类呢，type,或者任何可以使用到type和子类化type的东东都可以

5.自定义元类
就元类本身而言，他们其实很简单：
1.拦截类的创建
2.修改类
3.返回修改后的类


```python
class UpperAttrMetaClass(type):
    #__new__ 是在__init__之前被调用的特殊方法
    ## __new__是用来创建对象并返回之的方法
    # 而 __init__ 只是用来将传入的参数初始化给对象的
    # 你很少用到__new__ ,除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望自定义它，所以我们这里改成__new__
    # 如果你希望的话，你也可以在__init__中做一些时间
    # 还有一些高级的用法涉及到修改 __call__特殊方法，但是我们这里不用

    def __new__(cls,future_class_name,future_class_parents,future_class_attr):
        newAttr = {}
        for name,value in future_class_attr.items():
            if not name.startswitch("__"):
                newAttr[name.upper()] = value
                


```

## 动态语言

1.动态语言的定义
动态编程语言是高级程序设计语言的一个类别，在计算机领域已经被被广泛应用。它是一类在运行时可以改变其结构的语言：例如新的函数，对象，甚至是代码可以被引进，已有的函数可以被删除或者其他结构上面的改变，动态语言非常具备活力，例如JavaScript便是一个动态语言，除此之外如PHP，Ruby，python等也都属于动态语言，而C,C++等语言则不属于动态语言

2.运行过程中给对象绑定属性

```python
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
p = Person("小七","17")
print(p.name)
print(p.age)
p.sex = "male" #给类绑定属性
print(p.sex)

```

3.动态的过程中给类绑定属性

```python
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
p = Person("小七","17")
Person.sex = "female"
print(p.name)
print(p.age)
print(p.sex)

```

4.运行的过程中给类绑定方法

```python
import types

# 定义一个类
class Person(object):
    num = 0
    def __init__(self,name = None,age = None):
        self.name = name
        self.age = age
    def eat(self):
        print("eat food")

# 定义一个实例方法

def run(self,speed):
    print("%s 在移动，速度是%d km/h"%(self.name,speed))

# 定义一个类方法
@classmethod
def testClass(cls):
    cls.num = 100

# 定义静态方法

@staticmethod
def testStatic():
    print("----static method ---")

# 创建一个实例对象
P = Person("老王"，24)

#调用在class中的方法
P.eat()

# 给这个对象添加实例方法
P.run() = types.MethodType(run,P)

# 调用实例方法
P.run(180)

# 给Person类绑定类方法
Person.testClass = testClass

#调用类方法
print(Person.num)
Person.testClass()
print(Person.num)

#给Person类绑定静态方法
Person.teststatic = testStatic
#调用静态方法
Person.testStatic()
```

5.运行的过程中删除方法属性

删除方法：
1.del 对象.属性名
2.delattr(对象，"属性名")

6.__slots__ 
动态语言：可以运行的过程中，修改代码
静态语言：编译时已经确定好代码，运行过程中不能修改
Python允许在定义class的时候，定义一个特殊的 __slots__ 变量，来限制class实例能添加的属性
```python
class Person(object):
    __slot__ = ("name","age")
p = Person()
p.name = "小七"
p.age = 20
# p.sex = "male" ...会报错
 使用 __slots__ 要注意，__slots__ 定义的属性仅对当前类实例起作用，对于继承的子类是不起作用的

```

## 生成器

1.什么是生成器



