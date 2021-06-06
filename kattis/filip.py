import sys

A, B = sys.stdin.readline().split()
A_filip = int(A[::-1])
B_filip = int(B[::-1])
if A_filip > B_filip:
    print(A_filip)
else:
    print(B_filip)
