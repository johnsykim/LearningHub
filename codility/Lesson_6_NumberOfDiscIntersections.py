def solution(A):
    circles = []
    for i, v in enumerate(A):
        circles.append((i-v, -1))
        circles.append((i+v, 1))
    circles.sort()

    intersections = 0
    intervals = 0
    for i, v in enumerate(circles):
        if v[1] == 1:
            intervals -= 1
        if v[1] == -1:
            intersections += intervals
            intervals += 1

    return -1 if intersections > 10000000 else intersections


if __name__ == '__main__':
    A = [1, 5, 2, 1, 4, 0]
    print(solution(A))
