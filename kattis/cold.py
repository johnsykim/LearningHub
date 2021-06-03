import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
res = len([i for i in data if i < 0])
print(res)
