# 全局变量var
var = 33

# 修改全局变量
def update_var():
    # 标记在函数内部使用全局变量var，如果没有global关键字说明，则相当于在函数内部定义局部变量var
    global var
    var = 44

print(var)