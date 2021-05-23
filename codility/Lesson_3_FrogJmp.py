def solution(X, Y, D):
    div, mod = divmod(Y - X, D)
    if mod != 0:
        return (Y - X) // D + 1
    else:
        return (Y - X) // D


if __name__ == '__main__':
    print(solution(10, 85, 30))
    print(solution(1, 5, 2))
