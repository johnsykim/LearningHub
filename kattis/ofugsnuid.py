import sys
n = int(input())
data = [int(sys.stdin.readline().strip()) for i in range(n)]
data.reverse()
for i in data:
    print(i)
