import sys
from collections import deque

#arr = ['Bo', 'Pat', 'Jean', 'Kevin', 'Claude', 'William', 'Marybeth']
#arr = ['Jim', 'Ben', 'Zoe', 'Joey', 'Frederick', 'Annabelle']
#arr = ['John', 'Bill', 'Fran', 'Stan', 'Cece']


def parse_input():
    input = []
    n = 1
    while n != 0:
        n = int(sys.stdin.readline().strip())
        if n == 0:
            break
        data = [sys.stdin.readline().strip() for i in range(n)]
        input.append(data)
    return input


def symmetric_order(arr):
    n = len(arr)
    d = deque()
    if n % 2 == 0:
        for idx in range(n - 1, -1, -2):
            d.append(arr[idx])
        for idx in range(n - 2, -1, -2):
            d.appendleft(arr[idx])
        return list(d)
    else:
        for idx in range(n - 1, -1, -2):
            d.appendleft(arr[idx])
        for idx in range(n - 2, -1, -2):
            d.append(arr[idx])
        return list(d)


def main():
    input = parse_input()
    for num, arr in enumerate(input):
        res = symmetric_order(arr)
        print("SET {}".format(num + 1))
        for name in res:
            print(name)


main()
