from enum import Enum,unique
# 枚举用来定义常量

# 定义枚举方式一：
Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 定义枚举方式二：
# - 枚举成员不容许重复
# - @unique装饰器可以帮助检查枚举成员值没有重复
# - 枚举的成员放在枚举的名为__members__的字典中
@unique
class WeekDay(Enum):
    Sun = 0     # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# 枚举所有成员
for item in Month:
    print(item)         # Month.Jan...
    print(item.name)    # Jan...
    print(item.value)   # 1... 通过Enum构造生成的枚举，其枚举项的值是由系统生成的int类型常量，默认从1开始计数

# 枚举WeekDay的所有成员
for name,member in WeekDay.__members__.items():
    print(name,'=>',member,'value=',member.value)   # Sun => WeekDay.Sun value= 0...

# 访问枚举成员：
week1 = WeekDay.Sun
print(week1)            # WeekDay.Sun

week2 = WeekDay['Mon']
print(week2)            # WeekDay.Mon

# 访问枚举成员的值
print(WeekDay.Sun.value)# 0

# 通过值获取枚举项
print(WeekDay(6))       # WeekDay.Sat

# 练习：把Student的gender属性改造为枚举类型，可以避免使用字符串：
class Student(object):
    def __init__(self,name,age,gender):
        if not isinstance(gender,Gender):
            raise TypeError('bad type gender!')
        self._gender = gender
        self._name = name
        self._age = age

    @property
    def gender(self):
        return self._gender.value

    def __str__(self):
        return 'name=%s,age=%d,gender=%s'%(self._name,self._age,self._gender.value)

@unique
class Gender(Enum):
    male = '男'
    female = '女'

s = Student('zhangsan',23,Gender.male)
print(s.gender)