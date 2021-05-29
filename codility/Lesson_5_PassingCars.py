def solution(A):            # Time complexity: O(N), 100% score
    count = 0
    zero = 0
    for x in A:
        if x == 0:
            zero += 1
        if x == 1:
            count += zero

    if count > 1000000000:
        return -1
    return count


def solution_2(A):          # Time complexity: O(N^2), 50% score
    count = 0
    for i in range(0, len(A) - 1):
        if A[i] == 0:
            for j in range(1, len(A)):
                if A[j] == 1 and i < j:
                    count += 1
    if count > 1000000000:
        return -1
    return count


def solution_3(A):          # Time complexity: O(N^2), 50% score
    count = 0
    for idx, elm in enumerate(A):
        if elm == 0:
            count += A[idx + 1:].count(1)
    if count > 1000000000:
        return -1
    return count


if __name__ == '__main__':
    A = [0, 1, 0, 1, 1]
    print(solution(A))      # prints 5
