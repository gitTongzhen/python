1.单例模式
  定义：保证一个类只有一个实例，并提供一个访问它的全局访问点
  试用场景：当一个类只能有一个实例，而客户可以从一个总所周知的访问点访问它时
  优点：对唯一实例的受控访问，相当于全局变量，但是又可以防止此变量被篡改

```python
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
a = MyClass('a')
print(a)
print(a.name)

b=Myclass('b')
print(b)
print(b.name)

print(a)
print(a.name)

```

2.简单工厂模式

  定义：不直接面向客户暴露建造的细节，而是通过一个工厂类来负责创建产品类的实例
  角色：工厂角色，抽象产品角色，具体产品角色
  优点：隐藏了对象创建代码的细节，客户端不需要修改代码
  缺点：违反了单一职责原则，将创建的逻辑集中到一个工厂里面

```python
from abc import ABCMeta,abstractmethod

class Paymnet(metaclass=ABCMeta):
    #抽象产品角色
    @abstractmethod
    def pay(self,money):
        pass
class AliPay(Payment):
    def __init__(self,enable_yuebao=False):
        self.enable_yuebao=enable
    def pay(self,money):
        if self.enable_yuepao:
            print("使用余额宝付款%s元"%money)
        else:
            print("使用支付宝支付%s元"%money)

class ApplePay(Payment):
    #具体的产品角色
    def pay(self,money):
        print("使用苹果支付支付%s元"%money)
class PaymentFactory():
    def create_payment(self,method):
        if method == 'alipay':
            return Alipay

```

8.代理模式
定义:为其他对象提供一种代理以控制对于特定对象的访问
角色：抽象实体，实体，代理
适用场景：远程代理

9.观察者模式

定义：定义对象之间的一种一对多的依赖关系，当一个对象的状态发生改变是，所有依赖它的对象都会得到通知，并且被自动更新，因此，观察者模式又被称为发布订阅模式
角色：抽象主题，具体主题(发布者),具体观察者(订阅者)
适用场景：

```python
from abc import ABCMeta,abstractmethod

class notice():
    def __init__(self):
        self.observers=[]
        self.message=''
    def attach(self,observer):
        self.observers.append(observer)
    def notify(self):
        for observe in self.observers:
            observe.update()

class StockObserve():
    def __init__(self,name,notice):
        self.name = name
        self.notice = notice
    def update(self):
        print("here we go: %s fg %s "%(self.notice.message,self.name))

if __name__ == '__main__':
    notice=notice()
    observer1 = StockObserve('张三',notice)
    observer2 = StockObserve('Lisi',notice)
    notice.attach(observer1)
    notice.attach(observer2)
    notice.message ='laile laodi'
    notice.notify()

```
