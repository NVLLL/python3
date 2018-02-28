# python支持多重继承
class A(object):
    def foo(self):
        print('A foo')
    def bar(self):
        print('A bar')
class B(object):
    def foo(self):
        print('B foo')
    def bar(self):
        print('B bar')
class C1(A,B):
    pass
class C2(A,B):
    def bar(self):
        print('C2-bar')
class D(C1,C2):
    pass

if __name__ == '__main__':
    # MRO(Method Resolution Order):方法解析顺序
    print(D.__mro__) # (<class '__main__.D'>, <class '__main__.C1'>, <class '__main__.C2'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
    d = D()
    d.foo() # A foo
    d.bar() # C2-bar

# python的多继承MRO遵循C3算法(拓扑算法)，只要依据继承排序依次向上找到所需内容，就不在查找