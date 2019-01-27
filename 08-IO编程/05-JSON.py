import json

if __name__ == '__main__':
    d = dict(name='zhangsan', age=24, gender='male')
    # 将字典对象转为json字符串
    print(json.dumps(d))

    jsonstr = '{"name": "zhangsan", "age": 24, "gender": "male"}'
    # 将json字符串转为字典对象
    print(json.loads(jsonstr))

