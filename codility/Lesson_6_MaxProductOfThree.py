def solution(A):
    N = len(A)
    A.sort()
    prod_1 = A[N - 3] * A[N - 2] * A[N - 1]     # last three
    prod_2 = A[0] * A[1] * A[2]                 # first three
    prod_3 = A[0] * A[1] * A[N - 1]             # first two & last one
    prod_4 = A[0] * A[N - 2] * A[N - 1]         # first one & last two
    return max(prod_1, prod_2, prod_3, prod_4)


if __name__ == '__main__':
    A = [-3, 1, 2, -2, 5, 6]
    print(solution(A))          # prints 60
