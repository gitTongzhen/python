## 讨论那些稀奇古怪的写法
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
        if 
```
