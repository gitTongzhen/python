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

1通过列表生成式，我们可以直接创建一个列表。但是，受到内存的限制，列表的容量肯定是有限的，而且，扩展一个包含100万个元素的列表，不仅占用了很大的存储空间，如果我们仅仅访问前面几个元素，那后面绝大多数的元素占用的空间都白白浪费了。所以，如果列表元素可以按照可以按照某种算法推算出来，那我们是否可以在循环的过程中推算出后续的元素呢，这样不必创建完整的list,从而节省了大量的空间。在python中，这种一边循环一边计算的机制，叫做生成器：genereator

2.创建生成器的方法
1.第一种办法很简单，只要把一个列表生成式[]改成()

```python
l = [x*2 for x in range(10)]
g = [x*2 for x in range(10)]
print(l)
print(g)

```
创建l和g的区别在于最外层的[]和()，L是一个列表，而G是一个生成器，我们可以直接打印每一个元素，但是我们怎么打印出G的每一个元素呢？如果要一个个打出来，可以通过next()函数获得生成器的下一个返回值
```python
g = (x*2 for x in range(10))
print(next(g))
for i in g:
    print(i)

```
生成器保存的是算法，每次调用next(G),就计算出G的下一个元素的值，直到计算出最后一个元素，没有更多的元素时，抛出StopIteration的异常。当然，这种不断调用next()实在太变态了，没有正确的方法使用for循环，生成器也是可以迭代的对象

2.generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，可以用函数来实现

4.小结
生成器是这样的一个函数，它记住了上一次返回时在函数体中的位置，对于生成器函数的第二次(或者第n次)调用跳转至该函数的中坚，而上次调用的所有的局部变量都保持不变
生成器不仅记住了他数据的状态，生成器还记住了它在流控制的构造(在命令式编程中，这种构造不只是数据值)中的位置
生成器的特点：
1.节约内存
2.迭代到下一次调用时，所使用的参数都是第一次保留下的，即是说，在整个函数调用的参数都是第一次所调用保留的，而不是新创建的


## 闭包
1.函数引用

```python
def test1():
    print("---- in test1 func ----")
test1()

#引用函数
ret = test1
print(id(ret))
print(id(test1))

```

2.什么是闭包

```python
def test(number):
    #在函数的内部再定义一个函数，并且这个函数用到了外边函数的变量，那么将这个函数以及用到的一些变量称之为闭包
    def test_in(number_in):
        print("in test_in 函数，number_in is %d"%number_in)
        return number+number_in
    #其实这里返回的是闭包的结果
    return test_in

#给test函数赋值，这个20就是给参数number
ret = test(20)

#注意这里的100其实给参数number_in
print(ret(100))

#注意这里的200其实给参数number_in
print(ret(200))

```

内部函数对于外部函数作用域的变量的引用，则称内部函数为闭包

实例：
```python
def line_conf(a,b):
    def line(x):
        return a*x+b
    return line

line1 = line_conf(1,1)
line2 = line_conf(4,5)
print(line1(5)) #输出6
print(line2(5)) #输出23

```

这个例子中，函数line与变量a,b构成了闭包。在创建闭包的时候，我们通过line_conf的参数说明了这两个变量的取值，这样子，我们就确定了函数的最终形式(y =x +1和y = 4x +5)。我们只需要变换参数a,b，就可以获得不同的直线表达函数。由此，我们可以看到，闭包也具有提高代码可复用的作用

3.小结：
1.闭包优化了变量，原来的类对象完成的工作，闭包也可以完成
2.由于闭包引入了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存



## 装饰器

装饰器本质上就是一个python函数，他可以让其他的函数在不需要做任何代码变动的前提下，增加额外的功能，装饰器的返回值也是一个函数对象。它经常用于有切面需求的场景，比如插入日志，性能测试，事务处理，缓存，权限校验等场景。装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能无关的雷同代码并继续重用，概括来讲，装饰器的作用就是为已经存在的函数或者对象添加额外的功能

```python
# 定义函数：完成数据包裹
def makeBold(fn):
    def warpped():
        return "<b>"+fn() +"</b>"
        return warpped

# 定义函数：完成包裹数据
def makeItalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped


@makeBold
def test1():
    return "hello world-1"

@makeItalic
def test2():
    return "hello world-2"

@makeBold
@makeItalic
def test3():
    return "hello world-3"

print(test1())
print(test2())
print(test3())

```

装饰器的作用：
1.引入日志
2.函数执行时间统计
3.执行函数前预备处理
4.执行函数后的清理功能
5.权限校验等场景
6.缓存

