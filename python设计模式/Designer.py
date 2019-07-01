
from abc import ABCMeta,abstractmethod

# class Payment(metaclass=ABCMeta):
#     #抽象产品角色
#     @abstractmethod
#     def pay(self,money):
#         pass



class AiliPay():
    #具体产品角色
    def __init__(self,enable_yuebao=False):
        self.enable_yuebao = enable_yuebao

    def pay(self,money):
        if self.enable_yuebao:
            print('使用余额宝支付%s元'%money)
        else:
            print('使用支付宝支付%s元'%money)

class ApplePay():
    # 具体产品角色
    def pay(self,money):
        print('使用苹果支付支付%s元'%money)

class PaymentFactory():
    #工厂角色
    def create_payment(self,method):
        if method == 'alipay':
            return AiliPay()
        elif method == 'yuebao':
            return AiliPay(True)
        elif method == 'applepay':
            return ApplePay()
        else:
            return NameError

p = PaymentFactory()
f = p.create_payment('yuebao')
f.pay(100)




# class singleTon():
#     def __init__(self):
#         pass
#     @classmethod
#     def instance(cls,*args,**kwargs):
#         if not hasattr(singleTon,"_instance"):
#             singleTon._instance = singleTon(*args,**kwargs)
#         return singleTon._instance




# class monkey():
#     def pay(self):
#         print("请支付10元")

# class tiger():
#     def pay(self):
#         print("请致富50元")
# class elephant():
#     def pay(self):
#         print("请支付100元")

# class watchFactory():
#     def watch(self,method):
#         if method == 'monkey':
#             return monkey()
#         if method == 'tiger':
#             return tiger()
#         if method == 'elephant':
#             return elephant()

# watcher = watchFactory()
# a=watcher.watch('monkey')
# a.pay()

class person():
    name ="ren"
class animal(object):
    def __init__(self):
        self.name = 'dongwu'
        #print(dir(object))
a=animal()

print(a.__)
# b= person()
# print(dir(b))
# ### 单例模式
# class Singleton(object):
#     # 如果该类已经有一个实例了就直接返回，否则创建一个全局唯一的实例
#     def __new__(cls,*args,**kwargs):
#         if not hasattr(cls,'_instance'):
#             cls._instance = super(Singleton,cls).__new__(cls)
#         return cls._instance

# class Myclass(Singleton):
#     def __init__(self,name):
#         if name:
#             self.name = name
# a = Myclass('a')
# print(a)
# print(a.name)

# b=Myclass('b')
# print(b)
# print(b.name)

# print(a)
# print(a.name)

## 工厂模式的优点是不暴露接口
# class notice():
#     def __init__(self):
#         self.observers=[]
#         self.message=''
#     def attach(self,observer):
#         self.observers.append(observer)
#     def notify(self):
#         for observe in self.observers:
#             observe.update()

# class StockObserve():
#     def __init__(self,name,notice):
#         self.name = name
#         self.notice = notice
#     def update(self):
#         print("here we go: %s fg %s "%(self.notice.message,self.name))

# if __name__ == '__main__':
#     notice=notice()
#     observer1 = StockObserve('张三',notice)
#     observer2 = StockObserve('Lisi',notice)
#     notice.attach(observer1)
#     notice.attach(observer2)
#     notice.message ='laile laodi'
#     notice.notify()