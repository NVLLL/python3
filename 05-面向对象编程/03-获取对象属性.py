# 如何判断对象类型

# 1、type() 返回对象的Class类型
# print(type(123) == type(456))             # True
# print(type('abc'))                        # <class 'str'>
# print(type('abc') == str)                 # True

# 判断一个对象是否是函数，可以使用types模块中定义的常量
import types
def fn():
    pass

print(type(fn) == types.FunctionType)                       # True
print(type(abs) == types.BuiltinFunctionType)               # True
print(type(lambda x:x) == types.LambdaType)                 # True
print(type((x for x in range(10))) == types.GeneratorType)  # True

# 2、isinstance() 对于继承关系type判断起来不方便，isinstance()可以判断对象是否是某一类型
L = [1,2,3]
print(isinstance(L,(list,tuple,dict))) # 还可以判断是否是某些类型中的一种


# ########################## Python中的“反射” #######################################

# 1、dir() 获取对象中的所有属性和方法列表
print(dir('abc'))

# 前面提到过，Python中的__xx__方法有特殊用途，比如str中__len__方法用来返回字符串长度，
# 如果试图调用len()函数获取对象长度，实际上在len()函数内部，会自动调用对象的__len__方法
# 例如：
class MyObj(object):
    def __len__(self):
        return 100

myObj = MyObj()
print(len(myObj)) # 100

# 2、getattr()、setattr()、hasattr() 操作对象的属性
class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

# hasattr(obj,name) 判断该对象是否具有某个属性
print(hasattr(obj,'x'))         # True
print(hasattr(obj,'power'))     # True
print(hasattr(obj,'y'))         # False

# setattr(obj,name,value) 设置属性
setattr(obj,'y',10)
print(hasattr(obj,'y'))         # True

# getattr(obj,name,default) 获取属性
p = getattr(obj,'power')
print(type(p))  # <class 'method'>
print(p())      # 81
# 如果获取的属性不存在，会抛出AttributeError的错误
# v = getattr(obj,'z')
# 可以传入一个default参数，如果属性不存在，就返回该值
v = getattr(obj,'z',404)
print(v)