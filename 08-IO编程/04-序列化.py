import pickle

# Python提供的pickle模块用来序列化和反序列化

d = dict(name='zhangsan', age=28)
with open('F:/obj.txt', 'wb') as f:
    # 序列化
    pickle.dump(d, f)
    print('pickle complete')

with open('F:/obj.txt', 'rb') as f:
    # 反序列化
    d = pickle.load(f)
    print(d)

