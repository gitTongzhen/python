## 讨论那些稀奇古怪的写法
### 1.property 属性检查，确保变量既可以初始化，又可以做变量检查
1.在绑定属性的时候，如果我们直接把属性暴露出去，虽然写起来很简单，但是没有办法检查参数，导致成绩可以随意更改
所以这里做一层升级，用set和get函数来设置成绩
比如
```python

class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError("score must be an integer")
        if value < 0 or value > 100:
            raise ValueError('score must between 0-100')
        self._score = value

```
按着上面的例子虽然可以对于数值上面做校验
但是丢失了属性赋值的方便性
所以在这里，我们需要这么写
```python
class Student(object):

    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("score must be an integer!")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 -100")
        self._score = value

```


### 2.继承和不继承object对象有什么区别呢？

```python
class person():
    def __init__(self):
        self.name = "ren"
class animal(object):
    def __init__(self):
        self.name = 'dongwu'
        print(dir(object))
a=animal()

b= person()
print(dir(b))
```

在python3中默认帮你加载了object类，所以两者的打印并没有什么区别
但是在python2 中，二者是有区别的

### 3.装饰器 classmethod 和 staticmethod

```python
class stclass():
    d=1
    #对象方法
    def imethod(self):
        print(self)
        print("instance method")
    #类方法
    @classmethod
    def cmethod(cls):
        print(cls)
        print("class method")
    #静态方法
    @staticmethod
    def smethod():
        print("static method")
 
sc = stclass()
sc.imethod()
sc.cmethod()
sc.smethod()

```

1.第一个方法属于实例方法，该方法的第一个参数是当前实例，拥有当前类和实例的所有特性
2.类方法，该实例属于类，该方法的第一个参数是当前类，可以对类做一些处理，如果一个静态方法和类有关，但是和实例无关，那么使用该方法
3.静态方法，该实例属于类，但是该方法没有参数，也就是说该方法不能对类做处理，相当于全局方法
