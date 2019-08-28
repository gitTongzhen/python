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

class People(object):
    country = 'china'
    #类方法 用classmethod 来进行修饰
    @classmethod
    def getCountry(cls):
        return cls.country
    @classmethod
    def setCountry(cls,country):
        cls.country = country

p = People()

print(p.getCountry())   #可以用实例对象引用
print(People.getCountry())   #可以用类对象进行引用
People.setCountry('japen')
print(p.getCountry())
print(People.getCountry())