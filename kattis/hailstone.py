import sys

n = int(sys.stdin.readline())
seq = []

def h(n):
    if n == 1:
        seq.append(1)
        return seq
    else:
        seq.append(n)
        if n % 2 == 0:
            n = n // 2
            return h(n)
        else:
            n = 3 * n + 1
            return h(n)

print(sum(h(n)))
# 50 min
