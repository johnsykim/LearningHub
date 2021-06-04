import sys
data = [int(sys.stdin.readline().strip()) for i in range(10)]
res = len(set([i % 42 for i in data]))
print(res)
