# "+"运算符: 在字符串、列表和元组的作用
print('hello' + 'world') # helloworld 拼接字符串
print(['a','b'] + ['c', 'd']) # ['a','b','c','d']
print(('a','b') + ('c','d')) # ('a','b','c','d')

# "*"运算符：在字符串、列表和元组的作用--复制
print('ab' * 4)  # abababab
print([1,2] * 4) # [1, 2, 1, 2, 1, 2, 1, 2]
print((3,4) * 4) # (3, 4, 3, 4, 3, 4, 3, 4)

#############################       内置函数        ######################################
# cmp(item1, item2) 比较两个值   (异常)
# len(item) 计算长度
print(len('abc'))
print(len(['c','d']))

# max(item) 返回容器中元素的最大值
print(max(range(0,10)))
print(max([1,3,4]))

# min(item) 返回容器中元素的最小值
print(min(range(0,10)))
print(min([1,3,4]))

# del(item) 删除变量
a = set(['a','a','b'])
del a
print(a)   # NameError: name 'a' is not defined
