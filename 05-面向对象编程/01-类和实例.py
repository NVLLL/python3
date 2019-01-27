class Student(object):
    """
        __init__:
            1、__init__() 类似java中的构造方法
            2、如果没有定义，Python会自动创建，但不会执行任何操作
            3、在实例化对象时__init__被自动调用
            4、self类似java的this，表示当前实例对象引用，不需要手动传入，Python会自动传入。
    """
    def __init__(self,name,score):
        # 实例属性
        self.__name = name
        self.__score = score
        print("call __init__")

    """
        __str__:
            1、作用同Java的toString相同，在使用print打印实例对象时，调用该方法
            2、只有一个参数：self
    """
    def __str__(self):
        return "姓名：%s, 分数: %.2f" % (self.__name, self.__score)

    """
        __del__:
            当删除对象时，python解释器会默认调⽤ __del__ ⽅法
    """
    def __del__(self):
        print("call __del__")

    # 打印成绩
    def print_score(self):
        print('%s的成绩是:%d' % (self.__name,self.__score))

    # 获取成绩等级
    def get_grade(self):
        if self.__score > 90:
            print('A')
        elif self.__score > 70:
            print('B')
        elif self.__score > 60:
            print('C')
        else:
            print('D')

# 测试
if __name__ == '__main__':
    # 创建对象时调用 __init__
    stu = Student('Jerry',80)

    # print(stu.__name) 外部不应该直接访问私有属性
    stu.print_score()
    stu.get_grade()

    # 我们也可以为对象添加其他属性：
    stu.sex = 'M'
    print(stu.sex)

    # 测试 __str__
    print(stu)

    # 测试__del__  del会使对象的引用计数减一
    del(stu)
