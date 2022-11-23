def aA(f):
    def w():
        print('a')
        f()
        print('A')
    return w


def bB(f):
    def w():
        print('b')
        f()
        print('B')
    return w


@aA
@bB
def f():
    print("hello world")


f()
