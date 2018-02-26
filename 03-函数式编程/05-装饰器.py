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

# 使用Python的@符号，将decorator置于函数的定义处
@log
def now():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

print(now())