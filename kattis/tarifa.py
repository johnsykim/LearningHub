import sys

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
usage = sum([int(sys.stdin.readline().strip()) for i in range(N)])
remainder = X * (N + 1) - usage
print(remainder)
