def solution(H):
    block_cnt = 0
    stack_arr = []

    for i in range(len(H)):
        # print(stack_arr)
        while len(stack_arr) > 0 and stack_arr[-1] > H[i]:
            stack_arr.pop()

        if len(stack_arr) == 0 or stack_arr[-1] < H[i]:
            block_cnt += 1
            stack_arr.append(H[i])

    return block_cnt


if __name__ == '__main__':
    H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
    print(solution(H))          # prints 7
