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
    # test()
    print(sys.path)



# ######################################################################################

# 第一行的字符串，表示模块的文档注释，任何模块代码的第一行字符串都被视为模块的注释
# __author__变量标明作者

# 模块：在Python中，一个.py文件就是一个模块
# 包：组织模块的文件夹，且必须有一个__init__.py文件。包中的模块名： 包名.模块名

# 导入其他模块：
#   - import modelname
#   - from modelname improt name  从模块中导入一个指定的部分到当前命名空间中

# 当导入一个模块时，Python解释器搜索对应模块的顺序：
#   - 1、当前目录
#   - 2、PYTHONPATH下的每个目录
#   - 3、默认路径，UNIX下默认路径为：/usr/local/lib/python
# 通过sys.path可以查看模块的搜索路径

# 如果直接在命令行运行这个模块，Python解释器会把一个特殊变量__name__置为__main__，而如果是在其他模块中导入使用该模块时，if判断会失效

# 在Python中使用"_"前缀定义的变量，例如：_xxx,__xxx等是非公开的(private)，不应该被直接引用
# 像__xxx__变量名是公开的，可以被直接引用，但是它们有特殊用途，比如上面的__author__、__name__等

# ######################################################################################


