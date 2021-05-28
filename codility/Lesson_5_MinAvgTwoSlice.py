# https://codesays.com/2014/solution-to-min-avg-two-slice-by-codility/
# https://nukeguys.tistory.com/175

def solution(A):
    minAvg = (A[0] + A[1])/2
    minIdx = 0
    for i in range(2, len(A)):

        # 2-element slice
        avg = (A[i-1] + A[i])/2
        if (minAvg > avg):
            minAvg = avg
            minIdx = i-1

        # 3-element slice
        avg = (A[i-2] + A[i-1] + A[i])/3
        if (minAvg > avg):
            minAvg = avg
            minIdx = i-2

    return minIdx


if __name__ == '__main__':
    A = [4, 2, 2, 5, 1, 5, 8]
    print(solution(A))          # prints 1
