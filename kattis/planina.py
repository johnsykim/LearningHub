import sys

N = int(sys.stdin.readline())


def points_on_side(N):
    if N == 0:
        return 2
    else:
        return points_on_side(N - 1) + 2 ** (N - 1)


n_points = points_on_side(N) ** 2
print(n_points)
