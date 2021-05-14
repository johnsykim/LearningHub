# Even Fibonacci numbers

from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return fib(n-1) + fib(n-2)


n = 0
sum = 0
while fib(n) <= 4000000:
    n += 1
    if fib(n) % 2 == 0:
        sum += fib(n)
print(sum)
