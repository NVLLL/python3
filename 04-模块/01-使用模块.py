# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'a test module'

__author__='guowei'

import sys
def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World!')
    elif len(args) == 2:
        print('Hello %s!' % args[1])
    else:
        print('Too Many arguments!')

if __name__ == '__main__':
    test()
# ######################################################################################

# 第一行的字符串，表示模块的文档注释，任何模块代码的第一行字符串都被视为模块的注释
# __author__变量标明作者
# import sys  导入Python提供的sys模块，我们就有了变量sys指向该模块，使用sys这个变量，就可以访问sys模块的所有功能

# 如果直接在命令行运行这个模块，Python解释器会把一个特殊变量__name__置为__main__，而如果是在其他模块中导入使用该模块时，if判断会失效

# 在Python中使用"_"前缀定义的变量，例如：_xxx,__xxx等是非公开的(private)，不应该被直接引用
# 像__xxx__变量名是公开的，可以被直接引用，但是它们有特殊用途，比如上面的__author__、__name__等

# ######################################################################################

def _private_1(name):
    print('Hello %s' % name)
def _private_2(name):
    print('Hello %s' % name)

# 通过公开的greeting()函数把私有的函数隐藏起来
def greeting(name):
    if len(name) > 2:
        return _private_1(name)
    else:
        return _private_2(name)

