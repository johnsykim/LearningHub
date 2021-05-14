from collections import deque


def solution(A, K):         # Solution 1
    dA = deque(A)
    dA.rotate(K)
    return list(dA)


def solution_2(A, K):       # Solution 2

    def rotate(arr):
        # Turn given array into double-ended queue
        de_arr = deque(arr)

        # Pop the right-most element and append at left
        tmp = de_arr.pop()
        de_arr.appendleft(tmp)

        return list(de_arr)

    # Recursive call
    if K == 1:
        return rotate(A)
    else:
        tmp = rotate(A)
        return solution(tmp, K - 1)


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    print(solution(a, 1))       # [5, 1, 2, 3, 4]
    print(solution(a, 2))       # [4, 5, 1, 2, 3]
    print(solution(a, 3))       # [3, 4, 5, 1, 2]
    print(solution(a, 4))       # [2, 3, 4, 5, 1]
    print(solution(a, 5))       # [1, 2, 3, 4, 5]
