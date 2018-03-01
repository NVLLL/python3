# open(file,model,buffering,encoding,errors) 打开文件
# - encoding 指定字符编码
# - errors 指定当读取文件时遇到编码错误后如何处理，最简单的就是直接忽略:errors='ignore'

# 读取文本文件

# try:
#     # open() 打开文件，参数'r':读模式
#     f = open('C:/Users/Administrator/Desktop/spring中事务的传播行为.txt','r',encoding='UTF-8')
#     # read() 可以一次读取文件的全部内容到内存中，用一个str对象表示
#     text = f.read()
#     print(text)
# finally:
#     if f:
#         # 关闭文件
#         f.close()

# 上面的写法比较麻烦，Python引入with语句可以帮我们自动调用close()
# with open('C:/Users/Administrator/Desktop/spring中事务的传播行为.txt','r',encoding='UTF-8') as f:
#     print(f.read())

# read(size) 可以每次只读取size个字节的内容
# readline() 每次读取一行的内容
# readlines() 一次读取所有内容并按行返回list

# with open('C:/Users/Administrator/Desktop/spring中事务的传播行为.txt','r',encoding='UTF-8',errors='ignore') as f:
#     for line in f.readlines():
#         print(line.strip())

# 读取二进制文件(图片、视频等)  只需要将模式设为”rb“

# with open('../拓扑排序.png','rb') as f:
#     print(f.read())


# 写文件 将open模式设为"w"(文本)或"wb"(二进制文件)
# 在写过程中，操作系统往往不会马上将数据写入磁盘，而是放入缓存中，等空闲时写。只有调用close()时，操作系统才保证把没写入的数据马上写入(清空缓存)
# 而使用with语句则不需要关心这些
# with open('C:/Users/Administrator/Desktop/test.txt','w',encoding='GBK') as f:
#     f.write('ABC')
# 我们发现以"w"模式写入，如果文件存在会覆盖文件原有内容。如果只是追加，可以使用“a”模式
with open('C:/Users/Administrator/Desktop/test.txt','a',encoding='GBK') as f:
    f.write('ABC')

