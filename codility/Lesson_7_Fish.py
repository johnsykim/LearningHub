def solution(A, B):
    # Stack of fish going downstream
    stack = []
    count = 0
    N = len(A)

    for i in range(N):
        # If a fish goes downstream, add it to the stack
        if B[i] == 1:
            stack.append(A[i])
        # If a fish goes upstream
        else:
            # Keep checking if there is a downstream fish
            while len(stack) > 0:
                # If fish_down > fish_up, then fish_down lives
                if stack[len(stack) - 1] > A[i]:
                    break
                # If fish_up > fish_down, then fish_down gets eaten
                else:
                    stack.pop()
            # Count fish_up who are alive
            if len(stack) == 0:
                count += 1

    # Fish_down who are alive + fish_up who are alive
    return len(stack) + count


if __name__ == '__main__':
    A = [4, 3, 2, 1, 5]
    B = [0, 1, 0, 0, 0]
    print(solution(A, B))
