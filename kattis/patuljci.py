import sys
from itertools import combinations


def patuljci(hats):
    for pair in combinations(hats, 2):
        tmp = hats.copy()
        a, b = pair
        tmp.remove(a)
        tmp.remove(b)
        if sum(tmp) == 100:
            for n in tmp:
                print(n)


#hats = [7, 8, 10, 13, 15, 19, 20, 23, 25]
#hats = [8, 6, 5, 1, 37, 30, 28, 22, 36]
hats = [int(sys.stdin.readline().strip()) for i in range(9)]
patuljci(hats)
