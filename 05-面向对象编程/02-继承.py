class Master(object):
    def __init__(self):
        self.kongfu = "古法煎饼果⼦配⽅"

    def make_coke(self):
        print("按照 <%s> 制作了⼀份煎饼果⼦..." % self.kongfu)

class Prentice(Master):
    pass

if __name__ == '__main__':
    # 只要创建子类对象，就会默认执行父类的 __init__ 方法进行初始化
    p = Prentice()
    print(p.kongfu)
    p.make_coke()