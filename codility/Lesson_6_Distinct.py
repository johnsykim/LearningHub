def solution(A):
    return len(list(set(A)))


if __name__ == '__main__':
    A = [2, 1, 1, 2, 3, 1]
    print(solution_2(A))        # prints 3
