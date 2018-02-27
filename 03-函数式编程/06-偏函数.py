# int(x, [base]) 函数可以把字符串转换为整数，base指定int把字符串x视为对应进制来转成十进制
# 示例：将'1010101'当做二进制转换
v = int('1010101',base=2)
# print(v)
# 如果有大量的二进制需要转换，每调用int都需要指定base=2，我们可以定义下面函数来简化(将base=2作为默认参数)：
def int2(s,base=2):
    return int(s,base)
# print(int2('1010101'))

# 偏函数：借用functools模块的partial帮助我们创建一个偏函数的，不需要我们自己定义int2()
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
import functools
int2 = functools.partial(int,base=2)
print(int2('0000011'))

# 在创建偏函数时可以接受函数、*args(可变参数)、**kwargs(关键字参数)
int2 = functools.partial(int,base=2)  # 传入关键字参数base
max2 = functools.partial(max,10)      # 把10作为可变参数自动加入参数列表右边
print(max2(5,6,7)) # 10
