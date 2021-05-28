def solution(A, B, K):          # Mathematical approach: O(1)
    res = B // K - A // K
    if A % K == 0:
        res += 1
    return res


def solution_2(A, B, K):        # Brute-force approach: O(N^2)
    counter = 0
    for i in range(A, B + 1):
        if i % K == 0:
            counter += 1
    return counter


if __name__ == '__main__':
    print(solution(6, 11, 2))                   # prints 3
    print(solution(11, 345, 17))                # prints 20
    print(solution(101, 123456789, 10000))      # prints 12345
