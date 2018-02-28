from types import MethodType
class Student(object):
    pass

def _set_age(self,age):
    self.age = age

s1 = Student()
s1.set_age = MethodType(_set_age,s1)    # 给s1实例对象绑定一个方法，不能使用：s1.set_age = _set_age 这种方式给实例对象绑定方法
s1.set_age(23)                          # 调用绑定的方法
print(s1.age)

s2 = Student()
# s2.set_age(34)                        # 测试抛出异常，发现其他对象并没有set_age方法
# print(s2.age)

# 如果想给所有实例对象绑定方法，可以给class绑定方法：
def _set_score(self,score):
    self.score = score

Student.set_score = _set_score          # 为class绑定一个方法
s1.set_score(33)                        # 所有实例对象都可以使用
s2.set_score(44)
print(s1.score)
print(s2.score)

# Python中可以通过__slots__属性限制实例对象的属性，比如只容许对Student的实例添加name和age属性
class Stu(object):
    __slots__=('name','age')
    # score = 67                        # 可以给class定义score属性

    # def __init__(self,score):         # 通过__init__方法同样不能给实例对象定义score属性
    #     self.score = score

stu = Stu()
stu.name = 'zhangsan'
stu.age = 12
# stu.score = 99                        # 异常：AttributeError
# print(stu.score)

# 使用__slots__注意：其只能限制当前类的实例对象属性，对继承的子类不起做作用

