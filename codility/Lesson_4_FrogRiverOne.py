def solution(X, A):
    # All leaf positions needed for a frog to jump
    comp = set([i for i in range(1, X + 1)])

    # Initialize river's fallen leaves and compare
    river = set()
    for sec, pos in enumerate(A):
        river.add(pos)
        if river == comp:
            return sec
    return -1


if __name__ == '__main__':
    X = 5
    A = [1, 3, 1, 4, 2, 3, 5, 4]
    print(solution(X, A))       # prints 6
