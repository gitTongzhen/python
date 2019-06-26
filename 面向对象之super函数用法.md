###  [super函数的使用](https://blog.csdn.net/qq_37590544/article/details/88316165)

super函数在python的继承中使用，用来解决面向对象中的函数重载的问题
```python
class A(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print("I m A")
    def show(self):
        print("age: ",self.age)
        print("name: ",self.name)
class B(A)
```
当继承父类的函数成员的时候，super函数是用不到的


要理解super函数必须要去理解mro函数，mro函数将继承顺序列表放在一个列表中，利用super函数可以跨越层次的去调用

### [cls与self的区别](https://www.cnblogs.com/chllovegeyuting/archive/2013/03/14/2960532.html)

cls和self是一种命名上面的区别
cls 去引用类中的方法
self 去引用类中的静态变量

此外类中还有一种静态方法，用@staticmethod装饰器装饰，这种方法与类有某种关系但是不需要使用实例或者类来参与
比如：
```python
DEBUG = True

class A(object):
    a = 'a'
    @staticmethod
    def is_debug():
        return DEBUG
    def show_error_messages(self):
        if self.is_debug():
            print('error_messages')
        else:
            pass
foo = A()
foo.show_error_messages()
```

### python的内置属性
```
__dict__: 类的属性(包含一个字典，由类的数据属性组成)
__doc__: 类的文档字符串
__name__: 类名
__module__:类定义所在的模块
__bases__: 类所有的父类构成元素
```

python的方法重写
```python
class Parent:
    def myMethod(self):
        print("调用父类的方法")
class Child(Parent):
    def myMethod(self):
        print("调用子类的方法")

c = Child()    #子类的实例
c.myMethod()   

```

### hasattr()函数
描述 hasattr()用于判断对象是否包含对应的属性或者方法，有的话返回True,否则返回False
需要注意的是name要用括号括起来

```python
class test():
    name = "xiaohua"
    def run(self):
        return "hello world"
t=test()
hasattr(t,"name")


```