def solution(A):            # Time complexity: O(N*log(N))
    A.sort()
    N = len(A)
    for i in range(N - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            return 1
    return 0


def solution_2(A):          # Time complexity: O(N^3), 75% score
    N = len(A)
    for P in range(0, N - 2):
        for Q in range(1, N - 1):
            for R in range(2, N):
                if (P < Q and Q < R):
                    cond1 = (A[P] + A[Q] > A[R])
                    cond2 = (A[Q] + A[R] > A[P])
                    cond3 = (A[R] + A[P] > A[Q])
                    if cond1 and cond2 and cond3:
                        return 1
                    else:
                        continue
    return 0


if __name__ == '__main__':
    print(solution([10, 2, 5, 1, 8, 20]))       # prints 1
    print(solution([10, 50, 5, 1]))             # prints 0
    print(solution([1, 1, 2, 3, 5]))            # prints 0
