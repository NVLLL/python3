from collections import Iterable
# 1、在Python中，迭代是通过for ... in来完成的

d = {'a': 1, 'b': 2, 'c': 3}
# 迭代key
for k in d.keys():
    print(k)
# 迭代value
for v in d.values():
    print(v)
# 迭代key、value
for k,v in d.items():
    print(k + '=' + str(v))

# 2、如果要对list实现java中的通过下标循环怎么办？
# Python内置的enumerate()函数可以把list转为索引-元素对
for i,v in enumerate(['A','B','C']):
    print(i,v)

# 3、怎么判断对象是否可以通过for...in进行迭代？
# 方法是通过collections模块的Iterable类型判断：
flag = isinstance(d,Iterable)
print(flag)

# 练习：请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if(not isinstance(L,list) or L == []):
        return None,None
    result = []
    for i in L:
        if result == []:
            result.append(i)
            result.append(i)
        else:
            if i < result[0]:
                result[0] = i
            if i > result[1]:
                result[1] = i
    return tuple(result)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')