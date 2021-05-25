def solution(N, A):         # Time complexity: O(N + M)
    # Strategy:
    # Keep track of max of any counter as you iterate through the array
    # If max counter operation is called, initialize with dict.clear()
    # Count other values and stack them on top of max

    counters = {i: 0 for i in range(1, N + 1)}
    max_sum = 0
    max_val = 0
    for key in A:
        if key == N + 1:
            max_sum += max_val
            counters.clear()
            max_val = 0
        else:
            if counters.get(key) is None:
                counters[key] = 1
            else:
                counters[key] += 1
            max_val = max(max_val, counters[key])

    res = [max_sum] * N
    for key, val in counters.items():
        res[key - 1] += val

    return res


def solution_2(N, A):       # Time complexity: O(N * M)
    counters = [0] * N
    for val in A:
        if 1 <= val and val <= N:
            counters[val-1] += 1
        elif val == N + 1:
            max_val = max(counters)
            counters = [max_val] * N
    return counters


if __name__ == '__main__':
    N = 5
    A = [3, 4, 4, 6, 1, 4, 4]
    print(solution(N, A))
