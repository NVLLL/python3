class People(object):
    country = 'China'

    """
        静态方法：
            1、被装饰器@staticmethod修饰的方法，不需要额外定义参数
            2、可以通过类对象、实例对象调用
    """
    @staticmethod
    def get_country():
        # 静态方法中使用类属性，必须通过类对象来引用
        return People.country

if __name__ == '__main__':
    print(People.get_country())