import sys

Y, P = sys.stdin.readline().split()

if Y.endswith('e'):
    res = Y + 'x' + P
elif Y.endswith('a') or Y.endswith('i') or Y.endswith('o') or Y.endswith('u'):
    res = Y[:-1] + 'ex' + P
elif Y.endswith('ex'):
    res = Y + P
else:
    res = Y + 'ex' + P

print(res)

# 6 min
