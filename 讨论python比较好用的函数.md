### 好用的函数整理
1.isinstance()函数
isinstance() 用来判断一个函数是否是一个已知的类型
arg=123
bRet=isinstance(arg,int)

2.python 中的深拷贝与浅拷贝
```python
import copy 
a = [1,2,3,4,['a','b','c']]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
a.append(5)           #操作1的影响
a[4].append('hello')      # 操作2的影响
```
简单点来说 
1.copy.copy是浅拷贝，只拷贝父对象，不拷贝子对象
2.copy.deepcopy是深拷贝，不仅会拷贝父对象，子对象也会被拷贝
可以发现a,b受了操作1,2的影响，c只是受到操作2影响，d完全不受操作1和操作2的影响
由于b只是a的引用，所以两个本质上来说是相同的，c是a的浅拷贝，只拷贝了父对象，所以里面的子对象还是关联在一起的
d是深拷贝的对象，所以完全不受影响