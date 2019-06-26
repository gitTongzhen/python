
from abc import ABCMeta,abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod #定义抽象方法的关键字
    def pay(self,money):
        pass
class AliPay(Payment):
    def pay(self,money):
        print('使用支付宝支付%s元'%money)
class ApplePay(Payment):
    def pay(self,money):
        print("使用苹果支付支付了%s"%money)

### 单例模式
class Singleton(object):
    # 如果该类已经有一个实例了就直接返回，否则创建一个全局唯一的实例
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singleton,cls).__new__(cls)
        return cls._instance

class Myclass(Singleton):
    def __init__(self,name):
        if name:
            self.name = name
a = Myclass('a')
print(a)
print(a.name)

b=Myclass('b')
print(b)
print(b.name)

print(a)
print(a.name)

## 工厂模式的优点是不暴露接口

