def solution(S, P, Q):
    #mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    nucleotides = 'ACGT'
    mapping = {nucleotide: impact for impact, nucleotide in enumerate(nucleotides, 1)}
    res = []
    for query in range(len(P)):
        slice = S[P[query]:Q[query]+1]
        for nucleotide, impact in mapping.items():
            if nucleotide in slice:
                res.append(impact)
                break
    return res


def solution_2(S, P, Q):
    res = []
    for i in range(len(P)):
        if 'A' in S[P[i]:Q[i]+1]:
            res.append(1)
        elif 'C' in S[P[i]:Q[i]+1]:
            res.append(2)
        elif 'G' in S[P[i]:Q[i]+1]:
            res.append(3)
        else:
            res.append(4)
    return res


if __name__ == '__main__':
    S = 'CAGCCTA'
    P = [2, 5, 0]
    Q = [4, 5, 6]
    print(solution(S, P, Q))        # prints [2, 4, 1]
