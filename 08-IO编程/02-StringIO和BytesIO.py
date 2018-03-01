# StringIO和BytesIO用于在内存中读写(文本、二进制)内容

from io import StringIO,BytesIO

stream = StringIO()
stream.write('Hello')
stream.write('\nWorld!')

# print(stream.getvalue()) # getvalue() 用于获取写入内存中的str

# 还可以用一个str初始化StringIO,然后向读取文件一样读取：
f = StringIO('Java\nPython\nC++')
while True:
    line = f.readline()
    if line == '':
        break
    # print(line)

# BytesIO
b = BytesIO()
b.write('中国'.encode('UTF-8'))
# print(b.getvalue())

b2 = BytesIO(b'\xe4\xb8\xad\xe5\x9b\xbd')
print(b2.read())