import sys

A, I = map(int, sys.stdin.readline().split())
n_scientists = A * I
while True:
    if n_scientists / A <= I - 1:
        break
    n_scientists -= 1
print(n_scientists + 1)
