# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=alwlren_00&logNo=221614962593

def solution(S):
    nested = {'(': 1, ')': -1, '{': 2, '}': -2, '[': 3, ']': -3}
    nest = []
    for s in S:
        if nested[s] > 0:
            nest.append(s)
        if nested[s] < 0:
            if len(nest) == 0:
                return 0
            t = nest.pop()
            if abs(nested[t]) != abs(nested[s]):
                return 0
    if len(nest) != 0:
        return 0
    return 1


if __name__ == '__main__':
    S1 = "{[()()]}"
    S2 = "([)()]"
    print(solution(S1))
    print(solution(S2))
