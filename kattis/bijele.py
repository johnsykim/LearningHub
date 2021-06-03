import sys


def bijele():
    #data = list(map(int, sys.stdin.readline().split()))
    data = [int(x) for x in input().split()]
    comp = [1, 1, 2, 2, 2, 8]
    res = []
    for i, j in zip(data, comp):
        res.append(j - i)
    res = [str(i) for i in res]
    return ' '.join(res)


print(bijele())
# 0 1 2 2 2 7 should print 1 0 0 0 0 1
# 2 1 2 1 2 1 should print -1 0 0 1 0 7
