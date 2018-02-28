# Python中__xx__一些特殊用途的函数，可以帮助我们定制类

# #########################  __slots__ ####################################
# 前面学过 __slots__= (attr1,attr2...) 用来限定可以为实例对象绑定的属性名

# #########################  __len__() ####################################
# 为了能让class作用于len()函数
class A(object):
    def __len__(self):
        return 10
# print(len(A()))  # 10

# #########################  __str__()、__repr__() ########################
# __str__():用print方法打印对象时调用，类似java中的toString方法
# __repr__()：在交互模式下直接敲变量显示时调用
class Student(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'Student object (name,%s)' % self.name

    __repr__ = __str__

print(Student('Jerry'))

# #########################  __iter__()、__next__() #########################
# 如果类想被for...in迭代，就必须实现__iter__()方法，该方法返回一个迭代对象，
# 然后Python的for循环会不断的调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration时退出
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

# for i in Fib():
#     print(i)

# #########################  __getitem__() ################################
# 实现对对象的：obj[item] 操作
# -  如果将对象看为list，那么item可能是下标(int)，或者切片(slice)
# -  如果将对象看为dict，那么item就是可以作为key的object，例如：str
# 与之相关的还有
# -  __setitem__()：把对象视为list或dict进行赋值
# -  __delitem__()：删除某个元素

class FibExt():
    def __getitem__(self, item):
        a,b = 1,1
        if isinstance(item,int):    # 下标
            for i in range(item):
                a,b = b,a+b
            return a
        if isinstance(item,slice):  # 切片
            start =item.start
            end = item.stop
            if start is None:
                start = 0
            L = []
            for i in range(end):
                if i >= start:
                    L.append(a)
                a,b = b,a+b
            return L
f = FibExt()
print(f[4])
print(f[1:5])

# #########################  __getattr__() ################################
# 如果访问对象的不存在的属性时，比如Student的age属性，Python解释器会试图调用__getattr__(self,'age')来尝试获取属性
class Stu(object):
    def __init__(self,name):
        self.name = name

    def __getattr__(self, item):
        if item == 'age':
            return 20

s = Stu('zhangsan')
print(s.name)
print(s.age)
print(s.score) # None

# 注意：
# - 1、只有在没有找到属性时，解释器才会调用__getattr__()，而已有的属性，比如name，则不会到__getattr__()中查找
# - 2、任意调用，比如：s.abc返回的都是None，这是因为定义的__getattr__()默认返回None，如果想让class响应特定的属性，我们可以按约定，抛出AttributeError错误
# def __getattr__(self, item):
#     if item == 'age':
#         return 20
#     raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)

class Chain(object):

    def __init__(self,path=''):
        self._path = path

    def __getattr__(self, attr):
        return Chain('%s/%s' % (self._path,attr))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)

# #########################  __call__() ################################
# 使实例对象本身可以被调用
class S(object):
    def __init__(self,name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('My name is %s ' % self.name)

s = S('zhangsan')
s()   # My name is zhangsan

# __call__()模糊了对象和函数的界限
# 怎么判断对象是否可以被调用? 能别调用的函数是一个Callable对象，比如上面我们定义的带有__call__()的对象
print(callable(s))              # True
print(callable(lambda x:x))     # True