class Student(object):
    __slots__ = ('name', 'age') #  slot: 插槽
    pass

"""
    1、在Python中可以动态的为对象添加任何属性，通过__slots__可以限定[实例对象]只能添加指定属性
    2、__slots__定义的属性只对当前类的实例对象有效，对子类不起作用
    3、如果子类有__slots__属性，其范围为：子类__slots__ 加上 父类__slots__
"""
class ManStu(Student):
    pass

class FemaleStu(Student):
    __slots__ = ('score')

if __name__ == '__main__':
    def getName():
        pass

    s = Student()
    # 实例对象上不可以添加__slots__限定以外的属性
    # s.score = 98
    # print(s.score)        # AttributeError
    # s.getName = getName   # AttributeError

    # 类对象上可以添加
    Student.score = 98
    print(Student.score)

    # 父类__slots__对子类没有影响
    man = ManStu()
    man.score = 98
    print(man.score)

    f = FemaleStu()
    f.name = 'limei'
    f.age = 23
    f.score = 98
    # f.addr = 'earth'  # AttributeError
    print(f)