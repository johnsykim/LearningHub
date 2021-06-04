import sys
from collections import Counter


def dicecup():
    #N, M = map(int, input.split())
    N, M = map(int, sys.stdin.readline().split())
    arr = []
    res = []
    for n in range(1, N + 1):
        for m in range(1, M + 1):
            arr.append(n + m)
    most_common = Counter(arr).most_common(1)[0][1]
    for x in Counter(arr).most_common():
        if x[1] == most_common:
            res.append(x[0])
    return res


res = dicecup()
for i in res:
    print(i)
