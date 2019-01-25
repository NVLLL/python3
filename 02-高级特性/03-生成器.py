from collections import Iterable
from collections import Iterator

# 在Python中，一边循环一边计算的机制，称为生成器：generator，要创建生成器的方式有多种：

# 1、把列表生成式的[]改为(),就创建了一个生成器
g = (x * x for x in range(1,11))
print(g) # <generator object <genexpr> at 0x023A9270>

# 可以通过next()方法获取generator的下一个返回值
print(next(g))
# generator保存的是算法，每次调用next(),就计算下一个值，直到计算到最后一个元素，没有更多元素时抛出StopIteration的错误。
# 通过next()获取generator每个元素太麻烦。其实，generator也是可迭代对象，可以通过for...in进行迭代
print(isinstance(g,Iterable)) # True
for i in g:
    print(i)

# 2、在函数中使用yield关键字，实现复杂逻辑的generator
# 例如：著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
def fibonacci(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n += 1
    return 'done'
# 上面定义的函数可以计算出斐波拉契数列的前max个数，其实fibonacci函数定义了斐波拉契数列的推算规则
# 要把fibonacci函数变成generator，只需要把print(b)改为yield b就可以了：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'
# print(fib(6)) # <generator object fib at 0x006D96F0>
# for i in fib(6):
#     print('i',i)
# 通过上面的迭代发现，不能获取到fib的返回值，如果想获取其返回值，必须捕获StopIteration异常
g = fib(6)
while True:
    try:
        x = next(g)
        print(x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


# 注意：generator和函数的执行有区别：
# - 函数按顺序执行遇到return或执行到最后语句后返回；
# - generator是每调用next()时执行，遇到yield语句返回，再次执行从上次返回的yield语句处执行,结束同函数相同
# - 用变量可以接受到函数的返回值，而generator函数的“调用”实际返回一个generator对象

# 示例：
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
o = odd()
# print(next(o))
# print(next(o))

# 练习：杨辉三角
def triangles():
    pass

# Iterator和Iterable的区别：
# - Iterable，可迭代的对象，可以使用for...in进行迭代，如str、list、set、generator等，可以通过isinstance(o,Iterable)判断o是否为可迭代对象
# - Iterator，迭代器对象，不仅可以使用for...in进行迭代，还可以使用next()函数获取下一个值，如generator。直到最后抛出StopIteration异常，
#   可以通过isinstance(o,Iterator)判断o是否为可迭代对象，生成器都是Iterator对象，但是str、list等不属于Iterator
print(isinstance('abc',Iterable))  # True
print(isinstance('abc',Iterator))  # False

# 可以通过iter()方法将list、str等Iterable转为Iterator对象
print(isinstance(iter('abc'),Iterator)) # True

