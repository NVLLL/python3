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

# 4、关键字参数，容许传入任意个key-value形式参数，在方法内部被自动组装成一个tuple
def person(name,age,**kw):
    print('name:',name,'age:',age,'othor:',kw)

person('Tom',23,city='beijing',sex='F')
person('zhaosi',45)
# 和可变参数类似，可以先组装一dict，然后把dict作为关键字参数传给方法
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jeck',23,**extra)

# 5、命名关键字参数，对于关键字参数，调用者可以传入任意不受限制的关键字参数，
# 如果希望限制关键字参数的名字，就可以使用命名关键字参数，例如：只接受city和job作为关键字参数
def person(name,age,*,city,job): # 必须以key-value的形式传入city和job
    print('name:',name,'age:',age,'city:',city,'job:',job)
person('Jerry',23,city='TianJin',job='software engineer')

# 如果函数的参数已经有可变参数，那么命名关键字参数的*可以省略
def person(name,age,*args,city,job):
    print(name,age,*args,city,job)
person('NEW',23,'Hello','world',city='ShangHai',job='software engineer')

# 参数组合：各种形式的参数可组合使用，但顺序必须是：位置参数、默认参数、可变参数、命名关键字参数、关键字参数
def f1(a,b,*args,**kw):
    print(a,b,args,kw)
def f2(a,b,c=3,*args,d,**kw):
    print(a,b,c,args,d,kw)
f1(1,2,*[3,4],name='zhangsan',age=23,city='beijing')
f2('left','right',4,'width','height',d='value')

# 练习：计算乘积
def product(x,*args):
    r = x
    for i in args:
        r *= i
    return  r

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

