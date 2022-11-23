import time
from functools import lru_cache


def reverser(foo):
    def wrapper(*args):
        foo(*args[::-1])
    return wrapper


def printer(foo):
    def wrapper(*args):
        foo(*args)
        print(*args)
    return wrapper


def erroror(foo):
    def wrapper(*args):
        try:
            foo(*args)
        except:
            print("error")
    return wrapper


@reverser
def foo_1(a, b, c):
    print(a, b, c)


@printer
def foo_2(x, y, z):
    print(x + y + z)


@erroror
def foo_3(x):
    return 1 / x


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print(time.time() - start_time)
        return res
    return wrapper


def fib_recursive(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


@lru_cache(maxsize=None)
def fib_recursive_lru(n):
    return fib_recursive(n)


@time_decorator
def fib_recursive_lru_time(n):
    return fib_recursive_lru(n)


def fib_iter(n):
    n = n - 1
    if n <= 1:
        return n
    f = [0] * (n+1)
    f[1] = 1
    for i in range(2, n+1):
	    f[i] = f[i-1] + f[i-2]
    return f[n]


@lru_cache(maxsize=None)
def fib_iter_lru(n):
    return fib_iter(n)


@time_decorator
def fib_iter_lru_time(n):
    return fib_iter_lru(n)


print("reverser")
foo_1(1, 2, 3)

print("wrapper")
foo_2(1, 2, 3)

print("no error")
foo_3(1)
print("erroror")
foo_3(0)

print("\nFibonacci numbers calculators execution times comparison")
print("-> Recursive approach")
print(fib_recursive_lru_time(10))
print("-> Iterational approach")
print(fib_iter_lru_time(10))
