class Student(object):
    # 类似java中的构造方法
    def __init__(self,name,score):
        # 如果内部属性不想让外部直接访问，可以在属性前面加上两个下划线"__"
        self.__name = name
        self.__score = score

    # 对外提供getter/setter
    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        self.__score = score

    # 打印成绩
    def print_score(self):
        print('%s的成绩是:%d' % (self.name,self.score))

    # 获取成绩等级
    def get_grade(self):
        if self.score > 90:
            print('A')
        elif self.score > 70:
            print('B')
        elif self.score > 60:
            print('C')
        else:
            print('D')

# 测试
if __name__ == '__main__':
    stu = Student('Jerry',80)
    # print(stu.__name) 外部不能直接访问私有属性
    stu.print_score()
    stu.get_grade()
