# https://datacodingschool.tistory.com/43

def solution(S):
    arr = []

    for i in range(len(S)):
        # print(arr)
        if S[i] == '(':
            arr.append(S[i])
        else:
            # Instead of adding ')', delete '('
            if len(arr) != 0 and arr[-1] == '(':
                del arr[-1]
            # If the stack is empty
            else:
                arr.append(S[i])

    # If S were properly nested, the stack should be empty
    if len(arr) == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    S1 = "(()(())())"
    S2 = "())"
    print(solution(S1))
    print(solution(S2))
