# ############################## sorted ##################################
# sorted(iterable,key,reverse)
# - 通过key指定的函数，作用到iterable上，并根据key函数返回的结果进行排序
# - reverse=True，反向排序

# 示例1：根据绝对值排序
L = [36, 5, -12, 9, -21]
# print(sorted(L,key=abs))

# 示例2：忽略大小写，按照字母序排序
L = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(L)) # 默认根据首字母ASCII的大小排序：['Credit', 'Zoo', 'about', 'bob']
print(sorted(L,key=str.lower)) # ['about', 'bob', 'Credit', 'Zoo']
# 倒序
print(sorted(L,key=str.lower,reverse=True)) # ['Zoo', 'Credit', 'bob', 'about']

# 练习：L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 1)、请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
r = sorted(L,key=lambda t:t[0])
print(r)
# 2)、再按成绩从高到低排序
r = sorted(L,key=lambda t:t[1],reverse=True)
print(r)