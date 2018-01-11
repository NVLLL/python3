import math

# def定义函数
# 示例：自定义一个求绝对值的函数my_abs()
def my_abs(n):
    if n >= 0:
        return n
    else:
        return -n
print(my_abs(-3))

# 空函数
def nop():
    pass
# pass语句什么也不做，相当于一个占位符，保证语法正确

# 通过isinstance()函数可以对自定义函数的参数做类型检查
def my_abs(n):
    if not isinstance(n,(int,float)):
        raise TypeError('bad operand type')
    if n >= 0:
        return n
    else:
        return -n

# print(my_abs('A'))

# python中的函数可以返回多个值
# 示例：在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny
x,y = move(100,100,60,math.pi / 6)
print(x,y)
# 但其实这是一种假象，Python的函数返回的任然是单一的值：tuple。在语法上返回一个tuple括号可以省略，
# 而多个变量同时接受一个tuple，按位置赋给对应的值
r = move(100,100,60,math.pi / 6)
print(r) # (151.96152422706632, 70.0)