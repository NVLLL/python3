# ############################# 装饰器 ###################################
import time
# 获取系统时间
def now():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

# 如果我们要增强now函数功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def log(func):
    def wrapper(*args,**kwargs):
        print('call %s()' % func.__name__ )
        return func(*args,**kwargs)
    return wrapper

# 使用Python的@符号(语法糖)，将decorator置于函数的定义处，相当于执行了now=log(now)
@log
def now():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# print(now())

# 如果装饰器本身也需要传入参数：
def log(text):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args,**kwargs)
        return wrapper
    return decorator

@log('exeute') # 相当于：now = log('exeute')(now)
def now():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# print(now())

# 经过装饰器增强的函数名已经变了，如本例中由now变为wrapper，因为返回的是wrapper()函数，重新赋值给now变量
print(now.__name__) # wrapper
# 所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
# Python内置的functools.wraps就是干这个事的。所以完整的装饰器写法如下：
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('call %s' % func.__name__)
        return func(*args,**kwargs)
    return wrapper
@log
def now():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(now.__name__)

# 带参数的装饰器
def log(text):
    # 闭包
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print('%s %s()' % (text,func.__name__))
            return func(*args,**kwargs)
        return wrapper
    return decorator
@log('exeute：')
def now():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(now.__name__)

# 练习1：请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
def metric(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print('执行%s耗时:%d'%(func.__name__,end-start))
        return result
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y
@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

# 练习2：请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
