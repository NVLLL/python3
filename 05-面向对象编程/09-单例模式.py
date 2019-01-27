class Singleton(object):
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    print(id(s1) == id(s2))  # True