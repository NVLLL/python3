# ################################### map() ###################################################

# map(func,iter)  接受两个参数，一个函数，一个Iterable，将传入的函数依次作用到序列的每个元素上，并把结果作为Iterator返回

# 示例1：函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上
it = map(lambda x:x**2,list(range(1,10)))
print(it) # <map object at 0x005E3210>
# 得到的结果是一个Iterator，Iterator是惰性序列，因此可以通过list()让它把整个序列都计算出来
# print(list(it)) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 示例2：把这个list所有数字转为字符串
L = map(str,list(it))
# print(list(L))

# ################################### reduce() ###############################################

# reduce(func,sequence,initial) 必须接受两个参数，一个函数(且这个函数也必须有两个参数),一个Iterable,reduce用函数对这个序列做累积计算
from functools import reduce

# 示例1：对列表[1, 3, 5, 7, 9]求和
def g():
    n = 1
    while n < 11:
        yield n
        n += 2
result = reduce(lambda x,y:x+y,g())
print(result)

# 示例2：把序列[1, 3, 5, 7, 9]变换成整数13579
r = int(reduce(lambda x,y:x+y,map(str,g())))
print(r)
print(type(r)) # int

# 练习1：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
i = ['adam', 'LISA', 'barT']
o = list(map(lambda x:x.capitalize(),i))
print(o)

# 练习2：请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    if L or not isinstance(L,list) :
        return None
    return reduce(lambda x,y:x*y,L)

# 练习3：利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
    CHAR_TO_FLOAT = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '.': -1,
    }
    nums = map(lambda x: CHAR_TO_FLOAT[x], s)
    point = 0
    def to_float(f,s):
        nonlocal point
        if s == -1:             # s刚好为小数点，f直接返回
            point = 1           # 标记为有小数点
            return f

        if point == 0:          # f、s都是小数点前数字
            return f * 10 + s
        else:                   # 处理小数部分
            point = point * 10  # 记录小数的百分位
            return f + s / point

    return reduce(to_float, nums,0.0)

print(str2float('0'))
print(str2float('123.456'))