import sys


def pot():
    n = int(sys.stdin.readline())
    data = [sys.stdin.readline().strip() for i in range(n)]
    X = 0
    for P in data:
        x = int(P[:-1]) ** int(P[-1])
        X += x
    return X


print(pot())
