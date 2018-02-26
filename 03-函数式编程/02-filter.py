# ###################### filter() #######################################

# filter(func，iterable)  把传入的函数依次作用在序列的每个元素，然后根据返回值(True/False)决定保留还是丢弃元素,返回值为Iterator

# 示例1：在一个list中，删掉偶数，只保留奇数
L = filter(lambda x:x%2==1,[1, 2, 4, 5, 6, 9, 10, 15])
# print(list(L))

# 示例2:把一个序列中的空字符串删掉
L = filter(lambda x:x and x.strip(), ['A', '', 'B', None, 'C', '  '])
print(list(L))
