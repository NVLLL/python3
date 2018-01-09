# if

age = 20
if age > 18:
    # print('your age is %d' % age)
    print('your age is',age)
    print('adult')

# if...else...

age = 3
if age > 18:
    print('your age is',age)
    print('adult')
else:
    print('your age is',age)
    print('teenager')

# elif

if age > 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# if语句可以像JS一样进行简写
x = 1
if x:
    print(True)