class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

# 静态语言VS动态语言
# - 对于静态语言(如Java)来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或其子类
# - 对于Python等动态语言来说，不一定需传入Animal类型，只要保证传入对象有run()方法即可(具有鸭子类型)
class Timer(object):
    def run(self):
        print('Start...')

def runing(animal):
    animal.run()

if __name__ == '__main__':
    d = Dog()
    c = Cat()
    # 多态
    print(isinstance(d,Animal)) # True
    print(isinstance(d,Dog))    # True

    runing(d)
    runing(c)
    runing(Timer())