

class Singleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


def main():
    singleton1 = Singleton()
    print("Object created", singleton1)
    singleton2 = Singleton()
    print("Object created", singleton2)
    assert id(singleton1) == id(singleton2)


if __name__ == "__main__":
    main()
