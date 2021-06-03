import sys

parsed = [list(map(int, sys.stdin.readline().split())) for i in range(5)]
data = [sum(lst) for lst in parsed]
print(data.index(max(data)) + 1, max(data))
