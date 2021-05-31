from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def nth_prime(n):
    cnt = 0
    num = 2
    while True:
        if is_prime(num):
            cnt += 1
            if cnt == n:
                return num
        num += 1


if __name__ == '__main__':
    print(nth_prime(10001))     # prints 104743
