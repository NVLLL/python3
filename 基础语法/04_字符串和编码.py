# 对于单个字符，python提供了ord() 函数获取字符的整数表示，chr() 把编码转换为对应的字符
print(ord('A'))
print(chr(65))

# python中对bytes类型的数据用带b前缀的单引号或双引号表示

# 以Unicode表示的str通过 encode() 可以转换为指定的bytes
print('中文'.encode()) # b'\xe4\xb8\xad\xe6\x96\x87'
# 将bytes数据转为str可以 用decode() 函数
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# 如果bytes中有无法解码的字符，decode方法会抛出错误
# print(b'\xe4\xb8\xad\xe6\x96\xff'.decode('utf-8'))
# 如果只有小部分字符是无效的，可以向decode传入errors='ignore',进行忽略
print(b'\xe4\xb8\xad\xe6\x96\xff'.decode('utf-8',errors='ignore'))

# 要计算字符串有多少个字符可以使用len()
print(len('中文'))
print(len('中文'.encode('utf-8')))
print(len(b'ABC'))

# 格式化 在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：
print('hello %s' %'world')
print('Hi %s,your score is %d' %('Tom',99)) # 如果有多个占位符，格式的内容用括号括起来
# 常见的占位符有：%s 字符串，%d 整数，%f 浮点数，%x 十六进制数
# 其中格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print('%2d-%02d' % (3,1))
print('%.2f' % 3.1415926)
# 如果字符串中%是一个普通的字符，需要转义，这时候可以使用%%来表示一个 % 字符
print('%d%%-%d%%' % (7,8))

# format() 用传入的参数依次替换字符串中{0}、{1}...占位符
print('Hello {0},你的成绩提升了{1:.1f}%'.format('Tom',13.444))

# 练习：小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1 = 72
s2 = 85
r = ((s2 - s1) / s1) * 100
print('成绩提高了 %.1f %%' % r)