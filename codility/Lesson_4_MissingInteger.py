def solution(A):

    # Keep only unique elements
    A = set(A)

    # Special case where there are no positive elements
    if max(A) < 1:
        return 1

    # Check from the smallest positive integer
    for i in range(1, len(A) + 1):
        if i not in A:
            return i
        else:
            continue
    return i + 1


if __name__ == '__main__':
    print(solution([1, 3, 6, 4, 1, 2]))
    print(solution([1, 2, 3]))
    print(solution([-1, -3]))
