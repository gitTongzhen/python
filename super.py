class Base(object):

    def __init__(self):
        print("Base init")


class Medium1(Base):

    def __init__(self):
        super(Medium1, self).__init__()
        print("Medium1 init")


class Medium2(Base):

    def __init__(self):
        super(Medium2, self).__init__()
        print("Medium2 init")


class Leaf(Medium1, Medium2):

    def __init__(self):
        super(Leaf, self).__init__()
        #self.__init__()
        print("Leaf init")


import os
print(help(os.listdir()))