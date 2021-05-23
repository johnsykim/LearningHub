def solution(A):        # Solution 1
    N = len(A) + 1
    euler_sum = (N * (N + 1)) // 2
    return euler_sum - sum(A)


def solution_2(A):      # Solution 2
    # A is an array with one element missing
    xor_A = 0
    for a in A:
        xor_A ^= a

    # B in a full array containing integers in the range (1, len(A) + 2)
    xor_B = 0
    B = [i for i in range(1, len(A) + 2)]
    for b in B:
        xor_B ^= b

    # XOR the two results to find the missing element
    # return xor_B
    return xor_A ^ xor_B


if __name__ == '__main__':
    A = [2, 3, 1, 5]            # prints 4
    A = [1, 2, 3, 4, 6, 7, 8]   # prints 5
    A = [1, 3, 2, 4, 6, 5, 8]   # prints 7
    print(solution_2(A))
