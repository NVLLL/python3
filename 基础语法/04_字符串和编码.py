
# ##################    ord()、chr()      ########################################

# 对于单个字符，python提供了ord() 函数获取字符的整数表示，chr() 把编码转换为对应的字符
print(ord('A'))
print(chr(65))

# ################## encode()、decode()    ########################################

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

# ###################       格式化      #############################################

# 1、在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：
print('hello %s' %'world')
print('Hi %s,your score is %d' %('Tom',99)) # 如果有多个占位符，格式的内容用括号括起来
# 常见的占位符有：%s 字符串，%d 整数，%f 浮点数，%x 十六进制数
# 其中格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print('%2d-%02d' % (3,1))
print('%.2f' % 3.1415926)
# 如果字符串中%是一个普通的字符，需要转义，这时候可以使用%%来表示一个 % 字符
print('%d%%-%d%%' % (7,8))

# 2、format() 用传入的参数依次替换字符串中{0}、{1}...占位符
print('Hello {0},你的成绩提升了{1:.1f}%'.format('Tom',13.444))

# 练习：小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1 = 72
s2 = 85
r = ((s2 - s1) / s1) * 100
print('成绩提高了 %.1f %%' % r)

# ###################         字符串切片          ###################################

# str[起始位置:结束位置:步长] (包头不包尾)
name = 'abcdefABCDEF'

# 不指定步长，默认为1
print(name[2:-2]) # cdefABCD
#  步长的正负性决定了切片的方向
print(name[2:-2:-1]) # 空
print(name[2::-1]) # cba,不指定结束位置，缺省为字符串尾(首，由步长的正负性决定)
# 从某个下标起，截取字符串
print(name[3:]) # defABCDEF
# 翻转字符串
print(name[::-1]) # FEDCBAfedcba
# 间隔截取
print(name[3:-2:2]) # dfBD

# ################           字符串常用函数        ###################################

# 1、myStr.find(str) | myStr.rfind(str)
# find,从左向右查找str在myStr的位置(下标)，如果没有找到返回-1
# rfind,从右向左找...
str = 'hello world itcast heima itcastxxxxppc'
print(str.find('itcast'))
print(str.rfind('itcast'))

# 2、myStr.index(str) | myStr.rindex(str)
# 作用与find相同，不同之处在于，如果没有找到抛出异常
print(str.index('itcast'))
print(str.rindex('itcast'))
# print(str.index('java'))

# 3、myStr.count(str,start=0,end=len(myStr))
# 统计字符串str在start和end之间在myStr中出现的次数
print(str.count('itcast'))
print(str.count('itcast',0,10)) # 0

# 4、myStr.replace(str1,str2,count)
# 把myStr中的str1替换成str2，如果指定了count，替换不超过count次
print(str.replace('itcast','danei'))    # hello world danei heima daneixxxxppc
print(str.replace('itcast','danei',1))  # hello world danei heima itcastxxxxppc

# 5、myStr.split(str)
# 用str分割myStr,返回结果是一个列表
print(str.split(' ')) # ['hello', 'world', 'itcast', 'heima', 'itcastxxxxppc']
# 注意：如果split中不传参数，则采用空格或空白字符(\n等)分割字符串
# 练习：去掉下面字符串中的空格和换行符\n
s = 'dasf as \nfs df\nd df dsf sd\n'
print(''.join(s.split()))  # dasfasfsdfddfdsfsd

# 6、myStr.capitalize()
# 将字符串myStr首字符转为大写
print(str.capitalize()) # Hello world itcast heima itcastxxxxppc

# 7、myStr.title()
# 把字符串myStr中每个单词首字符转为大写
print(str.title()) # Hello World Itcast Heima Itcastxxxxppc

# 8、myStr.startswith(str)
# 判断字符串myStr是否以str开头
print(str.startswith('hello')) # True

# 9、myStr.endswith(str)
# 判断字符串myStr是否以str结尾
print(str.endswith('hello')) # False

# 10、myStr.lower()
# 将字符串myStr所有字母转成小写
print(str.lower())

# 11、myStr.upper()
# 将字符串myStr所有字母转为大写
print(str.upper())

# 12、myStr.ljust(width)
# 返回一个原字符串左对齐，并使用空格填充至长度width的新字符串
print(str.ljust(50))

# 13、myStr.rjust(width)
# ...右对齐
print(str.rjust(50))

# 14、myStr.center(width)
# ...居中
print(str.center(50))

# 15、myStr.lstrip()
# 去掉myStr左空格
s1 = '   xxx'
print(s1.lstrip())

# 16、myStr.rstrip()
# 去掉myStr右空格
s2 = '   xxxxx    ';
print(s2.rstrip())

# 17、myStr.strip()
# 去掉myStr两边空格
print(s2.strip())

# 18、myStr.partition(str)
# 把myStr以str分割成三部分(str前、str和str后)，返回的是一个元组
print(str.partition('itcast')) # ('hello world ', 'itcast', ' heima itcastxxxxppc')

# 19、myStr.rpartition(str)
# 类似partition，不过是从右边开始的
print(str.rpartition('itcast')) # ('hello world itcast heima ', 'itcast', 'xxxxppc')

# 20、myStr.splitlines()
# 按照行分割，返回一个包含各行作为元素的列表
s1 = 'asfas\nfsadfsd\newrwe\n'
print(s1.splitlines())  # ['asfas', 'fsadfsd', 'ewrwe']

# 21、myStr.isalpha()
# 判断myStr所有字符是否为字母
s1 = 'dsf中国'
print(s1.isalpha()) # True
s1 = '234343aaaa'
print(s1.isalpha()) # False

# 22、mystr.isdigit()
# 判断myStr所有字符是否都是数字
s1 = '234343'
print(s1.isdigit()) # True
s1 = 'aaa'
print(s1.isdigit()) # False

# 23、myStr.isalnum()
# 判断字符串myStr是否由数字和字母组成的
s1 = '342323'
print(s1.isalnum()) # True
s1 = 'bbb'
print(s1.isalnum()) # True
s1 = '23423afdsf'
print(s1.isalnum()) # True
s1 = '34324###dsf@'
print(s1.isalnum()) # False

# 24、myStr.isspace()
# 判断myStr是否是空格
s1 = ' '
print(s1.isspace()) # True
s1 = 'ss'
print(s1.isspace()) # False

# 25、myStr.join(list)
# 用myStr将list列表项拼接成一个字符串
print('='.join(['aa','java','c'])) # aa=java=c