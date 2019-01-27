class People(object):
    # 类属性
    country = "China"

    """
        类方法：
            1、方法被@classmethod修饰
            2、第一个参数必须是类对象，约定命名为'cls'， 通过它可以访问类属性
            3、可以通过类对象、实例对象调用
    """
    @classmethod
    def get_country(cls):
        return cls.country

    # 通过类方法修改类属性
    @classmethod
    def set_country(cls, country):
        cls.country = country


if __name__ == '__main__':
    print(People.get_country()) # China 通过类对象访问类方法

    p = People()
    print(p.get_country())      # China 通过实例对象访问类方法

    # 通过类方法修改类属性
    # People.set_country("America")
    p.set_country('America')
    print(p.get_country())