# 整数、浮点数、字符串  python不同于java，其整数没有大小限制
x = 22
y = 22
print(x == y)   # == 用来比较两个变量的值是否相等
print(x is y)   # is 用来比较两个变量在内存中所指向的地址值是否相同

# 转义字符\: \n 表示换行，\t表示制表符，\本身也需要转义，使用\\表示的字符就是\
print('I\'m OK')
print('I\'m learning\nPython')
print('\\\n\\')

# 如果字符串中有许多字符需要转义，就需要加很多的\，python提供了简写的方式：r'',''内部的字符串不转义
print(r'\\\n\\')
# 如果字符串中有许多换行，用\n写在一行不容易阅读，python容许使用：'''...''' 的格式表示多行内容
print('''line1
line2
line3''')

# 布尔值：True、False，布尔值可以用and、or和not运算
print(True and False)
print(True or False)
print(not True)

# 空值：None

# 变量
a = 'ABC'   # 在内存中创建'ABC'字符串，并使变量a指向其
b = a       # 在内存中创建变量b，且变量b指向变量a所指向的数据(内存)
a = 'EFG'   # 变量a重新指向'EFG'
print(b)
# 可以使用python自带的id()函数，查看变量在内存中的地址
print(id(a))
print(id(b))

# 在python中有两种除法
# /: 计算结果是浮点数，即使能整除
print(9 / 3)   # 3.0
# //: 地板除，取计算结果的整数部分
print(5 // 3)  # 1

print(10 / 3)  # 3.333333...
print(10 // 3) # 3