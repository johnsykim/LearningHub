def solution(A):
    B = [i for i in range(1, len(A) + 1)]

    xor_A = 0
    xor_B = 0
    for a in A:
        xor_A ^= a
    for b in B:
        xor_B ^= b

    if xor_A ^ xor_B == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    print(solution([4, 1, 3, 2]))
    print(solution([4, 1, 3]))
