import sys

C = float(sys.stdin.readline())
L = int(sys.stdin.readline())
data = []
for _ in range(L):
    lawn = tuple(map(float, sys.stdin.readline().split()))
    data.append(lawn)
area = 0
for lawn in data:
    area += lawn[0] * lawn[1]
print("{:.7f}".format(area * C))
