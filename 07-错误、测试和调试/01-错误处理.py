import logging
# try...except...finally 处理异常
try:
    print('try...')
    r = 10 / 0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('End')

# 还可以在except块后面加else，当没有错误发生时会自动执行else语句

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    # 利用logging模块打印异常堆栈消息
    logging.exception(e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error...')
finally:
    print('finally...')
print('End')

# Python中的异常都是由BaseException派生而来

# 可以用 raise 抛出异常
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise    # raise语句如果不带参数，就会把错误原样抛出

bar()