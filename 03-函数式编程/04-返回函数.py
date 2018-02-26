# ########################## 函数作为返回值 #################################
# 函数不仅可以作为参数传递，还可以作为返回值

# 示例：我现一个可变参数的求和
def lazy_sum(*args):
    def sum():
        result = 0
        for s in args:
            result += s
        return result
    return sum
f = lazy_sum(1,3,5,7) # 当我们调用lazy_sum时，返回的并不是求和的结果，而是一个函数
print(f)    # <function lazy_sum.<locals>.sum at 0x02145390>
print(f())  # 才真正计算求和的结果：16

# 注意：当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1,3,5,7)
f2 = lazy_sum(1,3,5,7)
print(f1 == f2) # False

# 在这个例子中，我们在函数lazy_sum中又定义了sum函数，sum函数可以访问lazy_sum函数的参数和局部变量，当lazy_sum返回sum函数时，
# 相关参数和变量被保存在返回的函数中，成为“闭包”

# ###################################### 闭包 #############################
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1,f2,f3 = count()
print(f1()) # 9
print(f2()) # 9
print(f3()) # 9
# 调用f1,f2,f3的结果都是9，这是因为返回函数引用了变量i，但他们并非立即执行，等3个函数返回时i的值已经变为3，所以结果都为9

# 注意：返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
# 如果一定要引用循环变量怎么办？
def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1,f2,f3 = count()
print(f1()) # 1
print(f2()) # 4
print(f3()) # 9


# 练习：利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    count = 0
    def add_count():
        nonlocal count
        count += 1
        return count
    return add_count

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5


# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。
