L = [11,3,44,555,6]
# 对列表进行排序
L.sort()  # 从小到大排
print(L)  # [3, 6, 11, 44, 555]
L.sort(reverse=True) # 从大到小排
print(L)  # [555, 44, 11, 6, 3]

# 对于不能直接排序的列表元素，需要通过匿名函数来指定排序规则
L = [{'name':'zhangsan','age':23},{'name':'wangwu','age':12},{'name':'lisi','age':45}]
# L.sort() 抛异常
L.sort(key=lambda x:x['age'])
print(L)