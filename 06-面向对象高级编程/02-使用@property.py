class Student(object):

    # def getScore(self):
    #     return self.__score
    #
    # def setScore(self, score):
    #     if not isinstance(score, int):
    #         raise ValueError('score type must is int')
    #     if score < 0 or score > 100:
    #         raise ValueError('score value is between 0 and 100')
    #     self.__score = score

    # 利用@property装饰器定义score属性
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score type must is int')
        if score < 0 or score > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = score

if __name__ == '__main__':
    s = Student()
    # getter/setter 方式访问score属性，略显复杂
    # s.setScore(9999)

    # s.score = 9999
    # print(s.score)  # ValueError
    s.score = 89
    print(s.score)
