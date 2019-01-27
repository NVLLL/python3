class A(object):

    def __init__(self):
        print('这是 init 方法')
    """
        __new__:
            1、至少要又有一个cls参数，代表要实例化的类对象，由解释器传入
            2、在创建实例对象时由解释器调用
            3、先于__init__调用，且必须有返回值，返回值可以是父类或object实例化的对象
            4、__init__接受的self对象，就是__new__()返回的对象
    """
    def __new__(cls):
        print('这是 new 方法')
        return object.__new__(cls)

if __name__ == '__main__':
    A()