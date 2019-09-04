# def square(x):
#     return x ** 2

# a = [1,2,3,4,5]

# b = list(map(square,a))

# print(b)

# class People:
#     def __init__(self,name):
#         self.__name = name
#     def getName(self): #提供调用私有属性的方法
#         return self.__name
#     def setName(self,newName):
#         if len(newName)>5:
#             self.__name = newName
#         else:
#             print("长大了")
# xiaoming = People("xaioming")
# xiaoming.setName("xiaohuang")
# print(xiaoming.getName())

# class People(object):
#     country = 'china'
#     ## 类方法，使用classmethod 来进行修饰
#     @classmethod
#     def getCountry(cls):
#         return cls.country

# p = People()
# print(p.getCountry())  #可以用过实例对象引用

# print(People.getCountry())

# class People(object):
#     country = 'china'
#     #类方法 用classmethod 来进行修饰
#     @classmethod
#     def getCountry(cls):
#         return cls.country
#     @classmethod
#     def setCountry(cls,country):
#         cls.country = country

# p = People()

# print(p.getCountry())   #可以用实例对象引用
# print(People.getCountry())   #可以用类对象进行引用
# People.setCountry('japen')
# print(p.getCountry())
# print(People.getCountry())

# def fun(a,b,*args,**kwargs):
#     print("a = ",a)
#     print("b = ",b)
#     print("args = ",args)
#     print("kwargs = ")
#     for key ,value in kwargs.items():
#         print(key,"=",value)

# fun(1,2,3,4,5,c=6,d=7,e=8)
# class A(object):
#     def __init__(self):
#         print("这是init方法")
    
#     def __new__(cls):
#         print("这是new方法")
#         return object.__new__(cls)
# a=A()


# import numpy as np
# import urllib.request as req
# import cv2
 
# # URL到图片
# def url_to_image(url):
#     # download the image, convert it to a NumPy array, and then read
#     # it into OpenCV format
#     resp = req.urlopen(url)
#     # bytearray将数据转换成（返回）一个新的字节数组
#     # asarray 复制数据，将结构化数据转换成ndarray
#     image = np.asarray(bytearray(resp.read()), dtype="uint8")
#     # cv2.imdecode()函数将数据解码成Opencv图像格式
#     image = cv2.imdecode(image, cv2.IMREAD_COLOR)
#     return  image


# url = "https://dancf-st-gdx.oss-cn-hangzhou.aliyuncs.com/zjz/images/15481222158466.png"

# image = url_to_image(url)
# print(image.shape)

def fib(times):
    n=0
    a,b=0,1
    while n<times:
        yield b
        a,b=b,a+b
        n+=1
    return "done"
for i in fib(4):
    print(i)

