import re


def binary(N):
    return '{0:b}'.format(N).strip('0')


def gap(b):
    p = re.compile('10+1')
    if not p.findall(b):
        return 0
    else:
        lst = b.split('1')
        return len(max(lst))


def solution(N):
    b = binary(N)
    return gap(b)


if __name__ == '__main__':
    print(solution(9))      # prints 2
    print(solution(529))    # prints 4
    print(solution(20))     # prints 1
    print(solution(15))     # prints 0
    print(solution(32))     # prints 0
    print(solution(1041))   # prints 5
