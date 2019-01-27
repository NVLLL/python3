import json

class Student(object):
    def __init__(self, name, age, gender='male'):
        self.name = name
        self.age = age
        self.gender = gender

if __name__ == '__main__':
    stu = Student('zhangsan', 28)
    # 直接将Student转为json异常
    # json.dumps(stu)   # TypeError: Object of type 'Student' is not JSON serializable

    def stu2dict(student):
        return {
            'name':student.name,
            'age': student.age,
            'gender': student.gender
        }
    # 通过default参数指定Student转dict的方式
    print(json.dumps(stu, default=stu2dict))

    # 更通用的做法:
    print(json.dumps(stu, default=lambda obj: obj.__dict__)) # 实例对象的__dict__以字典的形式存储所有实例属性

    def dict2stu(d):
        return Student(d['name'], d['age'], d['gender'])
    # 通过object_hook参数指定字典转Student的方式
    student = json.loads('{"name": "zhangsan", "age": 28, "gender": "male"}', object_hook=dict2stu)
    print(student)