"""
    由于Python是动态语言，根据类创建的实例对象可以绑定任意属性
    给实例绑定属性的方法是通过实例对象或self变量
"""
class Student(object):
    school = '清华大学'         # 类属性

    def __init__(self,name):
        self.name = name       # 实例属性

if __name__ == '__main__':
    print(Student.school)   # 通过类对象访问类属性

    s = Student('zhangsan')
    print(s.school)         # 通过实例对象访问类属性

    s.school = '北大'       # 为实例对象添加实例属性
    print(Student.school)   # 清华大学 没有修改类属性
    print(s.school)         # 北大

    print(hasattr(Student, 'school'))

