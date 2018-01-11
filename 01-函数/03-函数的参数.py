# 1、位置参数,调用函数时必须传入对应位置的参数
# 计算x的n次方
def my_power(x,n):
    if not isinstance(x,(int,float)) or not isinstance(n,(int,)):
        raise TypeError('bad operand type')
    r = 1

    if not n:           # n == 0
        return 1
    elif n > 0:
       while n >= 1:
           r *= x
           n = n - 1
    else:
        while n < 0:
            r *= 1 / x
            n = n + 1
    return r

# 2、默认参数，可以简化函数的调用  注意：默认参数必须放在位置参数后面
def enroll(name,gender,age = 6,city = 'beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Bob', 'M', 7)
# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。比如调用enroll('Adam', 'M', city='Tianjin')
#　enroll('zhangsan','男')
#　enroll('li','女',7)
enroll('Tom','猫',city='CCTV-1')

# 默认参数坑：自定义函数add_end()为传入的list添加一个end元素
def add_end(L=[]):
    L.append('end')
    return L
# 正常调用
print(add_end([1,3,'b']))
print(add_end([3,4,5]))
# 使用默认参数
print(add_end())   # ['end']
print(add_end())   # ['end', 'end']
# 原因：python函数在定义的时候，默认参数L在内存中就被创建出来了，即[](作用域是全局的？)
#      因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果
#      改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
def add_end(L=None):
    if L is None:
        L = []
    L.append('end')
    return L
print(add_end([1,2,3]))
print(add_end())
print(add_end())

# 定义默认参数要牢记一点：默认参数必须指向不可变对象

# 3、可变参数 顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
# 在函数的内部实际接受的是一个tuple
# 示例：计算a2 + b2 + c2 + ……
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n ** 2
    return sum
print(calc(1,2,3))
# 如果已经有一个list或者tuple，要调用一个可变参数怎么办？
print(calc(*[3,4]))