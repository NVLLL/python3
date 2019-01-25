
# ###################            字典简介          #####################################

# dict 同java中的map，使用键-值(key-value)存储数据
d = {'Michael':95,'Bob':88,'Tracy':60}
print(d['Michael'])

# ###################            增                #####################################

# dict[new_key] = value:把数据放入dict，除了初始化时指定外，还可以通过key放入：
d['Jerry'] = 70
print(d['Jerry'])

# 多次对同一个key放入value，后者会将前者覆盖
d['Jerry'] = 90
print(d['Jerry'])

# ###################            删                #####################################

# 1、del dict[key]:如果字典中不存在相应的key，会抛出异常
# del d['xxx']

# 2、dict.pop(key):删除特定的key,返回值为key所对应的value(同上，如果不存在key，抛出异常)
d.pop('Jerry')
print(d)
# 字典中没有remove方法

# ###################            改                #####################################

# dict[key] = new_value
d['Michael'] = 44
print(d)

# ###################            查                #####################################

# 1、如何判断dict中是否存在某个key
# 第一种方式：
print('Bob' in d)
# 第二种方式：dict.get(key)，如果key不存在返回None；如果存在则返回对应的value
print(d.get('Bob'))
print(d.get('Tom'))
# 还可以指定当key不存在时返回特定的值，示例：
print(d.get('Tom',-1)) # 当dict中不存在key='Tom'时，返回-1

# ###################            字典注意事项        #####################################

# 1、dict中数据的存取不一致

# 2、dict利用key通过hash算法来计算value的存储位置，所以不可变的对象(例如，整数、字符串等)才可以作为key，而list是可变的就不能作为key
l = [1,'b',3.122]
# d[l] = 'Hello'
# print(d[l])
t = ('a','b',1)         # 可以使用tuple作为dict的key
d[t] = 'Hello'
print(d[t])
# t1 = ('a','b',[1,2])
# d[t1] = 'python'      # 报错：tuple中有可变元素list
# print(d[t1])

# ###################            字典的遍历        #####################################
info = {'name':'zhangsan','age':17}
# 1、dict.keys():字典key的列表
print(info.keys())  # dict_keys(['name', 'age'])
# 2、dict.values()：字典的value列表
print(info.values())
# 3、items(): key-value对列表
print(info.items()) # dict_items([('name', 'zhangsan'), ('age', 17)])
# 遍历
for a,b in info.items():
    print(a,b)


# ###################            set简介          #####################################

# 创建set需要传入一个list作为输入集合
s = set([1,2,3,3,2])
print(s)
# 注意：
#   1、set同java中的一样，不能存重复元素
#   2、set中的元素存取不一致
#   3、同dict一样，set中也不可以存可变的对象，因为无法判断两个可变对象是否相等，也就无法保证set内没有重复元素

# 向set中添加元素：add()
s.add('Tom')
print(s)

# 删除set中的元素：remove()
s.remove(1)
print(s)
# set可以看成数学意义上的无序和无重复元素的集合,所以两个set可以做交集、并集等操作
s1 = set(['a','b','c'])
s2 = set(['c','e','f'])
print(s1 & s2)  # {'c'}
print(s1 | s2)  # {'c', 'f', 'a', 'b', 'e'}