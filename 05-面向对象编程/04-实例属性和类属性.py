# 由于Python是动态语言，根据类创建的实例对象可以绑定任意属性

# ################################## 对象属性 ##################################

# 给实例绑定属性的方法是通过实例对象或self变量
class Student(object):
    def __init__(self,name):
        self.name = name  # 通过self给实例对象绑定属性

s = Student('zhangsan')
s.age = 23                # 通过实例对象绑定属性
print(hasattr(s,'age'))

# ################################## 类属性 ####################################
class Stu(object):
    name = 'Student'      # 定义类属性

s2 = Stu()
print(hasattr(s2,'name')) # True 类属性，所有实例对象都可以访问到
print(s2.name)            # 由于实例对象没有name属性，所以会继续查找class的name属性
print(Stu.name)

s2.name = 'Jerry'         # 为实例对象绑定name属性
print(s2.name)            # Jerry
print(Stu.name)           # Student 同名的类属性不受影响
del s2.name
print(s2.name)            # Student 删除了s2对象的name属性，所以会查找class的name属性

