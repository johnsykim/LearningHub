from collections import Counter


def solution(A):        # Solution 1
    # XOR every element by looping
    # Since every pair of elements will cancel out,
    # Result will be the remaining unpaired element
    res = 0
    for a in A:
        res ^= a
    return res


def solution_2(A):      # Solution 2
    # Use Counter, a dict subclass for counting hashable objects
    c = Counter(A)

    # Define a submethod to compute n least common elements
    def least_common(obj, n):
        return obj.most_common()[:-n-1:-1]

    # Retrieve the value of the unpaired element
    res = least_common(c, 1)
    return res[0][0]


if __name__ == '__main__':
    A = [9, 3, 9, 3, 9, 7, 9]
    print(solution(A))          # prints 7
