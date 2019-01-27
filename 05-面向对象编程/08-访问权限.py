class People(object):
    """
        1、Python不同于Java，没有访问权限的关键字，标识符前面加上 '__' 代表私有
        2、私有属性不能在类外部被访问
        3、私有属性不能被继承
    """
    __country = 'china'

    def __init__(self, name):
        self.__name = name

    # 对私有属性提供公有的getter/setter
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

if __name__ == '__main__':
    # print(People.__country) # type object 'People' has no attribute '__country'
    pass

