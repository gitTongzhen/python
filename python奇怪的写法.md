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
但是在