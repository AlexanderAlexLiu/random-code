'''
Alex liu
2023-02-07
'''
from functools import lru_cache

USE_RECURSION = True

@lru_cache(None)
def fib(n : int) -> int:
    if USE_RECURSION:
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)
    else:
        a, b = 0, 1
        for _ in range(n):
            a, b  = b, a+b
        return a

if __name__ == '__main__':
    for i in range(100):
        print(fib(i))
    USE_RECURSION = False
    for i in range(100):
        print(fib(i))