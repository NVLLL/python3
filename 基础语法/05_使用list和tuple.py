# list是python内置的一种数据类型，特点：有序集合，可以随时添加和删除元素
classmates = ['Tom','Jerry','zhangsan']
print(classmates)

# 用len()可以查看list 的元素个数
print(len(classmates))

# 可以用索引来访问每个位置上的元素
print(classmates[0])
print(classmates[1])
print(classmates[2])

# 获取最后一个元素除了可以用len(list) - 1 做索引，还可以使用-1做索引直接获取
print(classmates[-1])
# 依次类推，可以获取倒数第二个、第三个....
print(classmates[-2])

# 向list末尾追加元素:append
classmates.append('Lisi')
print(classmates)

# 向指定位置插入元素:insert
classmates.insert(1,'唐僧')
print(classmates)

# 删除list末尾元素:pop
classmates.pop()
print(classmates)
# 删除指定位置上的元素：pop(index)
classmates.pop(1)
print(classmates)

# 替换某个位置上的元素，可以直接其赋值
classmates[1] = '猪八戒'
print(classmates)

# list里面的数据类型也可以不同
L = [2,'xxx',3]
print(L)

# 另一种有序列表：元组，特点：与list相似，不同之处在于元组一旦初始化后就不能再修改(元素的指向不能修改)
classmates = ('Bob','Michael','Tracy')
print(classmates)
# 它没有insert、append、pop这样的方法，但是获取元素的方法同list相同
print(classmates[-1])

# 注意：如果定义只有一个元素的元组,不能使用 t = (1) 这种形式，这种情况下会按数学公式中的小括号运算，所以定义的是整数1，而应该采用如下形式：
t = (1,)
print(t)

# 练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])