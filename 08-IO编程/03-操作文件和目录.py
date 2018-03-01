# Python的os和shutil模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中
import os,shutil

# - 获取操作系统类型：os.name
print(os.name)      # win是nt，Linux、Mac、UNIX是posix

# - 获取操作系统详细信息：os.uname() 在win系统上不提供

# - 操作系统中定义的环境变量：os.environ
print(os.environ)
# - 获取操作系统的某个环境变量：os.environ.get('key')
print(os.environ.get('PATH'))

# - 得到当前工作目录，即Python脚本所在路径：os.getcwd()
print(os.getcwd())  # E:\g_workspace\p_workspace\python3\08-IO编程

# - 返回指定路径下的所有文件和目录名：os.listdir(path)
print(os.listdir('.'))

# - 删除一个文件：os.remove(path)
# os.remove('./test.py')

# - 检验所给的路径是否是一个文件：os.path.isfile()
print(os.path.isfile(os.getcwd()))  # False

# - 检验所给路径是否是一个目录：os.path.isdir()
print(os.path.isdir(os.getcwd()))   # True

# - 判断所给路径是否为绝对路径：os.path.isabs()
print(os.path.isabs('./'))          # False
print(os.path.isabs('/a/b/c/e'))    # True 这里不需要路径真是存在，只是对字符串进行判断

# - 查看所给目录的绝对路径：os.path.abspath()
print(os.path.abspath('.'))

# - 检验所给的路径是否真实存在：os.path.exists()
print(os.path.exists('./02-StringIO和BytesIO.py'))   # True
print(os.path.exists('/ab/c'))      # False

# - 拆分路径：os.path.split() 可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split('/a/c/b/test.txt')) # ('/a/c/b', 'test.txt')

# - 分离扩展名：os.path.splitext()
print(os.path.splitext('/a/b/test.txt')) # ('/a/b/test', '.txt')

# - 在某个路径下创建新目录：os.mkdir(path)
# 先拼接路径,把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
path = os.path.join('./','testdir')
# os.mkdir(path)

# - 创建多级目录：os.makedirs()
# os.makedirs('C:/A/B')

# - 删除一个目录：os.rmdir(),目录为空时才可以删除
# os.rmdir('c:/A')

# - 对文件重命名：os.rename()
# os.rename('./test.html','test.py')

# - 删除文件：os.remove()
# os.remove('./test.py')

# - 复制文件：shutil.copyfile(src,dst) src和dst都只能是文件
# shutil.copyfile('D:/test/timg.gif','C:/sb.gif')

# - 复制文件：shutil.copy(src,dst)  src只能是文件，dst可以是文件或目录
# shutil.copy('D:/test/timg.gif','C:/sb.gif')

# - 复制文件夹：shutil.copytree(src,dst) src和dst都只能是目录，且dst必须不存在
# shutil.copytree('D:/test','C:/testdir')

# 练习1：过滤目录下的所有目录
dirs = [x for x in os.listdir('../') if os.path.isdir(os.path.join('../',x))]
print(dirs)

# 练习2：列出当前目录下所有以.py结尾的文件
pyfiles = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(pyfiles)

# 练习3：编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

if __name__ == '__main__':

    # 利用递归获取所给路径下的所有文件
    def get_target_file_path(dir,kw):
        for file in os.listdir(dir):
            full_path = os.path.join(dir,file)
            if os.path.isfile(full_path):
                if file.count(kw) > 0:
                    print(full_path)
            else:
                get_target_file_path(full_path,kw)

    get_target_file_path('D:/test','0')