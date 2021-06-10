import sys

n, V = map(int, sys.stdin.readline().split())
data = []
for _ in range(n):
    dimensions = list(map(int, sys.stdin.readline().split()))
    data.append(dimensions)

def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

volumes = []
for arr in data:
    box_vol = multiplyList(arr)
    volumes.append(box_vol)

d_i = max(volumes) - V
print(d_i)

# 24min
