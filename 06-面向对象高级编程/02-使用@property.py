class Student(object):
    @property               # 把一个getter方法变为属性
    def score(self):
        return self._score

    @score.setter           # @property本身又创建了另一个装饰器@score.setter,负责把一个setter方法变成属性赋值
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
# 对实例属性操作时(_score)，不是直接暴露的，而是通过getter/setter来操作的
s.score = 60
print(s.score)

class Stu(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value

    @property
    def age(self):
        return 2015-self._birth
    # age 属性没有提供setter方法，是只读属性


stu = Stu()
stu.birth = 2000
print(stu.birth)
print(stu.age)


# 练习：请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError('width must be an integer or float!')
        if value < 0:
            raise ValueError('width must be gt zero!')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError('height must be an integer or float!')
        if value < 0:
            raise ValueError('height must be gt zero!')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height