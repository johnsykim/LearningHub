# https://datacodingschool.tistory.com/39

def solution(S):
    if len(S) == 0:
        return 1

    arr = []

    for i in S:
        if i == "{":
            arr.append(3)
        elif i == "[":
            arr.append(2)
        elif i == "(":
            arr.append(1)
        elif i == ")":
            arr.append(-1)
        elif i == "]":
            arr.append(-2)
        elif i == "}":
            arr.append(-3)

    stack = []

    for i in range(len(arr)):
        # If the stack isn't empty,
        # current bracket is a closing bracket,
        # and is of the same type
        if len(stack) != 0 and arr[i] < 0 and (arr[i] == -1 * stack[len(stack)-1]):
            del stack[len(stack)-1]
        else:
            stack.append(arr[i])

    # If S were properly nested, the stack should be empty
    if len(stack) == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    S1 = "{[()()]}"
    S2 = "([)()]"
    print(solution(S1))
    print(solution(S2))
