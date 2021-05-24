def solution(A):                # Time complexity: O(N)
    sum_left = 0
    sum_right = sum(A)
    diff = None
    for i in range(len(A) - 1):
        sum_left += A[i]
        sum_right -= A[i]
        if diff == None:
            diff = abs(sum_right - sum_left)
        else:
            diff = min(diff, abs(sum_right - sum_left))
    return diff


def solution_2(A):              # Time complexity: O(N^2)
    lst_diff = []
    for i in range(1, len(A)):
        pt1 = sum(A[0:i])
        pt2 = sum(A[i:len(A)])
        diff = abs(pt1 - pt2)
        lst_diff.append(diff)
    return min(lst_diff)


if __name__ == '__main__':
    A = [3, 1, 2, 4, 3]
    print(solution(A))
