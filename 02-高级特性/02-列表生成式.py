import os
# list() 方法，可以用来生成list，例如：生成[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L = list(range(1,11))
# print(L)
# 但是，如果要生成形如：[1x1, 2x2, 3x3, ..., 10x10]等交复杂的列表时，该怎么做？

# 方法一：通过循环,但是比较麻烦
L = []
for i in range(1,11):
    L.append(i * i)
# print(L)

# 方法二：列表生成式
L = [x * x for x in range(1,11)]
# print(L)
print(type(L))  # <class 'list'>

# 练习：
# 1、筛选出仅偶数的平方
L = [x * x for x in range(1,11) if x % 2 == 0]
# print(L)
# 2、还可以使用两层循环，可以生成全排列
L = [m + n for m in 'ABC' for n in 'abc']
# print(L)
# 3、列出当前目录下的所有文件和目录名，可以通过一行代码实现
L = [f for f in os.listdir('.')]
# print(L)
# 4、循环其实可以同时使用两个甚至多个变量
d = {'name':'Lucy','age':23}
L = [k + '=' + v for k,v in d.items() if isinstance(v,str)]
print(L)