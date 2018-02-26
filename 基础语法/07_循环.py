# Python中提供两种循环方式：
# 1、for...in...
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
else:  # python中容许在for循环后面跟else，在循环完成之后执行else中语句，如果循环被break，则不会执行
    print('end!')

# range(n):生成0~n-1的序列，再通过list()可以转为list
print(list(range(5))) #[0, 1, 2, 3, 4]
# 示例：计算1~100之和
sum = 0
for i in range(101):
    sum += i
print(sum)

# 2、while循环
# 示例：计算100以内所有奇数之和
n = 1
sum = 0
while n <= 100:
    sum += n
    n += 2
print(sum)

# 练习：用循环依次对list中的每个名字打印出Hello, xxx!
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello,%s!' % name)

# break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环